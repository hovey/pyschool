from pathlib import Path  # stop using os.path, use pathlib instead
import sys
import argparse

from pubsub.factory import Factory


def main(argv):
    print("client main")

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "config", help="contains the client specification commands in .json format"
    )
    parser.add_argument(
        "--verbose", help="increased feedback in command line", action="store_true"
    )
    args = parser.parse_args()

    config_file = args.config

    if not Path(".", config_file).is_file():
        sys.exit(f"Error: cannot find file {config_file}")

    file_type = Path(config_file).suffix[1:]  # e.g., 'json' or 'csv'

    if file_type == "json":
        _factory = Factory(config_file)


if __name__ == "__main__":
    main(sys.argv[1:])
