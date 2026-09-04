from github import Github
from github import Auth


class GitHubService:

    def __init__(self, token, owner, repo):
        auth = Auth.Token(token)

        self.github = Github(auth=auth)

        self.repo = self.github.get_repo(
            f"{owner}/{repo}"
        )

    def get_pr_details(self, pr_number):

        pr = self.repo.get_pull(pr_number)

        return {
            "Number": pr.number,
            "Title": pr.title,
            "Description": pr.body,
            "Author": pr.user.login,
            "Files Changed": pr.changed_files,
            "Additions": pr.additions,
            "Deletions": pr.deletions,
        }

    def update_pr_description(
        self,
        pr_number,
        new_description,
    ):
        pr = self.repo.get_pull(pr_number)

        pr.edit(
            body=new_description,
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