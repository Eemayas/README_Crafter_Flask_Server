from flask import jsonify, request

from constants import project_icons

import global_variables


def get_project_icon():
    choice = request.args.get("choice")

    if (
        global_variables.global_project_image_choice == choice
        and global_variables.global_project_image_markdown
    ):
        return jsonify(
            {"project_image_markdown": global_variables.global_project_image_markdown}
        )

    if choice and choice.isdigit():  # Check if the input is a digit
        choice = int(choice)

        # Initialize icon_url to None
        icon_url = None

        # Check if the choice corresponds to a predefined project type
        if 1 <= choice <= len(project_icons):
            selected_type = list(project_icons.keys())[choice - 1]
            icon_url = project_icons[selected_type]["icon"]  # Get the icon URL

        # Check if the choice is 'Custom'
        elif choice == len(project_icons) + 1:
            custom_link = request.args.get("custom_link")
            if custom_link:
                icon_url = custom_link
            else:
                return jsonify({"error": "Custom link not provided"}), 400
        else:
            # If input is invalid, return an error message
            return jsonify({"error": "Invalid choice. Please try again."}), 400

        if icon_url:
            # Generate the Markdown for displaying the project icon
            project_image_markdown = f"""
<p align="center">
    <img src="{icon_url}" width="200" style="border-radius: 20px;" />
</p>
            """
        else:
            # Set an empty Markdown string if no icon is selected
            project_image_markdown = ""
        global_variables.global_project_image_choice = choice
        global_variables.global_project_image_markdown = project_image_markdown
        # Return the Markdown content as JSON
        return jsonify({"project_image_markdown": project_image_markdown})

    else:
        return jsonify({"error": "Invalid choice format"}), 400
