# Classe Position : represente une case de l'echiquier (ex: "e2")
# Utilise l'encapsulation (cours 02a) avec _attribut et @property


class Position:
    def __init__(self, column, row):
        self._column = column   # un caractere de "a" a "h"
        self._row = row         # un entier de 1 a 8

    # --- Getters (encapsulation, cours 02a) ---
    @property
    def column(self):
        return self._column

    @property
    def row(self):
        return self._row

    # --- Methodes speciales (dunder methods, cours 01b) ---
    def __str__(self):
        # Affiche la position au format standard echecs : "e2"
        return self._column + str(self._row)

    def __eq__(self, other):
        # Deux positions sont egales si meme colonne et meme ligne
        return self._column == other._column and self._row == other._row

    def __hash__(self):
        # Necessaire pour utiliser Position comme cle de dictionnaire
        return hash((self._column, self._row))
