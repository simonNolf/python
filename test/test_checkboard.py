import unittest
import sys

from Checkboard import Checkboard

sys.path.append("..")


class Test_chackboard(unittest.TestCase):
    def test_square(self):
        c = Checkboard()
        self.assertEqual(c.square, 10)

    def test_turn(self):
        c = Checkboard()
        self.assertEqual(c.turn, True)

    def test_board(self):
        c = Checkboard()
        self.assertEqual(type(c.board), type([]))

    def test_score(self):
        c = Checkboard()
        self.assertEqual(type(c.score), type({}))

    def test_changeturn(self):
        c = Checkboard()
        c.changeturn()
        self.assertEqual(c.turn, False)

    def test_update_score(self):
        c = Checkboard()
        c.update_score('blancs', 2)
        self.assertEqual(c.score, {'blancs': 2, 'noirs': 0})

    def test_loadpawns(self):
        c = Checkboard()
        self.assertEqual(type(c.loadpawns()), type({}))

    def test_modifyboard(self):
        c = Checkboard()
        c.modifyboard((4, 3), (4, 4))
        self.assertEqual(c.board,[
            ["--", "wp", "--", "wp", "--", "wp", "--", "wp", "--", "wp"],
            ["wp", "--", "wp", "--", "wp", "--", "wp", "--", "wp", "--"],
            ["--", "wp", "--", "wp", "--", "wp", "--", "wp", "--", "wp"],
            ["wp", "--", "wp", "--", "--", "--", "wp", "--", "wp", "--"],
            ["--", "--", "--", "--", "wp", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "bp", "--", "bp", "--", "bp", "--", "bp", "--", "bp"],
            ["bp", "--", "bp", "--", "bp", "--", "bp", "--", "bp", "--"],
            ["--", "bp", "--", "bp", "--", "bp", "--", "bp", "--", "bp"],
            ["bp", "--", "bp", "--", "bp", "--", "bp", "--", "bp", "--"]
        ])

    def test_count_pawn(self):
        c =  Checkboard()
        self.assertEqual(c.countpawns(), [20,20,0,0])

    def test_samepawn(self):
        c = Checkboard()
        self.assertEqual(c.modifyboard((4,4), (4,4)), False)

    def test_diagonale(self):
        c = Checkboard()
        self.assertEqual(c.modifyboard((4,3), (5,4)), False)
        self.assertEqual(c.modifyboard((4,3), (3,4)), False)

