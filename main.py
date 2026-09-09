import argparse
import os

from github_service import GitHubService
from report_generator import ReportGenerator


def main():
    parser = argparse.ArgumentParser(description="GitHub PR Tool")

    parser.add_argument(
        "--repo",
        required=True,
        help="Repository name in owner/repo format",
    )

    parser.add_argument(
        "--pr",
        type=int,
        required=True,
        help="Pull Request number",
    )

    args = parser.parse_args()

    token = os.getenv("GITHUB_TOKEN")

    if not token:
        print("GITHUB_TOKEN not found")
        return

    github = GitHubService(token, args.repo)

    print("\nPR DETAILS\n")

    pr_details = github.get_pr_details(args.pr)
    print(pr_details)

    config = github.get_pr_config(args.pr)

    print("\nCONFIG FROM PR DESCRIPTION\n")
    print(config)

    repo_name = (
        config["repo_url"]
        .replace("https://github.com/", "")
        .strip("/")
    )

    github = GitHubService(token, repo_name)

    prs = github.list_pull_requests(
        count=config["number_of_prs"],
        state=config["pr_state"],
    )

    print("\nLAST N PRs\n")
    print(prs)

    report = ReportGenerator()

    report.create_json(prs)
    report.create_excel(prs)

    print("\nReports Created Successfully")


if __name__ == "__main__":
    main()
