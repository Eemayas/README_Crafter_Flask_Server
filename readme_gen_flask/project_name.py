from pathlib import Path
from prettytable import PrettyTable
from github_metadata import fetch_git_repository_metadata
from utils.llama_configurations import get_description_data
from constants import ignore_list_folder_structure, ignore_list_extensions
from prettytable import PrettyTable
from flask import jsonify, request
import asyncio
import aiohttp
from clone_github import clone_github_repo
import global_variables


def get_project_name():
    try:
        repository_url = request.args.get("repository_url")
        if not repository_url:
            return jsonify({"error": "Missing 'repository_url' parameter"}), 400

        if not global_variables.global_metadata:
            repository_url = request.args.get("repository_url")
            if not repository_url:
                return jsonify({"error": "Missing 'repository_url' parameter"}), 400

            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

            async def main():
                async with aiohttp.ClientSession() as session:
                    metadata = await fetch_git_repository_metadata(
                        session, repository_url
                    )
                    return metadata

            metadata = loop.run_until_complete(main())
            global_variables.global_metadata = metadata

        project_name_markdown = f"""
<p align="center">
    <h1>{global_variables.global_metadata.name}</h1>
</p>
            """
        return jsonify({"project_name_markdown": project_name_markdown}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
