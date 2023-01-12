import unittest
import sys

sys.path.append("..")
from Game import Game


class Test_game(unittest.TestCase):
    def test_game(self):
        g = Game()
        self.assertEqual(g.game, True)

    def test_finished(self):
        g = Game()
        g.finished()
        self.assertEqual(g.game, False)
