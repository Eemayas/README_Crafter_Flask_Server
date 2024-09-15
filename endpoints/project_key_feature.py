from flask import jsonify, request
import global_variables
from lightrag.core.generator import Generator
from lightrag.core.component import Component
from lightrag.components.model_client import OllamaClient
from utils.llama_configurations import get_description_data, model
from endpoints.summary_generation import summary_generation_handler
from utils.check_new_repo_request import check_new_repo_requent


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


def project_key_feature():
    repository_url = request.args.get("repository_url")

    if not repository_url:
        return jsonify({"error": "Repository link is required."}), 400

    check_new_repo_requent(repository_url=repository_url)

    if not global_variables.global_combined_summary:
        print(
            "\nproject_key_feature -- Global combined summary is empty. Generating summary...\n"
        )
        summary_generation_handler()

    # Initialize FeatureQA component with model configuration
    feature_qa = FeatureQA(**model)

    if global_variables.global_combined_summary:
        # Generate the key features based on the combined summary
        key_feature = generate_key_feature(
            global_variables.global_combined_summary, feature_component=feature_qa
        )

        # Process the key features to ensure proper formatting
        key_feature = get_description_data(key_feature)
        # Create markdown format for key features
        key_feature_markdown = "# Key Features\n" + key_feature

        return jsonify({"key_feature_markdown": key_feature_markdown}), 200
    else:
        return (
            jsonify(
                {
                    "error": "No combined summary available to generate the key feature markdown."
                }
            ),
            404,
        )
