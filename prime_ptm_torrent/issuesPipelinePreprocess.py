import subprocess
from argparse import ArgumentParser, Namespace
from typing import List
from urllib.parse import ParseResult, urlparse


def getArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog="PRIME PTMTorrent Issues Pipeline",
        usage="The script to handle collecting issue data from PTMTorrent repositories",
        epilog="Written by Nicholas M. Synovic",
    )
    parser.add_argument(
        "-f",
        "--file",
        required=True,
        help="A file containing GitHub repo remote origin links to get issue data from",
    )
    parser.add_argument(
        "-t",
        "--token",
        required=True,
        help="A GitHub personal access token",
    )
    return parser.parse_args()


def runCommand(url: str, authorRepo: str, token: str) -> None:
    cmd_str: str = f"clime-gh-issues -r {url} -o {authorRepo}_gh_issues.json -t {token} --log {authorRepo}_gh_issues_log.log"
    subprocess.run(cmd_str, shell=True)


def main() -> None:
    args: Namespace = getArgs()

    line: str
    for line in open(args.file, "r"):
        line = line.strip()
        url: ParseResult = urlparse(url=line)
        authorRepo: str = url.path.strip("/").replace("/", "_")


if __name__ == "__main__":
    main()
