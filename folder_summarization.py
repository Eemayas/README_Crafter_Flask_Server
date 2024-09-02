summary_one_line_template = r"""<SYS>
You are a summarization assistant specialized in providing concise, one-line summaries of the given tesxt.
</SYS>
Summarize the following text in one sentence:
{{input_str}}
One-line Summary:"""
from lightrag.core.generator import Generator
from lightrag.core.component import Component
from lightrag.components.model_client import OllamaClient


class OneLineSummaryQA(Component):
    """
    A component that uses a summarization model to generate one-line summaries for code.

    Parameters:
    model_client (OllamaClient): The model client to interact with the summarization model.
    model_kwargs (dict): Additional keyword arguments for the model.
    """

    def __init__(self, model_client: OllamaClient, model_kwargs: dict):  # type: ignore
        super().__init__()
        self.generator = Generator(
            model_client=model_client,
            model_kwargs=model_kwargs,
            template=summary_one_line_template,
        )

    def call(self, input: str) -> str:
        """
        Generate a one-line summary for the provided code using the model.

        Parameters:
        input (str): The code to be summarized.

        Returns:
        str: The generated one-line summary.
        """
        return self.generator.call({"input_str": input})

    async def acall(self, input: str) -> str:
        """
        Asynchronously generate a one-line summary for the provided code using the model.

        Parameters:
        input (str): The code to be summarized.

        Returns:
        str: The generated one-line summary.
        """
        return await self.generator.acall({"input_str": input})
    
from typing import List, Dict
from pathlib import Path
import concurrent.futures


def generate_one_line_summary(
    one_line_summary_component: OneLineSummaryQA,
    summary_list: List[Dict[str, str]],
) -> List[Dict[str, str]]:
    """
    Generate one-line summaries of files in the given path using the summarization model.

    Parameters:
    path (Path): The root directory to start scanning for files.
    ignore_list (List[str]): A list of directory or file names to ignore.
    one_line_summary_component (OneLineSummaryQA): The summarization component to use for generating summaries.
    ignore_extensions (List[str]): A list of file extensions to ignore.

    Returns:
    List[Dict[str, str]]: A list of dictionaries where each dictionary contains the file path and its one-line summary.
    """
    one_line_summary = []

    # Initialize tqdm progress bar
    pbar = tqdm(summary_list, desc="Processing summaries", unit="file")

    for summary in pbar:
        file_path = summary["file"]
        description = summary["description"]

        # Update the progress bar with the current file
        pbar.set_description(f"Processing file: {file_path}")

        # Generate one-line summary using the model
        one_line_summary_text = one_line_summary_component.call(description)
        one_line_summary.append(
            {
                "file": file_path,
                "description": get_description_data(one_line_summary_text),
            }
        )

    return one_line_summary


one_line_summary_qa = OneLineSummaryQA(**model)
one_line_summary_list = generate_one_line_summary(
    one_line_summary_component=one_line_summary_qa, summary_list=summary
)
print(one_line_summary_list)

from prettytable import PrettyTable


def print_summaries_pretty_table(one_line_summaries: List[Dict[str, str]]) -> None:
    """
    Print the one-line summaries using PrettyTable.

    Parameters:
    one_line_summaries (List[Dict[str, str]]): A list of dictionaries containing file paths and their one-line summaries.
    """
    table = PrettyTable()
    table.field_names = ["File", "One-Line Summary"]

    for summary in one_line_summaries:
        table.add_row([summary["file"], summary["description"]])

    print(table)


print_summaries_pretty_table(one_line_summary_list)

from prettytable import PrettyTable
from pathlib import Path


def format_summaries_as_html(
    one_line_summaries: List[Dict[str, str]], base_url: str
) -> str:
    """
    Format the one-line summaries into an HTML-like format with PrettyTable.

    Parameters:
    one_line_summaries (List[Dict[str, str]]): A list of dictionaries containing file paths and their one-line summaries.
    base_url (str): The base URL for GitHub to generate links to files.

    Returns:
    str: A formatted string in HTML-like format.
    """
    result = ""

    # Group summaries by folders
    grouped_summaries = {}
    for summary in one_line_summaries:
        path = Path(summary["file"])
        folder = path.parent
        if folder not in grouped_summaries:
            grouped_summaries[folder] = []
        grouped_summaries[folder].append(summary)

    # Format each folder and its summaries
    for folder, summaries in grouped_summaries.items():
        # Convert folder path to relative path
        folder_path = str(folder).replace("\\", "/")
        result += f"<details closed><summary>{folder_path}({base_url}/{folder_path})</summary>\n\n"

        table = PrettyTable()
        table.field_names = ["File", "Summary"]
        for summary in summaries:
            file_name = Path(summary["file"]).name
            file_url = f"{base_url}/{summary['file'].as_posix()}"
            table.add_row(
                [f"[{file_name}]({file_url})", f"<code>{summary['description']}</code>"]
            )

        result += table.get_html_string() + "\n\n"
        result += "</details>\n"

    return result


# Example usage:
html_summary = format_summaries_as_html(one_line_summary_list, repository_url)
print(html_summary)

display(Markdown(html_summary))