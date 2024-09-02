from lightrag.core.generator import Generator
from lightrag.core.component import Component
from lightrag.components.model_client import OllamaClient
import os
from pathlib import Path
from typing import List, Dict
from prettytable import PrettyTable
from tqdm import tqdm
from github_metadata import github_metadata_endpoint_handler
from clone_github import clone_repo_endpoint_handler
from utils.llama_configurations import model, get_description_data
from constants import ignore_list_folder_structure, ignore_list_extensions
import pandas as pd
from prettytable import PrettyTable
from flask import jsonify, request, Response
import asyncio
import aiohttp
import global_variables
import time

summary_template = r"""<SYS>
You are a summarization assistant specialized in coding files.
</SYS>
Please summarize the following code:
{{input_str}}
Summary:"""


class SummaryQA(Component):
    """
    A component that uses a summarization model to generate summaries for code.

    Parameters:
    model_client (OllamaClient): The model client to interact with the summarization model.
    model_kwargs (dict): Additional keyword arguments for the model.
    """

    def __init__(self, model_client: OllamaClient, model_kwargs: dict):  # type: ignore
        super().__init__()
        self.generator = Generator(
            model_client=model_client,
            model_kwargs=model_kwargs,
            template=summary_template,
        )

    def call(self, input: str) -> str:
        """
        Generate a summary for the provided code using the model.

        Parameters:
        input (str): The code to be summarized.

        Returns:
        str: The generated summary.
        """
        return self.generator.call({"input_str": input})

    async def acall(self, input: str) -> str:
        """
        Asynchronously generate a summary for the provided code using the model.

        Parameters:
        input (str): The code to be summarized.

        Returns:
        str: The generated summary.
        """
        return await self.generator.acall({"input_str": input})


def generate_summary(
    path: Path,
    ignore_list: List[str],
    summary_component: SummaryQA,
    ignore_extensions: List[str],
) -> List[Dict[str, str]]:
    """
    Generate a summary of files in the given path using the summarization model.

    Parameters:
    path (Path): The root directory to start scanning for files.
    ignore_list (List[str]): A list of directory or file names to ignore.
    summary_component (SummaryQA): The summarization component to use for generating summaries.
    ignore_extensions (List[str]): A list of file extensions to ignore.

    Returns:
    List[Dict[str, str]]: A list of dictionaries where each dictionary contains the file path and its summary.
    """
    summary = []
    files_to_process = []

    for root, dirs, files in os.walk(path):
        # Get relative path for the current directory
        relative_root = os.path.relpath(root, path)

        # Check if the directory should be ignored
        if any(ignored in relative_root.split(os.sep) for ignored in ignore_list):
            continue

        if relative_root == ".":
            summary.append({"file": "Modules", "description": "."})
        else:
            summary.append({"file": relative_root, "description": "Not a File"})

        # List files in the current directory
        for file in files:
            file_path = Path(root) / file

            # Check if the file should be ignored
            if any(ignored in file_path.parts for ignored in ignore_list):
                continue

            # Check if the file has an extension that should be skipped
            if file_path.suffix.lower() in ignore_extensions:
                continue

            files_to_process.append(file_path)

    # Use tqdm to display progress
    pbar = tqdm(files_to_process, unit="file")
    for file_path in pbar:
        # Update the description dynamically
        pbar.set_description(f"Processing files - {file_path}")
        try:
            # Read file content
            with open(file_path, "r") as f:
                file_content = f.read()

            # Generate summary using the model
            summary_text = summary_component.call(file_content)
            summary.append({"file": file_path, "description": summary_text})
        except Exception as e:
            summary.append(
                {"file": file_path, "description": f"Error processing file: {str(e)}"}
            )

    return summary


def save_summary_to_excel_and_print_table(
    summary: List[Dict[str, str]],
    cloned_repo_path: str,
    excel_path: str = "output / summary.xlsx",
) -> None:
    """
    Save the summary data to an Excel file and print it in a formatted table.

    Parameters:
    summary (List[Dict[str, str]]): A list of dictionaries containing file paths and their summaries.
    cloned_repo_path (str): The path of the cloned repository to be used for naming the Excel file.
    excel_path (str): Define the path and name for the Excel file
    Returns:
    None
    """
    if summary:
        # Initialize PrettyTable
        table_summary = PrettyTable()
        table_summary.field_names = ["File", "Description"]

        # Create a list to hold data for the DataFrame
        summary_data_for_excel = []

        for item in summary:
            # Retrieve description data
            description_data = get_description_data(item["description"])
            # Add data to PrettyTable
            table_summary.add_row([item["file"], description_data])
            # Add data to the list for the DataFrame
            summary_data_for_excel.append(
                {"File": item["file"], "Description": description_data}
            )

        # Print the PrettyTable
        print(table_summary)

        # Convert the list to a DataFrame
        summary_df = pd.DataFrame(summary_data_for_excel)

        # Save DataFrame to an Excel file
        summary_df.to_excel(excel_path, index=False, engine="openpyxl")
        print(f"Summary saved to {excel_path}")
    else:
        print("No summary data available to save or print.")


summary_qa = SummaryQA(**model)


def summary_generation_handler():
    repository_url = request.args.get("repository_url")
    if not repository_url:
        return jsonify({"error": "Missing 'repository_url' parameter"}), 400

    if not global_variables.global_metadata:
        github_metadata_endpoint_handler()
        # repository_url = request.args.get("repository_url")
        # if not repository_url:
        #     return jsonify({"error": "Missing 'repository_url' parameter"}), 400

        # loop = asyncio.new_event_loop()
        # asyncio.set_event_loop(loop)

        # async def main():
        #     async with aiohttp.ClientSession() as session:
        #         metadata = await fetch_git_repository_metadata(
        #             session, repository_url
        #         )
        #         return metadata

        # metadata = loop.run_until_complete(main())
        # global_variables.global_metadata = metadata

    if not global_variables.global_cloned_repo_path:
        clone_repo_endpoint_handler()
        # loop = asyncio.new_event_loop()
        # asyncio.set_event_loop(loop)

        # async def main():
        #     async with aiohttp.ClientSession() as session:
        #         return await clone_github_repo(repository_url)

        # cloned_repo_path = loop.run_until_complete(main())
        # global_variables.global_cloned_repo_path = cloned_repo_path

    if global_variables.global_cloned_repo_path:
        path = Path(global_variables.global_cloned_repo_path)
        if not path.is_dir():
            return jsonify({"error": f"The path {path} is not a directory."}), 400

        summary = generate_summary(
            path,
            ignore_list=ignore_list_folder_structure,
            summary_component=summary_qa,
            ignore_extensions=ignore_list_extensions,
        )

        table_summary = PrettyTable()
        table_summary.field_names = ["File", "Description"]

        for item in summary:
            table_summary.add_row([item["file"], item["description"]])

        print(table_summary)
    else:
        return jsonify({"error": "Repository cloning failed or was skipped."}), 500

    # Assuming `summary` and `cloned_repo_path` are defined earlier in the code
    save_summary_to_excel_and_print_table(
        summary,
        global_variables.global_cloned_repo_path,
        excel_path=f"output/{global_variables.global_metadata.name}_summary.xlsx",
    )

    if summary:
        # Combine summaries, ignoring "Not a File" or error messages
        combined_summary = " ".join(
            [
                get_description_data(item["description"])
                for item in summary
                if get_description_data(item["description"])
                and get_description_data(item["description"]) != "Not a File"
                and get_description_data(item["description"]) != "."
                and not get_description_data(item["description"]).startswith(
                    "HTTP error 401"
                )
            ]
        )
        global_variables.global_combined_summary = combined_summary
        return combined_summary
    else:
        return jsonify({"error": "Summary generation failed."}), 500


def summary_generation():
    try:
        combined_summary = summary_generation_handler()
        return jsonify({"combined_summary": combined_summary}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def stream_data():
    def generate():
        repository_url = request.args.get("repository_url")
        if not repository_url:
            yield f"data: {jsonify({'error': 'Missing repository_url parameter'})}\n\n"
            return

        if not global_variables.global_metadata:
            github_metadata_endpoint_handler()

            if not global_variables.global_metadata:
                yield f"data: {jsonify({'error': 'Failed to extract metadata.'})}\n\n"
                return

            yield f"data: Metadata Fetch Sucessfull\n\n"
            time.sleep(1)

        if not global_variables.global_cloned_repo_path:
            clone_repo_endpoint_handler()

            if not global_variables.global_cloned_repo_path:
                yield f"data: {jsonify({'error': 'Repository cloning failed or was skipped.'})}\n\n"
                return

            yield f"data: Cloning repository successful: {global_variables.global_cloned_repo_path}\n\n"
            time.sleep(1)

        if global_variables.global_cloned_repo_path:
            path = Path(global_variables.global_cloned_repo_path)
            if not path.is_dir():
                yield f"data: {jsonify({'error': f'The path {path} is not a directory.'})}\n\n"
                return

            yield f"data: Generating summary...\n\n"
            time.sleep(1)

            summary = generate_summary(
                path,
                ignore_list=ignore_list_folder_structure,
                summary_component=summary_qa,
                ignore_extensions=ignore_list_extensions,
            )

            table_summary = PrettyTable()
            table_summary.field_names = ["File", "Description"]

            for item in summary:
                table_summary.add_row([item["file"], item["description"]])

            yield f"data: Summary generated.\n\n"
            time.sleep(1)

            # Save the summary to an Excel file
            save_summary_to_excel_and_print_table(
                summary,
                global_variables.global_cloned_repo_path,
                excel_path=f"output/{global_variables.global_metadata.name}_summary.xlsx",
            )

            if summary:
                combined_summary = " ".join(
                    [
                        get_description_data(item["description"])
                        for item in summary
                        if get_description_data(item["description"])
                        and get_description_data(item["description"]) != "Not a File"
                        and get_description_data(item["description"]) != "."
                        and not get_description_data(item["description"]).startswith(
                            "HTTP error 401"
                        )
                    ]
                )
                global_variables.global_combined_summary = combined_summary
                yield f"data: Combined Summary: {combined_summary}\n\n"
            else:
                yield f"data: {jsonify({'error': 'Summary generation failed.'})}\n\n"
        else:
            yield f"data: {jsonify({'error': 'Repository cloning failed or was skipped.'})}\n\n"

        yield "data: Process completed.\n\n"

    return Response(generate(), mimetype="text/event-stream")


# # %% [markdown]
# # <!-- @format -->
# #
# # #### Retry Summarization for Errors
# #
# # This section handles cases where summaries couldn't be generated initially, either due to errors or blank descriptions.
# #

# # %%
# from prettytable import PrettyTable

# # Check if there is any summary data available
# if summary:

#     # Variable to store rows with empty or error descriptions before adding to the table
#     blank_error_summary = []

#     # Iterate over each item in the summary
#     for item in summary:

#         # Retrieve the description data from the item
#         description_data = get_description_data(item["description"])

#         # Check if the description is empty or contains an error
#         if is_empty_or_error(description_data):

#             # Save the row data (file path and description) into a variable
#             row = [item["file"], description_data]

#             # Append the row to the list of blank or error summaries
#             blank_error_summary.append(row)

#     # Initialize PrettyTable to format the output
#     retry_table = PrettyTable()

#     # Set the field names (column headers) for the table
#     retry_table.field_names = ["File", "Description"]

#     # Add the saved rows (those with blank or error descriptions) to the table
#     for row in blank_error_summary:

#         retry_table.add_row(row)

#     # Print the PrettyTable with the rows that have blank or error descriptions
#     print(retry_table)

# else:
#     # Print a message if no summary data is available
#     print("NO SUMMARY DATA AVAILABLE")

# # %% [markdown]
# # <!-- @format -->
# #
# # #### Generate Summary for Specific Files
# #
# # This section provides functionality to manually generate or update summaries for individual files based on user input.
# #

# # %%
# from typing import List, Dict
# from pathlib import Path
# from prettytable import PrettyTable


# def generate_summary_for_file(
#     file_path: Path, qa_component: SummaryQA, existing_summaries: List[Dict[str, str]]
# ) -> List[Dict[str, str]]:
#     """
#     Generate or update a summary for a single file using the model.

#     Args:
#         file_path (Path): The path to the file to be summarized.
#         qa_component (SummaryQA): The component that generates the summary.
#         existing_summaries (List[Dict[str, str]]): A list of existing summaries to update.

#     Returns:
#         List[Dict[str, str]]: The updated list of summaries including the new or updated summary for the file.
#     """
#     file_name = file_path.name
#     updated = False

#     # Check if the file summary already exists in the existing_summaries list
#     for summary in existing_summaries:
#         if summary["file"] == file_name:
#             updated = True  # Mark as updated if the summary already exists
#             break

#     # If no summary exists for the file, add a new entry with an empty description
#     if not updated:
#         existing_summaries.append({"file": file_name, "description": ""})

#     try:
#         # Read the content of the file
#         with open(file_path, "r") as f:
#             file_content = f.read()

#         # Generate a summary for the file content using the qa_component
#         summary_text = qa_component.call(file_content)

#         # Update the description in the existing_summaries list
#         for summary in existing_summaries:
#             if summary["file"] == file_name:
#                 summary["description"] = summary_text
#                 break
#     except Exception as e:
#         # Handle exceptions and update the summary with an error message
#         for summary in existing_summaries:
#             if summary["file"] == file_name:
#                 summary["description"] = f"Error processing file {file_path}: {str(e)}"
#                 break

#     return existing_summaries


# if blank_error_summary:
#     # Initialize an empty list to store the summaries
#     summaries = []

#     # Prompt the user for a file path
#     user_input = input("Please enter the path to the file you want to summarize: ")
#     file_path = Path(user_input)

#     if file_path.is_file():
#         # Generate or update the summary for the specified file
#         summaries = generate_summary_for_file(file_path, summary_qa, summaries)

#         # Print the summary using PrettyTable
#         table_summary = PrettyTable()
#         table_summary.field_names = ["File", "Description"]

#         # Add each summary to the PrettyTable
#         for summary in summaries:
#             table_summary.add_row([summary["file"], summary["description"]])

#         print(table_summary)
#     else:
#         # If the path is not a valid file, print an error message
#         print(f"The path {file_path} is not a valid file.")

# %% [markdown]
# <!-- @format -->
#
# #### Combine Summaries
#
# This section combines all generated summaries into a single summary string, filtering out unnecessary or erroneous data.
#

# # %%
# if summary:
#     # Combine summaries, ignoring "Not a File" or error messages
#     combined_summary = " ".join(
#         [
#             get_description_data(item["description"])
#             for item in summary
#             if get_description_data(item["description"])
#             and get_description_data(item["description"]) != "Not a File"
#             and get_description_data(item["description"]) != "."
#             and not get_description_data(item["description"]).startswith(
#                 "HTTP error 401"
#             )
#         ]
#     )
#     print(combined_summary)
