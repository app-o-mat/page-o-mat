""" The command-line interface to the Page-o-Mat journal generator
"""
import sys
import yaml
from cli_arg_parser import CliArgParser
from pageomat.pdf_generator import PdfGenerator


def main():
    arg_parser = CliArgParser()
    arg_parser.parse(sys.argv[1:])

    with open(arg_parser.args.config, "r") as stream:
        try:
            config = yaml.safe_load(stream)
            pg = PdfGenerator(config)
            pg.make_pdf(arg_parser.args.output)
        except yaml.YAMLError as exc:
            print(exc)


if __name__ == "__main__":
    main()
