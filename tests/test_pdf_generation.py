import unittest
from pageomat.pdf_generator import PdfGenerator


class TestPdfGeneration(unittest.TestCase):

    def config_with_pages(self, pages):
        return {
            "page-size": "A5",
            "default-blank": {"type": "blank"},
            "pages": pages
        }

    def test_one_blank(self):
        config = self.config_with_pages([{"type": "blank"}])
        pg = PdfGenerator(config)
        self.assertEqual(pg.num_pages(), 1)

    def test_two_blanks(self):
        config = self.config_with_pages([
            {"type": "blank"},
            {"type": "blank"}
        ])
        pg = PdfGenerator(config)
        self.assertEqual(pg.num_pages(), 2)

    def test_count(self):
        config = self.config_with_pages([
            {"count": 2, "type": "blank"},
            {"count": 3, "type": "blank"}
        ])
        pg = PdfGenerator(config)
        self.assertEqual(pg.num_pages(), 5)

    def test_variant_count(self):
        config = self.config_with_pages([
            {"count": 2, "type": "blank", "variants": ["a", "b"]},
            {"count": 3, "type": "blank"}
        ])
        pg = PdfGenerator(config)
        self.assertEqual(pg.num_pages(), 7)
