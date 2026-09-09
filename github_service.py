import re

from github import Auth, Github


class GitHubService:
    def __init__(self, token, repo_name):
        auth = Auth.Token(token)
        self.github = Github(auth=auth)
        self.repo = self.github.get_repo(repo_name)

    def get_pr_details(self, pr_number):
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

    def update_pr_description(
        self,
        pr_number,
        new_description,
    ):
        pr = self.repo.get_pull(pr_number)

        pr.edit(body=new_description)

        print("PR Description Updated")

    def get_pr_config(
        self,
        pr_number,
    ):
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

        number_of_prs = int(count_match.group(1)) if count_match else 10

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

    def list_pull_requests(
        self,
        count=10,
        state="open",
    ):
        if state.lower() == "merged":
            merged_prs = [
                pr
                for pr in self.repo.get_pulls(state="closed")
                if pr.merged
            ]

            prs = merged_prs

        else:
            prs = self.repo.get_pulls(state=state)

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
