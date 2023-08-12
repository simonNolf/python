import unittest
import sys

import pygame

from Checkboard import Checkboard

sys.path.append("..")


class TestCheckboard(unittest.TestCase):
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

    def test_score_negatif(self):
        c = Checkboard()
        c.update_score('blancs', -2)
        self.assertEqual(c.score, {'blancs': -2, 'noirs': 0})

    def test_score_0(self):
        c = Checkboard()
        self.assertEqual(c.score, {'blancs': 0, 'noirs': 0})

    def test_loadpawns(self):
        c = Checkboard()
        self.assertEqual(type(c.loadpawns()), type({}))

    def test_modifyboard(self):
        c = Checkboard()
        c.modifyboard((4, 3), (4, 4))
        self.assertEqual(c.board, [
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

    def test_modifyboard_more_than_on_case(self):
        c = Checkboard()
        c.modifyboard((4, 3), (4, 5))
        self.assertEqual(c.board, [['--', 'wp', '--', 'wp', '--', 'wp', '--', 'wp', '--', 'wp'],
 ['wp', '--', 'wp', '--', 'wp', '--', 'wp', '--', 'wp', '--'],
 ['--', 'wp', '--', 'wp', '--', 'wp', '--', 'wp', '--', 'wp'],
 ['wp', '--', 'wp', '--', 'wp', '--', 'wp', '--', 'wp', '--'],
 ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--'],
 ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--'],
 ['--', 'bp', '--', 'bp', '--', 'bp', '--', 'bp', '--', 'bp'],
 ['bp', '--', 'bp', '--', 'bp', '--', 'bp', '--', 'bp', '--'],
 ['--', 'bp', '--', 'bp', '--', 'bp', '--', 'bp', '--', 'bp'],
 ['bp', '--', 'bp', '--', 'bp', '--', 'bp', '--', 'bp', '--']])

    def test_eat_pawn(self):
        c = Checkboard()
        c.modifyboard((4,3), (4,4))
        c.modifyboard((5,6), (5,5))
        c.modifyboard((4,4), (6,6))
        self.assertEqual(c.board, [
            ["--", "wp", "--", "wp", "--", "wp", "--", "wp", "--", "wp"],
            ["wp", "--", "wp", "--", "wp", "--", "wp", "--", "wp", "--"],
            ["--", "wp", "--", "wp", "--", "wp", "--", "wp", "--", "wp"],
            ["wp", "--", "wp", "--", "--", "--", "wp", "--", "wp", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "bp", "--", "bp", "--", "--", "wp", "bp", "--", "bp"],
            ["bp", "--", "bp", "--", "bp", "--", "bp", "--", "bp", "--"],
            ["--", "bp", "--", "bp", "--", "bp", "--", "bp", "--", "bp"],
            ["bp", "--", "bp", "--", "bp", "--", "bp", "--", "bp", "--"]])

    def test_travere_board(self):
        c = Checkboard()
        c.modifyboard((0,1), (9,1))
        self.assertEqual(c.board,[
            ["--", "wp", "--", "wp", "--", "wp", "--", "wp", "--", "wp"],
            ["wp", "--", "wp", "--", "wp", "--", "wp", "--", "wp", "--"],
            ["--", "wp", "--", "wp", "--", "wp", "--", "wp", "--", "wp"],
            ["wp", "--", "wp", "--", "wp", "--", "wp", "--", "wp", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "bp", "--", "bp", "--", "bp", "--", "bp", "--", "bp"],
            ["bp", "--", "bp", "--", "bp", "--", "bp", "--", "bp", "--"],
            ["--", "bp", "--", "bp", "--", "bp", "--", "bp", "--", "bp"],
            ["bp", "--", "bp", "--", "bp", "--", "bp", "--", "bp", "--"]
        ])

    def test_déplacement_droite(self):
        c = Checkboard()
        c.modifyboard((4,3), (5,3))
        self.assertEqual(c.board, [
            ["--", "wp", "--", "wp", "--", "wp", "--", "wp", "--", "wp"],
            ["wp", "--", "wp", "--", "wp", "--", "wp", "--", "wp", "--"],
            ["--", "wp", "--", "wp", "--", "wp", "--", "wp", "--", "wp"],
            ["wp", "--", "wp", "--", "wp", "--", "wp", "--", "wp", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "bp", "--", "bp", "--", "bp", "--", "bp", "--", "bp"],
            ["bp", "--", "bp", "--", "bp", "--", "bp", "--", "bp", "--"],
            ["--", "bp", "--", "bp", "--", "bp", "--", "bp", "--", "bp"],
            ["bp", "--", "bp", "--", "bp", "--", "bp", "--", "bp", "--"]
        ])
    def test_déplacement_gauche(self):
        c = Checkboard()
        c.modifyboard((4,3), (3,3))
        self.assertEqual(c.board, [
            ["--", "wp", "--", "wp", "--", "wp", "--", "wp", "--", "wp"],
            ["wp", "--", "wp", "--", "wp", "--", "wp", "--", "wp", "--"],
            ["--", "wp", "--", "wp", "--", "wp", "--", "wp", "--", "wp"],
            ["wp", "--", "wp", "--", "wp", "--", "wp", "--", "wp", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "bp", "--", "bp", "--", "bp", "--", "bp", "--", "bp"],
            ["bp", "--", "bp", "--", "bp", "--", "bp", "--", "bp", "--"],
            ["--", "bp", "--", "bp", "--", "bp", "--", "bp", "--", "bp"],
            ["bp", "--", "bp", "--", "bp", "--", "bp", "--", "bp", "--"]
        ])
    def test_diagonale_out_droite(self):
        c = Checkboard()
        c.modifyboard((8, 3), (8, 4))
        c.modifyboard((9, 6), (9, 5))
        with self.assertRaises(IndexError):
            c.modifyboard((8, 4), (10, 6))

    def test_multiple_moves(self):
        c = Checkboard()
        c.modifyboard((4,3),(4,4))
        c.modifyboard((6,7), (6,6))
        c.modifyboard((4,4), (4,5))
        c.modifyboard((4,9),(4,8))
        c.modifyboard((4,5),(6,7))
        c.modifyboard((6,6), (6,5))
        c.modifyboard((6,7), (4,9))
        self.assertEqual(c.board, [
            ['--', 'wp', '--', 'wp', '--', 'wp', '--', 'wp', '--', 'wp'],
            ['wp', '--', 'wp', '--', 'wp', '--', 'wp', '--', 'wp', '--'],
            ['--', 'wp', '--', 'wp', '--', 'wp', '--', 'wp', '--', 'wp'],
            ['wp', '--', 'wp', '--', '--', '--', 'wp', '--', 'wp', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', 'bp', '--', '--', '--'],
            ['--', 'bp', '--', 'bp', '--', '--', '--', 'bp', '--', 'bp'],
            ['bp', '--', 'bp', '--', 'bp', '--', '--', '--', 'bp', '--'],
            ['--', 'bp', '--', 'bp', 'bp', '--', '--', 'bp', '--', 'bp'],
            ['bp', '--', 'bp', '--', 'wp', '--', 'bp', '--', 'bp', '--']
        ])
    def test_convert_pawn_to_cheek(self):
        c = Checkboard()
        c.modifyboard((4, 3), (4, 4))
        c.modifyboard((6, 7), (6, 6))
        c.modifyboard((4, 4), (4, 5))
        c.modifyboard((4, 9), (4, 8))
        c.modifyboard((4, 5), (6, 7))
        c.modifyboard((6, 6), (6, 5))
        c.modifyboard((6, 7), (4, 9))
        c.pawn_to_cheek()
        self.assertEqual(c.board, [
            ['--', 'wp', '--', 'wp', '--', 'wp', '--', 'wp', '--', 'wp'],
             ['wp', '--', 'wp', '--', 'wp', '--', 'wp', '--', 'wp', '--'],
             ['--', 'wp', '--', 'wp', '--', 'wp', '--', 'wp', '--', 'wp'],
             ['wp', '--', 'wp', '--', '--', '--', 'wp', '--', 'wp', '--'],
             ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--'],
             ['--', '--', '--', '--', '--', '--', 'bp', '--', '--', '--'],
             ['--', 'bp', '--', 'bp', '--', '--', '--', 'bp', '--', 'bp'],
             ['bp', '--', 'bp', '--', 'bp', '--', '--', '--', 'bp', '--'],
             ['--', 'bp', '--', 'bp', 'bp', '--', '--', 'bp', '--', 'bp'],
             ['bp', '--', 'bp', '--', 'wc', '--', 'bp', '--', 'bp', '--']
        ])

    def test_count_pawn(self):
        c = Checkboard()
        self.assertEqual(c.countpawns(), [20, 20, 0, 0])

    def test_samepawn(self):
        c = Checkboard()
        self.assertEqual(c.modifyboard((4, 4), (4, 4)), False)

    def test_diagonale(self):
        c = Checkboard()
        self.assertEqual(c.modifyboard((4, 3), (5, 4)), False)
        self.assertEqual(c.modifyboard((4, 3), (3, 4)), False)

    def test_raise(self):
        c = Checkboard()
        with self.assertRaises(IndexError) as context:
            c.modifyboard((11, 2), (10, 2))
            self.assertEqual('index out of range', str(context.exception))

if __name__ == '__main__':
    unittest.main()



