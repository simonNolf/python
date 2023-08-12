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
    def test_set_name(self):
        w = Screen()
        w.set_name('test')
        self.assertEqual(w.screen.get_caption(), ('test', 'test'))

    def test_name(self):
        w = Screen()
        with self.assertRaises(TypeError):
            w.set_name(123)
