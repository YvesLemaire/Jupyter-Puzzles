# Jupyter-Puzzles
Ce dépôt contient des notebooks jupyter, avec noyau python ou sage, ayant pour objet la résolution de puzzles, de problèmes logiques, etc.

## Python

## Sage

### Utilisation d'un noteboook jupyter avec un noyau [SageMath](https://www.sagemath.org/)

Télécharger le notebook  `xxx.ipynb`.
- Pour une utilisation basique du programme, téléverser `xxx.ipynb` sur [ce site](https://dahn-research.eu/nbplayer/). 
- Sinon, 
    - si SageMath est installé sur votre machine, utiliser la commande `sage -n jupyter` dans un répertoire qui contient `xxx.ipynb`
    - ou vous pouvez ouvrir un compte sur [`sage.syzygy.ca`](https://sage.syzygy.ca/) ;
    - ou utiliser [cocalc](https://cocalc.com/).

### Rubik's Cube 3x3x3 ([`rubikcube.ipynb`](./sage/rubikcube/rubikcube.ipynb))
Interface avec les solveurs de Rubik's Cube fournis par Sage (si le package externe [`rubiks`](https://doc.sagemath.org/html/en/reference/spkg/rubiks.html) est installé) et [affichage graphique](./sage/rubikcube/exemple.png) des solutions.

### [Rubik's Snake](https://fr.wikipedia.org/wiki/Rubik%27s_Snake) ([`rubiksnake.ipynb`](./sage/rubiksnake/rubiksnake.ipynb))
Etude d'un Rubik's Snake donné par son code, par exemple [000000220220220102202200](https://raw.githack.com/YvesLemaire/images/main/cat.html) et [aide à sa réalisation](./sage/rubiksnake/cat.png)

### Algorithme X ([`algorithmeX.ipynb`](./sage/algorithmeX/algorithmeX.ipynb))
Applications de l'algorithme X à la résolution de [puzzles](./sage/algorithmeX/puzzle.png). L'algorithme est implémenté efficacement avec la méthode, incluse dans Sage, des [liens dansants](https://arxiv.org/pdf/cs/0011047.pdf) de [Donald Knuth](https://www-cs-faculty.stanford.edu/~knuth/). 
