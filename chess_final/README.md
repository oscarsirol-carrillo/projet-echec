# Jeu d'echecs - Projet I1 (2025/2026)

Implementation d'un jeu d'echecs en Python suivant une approche orientee objet,
realisee dans le cadre du module d'informatique I1 a l'ISEP.

## Lancer le jeu

```bash
python main.py
```

A l'invite, choisir `1` pour une nouvelle partie ou `2` pour charger une partie
sauvegardee. Pour faire jouer une IA, taper `AI` comme nom de joueur.

## Format des coups

Lettre de la piece + colonne + ligne, puis espace, puis la destination.
- `Pe2 Pe4` : avance le pion blanc de e2 a e4
- `Nb1 Nc3` : deplace le cavalier blanc de b1 a c3

Lettres des pieces : K (Roi), Q (Reine), B (Fou), N (Cavalier), R (Tour), P (Pion).

Commandes speciales pendant la partie :
- `SAVE` : sauvegarde la partie dans `partie.json`
- `QUIT` : quitte la partie

## Structure du projet

| Fichier              | Role                                                      |
|----------------------|-----------------------------------------------------------|
| `position.py`        | Classe `Position` (case de l'echiquier)                   |
| `piece.py`           | Classe abstraite `Piece` + 6 sous-classes                 |
| `board.py`           | Classe `Board` (echiquier 8x8, dictionnaire de pieces)    |
| `player.py`          | Classes `Player` et `AIPlayer`                            |
| `chess.py`           | Classe `Chess` (gestion de la partie)                     |
| `save_manager.py`    | Sauvegarde / chargement JSON                              |
| `main.py`            | Point d'entree du programme                               |
| `tests/`             | Tests unitaires (framework `unittest`)                    |

## Lancer les tests

```bash
python -m unittest discover -s tests -v
```

## Concepts POO utilises (cours)

- **Classes et objets** (cours 01b) : toutes les entites du jeu
- **Encapsulation** (cours 02a) : `_attribut` + `@property` / `@<attribut>.setter`
- **Heritage et polymorphisme** (cours 03a) : `Piece` -> 6 sous-classes,
  redefinition de `isValidMove`, `AIPlayer` herite de `Player`
- **Classes abstraites** (cours 04a) : `Piece(ABC)` avec `@abstractmethod`
- **Tests unitaires** : framework `unittest` (cours dedie)

## Contraintes du cahier des charges respectees

- [x] Au moins une **liste** : `Chess._players`
- [x] Au moins un **dictionnaire** : `Board._pieces` (cle = Position, valeur = Piece)
- [x] **Sauvegarde / restauration** dans un fichier (`partie.json`)
- [x] **Tests unitaires** pour chaque classe principale
- [x] Code partage sur **GitHub**
