import argparse
import os

from github_service import GitHubService
from report_generator import ReportGenerator


def main():

    parser = argparse.ArgumentParser(
        description="GitHub PR Tool"
    )

    parser.add_argument(
        "--repo",
        required=True,
        help="Repository name",
    )

    parser.add_argument(
        "--pr",
        type=int,
        help="Pull Request number",
    )

    parser.add_argument(
        "--get-pr",
        action="store_true",
        help="Get PR details",
    )

    parser.add_argument(
        "--update-pr",
        action="store_true",
        help="Update PR description",
    )

    parser.add_argument(
        "--list-prs",
        action="store_true",
        help="List pull requests",
    )

    parser.add_argument(
        "--description",
        help="New PR description",
    )

    parser.add_argument(
        "--numbers",
        type=int,
        default=10,
        help="Number of PRs",
    )

    parser.add_argument(
        "--status",
        choices=["open", "closed", "merged"],
        default="open",
        help="PR status",
    )

    args = parser.parse_args()

    token = os.getenv("GITHUB_TOKEN")

    if not token:
        print("GITHUB_TOKEN not found")
        return

    github = GitHubService(
        token,
        args.repo,
    )

    if args.get_pr:

        if not args.pr:
            print("--pr is required")
            return

        print(
            github.get_pr_details(
                args.pr
            )
        )

    elif args.update_pr:

        if not args.pr:
            print("--pr is required")
            return

        if not args.description:
            print("--description is required")
            return

        github.update_pr_description(
            args.pr,
            args.description,
        )

        print(
            "PR Description Updated Successfully"
        )

    elif args.list_prs:

        prs = github.list_pull_requests(
            count=args.numbers,
            state=args.status,
        )

        print("\nLAST N PRs\n")
        print(prs)

        report = ReportGenerator()

        report.create_json(prs)

        report.create_excel(prs)

        print(
            "\nReports Created Successfully"
        )

    else:

        print(
            "Select one operation:"
        )

        print(
            "--get-pr | --update-pr | --list-prs"
        )


if __name__ == "__main__":
    main()
