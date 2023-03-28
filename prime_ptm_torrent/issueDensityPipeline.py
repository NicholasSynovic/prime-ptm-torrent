import subprocess
from argparse import ArgumentParser, Namespace
from os import listdir
from pathlib import PurePath
from subprocess import CalledProcessError
from typing import List, Tuple


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


def extractAuthorRepoPairs(
    commitsDirectory: PurePath, issuesDirectory: PurePath
) -> List[Tuple[PurePath, PurePath, PurePath]]:
    data: List[Tuple[PurePath, PurePath, PurePath]] = []

    commitsSubString: str = "_commits_loc.json"
    issuesSubString: str = "_gh_issues.json"
    issueDensitySubString: str = "_issue_density.json"

    commitsFiles: List[str] = [
        file.replace(commitsSubString, "")
        for file in listdir(path=commitsDirectory)
        if PurePath(file).suffix == ".json"
    ]

    issuesFiles: List[str] = [
        file.replace(issuesSubString, "")
        for file in listdir(path=issuesDirectory)
        if PurePath(file).suffix == ".json"
    ]

    files: List[str] = issuesFiles + commitsFiles
    files: set[str] = set(files)

    file: str
    for file in files:
        commitsFilePath: PurePath = PurePath(
            commitsDirectory, f"{file}{commitsSubString}"
        )
        issuesFilePath: PurePath = PurePath(issuesDirectory, f"{file}{issuesSubString}")
        issueDensityFilePath: PurePath = PurePath(f"{file}{issueDensitySubString}")

        pair: Tuple[PurePath, PurePath, PurePath] = (
            commitsFilePath,
            issuesFilePath,
            issueDensityFilePath,
        )
        data.append(pair)

    return data


def runCommand(
    commitsFilePath: PurePath, issuesFilePath: PurePath, issueDensityFilePath: PurePath
) -> None:
    cmd_str: str = f"clime-issue-density-compute -c {commitsFilePath.__str__()} -i {issuesFilePath.__str__()} -o {issueDensityFilePath.__str__()}"

    try:
        subprocess.run(cmd_str, shell=True)
    except CalledProcessError:
        pass


def main() -> None:
    args: Namespace = getArgs()

    count: int = 0

    commitsDirectory: PurePath = PurePath(args.commits_directory)
    issuesDirectory: PurePath = PurePath(args.issues_directory)

    pairs: List[Tuple[PurePath, PurePath]] = extractAuthorRepoPairs(
        commitsDirectory, issuesDirectory
    )

    pair: Tuple[PurePath, PurePath, PurePath]
    for pair in pairs:
        print(count)

        issueDensityFilePath: PurePath = PurePath(args.out_directory, pair[2])
        runCommand(
            commitsFilePath=pair[0],
            issuesFilePath=pair[1],
            issueDensityFilePath=issueDensityFilePath,
        )

        count += 1


if __name__ == "__main__":
    main()
