from github_service import GitHubService
import os


def main():
    token = "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"

    print("Token:", token)  # Debug line

    owner = "Mounashree-2310"
    repo = "Python_tool"

    github = GitHubService(token, owner, repo)

    pull_requests = github.get_pull_requests()

    if not pull_requests:
        print("No open pull requests found.")
        return

    for pr in pull_requests:
        print("-" * 50)
        print(f"PR Number : {pr['number']}")
        print(f"Title     : {pr['title']}")
        print(f"Created By: {pr['user']['login']}")
        print(f"URL       : {pr['html_url']}")


if __name__ == "__main__":
    main()