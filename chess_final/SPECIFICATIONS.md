# Document de Specifications - Projet Jeu d'Echecs

**Equipe :** [a completer avec les noms des 4 membres]
**Module :** Informatique I1 - 2025/2026

---

## 1. Schema des classes (Diagramme UML)

```
                    +-------------------+
                    |   Piece (ABC)     |
                    +-------------------+
                    | - _position       |
                    | - _color          |
                    +-------------------+
                    | + isValidMove()   |  (abstraite)
                    | + __str__()       |  (abstraite)
                    | + _path_libre()   |  (concrete)
                    +---------+---------+
                              |
        +---------+-----------+-----------+---------+---------+
        |         |           |           |         |         |
     +-----+   +------+   +-------+   +-------+  +-----+   +-----+
     |King |   |Queen |   |Bishop |   |Knight |  |Rook |   |Pawn |
     +-----+   +------+   +-------+   +-------+  +-----+   +-----+


  +---------------+         +-------------------+
  |   Position    |         |      Board        |
  +---------------+         +-------------------+
  | - _column     |         | - _pieces (dict)  |
  | - _row        |         +-------------------+
  +---------------+         | + getPiece()      |
  | + __str__()   |         | + getPosition()   |
  | + __eq__()    |         | + move()          |
  | + __hash__()  |         +-------------------+
  +---------------+

  +---------------+                  +-------------------+
  |    Player     |                  |      Chess        |
  +---------------+                  +-------------------+
  | - _name       | <-- AIPlayer     | - _board          |
  | - _color      |                  | - _players (list) |
  +---------------+                  | - _currentPlayer  |
  | + askMove()   |                  +-------------------+
  +---------------+                  | + initPlayers()   |
                                     | + displayBoard()  |
                                     | + isValidMove()   |
                                     | + updateBoard()   |
                                     | + switchPlayer()  |
                                     | + isCheckMate()   |
                                     | + play()          |
                                     +-------------------+
```

**Relations :**
- `Piece` est abstraite (utilise `ABC` du module `abc`) - cours 04a
- `King`, `Queen`, `Bishop`, `Knight`, `Rook`, `Pawn` heritent de `Piece` et
  redefinissent `isValidMove()` et `__str__()` (polymorphisme, cours 03a)
- `AIPlayer` herite de `Player` et redefinit `askMove()` (cours 03a)
- `Chess` compose un `Board` et une liste de `Player`
- `Board` stocke les pieces dans un dictionnaire `{Position: Piece}`

## 2. Organisation de l'equipe

L'equipe est composee de 4 membres. La repartition s'est organisee comme suit :

- **Phase commune (seance 1-2)** : analyse du sujet et redaction des
  specifications par toute l'equipe.
- **Phase de developpement (seances 3-5)** : repartition des classes :
  - Membre 1 : `Position` + classe abstraite `Piece` + pion
  - Membre 2 : Tour + Fou (avec verification du chemin libre)
  - Membre 3 : Cavalier + Roi + Reine
  - Membre 4 : `Player`, `AIPlayer`, et systeme de sauvegarde JSON
- **Phase d'integration (seance 4-6)** : un membre assure la coherence des
  imports et l'integration dans `Chess`.

**Outils utilises :**
- GitHub pour le partage du code (branches par membre, merges via Pull Requests)
- Messagerie de groupe pour les questions rapides
- Reunions courtes en debut de chaque seance pour faire le point sur les blocages

**Pas de chef de projet fige** : un role tournant a chaque seance pour verifier
l'avancement et identifier les blocages.

## 3. Ameliorations envisagees

Idees identifiees pour gagner des points dans la partie "ameliorations" :
- Interface texte amelioree avec couleurs ANSI pour distinguer blancs/noirs
- Detection d'echec et mat reelle (au-dela du `return False`)
- Sauvegarde sous forme d'historique des coups (rejouable)
- IA un peu plus intelligente : prioriser les captures plutot que coups aleatoires
- Eventuellement : interface graphique avec `tkinter` si le temps le permet
