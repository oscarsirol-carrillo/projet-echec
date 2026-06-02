# Programme principal (point d'entree du jeu)

import os
from chess import Chess
from save_manager import load_game


def main():
    print("=" * 30)
    print("    JEU D'ECHECS - ISEP")
    print("=" * 30)
    print("1. Nouvelle partie")
    print("2. Charger une partie sauvegardee")
    choix = input("Votre choix : ").strip()

    if choix == "2" and os.path.exists("partie.json"):
        chess = load_game("partie.json")
        print(">> Partie chargee.")
    else:
        chess = Chess()

    print("\nCommandes pendant la partie : 'SAVE' pour sauvegarder, 'QUIT' pour quitter.\n")
    chess.play()


if __name__ == "__main__":
    main()
