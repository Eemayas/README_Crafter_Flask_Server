from flask import jsonify, request
import asyncio
import aiohttp
from typing import Any, Optional, List
import nest_asyncio
from global_types import RepositoryMetadata, Contributor
import global_variables
from utils.check_new_repo_request import check_new_repo_requent

# from global_variables import global_metadata


# Enable asyncio to be used in Flask with nest_asyncio
nest_asyncio.apply()

from typing import Any, List, Optional


# Helper functions for fetching and parsing data
async def _fetch_repository_metadata(
    session: aiohttp.ClientSession, url: str
) -> dict[str, Any]:
    async with session.get(url) as response:
        response.raise_for_status()
        return await response.json()


async def _fetch_contributors(
    session: aiohttp.ClientSession, url: str
) -> List[Contributor]:
    async with session.get(url) as response:
        response.raise_for_status()
        contributors_data = await response.json()
        return [
            Contributor(
                name=contributor.get("login", ""),
                profile_url=contributor.get("html_url", ""),
                avatar_url=contributor.get("avatar_url", ""),
                contributions=str(contributor.get("contributions", "")),
            )
            for contributor in contributors_data
        ]


def _parse_repository_metadata(
    repo_data: dict, contributors: List[Contributor]
) -> RepositoryMetadata:
    owner_info = repo_data.get("owner", {}) or {}
    license_info = repo_data.get("license", {}) or {}

    return RepositoryMetadata(
        id=repo_data.get("id", 0),
        node_id=repo_data.get("node_id", ""),
        name=repo_data.get("name", ""),
        full_name=repo_data.get("full_name", ""),
        private=repo_data.get("private", False),
        owner=owner_info,
        html_url=repo_data.get("html_url", ""),
        description=repo_data.get("description", ""),
        fork=repo_data.get("fork", False),
        url=repo_data.get("url", ""),
        forks_url=repo_data.get("forks_url", ""),
        keys_url=repo_data.get("keys_url", ""),
        collaborators_url=repo_data.get("collaborators_url", ""),
        teams_url=repo_data.get("teams_url", ""),
        hooks_url=repo_data.get("hooks_url", ""),
        issue_events_url=repo_data.get("issue_events_url", ""),
        events_url=repo_data.get("events_url", ""),
        assignees_url=repo_data.get("assignees_url", ""),
        branches_url=repo_data.get("branches_url", ""),
        tags_url=repo_data.get("tags_url", ""),
        blobs_url=repo_data.get("blobs_url", ""),
        git_tags_url=repo_data.get("git_tags_url", ""),
        git_refs_url=repo_data.get("git_refs_url", ""),
        trees_url=repo_data.get("trees_url", ""),
        statuses_url=repo_data.get("statuses_url", ""),
        languages_url=repo_data.get("languages_url", ""),
        stargazers_url=repo_data.get("stargazers_url", ""),
        contributors_url=repo_data.get("contributors_url", ""),
        subscribers_url=repo_data.get("subscribers_url", ""),
        subscription_url=repo_data.get("subscription_url", ""),
        commits_url=repo_data.get("commits_url", ""),
        git_commits_url=repo_data.get("git_commits_url", ""),
        comments_url=repo_data.get("comments_url", ""),
        issue_comment_url=repo_data.get("issue_comment_url", ""),
        contents_url=repo_data.get("contents_url", ""),
        compare_url=repo_data.get("compare_url", ""),
        merges_url=repo_data.get("merges_url", ""),
        archive_url=repo_data.get("archive_url", ""),
        downloads_url=repo_data.get("downloads_url", ""),
        issues_url=repo_data.get("issues_url", ""),
        pulls_url=repo_data.get("pulls_url", ""),
        milestones_url=repo_data.get("milestones_url", ""),
        notifications_url=repo_data.get("notifications_url", ""),
        labels_url=repo_data.get("labels_url", ""),
        releases_url=repo_data.get("releases_url", ""),
        deployments_url=repo_data.get("deployments_url", ""),
        created_at=repo_data.get("created_at", ""),
        updated_at=repo_data.get("updated_at", ""),
        pushed_at=repo_data.get("pushed_at", ""),
        git_url=repo_data.get("git_url", ""),
        ssh_url=repo_data.get("ssh_url", ""),
        clone_url=repo_data.get("clone_url", ""),
        svn_url=repo_data.get("svn_url", ""),
        homepage=repo_data.get("homepage", ""),
        size=repo_data.get("size", 0),
        stargazers_count=repo_data.get("stargazers_count", 0),
        watchers_count=repo_data.get("watchers_count", 0),
        language=repo_data.get("language", ""),
        has_issues=repo_data.get("has_issues", False),
        has_projects=repo_data.get("has_projects", False),
        has_downloads=repo_data.get("has_downloads", False),
        has_wiki=repo_data.get("has_wiki", False),
        has_pages=repo_data.get("has_pages", False),
        has_discussions=repo_data.get("has_discussions", False),
        forks_count=repo_data.get("forks_count", 0),
        mirror_url=repo_data.get("mirror_url", None),
        archived=repo_data.get("archived", False),
        disabled=repo_data.get("disabled", False),
        open_issues_count=repo_data.get("open_issues_count", 0),
        license=license_info,
        allow_forking=repo_data.get("allow_forking", False),
        is_template=repo_data.get("is_template", False),
        web_commit_signoff_required=repo_data.get("web_commit_signoff_required", False),
        topics=repo_data.get("topics", []),
        visibility=repo_data.get("visibility", ""),
        forks=repo_data.get("forks", 0),
        open_issues=repo_data.get("open_issues", 0),
        watchers=repo_data.get("watchers", 0),
        default_branch=repo_data.get("default_branch", ""),
        temp_clone_token=repo_data.get("temp_clone_token", None),
        network_count=repo_data.get("network_count", 0),
        subscribers_count=repo_data.get("subscribers_count", 0),
        contributors=contributors,
    )


async def fetch_git_repository_metadata(
    session: aiohttp.ClientSession, repository_url: str
) -> Optional[RepositoryMetadata]:
    api_url = repository_url.replace(
        "https://github.com/", "https://api.github.com/repos/"
    )

    try:
        metadata = await _fetch_repository_metadata(session, api_url)
        contributors_url = metadata.get("contributors_url", "")
        contributors = (
            await _fetch_contributors(session, contributors_url)
            if contributors_url
            else []
        )
        return _parse_repository_metadata(metadata, contributors) if metadata else None
    except aiohttp.ClientError as exc:
        print(f"Client error while fetching repository metadata: {exc}")
        return None


def metadata_to_dict(metadata: RepositoryMetadata) -> dict:
    metadata_dict = {}

    if not isinstance(metadata, RepositoryMetadata):
        return

    for field in metadata.__dataclass_fields__:
        value = getattr(metadata, field)
        if isinstance(value, dict):
            value = value
        elif isinstance(value, list):
            value = [str(item) for item in value]
        metadata_dict[field] = value

    if metadata.contributors:
        contributors_list = []
        for contributor in metadata.contributors:
            contributors_list.append(
                {
                    "name": contributor.name,
                    "profile_url": contributor.profile_url,
                    "avatar_url": contributor.avatar_url,
                    "contributions": contributor.contributions,
                }
            )
        metadata_dict["contributors"] = contributors_list

    return metadata_dict


def github_metadata_endpoint_handler():
    repository_url = request.args.get("repository_url")
    if not repository_url:
        return jsonify({"error": "Missing 'repository_url' parameter"}), 400

    try:
        check_new_repo_requent(repository_url)

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        async def main():
            async with aiohttp.ClientSession() as session:
                metadata = await fetch_git_repository_metadata(session, repository_url)
                return metadata

        metadata = loop.run_until_complete(main())
        global_variables.global_metadata = metadata
        return metadata
    except Exception as e:
        return (
            jsonify(
                {"error": "Failed to fetch repository metadata", "details": str(e)}
            ),
            500,
        )


def github_metadata_endpoint():
    metadata = github_metadata_endpoint_handler()
    if metadata:
        try:
            metadata_dict = metadata_to_dict(metadata)
            return jsonify({"metadata": metadata_dict}), 200
        except Exception as e:
            return jsonify({"error": "Failed to parse repository metadata Dict"}), 500
    else:
        return jsonify({"error": "Failed to fetch repository metadata"}), 500
