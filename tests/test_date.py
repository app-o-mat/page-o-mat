import unittest
from pageomat.pdf_generator import PdfGenerator
from tests.mock_config import mock_config


class TestDate(unittest.TestCase):
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
