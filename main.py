import os

from github_service import GitHubService
from report_generator import ReportGenerator


def main():

    token = os.getenv(
        "GITHUB_TOKEN"
    )

    owner = "Mounashree-2310"
    repo = "Python_tool"

    github = GitHubService(
        token,
        owner,
        repo
    )

    prs = github.list_pull_requests(
        count=10,
        state="open"
    )

    report = ReportGenerator()

    report.create_json(prs)

    report.create_excel(prs)

    print("Reports created")


if __name__ == "__main__":
    main()