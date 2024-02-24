# Jupyter-Puzzles
Ce dépôt contient des notebooks jupyter (fichiers de la forme `xxx.ipynb`), avec noyau python ou sage, ayant pour objet la résolution de puzzles, de problèmes logiques, etc.

## 1 Python

### Utilisation d'un noteboook jupyter `xxx.ipynb` avec un noyau [Python](https://www.python.org/)

- Si Python, avec [jupyter](https://jupyter.org/install), est installé sur votre machine, utiliser la commande `jupyter notebook` dans un répertoire qui contient `xxx.ipynb` ou ouvrir le fichier dans [VScode](https://code.visualstudio.com/) ;
- sinon, avec un compte Google, le plus simple est de téléverser les fichiers dans un sous répertoire de `Mon Drive/Colab Notebooks/` dans `Google Drive` et d'ouvrir `Mon Drive/Colab Notebooks/.../xxx.ipynb` dans un navigateur (partir de [Mon Drive](https://drive.google.com/drive/my-drive)). Noter que cela permet aussi de faire fonctionner Python sur un smartphone.  

### 1.1 Permutations ([`permutations.pynb`](./python/permutations/permutations.ipynb))

Génération de toutes les permutations d'un ensemble (fini) par un joli algorithme et application à des petites énigmes.

### 1.2 Parcours de graphe ([`parcours.ipynb`](./python/outils/parcours.ipynb)) 
Fournit trois fonctions python utilisées par d'autres notebooks
- `dfs` parcours en profondeur, utilisé par [`solitaire.ipynb`](./python/solitaire/solitaire.ipynb)
- `bfs` parcours en largeur
- `aStar` algorithme A*, utilisé par  [`sokoban.ipynb`](./python/sokoban/sokoban.ipynb) et [`8-puzzle.ipynb`](./python/8-puzzle/8-puzzle.ipynb)

### 1.3 [Solitaire](https://fr.wikipedia.org/wiki/Solitaire_(casse-t%C3%AAte)) ([`solitaire.ipynb`](./python/solitaire/solitaire.ipynb)) 

Utilisation du [parcours en profondeur](./python/outils/parcours.ipynb) d'un graphe pour la résolution de solitaires, par exemple [anglais](./python/solitaire/images/anglais.png), [français](./python/solitaire/images/francais.png) ou [allemand](./python/solitaire/images/allemand.png)

### 1.4 [Sokoban](https://fr.wikipedia.org/wiki/Sokoban) ([`sokoban.ipynb`](./python/sokoban/sokoban.ipynb) 

Utilisation de l'[Algorithme A*](./python/outils/parcours.ipynb) pour trouver une solution optimale (nombre minimum de déplacements) d'un sokoban de pas trop grande dimension, par exemple, le [microcosmos31](./python/sokoban/images/microcosmos31_0.png)

### 1.5 8-puzzle ([`8-puzzle.ipynb`](./python/8-puzzle/8-puzzle.ipynb))

Utilisation de l'[Algorithme A*](./python/outils/parcours.ipynb) pour trouver une solution optimale (nombre minimum de déplacements) d'une version simplifiée (8 pièces au lieu de 15) du [15-puzzle](https://fr.wikipedia.org/wiki/Taquin)

### 1.6 [Marche du cavalier](https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_cavalier) ([`cavalier.ipynb`](./python/cavalier/cavalier.ipynb))
Application de la notion de cycle hamiltonien d'un graphe à la [résolution du problème du cavalier](./python/cavalier/cavalier.png) cher à Euler.

### 1.7 [Automates](https://fr.wikipedia.org/wiki/Th%C3%A9orie_des_automates) ([`automates.ipynb`](./python/automates/automates.ipynb))
Applications de la théorie des automates à la résolution de quelques problèmes, comme [les 3 bouteilles](https://www.prise2tete.fr/forum/viewtopic.php?id=5151) ou [loup, chèvre et chou](https://fr.wikipedia.org/wiki/Le_loup,_la_ch%C3%A8vre_et_le_chou).

### 1.8 Deux problèmes de logique ([`logique.ipynb`](./python/logique/logique.ipynb))
choisis parmi les plus beaux (selon moi) problèmes du type "je sais, je sais pas" : le problème de Freudenthal et le problème de Axel Born, Kor Hurkens et Gerhard Woeginger, tous deux référencés [ici](https://interstices.info/jcms/c_33649/l-incroyable-probleme-de-freudenthal).

### 1.9 [Mastermind](https://fr.wikipedia.org/wiki/Mastermind) ([`mastermind.ipynb`](./python/mastermind/mastermind.ipynb))
Faire jouer à l'ordinateur le rôle du décodeur dans le jeu Mastermind. L'algorithme utilisé, dû à [Donald Knuth](https://fr.wikipedia.org/wiki/Donald_Knuth), est nommé *five-guess* car il permet de trouver le code caché en au plus cinq propositions (cinq motifs proposés).  
Un autre algorithme (D. L. Greenwell) est proposé pour le mastermind classique ($4$ positions et $6$ couleurs) qui consiste à proposer 6 motifs, toujours les mêmes, pour calculer le code.

### 1.10 [Rubik's Cube 2x2x2](https://fr.wikipedia.org/wiki/Pocket_Cube) ([`rubikcube2x2x2.ipynb`](./python/rubikcube/rubikcube2x2x2.ipynb))
Utilisation de la notion de parcours en largeur d'un graphe pour calculer efficacement une solution optimale d'un Rubik's Cube 2x2x2.

Pour être complet, le notebook comprend aussi une interface avec l'excellent [solveur](https://github.com/Wiston999/python-rubik) de Victor Cabezas qui calcule en un temps très raisonable une solution presque optimale d'un Rubik's Cube classique 3x3x3. Pour l'utiliser : `pip install rubik_solver`

### 1.11 [Snake Cube](https://fr.wikipedia.org/wiki/Cube_serpent) ([`snakecube.ipynb`](./python/snakecube/snakecube.ipynb)) 
Un [Cube-Serpent](./python/snakecube/cobra-bleu-dev.png) étant donné, calcul de ses [solutions](./python/snakecube/cobra-bleu.png).

## 2 Programmation par contraintes avec Python

### 2.1 Programmes élémentaires

TODO

### 2.2 Utilisation de cpmpy

TODO

### 2.3 Génération d'explications pour la résolution de problèmes de satisfaction de contraintes

TODO

## 3 Sage

### 3.1 Utilisation d'un noteboook jupyter `xxx.ipynb` avec un noyau [SageMath](https://www.sagemath.org/)

- Pour une utilisation basique, téléverser `xxx.ipynb` sur [ce site](https://dahn-research.eu/nbplayer/). 
- Sinon, 
    - si SageMath est installé sur votre machine, utiliser la commande `sage -n jupyter` dans un répertoire qui contient `xxx.ipynb`
    - ou vous pouvez ouvrir un compte [`sage.syzygy.ca`](https://sage.syzygy.ca/) ou [cocalc](https://cocalc.com/).

### 3.2 Rubik's Cube 3x3x3 ([`rubikcube.ipynb`](./sage/rubikcube/rubikcube.ipynb))
Interface avec les solveurs de Rubik's Cube fournis par Sage (si le package externe [`rubiks`](https://doc.sagemath.org/html/en/reference/spkg/rubiks.html) est installé [^1]) et [affichage graphique](./sage/rubikcube/exemple.png) des solutions.

### 3.3 [Rubik's Snake](https://fr.wikipedia.org/wiki/Rubik%27s_Snake) ([`rubiksnake.ipynb`](./sage/rubiksnake/rubiksnake.ipynb))
Etude d'un Rubik's Snake donné par son code, par exemple [000000220220220102202200](https://raw.githack.com/YvesLemaire/images/main/cat.html) et [aide à sa réalisation](./sage/rubiksnake/cat.png)

### 3.4 Algorithme X ([`algorithmeX.ipynb`](./sage/algorithmeX/algorithmeX.ipynb))
Applications de l'algorithme X à la résolution de [puzzles](./sage/algorithmeX/puzzle.png). L'algorithme est implémenté efficacement avec la méthode, incluse dans Sage, des [liens dansants](https://arxiv.org/pdf/cs/0011047.pdf) de [Donald Knuth](https://www-cs-faculty.stanford.edu/~knuth/). 

[^1]: `rubiks` est pré-installé sur  [`sage.syzygy.ca`](https://sage.syzygy.ca/) et [cocalc](https://cocalc.com/) mais pas sur [nbplayer](https://dahn-research.eu/nbplayer/)
