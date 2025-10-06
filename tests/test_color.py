import unittest
from pageomat.pages.color_utils import hex2num, hex2alpha, hex2red, hex2green, hex2blue


class TestColor(unittest.TestCase):
    def test_red(self):
        self.assertEqual(hex2red("#000"), 0)
        self.assertEqual(hex2red("000"), 0)
        self.assertEqual(hex2red("#000000"), 0)
        self.assertEqual(hex2red("#00FF00FF"), 0)
        self.assertEqual(hex2red("ff0000"), 255)
        self.assertEqual(hex2red("#0FF"), 0)
        self.assertEqual(hex2red("#fFFFFF"), 255)
        self.assertEqual(hex2red("#f00"), 255)
        self.assertEqual(hex2red("#F00"), 255)

    def test_green(self):
        self.assertEqual(hex2green("#040"), 68)
        self.assertEqual(hex2green("#000900"), 9)
        self.assertEqual(hex2green("040"), 68)
        self.assertEqual(hex2green("000900"), 9)
        self.assertEqual(hex2green("000900FF"), 9)
        self.assertEqual(hex2green("#F0F"), 0)
        self.assertEqual(hex2green("FF00FF"), 0)
        self.assertEqual(hex2green("#0F0"), 255)

    def test_blue(self):
        self.assertEqual(hex2blue("#003"), 51)
        self.assertEqual(hex2blue("#00000f"), 15)
        self.assertEqual(hex2blue("00F"), 255)
        self.assertEqual(hex2blue("000003"), 3)
        self.assertEqual(hex2blue("000003FF"), 3)
        self.assertEqual(hex2blue("#FF0"), 0)
        self.assertEqual(hex2blue("FFFF99"), 153)
        self.assertEqual(hex2blue("#009"), 153)

    def test_alpha(self):
        self.assertEqual(hex2alpha("#003"), 255)
        self.assertEqual(hex2alpha("#000000"), 255)
        self.assertEqual(hex2alpha("#000000ff"), 255)
        self.assertEqual(hex2alpha("#00000000"), 0)
        self.assertEqual(hex2alpha("#000000FF"), 255)

    def test_hex2num(self):
        self.assertEqual(hex2num("00"), 0)
        self.assertEqual(hex2num("ff"), 255)
        self.assertEqual(hex2num("FF"), 255)
        self.assertEqual(hex2num("09"), 9)
        self.assertEqual(hex2num("0f"), 15)
        self.assertEqual(hex2num("F0"), 240)
        self.assertEqual(hex2num("99"), 153)

    def test_invalid_color(self):
        with self.assertRaises(ValueError):
            hex2red("#12")
        with self.assertRaises(ValueError):
            hex2green("#1234")
        with self.assertRaises(ValueError):
            hex2blue("#12345")
        with self.assertRaises(ValueError):
            hex2alpha("#1234567")
