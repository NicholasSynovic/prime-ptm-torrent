import subprocess
from argparse import ArgumentParser, Namespace
from pathlib import PurePath
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

    count: int = 0

    line: str
    for line in open(args.file, "r"):
        print(count)
        parsedURL: ParseResult = urlparse(url=line.strip())
        url: str = parsedURL.path.strip("/")
        jsonFileName: str = f'{url.replace("/", "_")}_gh_issues.json'
        logFileName: str = f'{url.replace("/", "_")}_gh_issues.log'

        jsonFilePath: PurePath = PurePath(args.out_directory, jsonFileName)
        logFilePath: PurePath = PurePath(args.out_directory, logFileName)

        runCommand(url, jsonFilePath, logFilePath, token=args.token)
        count += 1


if __name__ == "__main__":
    main()
