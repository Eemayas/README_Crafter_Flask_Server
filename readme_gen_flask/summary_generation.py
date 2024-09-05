import json
from lightrag.core.generator import Generator
from lightrag.core.component import Component
from lightrag.components.model_client import OllamaClient
import os
from pathlib import Path
from typing import List, Dict
import typing
from prettytable import PrettyTable
from tqdm import tqdm
from github_metadata import github_metadata_endpoint_handler
from clone_github import clone_repo_endpoint_handler
from utils.llama_configurations import model, get_description_data
from constants import ignore_list_folder_structure, ignore_list_extensions
import pandas as pd
from prettytable import PrettyTable
from flask import jsonify, request, Response, stream_with_context
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
    redo = request.args.get("redo", "false").lower() == "true"
    if not repository_url:
        return jsonify({"error": "Missing 'repository_url' parameter"}), 400

    if not global_variables.global_metadata:
        print("No global metadata found. Retrieving metadata.....")
        github_metadata_endpoint_handler()

    if not global_variables.global_cloned_repo_path:
        print("No clone folder found. Cloning Folder.....")
        clone_repo_endpoint_handler()

    excel_path = f"output/{global_variables.global_metadata.name}_summary.xlsx"
    # excel_path = f"output/Daraz_Scraper_summary.xlsx"

    if redo or not os.path.exists(excel_path):
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

            # print(table_summary)

            save_summary_to_excel_and_print_table(
                summary,
                global_variables.global_cloned_repo_path,
                excel_path=excel_path,
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
                summary_dict = {
                    item["file"]: item["description"]
                    for item in summary
                    if get_description_data(item["description"])
                    and get_description_data(item["description"]) != "Not a File"
                    and get_description_data(item["description"]) != "."
                    and not get_description_data(item["description"]).startswith(
                        "HTTP error 401"
                    )
                }
                #
                global_variables.global_combined_summary = combined_summary
                global_variables.global_summary_dict = summary_dict
                return summary_dict
            else:
                return jsonify({"error": "Summary generation failed."}), 500
        else:
            return jsonify({"error": "Repository cloning failed or was skipped."}), 500
    else:
        # Load the summary from the existing Excel file
        try:
            summary_df = pd.read_excel(excel_path, engine="openpyxl")
            summary_data = summary_df.to_dict(orient="records")

            table_summary = PrettyTable()
            table_summary.field_names = ["File", "Description"]

            for item in summary_data:
                table_summary.add_row([item["File"], item["Description"]])

            # print(table_summary)

            # Extract combined summary from the loaded data
            combined_summary = " ".join(
                [
                    get_description_data(item["Description"])
                    for item in summary_data
                    if get_description_data(item["Description"])
                    and get_description_data(item["Description"]) != "Not a File"
                    and get_description_data(item["Description"]) != "."
                    and not get_description_data(item["Description"]).startswith(
                        "HTTP error 401"
                    )
                ]
            )
            summary_dict = {
                item["File"]: item["Description"]
                for item in summary_data
                if get_description_data(item["Description"])
                and get_description_data(item["Description"]) != "Not a File"
                and get_description_data(item["Description"]) != "."
                and not get_description_data(item["Description"]).startswith(
                    "HTTP error 401"
                )
            }

            global_variables.global_combined_summary = combined_summary
            global_variables.global_summary_dict = summary_dict
            return summary_dict
        except Exception as e:
            return (
                jsonify({"error": f"Failed to load or process Excel file: {str(e)}"}),
                500,
            )


def summary_generation():
    try:
        # Call the handler function
        result = summary_generation_handler()

        # Check if result is an instance of Response
        if isinstance(result, Response):
            return result  # Return the Response object directly

        # If result is not a Response, jsonify it
        return jsonify(result), 200
    except Exception as e:
        # Handle unexpected exceptions
        return jsonify({"error": str(e)}), 500


def file_summary_generation():
    repository_url = request.args.get("repository_url")
    file_path = request.args.get("file_path")
    if not repository_url:
        return jsonify({"error": "Missing 'repository_url' parameter"}), 400
    if not file_path:
        return jsonify({"error": "Missing 'file_path' parameter"}), 400

    if not global_variables.global_metadata:
        print("No global metadata found. Retrieving metadata.....")
        github_metadata_endpoint_handler()

    excel_path = Path(
        f"output/{global_variables.global_metadata.name}_api_reference_data.xlsx"
    )
    # excel_path = f"output/Daraz_Scraper_summary.xlsx"

    file_path = Path(file_path)
    excel_path = Path(excel_path)

    # Check if the file exists
    if not file_path.is_file():
        return jsonify({"error": f"The file {file_path} does not exist."}), 400

    # Initialize SummaryQA component
    summary_qa = SummaryQA(**model)
    try:
        # Extract HTTPS requests using SummaryQA
        with open(file_path, "r") as f:
            file_content = f.read()
        summary_text = summary_qa.call(file_content)
        # Check if the Excel file exists
        if excel_path.exists():
            # Load existing data
            df_summary_data = pd.read_excel(excel_path, engine="openpyxl")
            existing_data = df_summary_data.to_dict(orient="records")

            # Check if the file path already exists
            updated = False
            for entry in existing_data:
                if entry.get("File") == str(file_path):
                    # Update existing entry
                    entry["Description"] = get_description_data(summary_text)
                    updated = True
                    break

            if not updated:
                print("I am Here3")
                # Add new entry if file path does not exist
                existing_data.append(
                    {
                        "File": str(file_path),
                        "Description": get_description_data(summary_text),
                    }
                )

            # Save the updated data to Excel
            df_updated_data = pd.DataFrame(existing_data)
            df_updated_data.to_excel(excel_path, index=False, engine="openpyxl")
            return jsonify(
                {
                    "message": "Excel file updated with HTTPS request data.",
                    "updated_file": str(file_path),
                    "new_data": {
                        "File": str(file_path),
                        "Description": get_description_data(summary_text),
                    },
                }
            )
        else:

            # Create a new Excel file with the data
            new_data = [
                {
                    "File": str(file_path),
                    "Description": get_description_data(summary_text),
                }
            ]
            df_new_data = pd.DataFrame(new_data)
            df_new_data.to_excel(excel_path, index=False, engine="openpyxl")
            return jsonify(
                {
                    "message": "New Excel file created and data added.",
                    "created_file": str(excel_path),
                }
            )
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


def stream_data():
    def generate():
        repository_url = request.args.get("repository_url")
        if not repository_url:
            yield f"data: {jsonify({'error': 'Missing repository_url parameter'})}\n\n"
            return

        if not global_variables.global_metadata:
            print("No global metadata found. Retrieving metadata.....")
            github_metadata_endpoint_handler()

            if not global_variables.global_metadata:
                yield f"data: {jsonify({'error': 'Failed to extract metadata.'})}\n\n"
                return

            yield f"data: Metadata Fetch Sucessfull\n\n"
            time.sleep(1)

        if not global_variables.global_cloned_repo_path:
            print("No clone folder found. Cloning Folder.....")
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


def generate_summary_stream(
    path: Path,
    ignore_list: List[str],
    summary_component: SummaryQA,
    ignore_extensions: List[str],
) -> typing.Generator[Dict[str, str], None, None]:

    summary = []
    files_to_process = []

    for root, dirs, files in os.walk(path):
        relative_root = os.path.relpath(root, path)

        if any(ignored in relative_root.split(os.sep) for ignored in ignore_list):
            continue

        if relative_root == ".":
            summary.append({"file": "Modules", "description": "."})
        else:
            summary.append({"file": relative_root, "description": "Not a File"})

        for file in files:
            file_path = Path(root) / file

            if any(ignored in file_path.parts for ignored in ignore_list):
                continue

            if file_path.suffix.lower() in ignore_extensions:
                continue

            files_to_process.append(file_path)
    pbar = tqdm(files_to_process, unit="file")
    for file_path in pbar:
        pbar.set_description(f"Processing file - {file_path}")
        n = pbar.format_dict.get("n", 0)
        total = pbar.format_dict.get(
            "total", 1
        )  # Default to 1 to avoid division by zero
        percentage = (n / total) * 100 if total else 0
        elapsed = pbar.format_dict.get("elapsed", 0.0)
        rate = pbar.format_dict.get("rate", 0.0)
        remaining = total - n
        try:
            with open(file_path, "r") as f:
                file_content = f.read()

            summary_text = summary_component.call(file_content)
            summary.append(
                {
                    "file": str(file_path),
                    "description": get_description_data(summary_text),
                }
            )

            # Send intermediate progress as SSE
            yield f"""data: {json.dumps({
                'file': str(file_path), 
                'description':get_description_data(summary_text),
                "percentage":percentage,
                "n":n,
                "total":total,
                "elapsed":elapsed,
                "rate":rate,
                "remaining":remaining})}\n\n"""

        except Exception as e:
            summary.append({"file": str(file_path), "description": f"Error: {str(e)}"})
            yield f"""data: {json.dumps({
                'file': str(file_path), 
                'description': f'Error: {str(e)}',          
                "percentage":percentage,
                "n":n,
                "total":total,
                "elapsed":elapsed,
                "rate":rate,
                "remaining":remaining})}\n\n"""

    global_variables.global_combined_summary = summary

    yield f"data: {json.dumps({'final_summary': summary})}\n\n"


def summary_generation_handler_stream():
    repository_url = request.args.get("repository_url")
    redo = request.args.get("redo", "false").lower() == "true"
    if not repository_url:
        return jsonify({"error": "Missing 'repository_url' parameter"}), 400

    @stream_with_context
    def generate_and_stream_summary():
        if not global_variables.global_metadata:
            print("No global metadata found. Retrieving metadata.....")
            github_metadata_endpoint_handler()
            yield "event: status\ndata: Retrieved GitHub metadata\n\n"

        if not global_variables.global_cloned_repo_path:
            print("No clone folder found. Cloning Folder.....")
            clone_repo_endpoint_handler()
            yield "event: status\ndata: Repository cloned\n\n"

        excel_path = f"output/{global_variables.global_metadata.name}_summary.xlsx"

        if redo or not os.path.exists(excel_path):
            if global_variables.global_cloned_repo_path:
                path = Path(global_variables.global_cloned_repo_path)
                if not path.is_dir():
                    yield f"event: error\ndata: The path {path} is not a directory.\n\n"
                    return

                yield "event: status\ndata: Generating summary...\n\n"

                # Ensure this line is uncommented
                for summary_event in generate_summary_stream(
                    path,
                    ignore_list=ignore_list_folder_structure,
                    summary_component=summary_qa,
                    ignore_extensions=ignore_list_extensions,
                ):
                    yield summary_event
                summary = global_variables.global_combined_summary
                table_summary = PrettyTable()
                table_summary.field_names = ["File", "Description"]

                for item in summary:
                    table_summary.add_row([item["file"], item["description"]])

                save_summary_to_excel_and_print_table(
                    summary,
                    global_variables.global_cloned_repo_path,
                    excel_path=excel_path,
                )

                if summary:
                    combined_summary = " ".join(
                        [
                            get_description_data(item["description"])
                            for item in summary
                            if get_description_data(item["description"])
                            and get_description_data(item["description"])
                            != "Not a File"
                            and get_description_data(item["description"]) != "."
                            and not get_description_data(
                                item["description"]
                            ).startswith("HTTP error 401")
                        ]
                    )
                    global_variables.global_combined_summary = combined_summary
                    yield f"event: combined_summary\ndata: {combined_summary}\n\n"
                else:
                    yield "event: error\ndata: Summary generation failed.\n\n"
            else:
                yield "event: error\ndata: Repository cloning failed or was skipped.\n\n"
        else:
            try:
                summary_df = pd.read_excel(excel_path, engine="openpyxl")
                summary_data = summary_df.to_dict(orient="records")

                table_summary = PrettyTable()
                table_summary.field_names = ["File", "Description"]

                for item in summary_data:
                    table_summary.add_row([item["File"], item["Description"]])

                combined_summary = " ".join(
                    [
                        get_description_data(item["Description"])
                        for item in summary_data
                        if get_description_data(item["Description"])
                        and get_description_data(item["Description"]) != "Not a File"
                        and get_description_data(item["Description"]) != "."
                        and not get_description_data(item["Description"]).startswith(
                            "HTTP error 401"
                        )
                    ]
                )
                global_variables.global_combined_summary = combined_summary
                yield f"event: combined_summary\ndata: {combined_summary}\n\n"
            except Exception as e:
                yield f"event: error\ndata: Failed to load or process Excel file: {str(e)}\n\n"

    return Response(generate_and_stream_summary(), content_type="text/event-stream")


# TODO: Retry Summarization for Errors
