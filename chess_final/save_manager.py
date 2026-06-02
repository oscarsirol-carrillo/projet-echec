# Sauvegarde et restauration de la partie dans un fichier JSON
# (contrainte du sujet : pouvoir sauvegarder et restaurer la partie)

import json
from position import Position
from piece import King, Queen, Bishop, Knight, Rook, Pawn
from player import Player, AIPlayer

# Dictionnaire qui associe la lettre d'une piece a sa classe.
# Sert pour reconstruire les bons objets depuis un fichier sauvegarde.
LETTRE_VERS_CLASSE = {
    "K": King, "Q": Queen, "B": Bishop,
    "N": Knight, "R": Rook, "P": Pawn,
}


def save_game(chess, filename):
    """Enregistre l'etat de la partie dans un fichier JSON."""
    data = {
        "players": [
            [p.name, p.color, isinstance(p, AIPlayer)]
            for p in chess.players
        ],
        "current": chess.players.index(chess.currentPlayer),
        "pieces": [
            [str(piece), piece.color, str(pos)]
            for pos, piece in chess.board.pieces.items()
        ],
    }
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)


def load_game(filename):
    """Charge une partie depuis un fichier JSON et reconstruit l'objet Chess."""
    from chess import Chess
    with open(filename, "r") as f:
        data = json.load(f)

    chess = Chess()

    # Reconstruction des joueurs
    chess._players = []
    for nom, color, is_ai in data["players"]:
        joueur = AIPlayer(nom, color) if is_ai else Player(nom, color)
        chess._players.append(joueur)
    chess._currentPlayer = chess._players[data["current"]]

    # Reconstruction du plateau (on vide d'abord)
    chess._board._pieces = {}
    for lettre, color, pos_str in data["pieces"]:
        pos = Position(pos_str[0], int(pos_str[1]))
        chess._board._pieces[pos] = LETTRE_VERS_CLASSE[lettre](pos, color)

    return chess
