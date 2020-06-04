from pathlib import Path # stop using os.path, use pathlib instead
import sys
import argparse

# from pubsub.factory import Factory
from pubsub.factory import Factory

def main(argv):
    print('client main')

    parser = argparse.ArgumentParser()
    parser.add_argument("config", help="contains the client specification commands in .json format")
    parser.add_argument("--verbose", help="increased feedback in command line", action="store_true")
    args = parser.parse_args()

    config_file = args.config

    if not Path('.', config_file).is_file():
        sys.exit(f'Error: cannot find file {config_file}')

    file_type = Path(config_file).suffix[1:]  # e.g., 'json' or 'csv'

    # _factory = Factory()
    # _reader_type = _factory.reader_factory(mode=file_type)
    # _reader = _reader_type(config_file)
    # _data = _reader.data

    # if args.verbose:
    #     print('verbose is on')
    #     print(f'Created a reader factory of type {file_type}')
    #     print('with data:')
    #     print(_data)
    # else:
    #     print('verbose is off')

    if file_type == 'json':
        _factory = Factory(config_file)

        # if args.verbose:
        #     print('The factory created items with the following guids:')
        #     for item in _factory.items:
        #         print(item.guid)


if __name__ == '__main__':
    main(sys.argv[1:])