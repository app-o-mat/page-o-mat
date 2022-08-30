import unittest
from pageomat.pages.page import Page

from pageomat.pdf_generator import PdfGenerator
from tests.mock_config import mock_config


class TestPages(unittest.TestCase):
    def test_blank_paper_default(self):
        p = {"type": "simple"}
        pg = PdfGenerator(mock_config([p]))
        self.assertEqual(pg.module_for_paper(p), "pageomat.pages.paper.blank")
        self.assertEqual(pg.module_for_template(p), "pageomat.pages.template.simple")

    def test_default_paper_override(self):
        p = {"type": "horizontal-split"}
        c = mock_config([p])
        c["defaults"] = {"paper": {"type": "grid"}}
        pg = PdfGenerator(c)
        self.assertEqual(pg.module_for_paper(p), "pageomat.pages.paper.grid")
        self.assertEqual(pg.module_for_template(p), "pageomat.pages.template.horizontal_split")

    def test_page_paper_override(self):
        p = {"type": "simple", "paper": {"type": "dot"}}
        pg = PdfGenerator(mock_config([p]))
        self.assertEqual(pg.module_for_paper(p), "pageomat.pages.paper.dot")

    def test_grid_snap(self):
        p = Page()
        self.assertEqual(p.grid_snap_value(0, 1), 1)
        self.assertEqual(p.grid_snap_value(0, 2), 2)

        self.assertEqual(p.grid_snap_value(1, 1), 1)
        self.assertEqual(p.grid_snap_value(1, 2), 2)
        self.assertEqual(p.grid_snap_value(1, 2.1), 2)

        self.assertEqual(p.grid_snap_value(2, 1), 0)
        self.assertEqual(p.grid_snap_value(2, 2), 2)
        self.assertEqual(p.grid_snap_value(2, 3), 2)
        self.assertEqual(p.grid_snap_value(2, 3.2), 2)

        self.assertEqual(p.grid_snap_value(5, 5), 5)
        self.assertEqual(p.grid_snap_value(5, 6), 5)
        self.assertEqual(p.grid_snap_value(5, 10.2), 10)
        self.assertEqual(p.grid_snap_value(5, 28.2), 25)
