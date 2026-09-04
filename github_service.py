import re

from github import Auth
from github import Github


class GitHubService:

    def __init__(self, token, owner, repo):

        auth = Auth.Token(token)

        self.github = Github(auth=auth)

        self.repo = self.github.get_repo(
            f"{owner}/{repo}"
        )

    def get_pr_details(
        self,
        pr_number
    ):

        pr = self.repo.get_pull(pr_number)

        return {
            "Number": pr.number,
            "Title": pr.title,
            "Description": pr.body,
            "Author": pr.user.login,
            "Files Changed": pr.changed_files,
            "Files Added": pr.additions,
            "Files Deleted": pr.deletions,
        }

    def update_pr_description(
        self,
        pr_number,
        new_description,
    ):

        pr = self.repo.get_pull(pr_number)

        pr.edit(
            body=new_description
        )

        print(
            "PR Description Updated"
        )

    def list_pull_requests(
        self,
        count=10,
        state="open",
    ):

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

    def get_pr_config(
        self,
        pr_number,
    ):

        pr = self.repo.get_pull(
            pr_number
        )

        description = pr.body or ""

        count_match = re.search(
            r"number_of_prs=(\d+)",
            description
        )

        repo_match = re.search(
            r"repo_url=(.+)",
            description
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

        return {
            "number_of_prs": number_of_prs,
            "repo_url": repo_url,
        }