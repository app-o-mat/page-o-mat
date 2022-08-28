""" The command-line interface to the journal generator
"""
import sys
from jg_cli_args import JGArgParser


def main():
    arg_parser = JGArgParser()
    arg_parser.parse(sys.argv[1:])


if __name__ == "__main__":
    main()
