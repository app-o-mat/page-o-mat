import unittest
from tests.mock_config import mock_config
from pageomat.pdf_generator import PdfGenerator


class TestPdfGeneration(unittest.TestCase):

    def test_page_size_default(self):
        config = mock_config([{"type": "blank"}])
        pg = PdfGenerator(config)
        self.assertEqual(pg.page_size_name(), "A5")
        self.assertEqual(pg.page_unit(), "mm")

    def test_page_size(self):
        config = mock_config([{"type": "blank"}])
        config["page-size"] = "Letter"
        pg = PdfGenerator(config)
        self.assertEqual(pg.page_size_name(), "Letter")
        self.assertEqual(pg.page_unit(), "in")

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

    def test_simple_flatten_pages_indices(self):
        config = mock_config([
            {"type": "blank"},
            {"type": "blank"}
        ])
        pg = PdfGenerator(config)
        pages = pg.pages(include_indices=True)
        self.assertEqual(pages, [
            {"type": "blank", "indices": {"p": 0, "c": [0], "v": 0}},
            {"type": "blank", "indices": {"p": 1, "c": [0], "v": 0}}
        ])

    def test_flatten_pages_indices(self):
        config = mock_config([
            {"count": 2, "type": "blank", "variants": ["a", "b"]},
            {"count": 3, "type": "blank"}
        ])
        pg = PdfGenerator(config)
        pages = pg.pages(include_indices=True)
        self.assertEqual(pages, [
            {"type": "blank", "variant": "a", "indices": {"p": 0, "c": [0], "v": 0}},
            {"type": "blank", "variant": "a", "indices": {"p": 1, "c": [1], "v": 0}},
            {"type": "blank", "variant": "b", "indices": {"p": 2, "c": [0], "v": 1}},
            {"type": "blank", "variant": "b", "indices": {"p": 3, "c": [1], "v": 1}},
            {"type": "blank", "indices": {"p": 4, "c": [0], "v": 0}},
            {"type": "blank", "indices": {"p": 5, "c": [1], "v": 0}},
            {"type": "blank", "indices": {"p": 6, "c": [2], "v": 0}}
        ])

    def test_flatten_pages_parent_variant(self):
        config = mock_config([
            {"variants": ["a", "b"], "pages": [{"type": "blank"}]},
        ])
        pg = PdfGenerator(config)
        pages = pg.pages()
        self.assertEqual(pages, [
            {"type": "blank", "variant": "a"},
            {"type": "blank", "variant": "b"}
        ])

    def test_flatten_pages_parent_variant_override(self):
        config = mock_config([
            {"variants": ["a", "b"], "pages": [{"type": "blank", "variants": ["$variant$ c"]}]},
        ])
        pg = PdfGenerator(config)
        pages = pg.pages()
        self.assertEqual(pages, [
            {"type": "blank", "variant": "a c"},
            {"type": "blank", "variant": "b c"}
        ])

    def test_flatten_sub_pages(self):
        config = mock_config([
            {"count": 3, "pages": [{"count": 2, "type": "blank", "variants": ["a", "b"]}]}
        ])
        pg = PdfGenerator(config)
        pages = pg.pages(include_indices=True)
        self.assertEqual(pages, [
            {"type": "blank", "variant": "a", "indices": {"p": 0, "c": [0, 0], "v": 0}},
            {"type": "blank", "variant": "a", "indices": {"p": 1, "c": [0, 1], "v": 0}},
            {"type": "blank", "variant": "b", "indices": {"p": 2, "c": [0, 0], "v": 1}},
            {"type": "blank", "variant": "b", "indices": {"p": 3, "c": [0, 1], "v": 1}},
            {"type": "blank", "variant": "a", "indices": {"p": 4, "c": [1, 0], "v": 0}},
            {"type": "blank", "variant": "a", "indices": {"p": 5, "c": [1, 1], "v": 0}},
            {"type": "blank", "variant": "b", "indices": {"p": 6, "c": [1, 0], "v": 1}},
            {"type": "blank", "variant": "b", "indices": {"p": 7, "c": [1, 1], "v": 1}},
            {"type": "blank", "variant": "a", "indices": {"p": 8, "c": [2, 0], "v": 0}},
            {"type": "blank", "variant": "a", "indices": {"p": 9, "c": [2, 1], "v": 0}},
            {"type": "blank", "variant": "b", "indices": {"p": 10, "c": [2, 0], "v": 1}},
            {"type": "blank", "variant": "b", "indices": {"p": 11, "c": [2, 1], "v": 1}},
        ])

    def test_substitute_variables(self):
        pg = PdfGenerator({})
        self.assertEqual(pg.substitute_variables("", {}), "")
        self.assertEqual(pg.substitute_variables("a", {}), "a")
        self.assertEqual(pg.substitute_variables("a", {"variant": "XX"}), "a")
        self.assertEqual(pg.substitute_variables("a$variant$", {"variant": "XX"}), "aXX")
        self.assertEqual(pg.substitute_variables("$variant$$variant$", {"variant": "XX"}), "XXXX")

    def test_sub_variables_in_page(self):
        config = mock_config([
            {"count": 2, "type": "blank", "variants": ["a", "b"], "title": "$variant$"}
        ])
        pg = PdfGenerator(config)
        pages = pg.pages()
        self.assertEqual(pages, [
            {"type": "blank", "variant": "a", "title": "a"},
            {"type": "blank", "variant": "a", "title": "a"},
            {"type": "blank", "variant": "b", "title": "b"},
            {"type": "blank", "variant": "b", "title": "b"},
        ])
