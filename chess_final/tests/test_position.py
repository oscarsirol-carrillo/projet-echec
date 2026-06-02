# Tests unitaires de la classe Position (framework unittest, cf cours)

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import unittest
from position import Position


class TestPosition(unittest.TestCase):
    def test_str_format_echecs(self):
        """La methode __str__ doit renvoyer 'e2' pour la colonne e et la ligne 2."""
        p = Position("e", 2)
        self.assertEqual(str(p), "e2")

    def test_egalite_deux_positions(self):
        """Deux Position avec memes col/row doivent etre egales (__eq__)."""
        self.assertEqual(Position("a", 1), Position("a", 1))
        self.assertNotEqual(Position("a", 1), Position("a", 2))

    def test_position_utilisable_dans_un_dict(self):
        """Position doit etre hashable pour servir de cle de dictionnaire."""
        d = {Position("e", 4): "pion blanc"}
        self.assertEqual(d[Position("e", 4)], "pion blanc")

    def test_getters_encapsulation(self):
        """Les attributs sont accessibles via @property."""
        p = Position("h", 8)
        self.assertEqual(p.column, "h")
        self.assertEqual(p.row, 8)


if __name__ == "__main__":
    unittest.main()
