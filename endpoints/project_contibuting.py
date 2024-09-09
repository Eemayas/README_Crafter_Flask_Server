from flask import Flask, request, jsonify
import re
from utils.check_new_repo_request import check_new_repo_requent


def generate_contributing_guide(repository_url):
    """
    Generate a contributing guide for a GitHub repository.

    Parameters:
    repository_url (str): The URL of the GitHub repository.

    Returns:
    str: The contributing guide in markdown format.
    """
    # Extract the username and repository name from the link
    match = re.match(r"https://github.com/([^/]+)/([^/]+)", repository_url)
    if not match:
        raise ValueError("Invalid GitHub repository link")

    username, repo_name = match.groups()

    # Define the guide with placeholders for URLs
    guide_template = f"""
# Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/{username}/{repo_name}/pulls)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/{username}/{repo_name}/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/{username}/{repo_name}/issues)**: Submit bugs found or log feature requests for {repo_name}.

### Contributing Guidelines

1. **Fork the Repository**:
    - Start by forking the project repository to your GitHub account.
2. **Clone the Repository**:
    - Clone your forked repository to your local machine using the command:
    ```sh
    git clone https://github.com/your-username/{repo_name}.git
    ```
    - Replace ``your-username`` with your GitHub username.
3. **Create a New Branch**:
    - Create a new branch for your changes using the command:
    ```sh
    git checkout -b your-branch-name
    ```
4. **Make Your Changes**:
    - Edit, add, or delete files as needed. Ensure your changes align with the project's contribution guidelines.
5. **Commit Your Changes**:
    - Stage your changes and commit them with a descriptive message:
      ```bash
      git add .
      git commit -m "Your descriptive message"
      ```
6. **Push Your Changes:**
    - Push your branch to your forked repository:
      ```bash
      git push origin your-branch-name
      ```
7. **Create a Pull Request (PR):**
    - Go to the original repository on GitHub and click “Compare & pull request.” Provide a clear description of the changes and submit the PR.

Once your PR is reviewed and approved, it will be merged into the main branch.
    """

    return guide_template


def contributing_guide():
    repository_url = request.args.get("repository_url")

    if not repository_url:
        return jsonify({"error": "Repository link is required."}), 400

    check_new_repo_requent(repository_url=repository_url)
    try:
        # Generate the contributing guide
        guide_markdown = generate_contributing_guide(repository_url)
        return jsonify({"contributing_guide_markdown": guide_markdown}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
