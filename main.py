import os

from github_service import GitHubService
from report_generator import ReportGenerator


def main():

    token = os.getenv("GITHUB_TOKEN")

    owner = "Mounashree-2310"
    repo = "Python_tool"

    github = GitHubService(
        token,
        owner,
        repo
    )

    pr_details = github.get_pr_details(1)

    print("\nPR DETAILS:\n")
    print(pr_details)

    report = ReportGenerator()

    report.create_json(pr_details)

    report.create_excel([pr_details])

    print("\nReports created")


if __name__ == "__main__":
    main()
