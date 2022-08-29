import unittest

from pageomat.pdf_generator import PdfGenerator
from tests.mock_config import mock_config


class TestBlankPages(unittest.TestCase):
    def test_blank_paper_default(self):
        p = {"type": "blank"}
        pg = PdfGenerator(mock_config([p]))
        self.assertEqual(pg.module_for_paper(p), "pageomat.pages.paper.blank")

    def test_default_paper_override(self):
        p = {"type": "blank"}
        c = mock_config([p])
        c["defaults"] = {"paper": {"type": "grid"}}
        pg = PdfGenerator(c)
        self.assertEqual(pg.module_for_paper(p), "pageomat.pages.paper.grid")

    def test_page_paper_override(self):
        p = {"type": "blank", "paper": {"type": "dot"}}
        pg = PdfGenerator(mock_config([p]))
        self.assertEqual(pg.module_for_paper(p), "pageomat.pages.paper.dot")
