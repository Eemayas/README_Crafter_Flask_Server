from pathlib import Path
from typing import List
from flask import jsonify, request
from typing import List
from constants import ignore_list_folder_structure
from endpoints.clone_github import clone_repo_endpoint_handler
from utils.check_new_repo_request import check_new_repo_requent
from utils.check_new_repo_request import check_new_repo_requent
import global_variables
from utils.handle_metadata_and_clone import handle_metadata_and_clone


def print_folder_structure(
    dir_path: Path,
    level: int = -1,
    limit_to_directories: bool = False,
    length_limit: int = 1000,
    file_folder_to_be_ignored: List[str] = None,
) -> List[str]:
    """
    Generate a visual tree structure of the directory contents.

    Parameters:
    dir_path (Path): The root directory to start the tree from.
    level (int, optional): The depth of recursion. Defaults to -1 (no limit).
    limit_to_directories (bool, optional): If True, only directories are listed. Defaults to False.
    length_limit (int, optional): Limits the number of lines output. Defaults to 1000.
    file_folder_to_be_ignored (List[str], optional): A list of directory or file names to ignore. Defaults to None.

    Returns:
    List[str]: A list of strings representing the directory tree structure.
    """
    space = "    "
    branch = "│   "
    tee = "├── "
    last = "└── "
    dir_path = Path(dir_path)  # Ensure dir_path is a Path object
    files = 0
    directories = 0
    output = []

    if file_folder_to_be_ignored is None:
        file_folder_to_be_ignored = []

    def inner(dir_path: Path, prefix: str = "", level: int = -1):
        nonlocal files, directories
        if level == 0:
            return  # Stop recursion if level is 0
        if limit_to_directories:
            contents = [
                d
                for d in dir_path.iterdir()
                if d.is_dir() and d.name not in file_folder_to_be_ignored
            ]
        else:
            contents = [
                d for d in dir_path.iterdir() if d.name not in file_folder_to_be_ignored
            ]
        pointers = [tee] * (len(contents) - 1) + [last]
        for pointer, path in zip(pointers, contents):
            if path.is_dir():
                output.append(prefix + pointer + path.name + "/")
                directories += 1
                extension = branch if pointer == tee else space
                inner(path, prefix=prefix + extension, level=level - 1)
            elif not limit_to_directories:
                output.append(prefix + pointer + path.name)
                files += 1

    # Add the root directory name
    output.append(dir_path.name + "/")
    # Create an iterator from the inner function
    inner(dir_path, level=level)
    # Limit the output by length_limit
    if len(output) > length_limit:
        output = output[:length_limit]
        output.append(f"... length_limit, {length_limit}, reached, counted:")
    # Add the summary of directories and files
    output.append(
        f"\n{directories} directories" + (f", {files} files" if files else "")
    )

    return output


def folder_structure_endpoint_handler():
    repository_url = request.args.get("repository_url")
    if not repository_url:
        return jsonify({"error": "Missing 'repository_url' parameter"}), 400

    check_new_repo_requent(repository_url=repository_url)

    folder_structure_markdown = None

    handle_metadata_and_clone(function_name="folder_structure_endpoint_handler")

    if global_variables.global_cloned_repo_path:
        # Print the folder structure
        folder_structure = print_folder_structure(
            dir_path=Path(global_variables.global_cloned_repo_path),
            file_folder_to_be_ignored=ignore_list_folder_structure,
        )
        folder_structure_str = "\n".join(folder_structure)
        folder_structure_markdown = (
            "# Folder Structure\n" + "```sh\n" + folder_structure_str + "\n" + "```"
        )
        global_variables.global_folder_structure_str = folder_structure
        return folder_structure_markdown
    else:
        print("\nRepository cloning failed or was skipped.\n")


from pathlib import Path
from typing import List, Dict


def get_folder_structure(
    dir_path: Path,
    level: int = -1,
    limit_to_directories: bool = False,
    length_limit: int = 1000,
    file_folder_to_be_ignored: List[str] = None,
) -> Dict:
    """
    Generate a nested dictionary representing the directory structure.

    Parameters:
    dir_path (Path): The root directory to start the structure from.
    level (int, optional): The depth of recursion. Defaults to -1 (no limit).
    limit_to_directories (bool, optional): If True, only directories are listed. Defaults to False.
    length_limit (int, optional): Limits the number of lines output. Defaults to 1000.
    file_folder_to_be_ignored (List[str], optional): A list of directory or file names to ignore. Defaults to None.

    Returns:
    Dict: A nested dictionary representing the directory structure.
    """
    dir_path = Path(dir_path)  # Ensure dir_path is a Path object
    if file_folder_to_be_ignored is None:
        file_folder_to_be_ignored = []

    def inner(path: Path, current_level: int) -> Dict:
        if current_level == 0:
            return {}

        structure = {}
        contents = [
            item
            for item in path.iterdir()
            if item.name not in file_folder_to_be_ignored
        ]

        if limit_to_directories:
            contents = [item for item in contents if item.is_dir()]

        for item in contents:
            if item.is_dir():
                structure[item.name] = inner(item, current_level - 1)
            elif not limit_to_directories:
                structure[item.name] = None

            if length_limit and len(structure) >= length_limit:
                break

        return structure

    return {dir_path.name: inner(dir_path, level)}


def folder_structure_dict_endpoint():
    repository_url = request.args.get("repository_url")
    if not repository_url:
        return jsonify({"error": "Missing 'repository_url' parameter"}), 400

    check_new_repo_requent(repository_url=repository_url)

    handle_metadata_and_clone(function_name="folder_structure_dict_endpoint")

    if global_variables.global_cloned_repo_path:
        folder_structure = get_folder_structure(
            Path(global_variables.global_cloned_repo_path),
            file_folder_to_be_ignored=ignore_list_folder_structure,
        )
        return jsonify({"folder_structure": folder_structure})
    else:
        return jsonify({"error": "Repository cloning failed or was skipped."}), 500


def folder_structure_endpoint():
    folder_structure_markdown = folder_structure_endpoint_handler()
    if folder_structure_markdown:
        return jsonify({"folder_structure_markdown": folder_structure_markdown})
    else:
        return jsonify({"error": "Repository cloning failed or was skipped."}), 500
