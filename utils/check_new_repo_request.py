import global_variables


def check_new_repo_requent(repository_url):
    try:
        # Check if the repository URL is the same as the global one
        if global_variables.global_repository_url != repository_url:
            print("New Repository requested. Resetting global variables....\n")
            # Reset global variables for the new repository
            global_variables.global_repository_url = repository_url
            global_variables.global_metadata = None
            global_variables.global_cloned_repo_path = None
            global_variables.global_folder_structure = None
            global_variables.global_folder_structure_str = None
            global_variables.global_combined_summary = None
            global_variables.global_summary_dict = None
            global_variables.global_project_image_choice = None
            global_variables.global_project_image_markdown = None
            global_variables.global_project_name = None
            global_variables.global_project_badges = None
            global_variables.global_project_languages = None

            return True
        else:
            print("Same repository requested. Using existing global variables......\n")
            return False
    except OSError as e:
        print(f"An I/O error occurred: {e}\n")
        return False
    except Exception as e:
        print(f"An unexpected error occurred:{e}\n")
        return False
