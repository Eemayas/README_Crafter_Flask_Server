from flask import jsonify, request
import global_variables
from lightrag.core.generator import Generator
from lightrag.core.component import Component
from lightrag.components.model_client import OllamaClient
from utils.check_new_repo_request import check_new_repo_requent

from utils.llama_configurations import get_description_data, model
from endpoints.summary_generation import summary_generation_handler

# Define the template for generating a project overview
project_overview_template = r"""<SYS>
You are a summarization assistant specialized in project documentation.
</SYS>
Based on the provided file summaries:
{{input_str}},

Generate a concise and descriptive one-paragraph overview of the project, including:
1. What the project is about (2 sentences).
2. What the project does (more than 3 sentences).
3. The technologies used.
4. The key features of the project.

Don't add predescription and post description in the answer.
Summary:"""


class OverviewQA(Component):
    """
    Component for generating a project overview.

    This class uses a model to generate a summary of the project based on the provided file summaries.
    """

    def __init__(self, model_client: OllamaClient, model_kwargs: dict):  # type: ignore
        """
        Initialize the OverviewQA component.

        Parameters:
        model_client (OllamaClient): The client used to interact with the model.
        model_kwargs (dict): Additional keyword arguments for the model.
        """
        super().__init__()
        self.generator = Generator(
            model_client=model_client,
            model_kwargs=model_kwargs,
            template=project_overview_template,
        )

    def call(self, summaries: str) -> str:
        """
        Generate a project overview based on file summaries.

        Parameters:
        summaries (str): The file summaries to use for generating the overview.

        Returns:
        str: The generated project overview.
        """
        return self.generator.call({"input_str": summaries})

    async def acall(self, summaries: str) -> str:
        """
        Asynchronous version for generating a project overview.

        Parameters:
        summaries (str): The file summaries to use for generating the overview.

        Returns:
        str: The generated project overview.
        """
        return await self.generator.acall({"input_str": summaries})


def generate_project_overview(
    combined_summary: str, overview_component: OverviewQA
) -> str:
    """
    Generate a concise and descriptive overview of the project.

    This function uses the OverviewQA component to create a project overview based on the combined summaries of the project files.

    Parameters:
    combined_summary (str): A string containing the combined summaries of the project files.
    overview_component (OverviewQA): The component used to generate the project overview.

    Returns:
    str: The generated project overview.
    """
    return overview_component.generator.call({"input_str": combined_summary})


def project_overview():
    repository_url = request.args.get("repository_url")

    if not repository_url:
        return jsonify({"error": "Repository link is required."}), 400

    check_new_repo_requent(repository_url=repository_url)

    if not global_variables.global_combined_summary:
        print(
            "project_overview -- Global combined summary is empty. Generating summary..."
        )
        summary_generation_handler()

    # Initialize OverviewQA component with model configuration
    overview_qa = OverviewQA(**model)

    if global_variables.global_combined_summary:
        # Generate the project overview
        project_overview = generate_project_overview(
            global_variables.global_combined_summary, overview_component=overview_qa
        )
        # Clean and format the project overview text
        project_overview = get_description_data(project_overview)
        project_overview_markdown = (
            "# Project Overview\n\n"
            + project_overview.strip().replace("\n\n", "\n\n").replace("  ", " ")
        )
        return jsonify({"project_overview_markdown": project_overview_markdown}), 200
    else:
        return (
            jsonify(
                {
                    "error": "No combined summary available to generate the project overview."
                }
            ),
            404,
        )
