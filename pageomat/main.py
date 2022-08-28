""" The command-line interface to the Page-o-Mat journal generator
"""
import sys
from cli_arg_parser import CliArgParser


def main():
    arg_parser = CliArgParser()
    arg_parser.parse(sys.argv[1:])


if __name__ == "__main__":
    main()
