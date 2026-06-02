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
    """Joueur IA : redefinit askMove pour generer un coup aleatoire (cours 03a)."""

    def askMove(self):
        cols = "abcdefgh"
        depart = random.choice(cols) + str(random.randint(1, 8))
        arrivee = random.choice(cols) + str(random.randint(1, 8))
        lettre = random.choice("KQBNRP")
        coup = lettre + depart + " " + lettre + arrivee
        print(f"{self._name} (IA) joue : {coup}")
        return coup
