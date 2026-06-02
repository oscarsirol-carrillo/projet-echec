# Classe Board : represente l'echiquier 8x8
# Utilise un DICTIONNAIRE { Position : Piece } pour stocker les pieces
# (contrainte du sujet : au moins 1 liste et 1 dictionnaire dans le projet)

from position import Position
from piece import King, Queen, Bishop, Knight, Rook, Pawn


class Board:
    def __init__(self):
        # Dictionnaire qui associe une Position a la Piece presente dessus.
        # Pourquoi un dict ? Acces direct en O(1) par Position, et une case
        # vide = absence de cle (au lieu de stocker None partout).
        self._pieces = {}

        # L'ordre des pieces sur la 1ere et la 8eme rangee
        ordre = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i, col in enumerate("abcdefgh"):
            # Pieces blanches (ligne 1) et leurs pions (ligne 2)
            self._pieces[Position(col, 1)] = ordre[i](Position(col, 1), 0)
            self._pieces[Position(col, 2)] = Pawn(Position(col, 2), 0)
            # Pions noirs (ligne 7) et pieces noires (ligne 8)
            self._pieces[Position(col, 7)] = Pawn(Position(col, 7), 1)
            self._pieces[Position(col, 8)] = ordre[i](Position(col, 8), 1)

    # Encapsulation : on expose un getter pour le dict
    @property
    def pieces(self):
        return self._pieces

    def getPiece(self, position):
        """Retourne la piece a la position donnee, ou None si vide."""
        return self._pieces.get(position)

    def getPosition(self, piece):
        """Retourne la position de la piece, ou None si elle a ete capturee."""
        for pos, p in self._pieces.items():
            if p is piece:
                return pos
        return None

    def move(self, from_pos, to_pos):
        """Deplace la piece (capture eventuelle de la piece adverse)."""
        piece = self._pieces.pop(from_pos)
        self._pieces[to_pos] = piece     # ecrase la piece capturee si presente
        piece.position = to_pos
