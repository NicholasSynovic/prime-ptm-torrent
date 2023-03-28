import subprocess
from argparse import ArgumentParser, Namespace
from os import listdir
from pathlib import PurePath
from typing import List
from urllib.parse import ParseResult, urlparse


def getArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog="PRIME PTMTorrent Issue Density Pipeline",
        usage="The script to handle collecting issue data from PTMTorrent repositories",
        epilog="Written by Nicholas M. Synovic",
    )
    parser.add_argument(
        "-c",
        "--commits-directory",
        required=True,
        help="A directory path containing commits files",
    )
    parser.add_argument(
        "-i",
        "--issues-directory",
        required=True,
        help="A directory path containing issues files",
    )
    parser.add_argument(
        "-d", "--out-directory", required=True, help="Directory to store output data"
    )
    return parser.parse_args()


def runCommand(
    url: str, jsonFilePath: PurePath, logFilePath: PurePath, token: str
) -> None:
    cmd_str: str = f"clime-gh-issues -r {url} -o {jsonFilePath.__str__()} -t {token} --log {logFilePath.__str__()}"
    subprocess.run(cmd_str, shell=True)


def main() -> None:
    args: Namespace = getArgs()

    commitsDir: PurePath = PurePath(args.commits_directory)
    issuesDir: PurePath = PurePath(args.issues_directory)

    commitsFiles: List[str] = listdir(path=commitsDir)
    issuesFiles: List[str] = listdir(path=issuesDir)

    print(commitsFiles)
    print(issuesDir)


if __name__ == "__main__":
    main()
