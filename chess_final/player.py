# Classes Player et AIPlayer (heritage simple, cours 03a)

import random


class Player:
    def __init__(self, name, color):
        self._name = name
        self._color = color   # 0 = blanc, 1 = noir

    @property
    def name(self):
        return self._name

    @property
    def color(self):
        return self._color

    def askMove(self):
        """Demande au joueur de saisir son coup au format 'Pe2 Pe4'."""
        couleur = "blanc" if self._color == 0 else "noir"
        return input(f"{self._name} ({couleur}) - votre coup (ex: Pe2 Pe4) : ").strip()


class AIPlayer(Player):
    """Joueur IA : redefinit askMove pour generer un coup valide aleatoire (cours 03a)."""

    def askMove(self):
        from position import Position
        board = self._board
        cols = "abcdefgh"
        coups_valides = []
        for pos, piece in list(board.pieces.items()):
            if piece.color != self._color:
                continue
            for c in cols:
                for r in range(1, 9):
                    dest = Position(c, r)
                    cible = board.getPiece(dest)
                    if cible is not None and cible.color == self._color:
                        continue
                    if piece.isValidMove(dest, board):
                        lettre = str(piece)
                        coup = f"{lettre}{pos} {lettre}{dest}"
                        coups_valides.append(coup)
        if not coups_valides:
            return "QUIT"
        coup = random.choice(coups_valides)
        print(f"{self._name} (IA) joue : {coup}")
        return coup
