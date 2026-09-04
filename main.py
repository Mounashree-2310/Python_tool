import os

from github_service import GitHubService
from report_generator import ReportGenerator


def main():

    token = os.getenv("GITHUB_TOKEN")

    if not token:
        print("GITHUB_TOKEN not found")
        return

    owner = "Mounashree-2310"
    repo = "Python_tool"

    github = GitHubService(
        token,
        owner,
        repo
    )

    print("\nPR DETAILS:\n")

    pr_details = github.get_pr_details(1)

    print(pr_details)

    print("\nLAST N PRs:\n")

    prs = github.list_pull_requests(
        count=10,
        state="all"
    )

    print(prs)

    report = ReportGenerator()

    report.create_json(prs)

    report.create_excel(prs)

    print("\nReports created")


if __name__ == "__main__":
    main()
