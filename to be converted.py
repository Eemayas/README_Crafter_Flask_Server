
# %% [markdown]
# <!-- @format -->
#
# ### Key Features
#

# %%
from lightrag.core.generator import Generator
from lightrag.core.component import Component
from lightrag.components.model_client import OllamaClient

key_feature_template = r"""<SYS>
You are an expert computer engineer specializing in project documentation and coding, with advanced knowledge of various programming technologies.
</SYS>
Based on the provided file summaries:
{{input_str}},

Extract and list the key features (minimum 5 features) in a concise format. Each feature should include:
- Feature Name: A brief description of the feature and its significance.

Use the following format for listing the features:
- **Feature Name**: Description of the feature and its significance.

Ensure that the features are listed clearly and concisely, highlighting the most important aspects and functionalities that define the project’s value and just give me bulletin. No explanation need before and after bulletin likes "Here are the key features extracted from the provided code snippets:", "Let me know if you'd like me to help with anything else!"
Summary:
"""


class FeatureQA(Component):
    """Component for extracting key features of the project."""

    def __init__(self, model_client: OllamaClient, model_kwargs: dict):  # type: ignore
        """
        Initialize the FeatureQA component.

        Parameters:
        model_client (OllamaClient): The model client used for generating features.
        model_kwargs (dict): Additional model parameters.
        """
        super().__init__()
        self.generator = Generator(
            model_client=model_client,
            model_kwargs=model_kwargs,
            template=key_feature_template,
        )

    def call(self, summaries: str) -> str:
        """
        Extract key features based on file summaries.

        Parameters:
        summaries (str): A string containing the combined summaries of the project files.

        Returns:
        str: A list of key features extracted from the file summaries.
        """
        return self.generator.call({"input_str": summaries})

    async def acall(self, summaries: str) -> str:
        """
        Asynchronous version for extracting key features.

        Parameters:
        summaries (str): A string containing the combined summaries of the project files.

        Returns:
        str: A list of key features extracted from the file summaries.
        """
        return await self.generator.acall({"input_str": summaries})


def generate_key_feature(combined_summary: str, feature_component: FeatureQA) -> str:
    """
    Generate a list of key features based on file summaries.

    Parameters:
    combined_summary (str): A string containing the combined summaries of the project files.
    feature_component (FeatureQA): The component used to extract key features.

    Returns:
    str: The generated list of key features in the specified format.
    """
    return feature_component.generator.call({"input_str": combined_summary})


# %%
# Initialize FeatureQA component with model configuration
feature_qa = FeatureQA(**model)

if combined_summary:
    # Generate the key features based on the combined summary
    key_feature = generate_key_feature(summary, feature_component=feature_qa)

    # Process the key features to ensure proper formatting
    key_feature = get_description_data(key_feature)

    # Create markdown format for key features
    key_feature_markdown = "# Key Features\n" + key_feature

    # Print the key features in markdown format
    print(key_feature_markdown)

    # Display the key features in a Markdown view (for environments that support it)
    display(Markdown(key_feature_markdown))

# %% [markdown]
# <!-- @format -->
#
# ### Getting Started
#

# %%
from lightrag.core.generator import Generator
from lightrag.core.component import Component
from lightrag.components.model_client import OllamaClient

# Define the template for generating installation instructions
installation_template = r"""<SYS>
You are a highly skilled software engineer with expertise in documentation and project setup. You are adept at analyzing project summaries and folder structures to create clear installation instructions.
</SYS>
Based on the following project summary and folder structure:
Summary:
{{project_summary}}

Folder Structure:
{{folder_structure}}

GitHub repo Link:
{{repo_link}}

Create a detailed installation guide that includes:
1. **Prerequisites**: List any software, tools, or environment setups required before installation (e.g., Node.js, Docker) and provide link to download or install them.
2. **Setup Instructions**: Step-by-step instructions to set up the project, including installing dependencies, configuring environment variables, and any other necessary setup.
3. **Running the Project**: Detailed commands and steps to run the project locally, including any necessary build steps or configuration commands.
4. **Troubleshooting**: Common issues that may arise during installation and how to resolve them.
Ensure that the installation guide is comprehensive and easy to follow for someone new to the project and properly format them with heading like # Getting Started, ## Prerequisites, ## Installation, ## Running the Project, ## Tests, ## Troubleshooting
Summary:"""


class InstallationQA(Component):
    """Component for generating installation instructions."""

    def __init__(self, model_client: OllamaClient, model_kwargs: dict):  # type: ignore
        """
        Initialize the InstallationQA component.

        Parameters:
        - model_client (OllamaClient): The client to interact with the model.
        - model_kwargs (dict): Additional arguments for the model.
        """
        super().__init__()
        # Create a Generator instance with the provided model client and template
        self.generator = Generator(
            model_client=model_client,
            model_kwargs=model_kwargs,
            template=installation_template,
        )

    def call(self, project_summary: str, folder_structure: str, repo_link: str) -> str:
        """
        Generate installation guide based on project summary, folder structure, and repo link.

        Parameters:
        - project_summary (str): Summary of the project.
        - folder_structure (str): Structure of the project folders.
        - repo_link (str): URL of the GitHub repository.

        Returns:
        - str: The generated installation guide.
        """
        return self.generator.call(
            {
                "project_summary": project_summary,
                "folder_structure": folder_structure,
                "repo_link": repo_link,
            }
        )

    async def acall(
        self, project_summary: str, folder_structure: str, repo_link: str
    ) -> str:
        """
        Asynchronous version for generating installation guide.

        Parameters:
        - project_summary (str): Summary of the project.
        - folder_structure (str): Structure of the project folders.
        - repo_link (str): URL of the GitHub repository.

        Returns:
        - str: The generated installation guide.
        """
        return await self.generator.acall(
            {
                "project_summary": project_summary,
                "folder_structure": folder_structure,
                "repo_link": repo_link,
            }
        )


# %%
def generate_installation_guide(
    project_summary: str,
    folder_structure: str,
    repo_link: str,
    installation_component: InstallationQA,
) -> str:
    """
    Generate a comprehensive installation guide for the project.

    Parameters:
    - project_summary (str): Summary of the project.
    - folder_structure (str): Structure of the project folders.
    - repo_link (str): URL of the GitHub repository.
    - installation_component (InstallationQA): Component for generating the installation guide.

    Returns:
    - str: The generated installation guide.
    """
    return installation_component.call(project_summary, folder_structure, repo_link)


# Initialize InstallationQA component with model configuration
installation_qa = InstallationQA(**model)

if combined_summary:
    # Generate the installation guide using the provided summaries and folder structure
    installation_guide = generate_installation_guide(
        combined_summary,
        folder_structure_str,
        repository_url,
        installation_component=installation_qa,
    )
    # Process the generated guide (e.g., clean or format the content)
    installation_guide = get_description_data(installation_guide)

    # Format and display the installation guide in Markdown
    installation_guide_markdown = installation_guide
    print(installation_guide_markdown)
    display(Markdown(installation_guide_markdown))

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
# ### Contributing
#


# %%
def generate_contributing_guide(repo_link):
    """
    Generate a contributing guide for a GitHub repository.

    Parameters:
    repo_link (str): The URL of the GitHub repository.

    Returns:
    str: The contributing guide in markdown format.
    """
    import re

    # Extract the username and repository name from the link
    match = re.match(r"https://github.com/([^/]+)/([^/]+)", repo_link)
    if not match:
        raise ValueError("Invalid GitHub repository link")

    username, repo_name = match.groups()

    # Define the guide with placeholders for URLs
    guide_template = f"""
# Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/{username}/{repo_name}/pulls)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/{username}/{repo_name}/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/{username}/{repo_name}/issues)**: Submit bugs found or log feature requests for {repo_name}.

### Contributing Guidelines

1. **Fork the Repository**:
    - Start by forking the project repository to your GitHub account.
2. **Clone the Repository**:
    - Clone your forked repository to your local machine using the command:
    ```sh
    git clone https://github.com/your-username/{repo_name}.git
    ```
    - Replace ``your-username`` with your GitHub username.
3. **Create a New Branch**:
    - Create a new branch for your changes using the command:
    ```sh
    git checkout -b your-branch-name
    ```
4. **Make Your Changes**:
    - Edit, add, or delete files as needed. Ensure your changes align with the project's contribution guidelines.
5. **Commit Your Changes**:
    - Stage your changes and commit them with a descriptive message:
      ```bash
      git add .
      git commit -m "Your descriptive message"
      ```
6. **Push Your Changes:**
    - Push your branch to your forked repository:
      ```bash
      git push origin your-branch-name
      ```
7. **Create a Pull Request (PR):**
    - Go to the original repository on GitHub and click “Compare & pull request.” Provide a clear description of the changes and submit the PR.

Once your PR is reviewed and approved, it will be merged into the main branch.
    """

    return guide_template


# Generate the contributing guide for the given repository URL
contribution_markdown = generate_contributing_guide(repository_url)
print(contribution_markdown)
display(Markdown(contribution_markdown))

# %% [markdown]
# <!-- @format -->
#
# ### Contributors
#


# %%
def generate_contributors_table(contributors):
    """
    Generate a markdown table of contributors with their avatars, GitHub profiles, and contribution counts.

    Parameters:
    contributors (list): A list of contributor objects with attributes 'avatar_url', 'name', 'profile_url', and 'contributions'.

    Returns:
    str: The contributors table in markdown format.
    """
    # Start with the table header
    table = "| Avatar | Contributor | GitHub Profile | No of Contributions |\n"
    table += "|:--------:|:--------------:|:----------------:|:-------------------:|\n"

    # Add each contributor to the table
    for contributor in contributors:
        table += (
            f"| <img src='{contributor.avatar_url}' width='40' height='40' style='border-radius:50%;'/> | "
            f"{contributor.name} | "
            f"[@{contributor.name}]({contributor.profile_url}) | "
            f"{contributor.contributions} |\n"
        )

    return table


# Example usage for generating contributors markdown
contributor_markdown = f"""
# Contributors\n
{generate_contributors_table(metadata.contributors)}
    """
print(contributor_markdown)
display(Markdown(contributor_markdown))

# %% [markdown]
# <!-- @format -->
#
# ### License
#

# %%
license_markdown = """
# License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
"""

# Display the license information
print(license_markdown)
display(Markdown(license_markdown))

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
