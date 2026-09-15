import re

from github import Auth, Github


class GitHubService:
    """GitHub Pull Request operations."""

    def __init__(self, token, repo_name):
        """Initialize GitHub repository."""

        try:
            auth = Auth.Token(token)
            self.github = Github(auth=auth)
            self.repo = self.github.get_repo(repo_name)

        except Exception:
            raise Exception(
                "Invalid repository name or no access to repository"
            )

    def get_pr_details(self, pr_number):
        """Get pull request details."""

        try:
            pr = self.repo.get_pull(pr_number)

            return {
                "PR Number": pr.number,
                "Title": pr.title,
                "Description": pr.body,
                "Author": pr.user.login,
                "Files Changed": pr.changed_files,
                "Files Added": pr.additions,
                "Files Deleted": pr.deletions,
            }

        except Exception:
            raise Exception(
                "Invalid PR number"
            )

    def update_pr_description(
        self,
        pr_number,
        new_description,
    ):
        """Update PR description."""

        try:
            pr = self.repo.get_pull(pr_number)

            pr.edit(body=new_description)

            print("PR Description Updated")

        except Exception:
            raise Exception(
                "Failed to update PR description"
            )

    def get_pr_config(
        self,
        pr_number,
    ):
        """Read configuration from PR description."""

        try:

            pr = self.repo.get_pull(pr_number)

            description = pr.body or ""

            count_match = re.search(
                r"number_of_prs=(\d+)",
                description,
            )

            repo_match = re.search(
                r"repo_url=(.+)",
                description,
            )

            state_match = re.search(
                r"pr_state=(\w+)",
                description,
            )

            number_of_prs = (
                int(count_match.group(1))
                if count_match
                else 10
            )

            repo_url = (
                repo_match.group(1).strip()
                if repo_match
                else self.repo.html_url
            )

            pr_state = (
                state_match.group(1).strip()
                if state_match
                else "open"
            )

            return {
                "number_of_prs": number_of_prs,
                "repo_url": repo_url,
                "pr_state": pr_state,
            }

        except Exception:
            raise Exception(
                "Failed to read PR configuration"
            )

    def list_pull_requests(
        self,
        count,
        state,
    ):
        """List pull requests."""

        try:

            if state.lower() == "merged":

                prs = [
                    pr
                    for pr in self.repo.get_pulls(
                        state="closed"
                    )
                    if pr.merged
                ]

            else:

                prs = self.repo.get_pulls(
                    state=state
                )

            pr_list = []

            for index, pr in enumerate(prs):

                if index >= count:
                    break

                pr_list.append(
                    {
                        "PR Number": pr.number,
                        "Title": pr.title,
                        "Author": pr.user.login,
                    }
                )

            return pr_list

        except Exception:
            raise Exception(
                "Failed to list pull requests"
            )
