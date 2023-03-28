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
        default="ghRepos.txt",
        required=True,
        help="A file containing GitHub repo remote origin links to get issue data from",
    )
    return parser.parse_args()


def main() -> None:
    args: Namespace = getArgs()

    line: str
    for line in open(args.file, "r"):
        line = line.strip()
        url: ParseResult = urlparse(url=line)
        authorRepo: str = url.path.strip("/").replace("/", "_")
        print(authorRepo)


if __name__ == "__main__":
    main()
