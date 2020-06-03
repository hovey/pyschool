from pathlib import Path # stop using os.path, use pathlib instead
import sys
import argparse


def main(argv):
    print('client main')

    parser = argparse.ArgumentParser()
    parser.add_argument("config", help="contains the client specification in .json format")
    parser.add_argument("--verbose", help="increased feedback in command line", action="store_true")
    args = parser.parse_args()

    if args.verbose:
        print('verbose is on')
    else:
        print('verbose is off')

    config_file = args.config

    if not Path('.', config_file).is_file():
        # print(f'Error: cannot find file {config_file}')
        sys.exit(f'Error: cannot find file {config_file}')






if __name__ == '__main__':
    main(sys.argv[1:])