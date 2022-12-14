import unittest
import argparse
from pageomat.cli_arg_parser import CliArgParser


class ErrorRaisingArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise ValueError(message)


class TestArgParser(unittest.TestCase):

    def test_empty_args_has_error(self):
        arg_parser = CliArgParser(ErrorRaisingArgumentParser())
        with self.assertRaises(ValueError) as cm1:
            arg_parser.parse([])
        self.assertIn("arguments are required", str(cm1.exception))

    def test_missing_arg_has_error(self):
        arg_parser = CliArgParser(ErrorRaisingArgumentParser())
        with self.assertRaises(ValueError) as cm1:
            arg_parser.parse(["--config", "c"])
        self.assertIn("arguments are required", str(cm1.exception))

        with self.assertRaises(ValueError) as cm2:
            arg_parser.parse(["--output", "o"])
        self.assertIn("arguments are required", str(cm2.exception))

    def test_correct_args(self):
        arg_parser = CliArgParser(ErrorRaisingArgumentParser())
        arg_parser.parse(["--config", "c", "--output", "o"])
        self.assertEqual(arg_parser.args.config, "c")
        self.assertEqual(arg_parser.args.output, "o")
