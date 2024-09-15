import global_variables
import logging

logging.basicConfig(level=logging.INFO)

logging.info("New Repository requested. Resetting global variables...")


def check_new_repo_requent(repository_url):
    try:
        # Check if the repository URL is the same as the global one
        if global_variables.global_repository_url != repository_url:
            logging.info("New Repository requested. Resetting global variables....")
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
            logging.info(
                "Same repository requested. Using existing global variables......"
            )
            return False
    except OSError as e:
        logging.info(f"An I/O error occurred: {e}")
        return False
    except Exception as e:
        logging.info(f"An unexpected error occurred:{e}")
        return False
