import argparse


class JGArgParser:

    arg_parser = None
    args = None

    def __init__(self, parser=None):
        """Unittests use the parser argument so that they can test the errors."""
        if parser is not None:
            self.arg_parser = parser
        else:
            self.arg_parser = argparse.ArgumentParser(description="Runs Journal Generator")

        self.arg_parser.add_argument(
            "--config", help="name of the journal config file", required=True
        )
        self.arg_parser.add_argument(
            "--output", help="name of the pdf file", required=True
        )

    def parse(self, arg_array):
        self.args = self.arg_parser.parse_args(arg_array)
