import requests


class GitHubService:
    def __init__(self, token, owner, repo):
        self.token = token
        self.owner = owner
        self.repo = repo

    def get_pull_requests(self):
        url = f"https://api.github.com/repos/{self.owner}/{self.repo}/pulls"

        headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github+json",
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        return response.json()