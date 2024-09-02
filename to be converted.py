
# %% [markdown]
# <!-- @format -->
#
# ### API Reference
#

# %%
from lightrag.core.generator import Generator
from lightrag.core.component import Component


# Define the template for API reference extraction
api_template_v1 = r"""<SYS>
You are an API reference extraction assistant specialized in coding files.
</SYS>
Please extract the API reference from the following code and provide the following information:
1. API endpoint
2. Purpose of the API
3. Parameters
4. Parameter types
5. Parameter descriptions
6. HTTP method

Format:

#### {Purpose of the API}

```http
  {HTTP method} {API endpoint}
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


If there is no API Reference, please return "No API Reference". No description needed in that case. Avoid asking for response like this "Let me know if you'd like me to clarify anything!" and write the Notes in third person narrative

Code:
{{input_str}}
"""

# Define the template for API reference extraction
api_template = r"""
You are an API reference extraction assistant specializing in coding files. Your task is to identify and extract information about HTTP API methods from the provided code. Focus only on endpoints that use HTTP methods (GET, POST, PUT, DELETE, etc.).

For each API reference found, provide the following details:
1. API endpoint
2. Purpose of the API
3. Parameters
4. Parameter types
5. Parameter descriptions
6. HTTP method

If the code does not include any API references or if no HTTP methods are present, return "No API Reference."

Format:

#### {Purpose of the API}

```http
  {HTTP method} {API endpoint}
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

    def __init__(self, model_client: OllamaClient, model_kwargs: dict):  # type: ignore
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


# %%
import os
from pathlib import Path
from typing import List, Dict
from tqdm import tqdm
from prettytable import PrettyTable


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

if cloned_repo_path:
    path = Path(cloned_repo_path)
    if not path.is_dir():
        print(f"The path {path} is not a directory.")
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

    # Print the PrettyTable
    print(api_table)
else:
    print("Repository cloning failed or was skipped.")

# %%
for item in api_reference:
    # Check if the item is a dictionary and contains the 'api_reference' key
    if isinstance(item, dict) and "api_reference" in item:
        description_data = get_description_data(item["api_reference"])

        # Skip items with no API reference
        if "No API Reference" in description_data:
            continue

        # Add valid items to the PrettyTable
        api_table.add_row([item["file"], description_data])
        api_data_for_excel.append(
            {"File": item["file"], "api_reference": description_data}
        )
    else:
        # Print a message if the item format is unexpected
        print(f"Unexpected item format: {item}\n")

# %% [markdown]
# <!-- @format -->
#
# #### API Reference Data Export
#

# %%
import pandas as pd

if api_data_for_excel:
    # Convert the list of dictionaries to a DataFrame
    df_api_data = pd.DataFrame(api_data_for_excel)

    # Define the path and name for the Excel file
    excel_path = f"output/{metadata.name}_api_reference.xlsx"

    # Save the DataFrame to an Excel file with the specified path
    df_api_data.to_excel(excel_path, index=False, engine="openpyxl")

    # Print a confirmation message with the file path
    print(f"API reference data saved to {excel_path}")

# %% [markdown]
# <!-- @format -->
#
# #### API Reference Markdown
#

# %%
# Convert to string in the desired format
api_reference_markdown = "# API Reference\n\n"
for i, entry in enumerate(api_data_for_excel, start=1):
    file = entry["File"]
    api_reference = entry["api_reference"]
    # Append formatted API reference to the markdown string
    api_reference_markdown += f"**File:** {file}\n\n{api_reference}\n\n"

print(api_reference_markdown)
display(Markdown(api_reference_markdown))





# %% [markdown]
# <!-- @format -->
#
# # Markdown
#

# %% [markdown]
# <!-- @format -->
#
# ### Combine and Save README Content
#

# %%
# Combine all markdown sections into a single markdown string
combined_markdown = (
    header_markdown
    + "\n\n---\n"
    + project_overview_markdown
    + "\n\n---\n"
    + key_feature_markdown
    + "\n\n---\n"
    + folder_structure_markdown
    + "\n\n---\n"
    + installation_guide_markdown
    + "\n\n---\n"
    + api_reference_markdown
    + "\n\n---\n"
    + contribution_markdown
    + "\n\n---\n"
    + contributor_markdown
    + "\n\n---\n"
    + license_markdown
    + "\n\n---\n"
)

# Display the combined markdown
print(combined_markdown)
display(Markdown(combined_markdown))

# %% [markdown]
# <!-- @format -->
#
# ### Save README to File
#

# %%
# Specify the file name
file_name = f"output/{metadata.name}_README.md"

# Open the file in write mode with utf-8 encoding and save the content
with open(file_name, "w", encoding="utf-8") as file:
    file.write(str(combined_markdown))

print(f"{file_name} has been created and saved.")
