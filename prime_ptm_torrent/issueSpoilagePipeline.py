import subprocess
from argparse import ArgumentParser, Namespace
from os import listdir
from pathlib import PurePath
from typing import List, Tuple


def getArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog="PRIME PTMTorrent Issue Density Pipeline",
        usage="The script to handle collecting issue data from PTMTorrent repositories",
        epilog="Written by Nicholas M. Synovic",
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


def extractAuthorRepoPairs(
    issuesDirectory: PurePath,
) -> List[Tuple[PurePath, PurePath]]:
    data: List[Tuple[PurePath, PurePath]] = []

    issuesSubString: str = "_gh_issues.json"
    issueSpoilageSubString: str = "_issue_spoilage.json"

    issuesFiles: List[str] = [
        file.replace(issuesSubString, "")
        for file in listdir(path=issuesDirectory)
        if PurePath(file).suffix == ".json"
    ]

    file: str
    for file in issuesFiles:
        issuesFilePath: PurePath = PurePath(issuesDirectory, f"{file}{issuesSubString}")
        issueSpoilageFilePath: PurePath = PurePath(f"{file}{issueSpoilageSubString}")

        pair: Tuple[PurePath, PurePath] = (
            issuesFilePath,
            issueSpoilageFilePath,
        )
        data.append(pair)

    return data


def runCommand(issuesFilePath: PurePath, issueSpoilageFilePath: PurePath) -> None:
    cmd_str: str = f"clime-issue-spoilage-compute -i {issuesFilePath.__str__()} -o {issueSpoilageFilePath.__str__()}"
    subprocess.run(cmd_str, shell=True)


def main() -> None:
    args: Namespace = getArgs()

    count: int = 0

    issuesDirectory: PurePath = PurePath(args.issues_directory)

    pairs: List[Tuple[PurePath, PurePath]] = extractAuthorRepoPairs(issuesDirectory)

    pair: Tuple[PurePath, PurePath, PurePath]
    for pair in pairs:
        print(count)

        issueSpoilageFilePath: PurePath = PurePath(args.out_directory, pair[2])
        runCommand(
            issuesFilePath=pair[1],
            issueSpoilageFilePath=issueSpoilageFilePath,
        )

        count += 1


if __name__ == "__main__":
    main()
