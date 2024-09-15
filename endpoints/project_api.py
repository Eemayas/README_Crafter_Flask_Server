import os
import pandas as pd
from tqdm import tqdm
from flask import jsonify, request
from prettytable import PrettyTable

from pathlib import Path
from typing import List, Dict

from lightrag.core.generator import Generator
from lightrag.core.component import Component

import global_variables

from constants import (
    ignore_list_folder_structure,
    specific_ignores_api,
    api_ignore_extensions,
)

from utils.save_dataframe_to_excel import save_dataframe_to_excel
from utils.handle_metadata_and_clone import handle_metadata_and_clone
from utils.llama_configurations import get_description_data, model
from utils.check_new_repo_request import check_new_repo_requent

# Define the template for API reference extraction
api_template = r"""
You are an HTTP method extraction assistant specializing in coding files. Your task is to identify and extract information about HTTP methods from the provided code. Focus only on endpoints that use HTTP methods (GET, POST, PUT, DELETE, etc.).

For each API reference found, provide the following details:
1. HTTP endpoint
2. Purpose of the HTTP endpoints
3. Parameters
4. Parameter types
5. Parameter descriptions
6. HTTP method

If the code does not include any API references or if no HTTP methods are present, return "No API Reference."

Format:

#### {Purpose of the API}

```http
  {HTTP method} {HTTP endpoint}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
{parameter_rows}

Example:

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |
| `limit`   | `integer`| **Optional**. Limit the number of items |

Code:
{{input_str}}

"""


class APIReferenceExtractorQA(Component):
    """Component for extracting API references from code."""

    def __init__(self, model_client, model_kwargs: dict):  # type: ignore
        super().__init__()
        self.generator = Generator(
            model_client=model_client,
            model_kwargs=model_kwargs,
            template=api_template,
        )

    def call(self, input: str) -> str:
        """Extract API references from the provided code."""
        return self.generator.call({"input_str": input})

    async def acall(self, input: str) -> str:
        """Asynchronous extraction of API references."""
        return await self.generator.acall({"input_str": input})


def generate_api_reference(
    path: Path,
    ignore_list: List[str],
    api_reference_extractor_component: APIReferenceExtractorQA,
    api_ignore_extensions: List[str],
) -> List[Dict[str, str]]:
    """
    Generate an API reference of files in the given path using the model.

    This function processes files in the specified directory, excluding those
    listed in the ignore list and files with extensions specified in
    `api_ignore_extensions`. It uses the `APIReferenceExtractorQA` component
    to extract API references from the file content.

    Parameters:
    path (Path): The directory path containing the files to process.
    ignore_list (List[str]): List of folder names or file names to ignore.
    api_reference_extractor_component (APIReferenceExtractorQA): The component used to extract API references.
    api_ignore_extensions (List[str]): List of file extensions to ignore.

    Returns:
    List[Dict[str, str]]: A list of dictionaries where each dictionary contains
    the file path and the extracted API reference or an error message.
    """
    api_reference = []
    files_to_process = []

    for root, dirs, files in os.walk(path):
        relative_root = os.path.relpath(root, path)

        # Skip directories that are in the ignore list
        if any(ignored in relative_root.split(os.sep) for ignored in ignore_list):
            continue

        for file in files:
            file_path = Path(root) / file

            # Skip files that are in the ignore list or have ignored extensions
            if any(ignored in file_path.parts for ignored in ignore_list):
                continue

            if any(ignore in file_path.name for ignore in specific_ignores_api):
                continue

            if file_path.suffix.lower() in api_ignore_extensions:
                continue

            files_to_process.append(file_path)

    # Create a progress bar for processing files
    pbar = tqdm(files_to_process, unit="file")
    for file_path in pbar:
        # Update the progress bar description
        pbar.set_description(f"Processing files - {file_path}")
        try:
            with open(file_path, "r") as f:
                file_content = f.read()

            # Extract API references from the file content
            api_text = api_reference_extractor_component.call(file_content)
            api_reference.append({"file": file_path, "api_reference": api_text})
        except Exception as e:
            # Append an error message if file processing fails
            api_reference.append(
                {"file": file_path, "api_reference": f"Error processing file: {str(e)}"}
            )

    return api_reference


# Initialize APIReferenceExtractorQA component with model configuration
api_reference_extractor_qa = APIReferenceExtractorQA(**model)


import pandas as pd
from pathlib import Path


def update_https_requests_endpoint():
    repository_url = request.args.get("repository_url")
    file_path = request.args.get("file_path")
    if not repository_url:
        return jsonify({"error": "Missing 'repository_url' parameter"}), 400

    check_new_repo_requent(repository_url=repository_url)

    if not file_path:
        return jsonify({"error": "Missing 'file_path' parameter"}), 400

    handle_metadata_and_clone(function_name="update_https_requests_endpoint")

    excel_path = Path(
        f"output/{global_variables.global_metadata.name}_api_reference_data.xlsx"
    )

    file_path = Path(file_path)
    excel_path = Path(excel_path)

    # Check if the file exists
    if not file_path.is_file():
        return jsonify({"error": f"The file {file_path} does not exist."}), 400

    # Initialize APIReferenceExtractorQA component
    api_reference_extractor_qa = APIReferenceExtractorQA(**model)

    try:
        # Extract HTTPS requests using APIReferenceExtractorQA
        with open(file_path, "r") as f:
            file_content = f.read()

        api_text = api_reference_extractor_qa.call(file_content)

        # Check if the Excel file exists
        if excel_path.exists():
            # Load existing data
            df_api_data = pd.read_excel(excel_path, engine="openpyxl")
            existing_data = df_api_data.to_dict(orient="records")

            # Check if the file path already exists
            updated = False
            for entry in existing_data:
                if entry.get("File") == str(file_path):
                    # Update existing entry
                    entry["api_reference"] = api_text
                    updated = True
                    break

            if not updated:
                # Add new entry if file path does not exist
                existing_data.append(
                    {"File": str(file_path), "api_reference": api_text}
                )

            # Save the updated data to Excel
            df_updated_data = pd.DataFrame(existing_data)
            save_dataframe_to_excel(data=df_updated_data, excel_path=excel_path)
            return jsonify(
                {
                    "message": "Excel file updated with HTTPS request data.",
                    "updated_file": str(file_path),
                    "new_data": {"File": str(file_path), "api_reference": api_text},
                }
            )
        else:
            # Create a new Excel file with the data
            new_data = [{"File": str(file_path), "api_reference": api_text}]
            df_new_data = pd.DataFrame(new_data)
            save_dataframe_to_excel(data=df_new_data, excel_path=excel_path)
            return jsonify(
                {
                    "message": "New Excel file created and data added.",
                    "created_file": str(excel_path),
                }
            )
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


def get_api_references():
    """
    Endpoint to return the API reference data as a dictionary and save it to an Excel file.
    """
    repository_url = request.args.get("repository_url")
    redo = request.args.get("redo", "false").lower() == "true"
    if not repository_url:
        return jsonify({"error": "Missing 'repository_url' parameter"}), 400

    check_new_repo_requent(repository_url=repository_url)

    handle_metadata_and_clone(function_name="get_api_references")

    excel_path = Path(
        f"output/{global_variables.global_metadata.name}_api_reference_data.xlsx"
    )

    # Check if the Excel file exists and if redo is not requested
    if excel_path.exists() and not redo:
        # Load the data from the existing Excel file
        df_api_data = pd.read_excel(excel_path, engine="openpyxl")
        api_data_for_excel = df_api_data.to_dict(orient="records")
        return jsonify(
            {
                "message": f"Data loaded from {str(excel_path)}",
                "api_reference": api_data_for_excel,
            }
        )

    if global_variables.global_cloned_repo_path:
        path = Path(global_variables.global_cloned_repo_path)
        if not path.is_dir():
            return (
                jsonify(
                    {
                        "error": f"The path {global_variables.global_cloned_repo_path} is not a directory."
                    }
                ),
                400,
            )

        # Generate API references
        api_reference = generate_api_reference(
            path,
            ignore_list=ignore_list_folder_structure,
            api_reference_extractor_component=api_reference_extractor_qa,
            api_ignore_extensions=api_ignore_extensions,
        )

        # Initialize PrettyTable for formatted output
        api_table = PrettyTable()
        api_table.field_names = ["File", "API Reference"]

        # Create a list to hold data for further processing (e.g., saving to Excel)
        api_data_for_excel = []

        for item in api_reference:
            # Process the API reference text to get description data
            description_data = get_description_data(item["api_reference"])
            if "No API Reference" in description_data:
                continue
            # Add rows to the PrettyTable
            api_table.add_row([item["file"], description_data])
            api_data_for_excel.append(
                {"File": item["file"], "api_reference": description_data}
            )

        # Save to Excel
        if api_data_for_excel:
            # Convert any Path objects in api_data_for_excel to strings
            for data in api_data_for_excel:
                if isinstance(data.get("File"), Path):
                    data["File"] = str(data["File"])

            # Convert the list of dictionaries to a DataFrame
            df_api_data = pd.DataFrame(api_data_for_excel)

            # Save the DataFrame to an Excel file with the specified path
            save_dataframe_to_excel(data=df_api_data, excel_path=excel_path)

            print(f"\nAPI reference data saved to {str(excel_path)}\n")

        return jsonify(
            {
                "message": "API reference data generated",
                "api_reference": api_data_for_excel,
            }
        )
    else:
        return jsonify({"error": "Repository cloning failed or was skipped."}), 400
