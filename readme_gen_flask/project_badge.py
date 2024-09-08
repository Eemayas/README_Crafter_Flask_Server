from flask import Flask, request, jsonify
import global_variables
from utils.check_new_repo_request import check_new_repo_requent


def update_github_badge_urls(repository_url, badges):
    """Update GitHub status badge URLs based on the selected badges.

    Args:
        repository_url (str): The GitHub repository link.
        badges (list): A list of badge identifiers to include.

    Returns:
        str: A string containing the HTML code for the selected badges.
    """
    # Extract the owner and repository name from the GitHub link
    repo_path = repository_url.rstrip("/").replace("https://github.com/", "")

    # Define the badge URLs
    badge_urls = {
        "license": f"https://img.shields.io/github/license/{repo_path}?style=flat&color=0080ff",
        # "last-commit": f"https://img.shields.io/github/last-commit/{repo_path}?style=flat&logo=git&logoColor=white&color=0080ff",
        # "repo-top-language": f"https://img.shields.io/github/languages/top/{repo_path}?style=flat&color=0080ff",
        # "repo-language-count": f"https://img.shields.io/github/languages/count/{repo_path}?style=flat&color=0080ff",
        # "build-status": f"https://img.shields.io/github/actions/workflow/status/{repo_path}/build.yml?branch=main&style=flat&color=0080ff",
        # "open-issues": f"https://img.shields.io/github/issues/{repo_path}?style=flat&color=0080ff",
        # "forks": f"https://img.shields.io/github/forks/{repo_path}?style=flat&color=0080ff",
        # "stars": f"https://img.shields.io/github/stars/{repo_path}?style=flat&color=0080ff",
        # "pull-requests": f"https://img.shields.io/github/issues-pr/{repo_path}?style=flat&color=0080ff",
        # "contributors": f"https://img.shields.io/github/contributors/{repo_path}?style=flat&color=0080ff",
        # "commit-activity": f"https://img.shields.io/github/commit-activity/m/{repo_path}?style=flat&color=0080ff",
        # "code-size": f"https://img.shields.io/github/languages/code-size/{repo_path}?style=flat&color=0080ff",
        # "repo-size": f"https://img.shields.io/github/repo-size/{repo_path}?style=flat&color=0080ff",
        # "downloads": f"https://img.shields.io/github/downloads/{repo_path}/total?style=flat&color=0080ff",
        # "sponsors": f"https://img.shields.io/github/sponsors/{repo_path}?style=flat&color=0080ff",
        # "release-version": f"https://img.shields.io/github/v/release/{repo_path}?style=flat&color=0080ff",
        # "coverage": f"https://img.shields.io/codecov/c/github/{repo_path}?style=flat&color=0080ff",
        # "code-quality": f"https://img.shields.io/codeclimate/quality/a/{repo_path}?style=flat&color=0080ff",
        # "dependencies": f"https://img.shields.io/david/{repo_path}?style=flat&color=0080ff",
        # "dev-dependencies": f"https://img.shields.io/david/dev/{repo_path}?style=flat&color=0080ff",
        # "security": f"https://img.shields.io/snyk/vulnerabilities/github/{repo_path}?style=flat&color=0080ff",
        # "performance": f"https://img.shields.io/website?style=flat&color=0080ff&url=https%3A%2F%2Fexample.com",
        # "activity": f"https://img.shields.io/github/commit-activity/y/{repo_path}?style=flat&color=0080ff",
        # "documentation": f"https://img.shields.io/docsify/docs?style=flat&color=0080ff",
        # "version": f"https://img.shields.io/github/v/tag/{repo_path}?style=flat&color=0080ff",
    }

    # Create the HTML string based on the selected badges
    badges_html = "\n".join(
        f'  <img src="{badge_urls[badge]}" alt="{badge}">'
        for badge in badges
        if badge in badge_urls
    )

    # Generate the final HTML template
    html_template = f"""
<p align="center">
{badges_html}
</p>
    """

    return html_template


def get_project_badges():
    repository_url = request.args.get("repository_url")
    badges = request.args.getlist("badges")

    if not repository_url or not badges:
        return (
            jsonify({"error": "GitHub repository link and badges list are required."}),
            400,
        )

    check_new_repo_requent(repository_url=repository_url)

    if global_variables.global_project_badges:
        return jsonify({"badges_html": global_variables.global_project_badges}), 200

    badges_html = update_github_badge_urls(repository_url, badges)
    global_variables.global_project_badges = badges_html
    return jsonify({"badges_html": badges_html}), 200
