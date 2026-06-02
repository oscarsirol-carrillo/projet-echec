# Tests unitaires des pieces du jeu

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import unittest
from position import Position
from piece import Piece, King, Queen, Bishop, Knight, Rook, Pawn
from board import Board


class TestPieces(unittest.TestCase):

    def test_classe_abstraite_non_instanciable(self):
        """Piece est abstraite, on ne peut pas l'instancier directement (cours 04a)."""
        with self.assertRaises(TypeError):
            Piece(Position("a", 1), 0)

    def test_lettres_str(self):
        """__str__ doit renvoyer la lettre conforme au cahier des charges."""
        p = Position("a", 1)
        self.assertEqual(str(King(p, 0)), "K")
        self.assertEqual(str(Queen(p, 0)), "Q")
        self.assertEqual(str(Bishop(p, 0)), "B")
        self.assertEqual(str(Knight(p, 0)), "N")
        self.assertEqual(str(Rook(p, 0)), "R")
        self.assertEqual(str(Pawn(p, 0)), "P")

    def test_pion_avance_d_une_case(self):
        b = Board()
        # Vide la case devant le pion e2
        b._pieces.pop(Position("e", 3), None)
        pion = b.getPiece(Position("e", 2))
        self.assertTrue(pion.isValidMove(Position("e", 3), b))
        # Recule = interdit
        self.assertFalse(pion.isValidMove(Position("e", 1), b))

    def test_pion_double_avance_depuis_position_initiale(self):
        b = Board()
        pion = b.getPiece(Position("e", 2))
        self.assertTrue(pion.isValidMove(Position("e", 4), b))

    def test_cavalier_en_L(self):
        b = Board()
        cav = b.getPiece(Position("b", 1))
        # Saut en L valide
        self.assertTrue(cav.isValidMove(Position("c", 3), b))
        # Trop loin
        self.assertFalse(cav.isValidMove(Position("b", 3), b))

    def test_tour_bloquee_par_pion(self):
        """La tour ne peut pas traverser un pion en debut de partie."""
        b = Board()
        tour = b.getPiece(Position("a", 1))
        # a3 est inaccessible car le pion a2 bloque le passage
        self.assertFalse(tour.isValidMove(Position("a", 3), b))

    def test_fou_diagonale(self):
        b = Board()
        fou = Bishop(Position("c", 4), 0)
        # Diagonale libre (les cases sont vides au milieu)
        self.assertTrue(fou.isValidMove(Position("e", 6), b))
        # Pas une diagonale
        self.assertFalse(fou.isValidMove(Position("c", 6), b))

    def test_roi_une_case_seulement(self):
        b = Board()
        roi = King(Position("e", 4), 0)
        self.assertTrue(roi.isValidMove(Position("e", 5), b))
        self.assertFalse(roi.isValidMove(Position("e", 6), b))

    def test_reine_combine_tour_et_fou(self):
        b = Board()
        reine = Queen(Position("d", 4), 0)
        self.assertTrue(reine.isValidMove(Position("d", 6), b))     # ligne
        self.assertTrue(reine.isValidMove(Position("g", 4), b))     # colonne
        self.assertTrue(reine.isValidMove(Position("f", 6), b))     # diagonale
        self.assertFalse(reine.isValidMove(Position("e", 6), b))    # ni l'un ni l'autre


if __name__ == "__main__":
    unittest.main()
