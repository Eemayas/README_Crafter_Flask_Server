import global_variables


def check_new_repo_requent(repository_url):
    if global_variables.global_repository_url != repository_url:
        print("New Repository requested. Reseting global variables......\n")
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
    return False
