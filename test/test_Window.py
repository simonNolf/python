import unittest
import sys

sys.path.append("..")
from Windows import Screen


class TestWindow(unittest.TestCase):
    def test_width(self):
        w = Screen()
        self.assertEqual(w.width, 800)

    def test_height(self):
        w = Screen()
        self.assertEqual(w.height, 950)
