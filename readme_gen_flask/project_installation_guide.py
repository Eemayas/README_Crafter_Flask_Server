from flask import jsonify, request
import global_variables
from lightrag.core.generator import Generator
from lightrag.core.component import Component
from lightrag.components.model_client import OllamaClient

from folder_structure import folder_structure_endpoint_handler
from utils.llama_configurations import get_description_data, model
from summary_generation import summary_generation_handler

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


def project_installation_guide():
    repository_url = request.args.get("repository_url")

    if not repository_url:
        return jsonify({"error": "Repository link is required."}), 400

    if not global_variables.global_combined_summary:
        summary_generation_handler()

    if not global_variables.global_folder_structure_str:
        folder_structure_endpoint_handler()

    # Initialize InstallationQA component with model configuration
    installation_qa = InstallationQA(**model)

    if global_variables.global_combined_summary:
        # Generate the installation guide using the provided summaries and folder structure
        installation_guide = generate_installation_guide(
            global_variables.global_combined_summary,
            global_variables.folder_structure_str,
            repository_url,
            installation_component=installation_qa,
        )
        # Process the generated guide (e.g., clean or format the content)
        installation_guide = get_description_data(installation_guide)

        # Format and display the installation guide in Markdown
        installation_guide_markdown = installation_guide

        return (
            jsonify({"installation_guide_markdown": installation_guide_markdown}),
            200,
        )
    else:
        return (
            jsonify(
                {
                    "error": "No combined summary available to generate the installation guide markdown."
                }
            ),
            404,
        )


# # Initialize InstallationQA component with model configuration
# installation_qa = InstallationQA(**model)

# if combined_summary:
#     # Generate the installation guide using the provided summaries and folder structure
#     installation_guide = generate_installation_guide(
#         combined_summary,
#         folder_structure_str,
#         repository_url,
#         installation_component=installation_qa,
#     )
#     # Process the generated guide (e.g., clean or format the content)
#     installation_guide = get_description_data(installation_guide)

#     # Format and display the installation guide in Markdown
#     installation_guide_markdown = installation_guide
#     print(installation_guide_markdown)
#     display(Markdown(installation_guide_markdown))
