import unittest
from pageomat.pages.date_utils import format_day_of_year
from pageomat.pdf_generator import PdfGenerator
from tests.mock_config import mock_config


class TestDate(unittest.TestCase):
    def test_date_format(self):
        self.assertEqual(format_day_of_year(2023, 1, "%A - %-d %b", {}), "Sunday - 1 Jan")
        self.assertEqual(format_day_of_year(2023, 365, "%A - %-d %b", {}), "Sunday - 31 Dec")

    def test_date_format_vars(self):
        vars = {"__builtins__": None, "c": [1]}
        self.assertEqual(format_day_of_year(2023, "c[0]", "%A - %-d %b", vars), "Sunday - 1 Jan")
        self.assertEqual(format_day_of_year(2023, "364 + c[0]", "%A - %-d %b", vars), "Sunday - 31 Dec")

    def test_date(self):
        config = mock_config([{
            "type": "simple",
            "title": "$date$",
            "day-of-year": 1,
            "date-format": "%A - %-d %b"
        }, {
            "type": "simple",
            "title": "$date$",
            "day-of-year": 32,
            "date-format": "%A - %-d %b"
        }])
        config["defaults"] = {"year": 2023}
        pg = PdfGenerator(config)
        pages = pg.pages()
        self.assertEqual(pages[0]["title"], "Sunday - 1 Jan")
        self.assertEqual(pages[1]["title"], "Wednesday - 1 Feb")
