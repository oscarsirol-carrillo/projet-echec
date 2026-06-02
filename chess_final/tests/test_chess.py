# Tests unitaires de la classe Chess

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import unittest
from chess import Chess
from player import Player


class TestChess(unittest.TestCase):

    def setUp(self):
        """Prepare un Chess avec 2 joueurs sans demander de saisie clavier."""
        self.chess = Chess()
        self.chess._players = [Player("Alice", 0), Player("Bob", 1)]
        self.chess._currentPlayer = self.chess._players[0]

    def test_coup_valide_pion_blanc(self):
        self.assertTrue(self.chess.isValidMove("Pe2 Pe4"))

    def test_coup_invalide_format_incorrect(self):
        self.assertFalse(self.chess.isValidMove("blabla"))

    def test_coup_invalide_piece_adverse(self):
        """Les blancs ne peuvent pas deplacer un pion noir."""
        self.assertFalse(self.chess.isValidMove("Pe7 Pe5"))

    def test_updateBoard_applique_le_coup(self):
        self.chess.updateBoard("Pe2 Pe4")
        from position import Position
        self.assertIsNone(self.chess.board.getPiece(Position("e", 2)))
        self.assertIsNotNone(self.chess.board.getPiece(Position("e", 4)))

    def test_switchPlayer_change_de_joueur(self):
        joueur1 = self.chess.currentPlayer
        self.chess.switchPlayer()
        self.assertIsNot(self.chess.currentPlayer, joueur1)
        self.chess.switchPlayer()
        self.assertIs(self.chess.currentPlayer, joueur1)

    def test_isCheckMate_retourne_false(self):
        """Premiere version : doit toujours retourner False."""
        self.assertFalse(self.chess.isCheckMate())


if __name__ == "__main__":
    unittest.main()
