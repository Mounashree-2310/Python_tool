from github import Github


class GitHubService:

    def __init__(self, token, owner, repo):
        self.github = Github(token)
        self.repo = self.github.get_repo(
            f"{owner}/{repo}"
        )

    def get_pr_details(self, pr_number):

        pr = self.repo.get_pull(pr_number)

        return {
            "title": pr.title,
            "description": pr.body,
            "author": pr.user.login,
            "files_changed": pr.changed_files,
            "additions": pr.additions,
            "deletions": pr.deletions
        }

    def update_pr_description(
        self,
        pr_number,
        description
    ):
        pr = self.repo.get_pull(pr_number)

        pr.edit(body=description)

    def list_pull_requests(
        self,
        count=10,
        state="open"
    ):

        prs = self.repo.get_pulls(
            state=state
        )

        result = []

        for index, pr in enumerate(prs):

            if index >= count:
                break

            result.append({
                "Number": pr.number,
                "Title": pr.title,
                "Author": pr.user.login
            })

        return result