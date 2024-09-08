from flask import jsonify, request
import global_variables
from endpoints.github_metadata import github_metadata_endpoint_handler
from utils.check_new_repo_request import check_new_repo_requent


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


def project_contributors():
    repository_url = request.args.get("repository_url")

    if not repository_url:
        return jsonify({"error": "Repository link is required."}), 400
    
    check_new_repo_requent(repository_url=repository_url)

    if not global_variables.global_metadata:
        print("No global metadata found. Retrieving metadata.....")
        github_metadata_endpoint_handler()

    try:
        # Generate the contributors markdown table
        contributors_markdown = f"""
# Contributors\n
{generate_contributors_table(global_variables.global_metadata.contributors)}
        """

        return jsonify({"contributors_markdown": contributors_markdown}), 200
    except KeyError as e:
        return jsonify({"error": f"Missing field in contributor data: {e}"}), 400
