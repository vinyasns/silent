import argparse
import sys

from .client import Client


class Silent:
    PROJECT_URL = 'https://github.com/vinyasns/silent'

    def __init__(self):
        self._parser = None
        self._setup_parsers()
        self._args = self._parser.parse_args()

    def _setup_parsers(self):
        self._parser = argparse.ArgumentParser(
            description='A commandline client for file.io',
            epilog='Project Page: ` {0} `'.format(Silent.PROJECT_URL),
            formatter_class=argparse.RawTextHelpFormatter
        )

        self._parser.add_argument('file', help="File to be uploaded anonymously")
        self._parser.add_argument('-e', '--expiry', help='Expiry time for the file on server.\n'
                                                         'Following formats are allowed,\n'
                                                         'Nw, expires in N weeks\n'
                                                         'Nm, expires in N months\n'
                                                         'Ny, expires in N years\n'
                                                         'Where N is a positive integer')

    def run(self):
        if not self._args.file:
            self._parser.print_help()
            print(":(")
            sys.exit(1)

        silent = Client(self._args)
        silent.run()


def main():
    app = Silent()
    app.run()


if __name__ == '__main__':
    main()
