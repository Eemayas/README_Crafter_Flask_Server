import os
import shutil
import asyncio
import subprocess
from typing import Optional
from flask import request, jsonify

import global_variables

from utils.check_new_repo_request import check_new_repo_requent


async def clone_github_repo(
    repository_url: str, target_folder: str = "Github_repos"
) -> Optional[str]:
    """
    Clone a GitHub repository to a specific folder and remove the .git folder.

    Args:
        repository_url (str): The URL of the GitHub repository to clone.
        target_folder (str, optional): The target directory to clone the repository into. Defaults to 'Github_repos'.

    Returns:
        Optional[str]: The path to the cloned repository, or None if cloning failed.
    """
    # Extract the repository name from the URL
    repo_name = repository_url.split("/")[-1]
    target_path = os.path.join(target_folder, repo_name)

    if not os.path.exists(target_path):
        # Ensure the target folder exists
        os.makedirs(target_folder, exist_ok=True)
        print(f"\nCloning repository from {repository_url} into {target_path}...\n")

        try:
            # Run the git clone command to clone the repository
            subprocess.run(["git", "clone", repository_url, target_path], check=True)
            print(f"\nRepository cloned into {target_path}\n")

            # # Remove the .git folder to clean up the cloned repository
            # git_folder_path = os.path.join(target_path, ".git")
            # if os.path.exists(git_folder_path):
            #     shutil.rmtree(git_folder_path)
            #     print(f"\nRemoved .git folder from {target_path}\n")

            # Return the path to the cloned repository
            return target_path
        except subprocess.CalledProcessError as e:
            # Handle errors that occur during the cloning process
            print(f"\nError cloning repository: {e}\n")
            return None
    else:
        # If the repository folder already exists, skip the cloning process
        print(f"\nRepository folder '{target_path}' already exists. Skipping clone.\n")
        return target_path


def clone_repo_endpoint_handler():
    repository_url = request.args.get("repository_url")
    if not repository_url:
        return jsonify({"error": "Missing 'repository_url' parameter"}), 400
    try:
        check_new_repo_requent(repository_url)

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        async def main():
            return await clone_github_repo(repository_url)

        cloned_repo_path = loop.run_until_complete(main())
        global_variables.global_cloned_repo_path = cloned_repo_path

        return cloned_repo_path
    except Exception as e:
        return jsonify({"error": "Failed to clone repository", "details": str(e)}), 500


def clone_repo_endpoint():
    cloned_repo_path = clone_repo_endpoint_handler()

    if cloned_repo_path:
        return (
            jsonify(
                {"message": "Repository cloned successfully", "path": cloned_repo_path}
            ),
            200,
        )
    else:
        return jsonify({"error": "Failed to clone repository"}), 500
