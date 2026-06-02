
       def initPlayers(self):
        nom1 = input("Nom joueur blanc (ou 'AI') : ").strip() or "Blanc"
        nom2 = input("Nom joueur noir (ou 'AI') : ").strip() or "Noir"
        j1 = AIPlayer(nom1, 0) if nom1 == "AI" else Player(nom1, 0)
        j2 = AIPlayer(nom2, 1) if nom2 == "AI" else Player(nom2, 1)
        self._players = [j1, j2]
        self._currentPlayer = j1
        for j in self._players:
            if isinstance(j, AIPlayer):
                j._board = self._board
