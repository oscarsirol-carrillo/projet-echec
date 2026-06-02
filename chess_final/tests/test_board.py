# Tests unitaires de la classe Board

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import unittest
from position import Position
from piece import King, Pawn
from board import Board


class TestBoard(unittest.TestCase):

    def test_initialisation_32_pieces(self):
        """Au depart, l'echiquier doit contenir exactement 32 pieces."""
        b = Board()
        self.assertEqual(len(b.pieces), 32)

    def test_roi_blanc_en_e1(self):
        b = Board()
        roi = b.getPiece(Position("e", 1))
        self.assertIsInstance(roi, King)
        self.assertEqual(roi.color, 0)

    def test_case_centrale_vide(self):
        b = Board()
        self.assertIsNone(b.getPiece(Position("e", 4)))

    def test_getPosition_d_une_piece(self):
        b = Board()
        pion = b.getPiece(Position("d", 2))
        self.assertEqual(b.getPosition(pion), Position("d", 2))

    def test_move_deplace_la_piece(self):
        b = Board()
        b.move(Position("e", 2), Position("e", 4))
        self.assertIsNone(b.getPiece(Position("e", 2)))
        piece = b.getPiece(Position("e", 4))
        self.assertIsInstance(piece, Pawn)


if __name__ == "__main__":
    unittest.main()
