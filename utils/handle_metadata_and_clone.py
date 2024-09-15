from endpoints.clone_github import clone_repo_endpoint_handler
from endpoints.github_metadata import github_metadata_endpoint_handler
import global_variables


def handle_metadata_and_clone(function_name: str = ""):
    if not global_variables.global_metadata:
        print(
            f"\n{function_name} -- No global metadata found. Retrieving metadata.....\n"
        )
        github_metadata_endpoint_handler()
    else:
        print(
            f"\n{function_name} -- Global metadata found. Skipping metadata retrieval.....\n"
        )

    if not global_variables.global_cloned_repo_path:
        print(f"\n{function_name} -- No clone folder found. Cloning Folder.....\n")
        clone_repo_endpoint_handler()
    else:
        print(f"\n{function_name} -- Cloned folder found. Skipping cloning.....\n")
