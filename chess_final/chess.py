# Classe Chess : gere globalement la partie

from board import Board
from player import Player, AIPlayer
from position import Position


class Chess:
    def __init__(self):
        self._board = Board()
        self._players = []            # LISTE de 2 joueurs (contrainte du sujet)
        self._currentPlayer = None

    @property
    def board(self):
        return self._board

    @property
    def players(self):
        return self._players

    @property
    def currentPlayer(self):
        return self._currentPlayer

    def initPlayers(self):
        nom1 = input("Nom joueur blanc (ou 'AI') : ").strip() or "Blanc"
        nom2 = input("Nom joueur noir (ou 'AI') : ").strip() or "Noir"
        j1 = AIPlayer(nom1, 0) if nom1 == "AI" else Player(nom1, 0)
        j2 = AIPlayer(nom2, 1) if nom2 == "AI" else Player(nom2, 1)
        self._players = [j1, j2]
        self._currentPlayer = j1      # Les blancs commencent

    def displayBoard(self):
        """Affiche l'echiquier en mode texte. Blancs en majuscule, noirs en minuscule."""
        print()
        for row in range(8, 0, -1):
            ligne = str(row) + "  "
            for col in "abcdefgh":
                p = self._board.getPiece(Position(col, row))
                if p is None:
                    ligne += ".  "
                elif p.color == 0:
                    ligne += str(p) + "  "
                else:
                    ligne += str(p).lower() + "  "
            print(ligne)
        print("   a  b  c  d  e  f  g  h\n")

    def _parse(self, move):
        """Analyse une chaine 'Pe2 Pe4' -> (from_pos, to_pos). Renvoie None si invalide."""
        try:
            depart, arrivee = move.split()
            # depart[0] = lettre piece, depart[1] = colonne, depart[2] = ligne
            from_pos = Position(depart[1], int(depart[2]))
            to_pos = Position(arrivee[1], int(arrivee[2]))
            return from_pos, to_pos
        except (ValueError, IndexError):
            return None

    def isValidMove(self, move):
        """Verifie qu'un coup est valide (analyse de la chaine + regles)."""
        parsed = self._parse(move)
        if parsed is None:
            return False
        from_pos, to_pos = parsed

        piece = self._board.getPiece(from_pos)
        # Il faut une piece, et elle doit appartenir au joueur courant
        if piece is None or piece.color != self._currentPlayer.color:
            return False

        # Interdit de capturer ses propres pieces
        cible = self._board.getPiece(to_pos)
        if cible is not None and cible.color == self._currentPlayer.color:
            return False

        # Polymorphisme : appel de la bonne version de isValidMove (cours 03a)
        return piece.isValidMove(to_pos, self._board)

    def updateBoard(self, move):
        """Applique le coup sur l'echiquier."""
        from_pos, to_pos = self._parse(move)
        self._board.move(from_pos, to_pos)

    def switchPlayer(self):
        """Bascule vers l'autre joueur."""
        i = self._players.index(self._currentPlayer)
        self._currentPlayer = self._players[1 - i]

    def isCheckMate(self):
        """Premiere version : retourne toujours False (cf cahier des charges)."""
        return False

    def play(self):
        """Deroulement complet de la partie (pseudo-code du cahier des charges)."""
        if not self._players:
            self.initPlayers()

        while not self.isCheckMate():
            self.displayBoard()
            move = self._currentPlayer.askMove()

            # Commandes speciales
            if move.upper() == "QUIT":
                print("Partie abandonnee.")
                return
            if move.upper() == "SAVE":
                from save_manager import save_game
                save_game(self, "partie.json")
                print(">> Partie sauvegardee dans partie.json")
                continue

            if self.isValidMove(move):
                self.updateBoard(move)
                self.switchPlayer()
            else:
                print(">> Coup invalide, reessayez.")
