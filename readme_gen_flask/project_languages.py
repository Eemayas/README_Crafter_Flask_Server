from flask import Flask, request, jsonify
import json
import requests
import os
from constants import extensions, frameworks_extensions, tools_extensions
import global_variables
from github_metadata import github_metadata_endpoint_handler
from clone_github import clone_repo_endpoint_handler
from utils.check_new_repo_request import check_new_repo_requent


# Global variables to store detected languages, frameworks, and tools
languages_found = set()
frameworks_found = set()
tools_found = set()


# Load shields.io icons data from a JSON file
def load_shields_data(filename):
    with open(filename, "r") as file:
        return json.load(file)


# Get badges URLs for technologies
def get_shields_urls(technologies, shields_data):
    results = {}
    for tech in technologies:
        if tech in shields_data:
            url, _ = shields_data[tech]
            results[tech] = url.format("for-the-badge")
        else:
            fallback_url = f"https://img.shields.io/badge/{tech}-ED8B00?logo={tech}&logoColor=white"
            results[tech] = fallback_url
    return results


# Generate HTML for badges
def generate_language_badges(urls_map):
    badges_html = "\n".join(
        f'  <img src="{urls_map[language]}" alt="{language}">'
        for language in urls_map.keys()
    )
    html_template = f"""
<p align="center">
{badges_html}
</p>
    """
    return html_template


def get_project_languages():
    repository_url = request.args.get("repository_url")
    if not repository_url:
        return jsonify({"error": "Missing 'repository_url' parameter"}), 400
    shields_data_file = "./shieldsio_icons.json"

    check_new_repo_requent(repository_url=repository_url)

    if global_variables.global_project_languages:
        return jsonify({"badges_html": global_variables.global_project_languages}), 200

    if not global_variables.global_metadata:
        print("No global metadata found. Retrieving metadata.....")
        github_metadata_endpoint_handler()

    if not global_variables.global_cloned_repo_path:
        print("No clone folder found. Cloning Folder.....")
        clone_repo_endpoint_handler()

    # Step 1: Identify languages, frameworks, and tools
    global languages_found, frameworks_found, tools_found
    languages_found.clear()
    frameworks_found.clear()
    tools_found.clear()

    def identify_project(cloned_repo_path):
        for root, _, files in os.walk(cloned_repo_path):
            for file in files:
                ext = os.path.splitext(file)[1]
                if ext in [e for exts in extensions.values() for e in exts]:
                    for language, exts in extensions.items():
                        if ext in exts:
                            languages_found.add(language)
                for framework, config_files in frameworks_extensions.items():
                    if file in config_files:
                        frameworks_found.add(framework)
                for tool, config_files in tools_extensions.items():
                    if file in config_files:
                        tools_found.add(tool)

    print(global_variables.global_cloned_repo_path)

    identify_project(global_variables.global_cloned_repo_path)

    # Step 2: Get languages from GitHub
    def get_languages_from_github(languages_url):
        response = requests.get(languages_url)
        response.raise_for_status()
        return response.json()

    try:
        languages_from_github = get_languages_from_github(
            global_variables.global_metadata.languages_url
        )
        for language in languages_from_github.keys():
            languages_found.add(language)
    except Exception as e:
        return (
            jsonify({"error": f"Failed to fetch languages from GitHub: {str(e)}"}),
            500,
        )

    # Step 3: Load shields.io data
    shields_data = load_shields_data(shields_data_file)

    # Step 4: Combine results and search in shields.io data
    combined_results = {
        **{lang: None for lang in languages_found},
        **{framework: None for framework in frameworks_found},
        **{tool: None for tool in tools_found},
    }

    # Step 5: Get URLs for combined results
    badges_urls_map = get_shields_urls(combined_results.keys(), shields_data)

    # Step 6: Generate HTML for badges
    language_badges_markdown = f"""
<p align="center">
    <em>Constructed using the following tools and technologies:</em>
</p>
{generate_language_badges(badges_urls_map)}
"""
    global_variables.global_project_languages = language_badges_markdown
    return jsonify({"badges_html": language_badges_markdown}), 200
