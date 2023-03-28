from argparse import ArgumentParser, Namespace

def getArgs()   ->  Namespace:
    parser: ArgumentParser = ArgumentParser()
    parser.add_arg("-u", "--url", required=True)
    return parser.parse_args()

def main()  ->  None:
    pass

if __name__ == "__main__":
    main()
