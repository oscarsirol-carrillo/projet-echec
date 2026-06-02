# Classes des pieces : une classe abstraite Piece (cours 04a)
# et 6 sous-classes utilisant le polymorphisme (cours 03a)

from abc import ABC, abstractmethod


class Piece(ABC):
    """Classe abstraite : impose un contrat aux sous-classes (cours 04a)."""

    def __init__(self, position, color):
        self._position = position
        self._color = color   # 0 = blanc, 1 = noir

    # --- Encapsulation : getters et setter pour la position (cours 02a) ---
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position):
        self._position = new_position

    @property
    def color(self):
        return self._color

    # --- Methode abstraite : DOIT etre redefinie dans chaque sous-classe ---
    @abstractmethod
    def isValidMove(self, newPosition, board):
        """Retourne True si le deplacement respecte les regles."""
        pass

    @abstractmethod
    def __str__(self):
        pass

    # --- Methode concrete utilisable par toutes les sous-classes ---
    # (une classe abstraite peut contenir des methodes concretes, cf cours 04a)
    def _path_libre(self, newPosition, board):
        """Verifie qu'aucune piece ne bloque le chemin en ligne droite ou diagonale.
        Ne verifie PAS la case de destination (geree separement)."""
        c1 = ord(self._position.column)
        c2 = ord(newPosition.column)
        r1 = self._position.row
        r2 = newPosition.row
        # Direction du deplacement (-1, 0 ou +1 sur chaque axe)
        dc = (c2 > c1) - (c2 < c1)
        dr = (r2 > r1) - (r2 < r1)
        # On avance case par case
        c, r = c1 + dc, r1 + dr
        from position import Position
        while (c, r) != (c2, r2):
            if board.getPiece(Position(chr(c), r)) is not None:
                return False
            c += dc
            r += dr
        return True


# --------- Les 6 sous-classes (polymorphisme : isValidMove redefini) ---------

class King(Piece):
    def isValidMove(self, newPosition, board):
        dc = abs(ord(newPosition.column) - ord(self._position.column))
        dr = abs(newPosition.row - self._position.row)
        return (dc + dr > 0) and dc <= 1 and dr <= 1

    def __str__(self):
        return "K"


class Queen(Piece):
    def isValidMove(self, newPosition, board):
        dc = abs(ord(newPosition.column) - ord(self._position.column))
        dr = abs(newPosition.row - self._position.row)
        # Reine = combinaison Tour + Fou
        ligne_droite = (dc == 0 or dr == 0)
        diagonale = (dc == dr)
        if not (ligne_droite or diagonale) or (dc + dr == 0):
            return False
        return self._path_libre(newPosition, board)

    def __str__(self):
        return "Q"


class Bishop(Piece):
    def isValidMove(self, newPosition, board):
        dc = abs(ord(newPosition.column) - ord(self._position.column))
        dr = abs(newPosition.row - self._position.row)
        if dc != dr or dc == 0:
            return False
        return self._path_libre(newPosition, board)

    def __str__(self):
        return "B"


class Knight(Piece):
    def isValidMove(self, newPosition, board):
        dc = abs(ord(newPosition.column) - ord(self._position.column))
        dr = abs(newPosition.row - self._position.row)
        # Le cavalier saute par dessus les pieces : pas de verif du chemin
        return (dc == 1 and dr == 2) or (dc == 2 and dr == 1)

    def __str__(self):
        return "N"


class Rook(Piece):
    def isValidMove(self, newPosition, board):
        meme_col = newPosition.column == self._position.column
        meme_row = newPosition.row == self._position.row
        # Exactement un des deux doit etre vrai (XOR)
        if meme_col == meme_row:
            return False
        return self._path_libre(newPosition, board)

    def __str__(self):
        return "R"


class Pawn(Piece):
    def isValidMove(self, newPosition, board):
        # Blanc avance vers le haut (+1), noir vers le bas (-1)
        direction = 1 if self._color == 0 else -1
        rangee_init = 2 if self._color == 0 else 7
        dc = ord(newPosition.column) - ord(self._position.column)
        dr = newPosition.row - self._position.row
        cible = board.getPiece(newPosition)

        # Avance tout droit (pas de capture autorisee)
        if dc == 0 and cible is None:
            if dr == direction:
                return True
            # Double avance depuis la rangee initiale
            if dr == 2 * direction and self._position.row == rangee_init:
                return self._path_libre(newPosition, board)
            return False

        # Capture en diagonale (1 case)
        if abs(dc) == 1 and dr == direction and cible is not None:
            return True

        return False

    def __str__(self):
        return "P"
