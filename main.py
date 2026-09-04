import os

from github_service import GitHubService
from report_generator import ReportGenerator


def main():

    token = os.getenv(
        "GITHUB_TOKEN"
    )

    if not token:

        print(
            "GITHUB_TOKEN not found"
        )

        return

    owner = "Mounashree-2310"
    repo = "Python_tool"

    github = GitHubService(
        token,
        owner,
        repo,
    )

    pr_number = 1

    print("\nPR DETAILS:\n")

    pr_details = (
        github.get_pr_details(
            pr_number
        )
    )

    print(pr_details)

    print(
        "\nCONFIG FROM PR DESCRIPTION:\n"
    )

    config = github.get_pr_config(
        pr_number
    )

    print(config)

    print("\nLAST N PRs:\n")

    prs = github.list_pull_requests(
        count=config[
            "number_of_prs"
        ],
        state="open",
    )

    print(prs)

    report = ReportGenerator()

    report.create_json(
        pr_details
    )

    report.create_excel(
        [pr_details]
    )

    print(
        "\nReports created"
    )


if __name__ == "__main__":
    main()