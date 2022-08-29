import unittest
from tests.mock_config import mock_config
from pageomat.pdf_generator import PdfGenerator


class TestPdfGeneration(unittest.TestCase):
    def test_one_blank(self):
        config = mock_config([{"type": "blank"}])
        pg = PdfGenerator(config)
        self.assertEqual(pg.num_pages(), 1)

    def test_two_blanks(self):
        config = mock_config([
            {"type": "blank"},
            {"type": "blank"}
        ])
        pg = PdfGenerator(config)
        self.assertEqual(pg.num_pages(), 2)

    def test_count(self):
        config = mock_config([
            {"count": 2, "type": "blank"},
            {"count": 3, "type": "blank"}
        ])
        pg = PdfGenerator(config)
        self.assertEqual(pg.num_pages(), 5)

    def test_variant_count(self):
        config = mock_config([
            {"count": 2, "type": "blank", "variants": ["a", "b"]},
            {"count": 3, "type": "blank"}
        ])
        pg = PdfGenerator(config)
        self.assertEqual(pg.num_pages(), 7)

    def test_flatten_pages(self):
        config = mock_config([
            {"count": 2, "type": "blank", "variants": ["a", "b"]},
            {"count": 3, "type": "blank"}
        ])
        pg = PdfGenerator(config)
        pages = pg.pages()
        self.assertEqual(pages, [
            {"type": "blank", "variant": "a"},
            {"type": "blank", "variant": "a"},
            {"type": "blank", "variant": "b"},
            {"type": "blank", "variant": "b"},
            {"type": "blank"},
            {"type": "blank"},
            {"type": "blank"}
        ])

    def test_flatten_sub_pages(self):
        config = mock_config([
            {"count": 3, "pages": [{"count": 2, "type": "blank", "variants": ["a", "b"]}]}
        ])
        pg = PdfGenerator(config)
        pages = pg.pages()
        self.assertEqual(pages, [
            {"type": "blank", "variant": "a"},
            {"type": "blank", "variant": "a"},
            {"type": "blank", "variant": "b"},
            {"type": "blank", "variant": "b"},
            {"type": "blank", "variant": "a"},
            {"type": "blank", "variant": "a"},
            {"type": "blank", "variant": "b"},
            {"type": "blank", "variant": "b"},
            {"type": "blank", "variant": "a"},
            {"type": "blank", "variant": "a"},
            {"type": "blank", "variant": "b"},
            {"type": "blank", "variant": "b"},
        ])
