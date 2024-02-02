# Jupyter-Puzzles
Ce dépôt contient des notebooks jupyter (fichiers de la forme `xxx.ipynb`), avec noyau python ou sage, ayant pour objet la résolution de puzzles, de problèmes logiques, etc.

## Python

### Utilisation d'un noteboook jupyter `xxx.ipynb` avec un noyau [Python](https://www.python.org/)

Télécharger le notebook  `xxx.ipynb` et, éventuellement les autres fichiers du même répertoire.
- Si Python, avec [jupyter](https://jupyter.org/install), est installé sur votre machine, utiliser la commande `jupyter notebook` dans un répertoire qui contient `xxx.ipynb` ou ouvrir le fichier dans [VScode](https://code.visualstudio.com/) ;
- sinon, avec un compte Google, le plus simple est de téléverser les fichiers dans un sous répertoire de `Mon Drive/Colab Notebooks/` dans `Google Drive` et d'ouvrir `Mon Drive/Colab Notebooks/.../xxx.ipynb` dans un navigateur (partir de [Mon Drive](https://drive.google.com/drive/my-drive)). Noter que cela permet aussi de faire fonctionner Python sur un smartphone.  

### [Marche du cavalier](https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_cavalier) ([`cavalier.ipynb`](./python/cavalier/cavalier.ipynb))
Application de la notion de cycle hamiltonien d'un graphe à la [résolution du problème du cavalier](./python/cavalier/cavalier.png) cher à Euler.

### [Automates](https://fr.wikipedia.org/wiki/Th%C3%A9orie_des_automates) ([`automates.ipynb`](./python/automates/automates.ipynb))
Applications de la théorie des automates à la résolution de quelques problèmes, comme [les 3 bouteilles](https://www.prise2tete.fr/forum/viewtopic.php?id=5151) ou [loup, chèvre et chou](https://fr.wikipedia.org/wiki/Le_loup,_la_ch%C3%A8vre_et_le_chou).

### Deux problèmes de logique ([`logique.ipynb`](./python/logique/logique.ipynb))
choisis parmi les plus beaux (selon moi) problèmes du type "je sais, je sais pas" : le problème de Freudenthal et le problème de Axel Born, Kor Hurkens et Gerhard Woeginger, tous deux référencés [ici](https://interstices.info/jcms/c_33649/l-incroyable-probleme-de-freudenthal).

### [Rubik's Cube 2x2x2](https://fr.wikipedia.org/wiki/Pocket_Cube) ([`rubikcube2x2x2.ipynb`](./python/rubikcube/rubikcube2x2x2.ipynb))
Utilisation de la notion de parcours en largeur d'un graphe pour calculer efficacement une solution optimale d'un Rubik's Cube 2x2x2.

Pour être complet, le notebook comprend aussi une interface avec l'excellent [solveur](https://github.com/Wiston999/python-rubik) de Victor Cabezas qui calcule en un temps très raisonable une solution presque optimale d'un Rubik's Cube classique 3x3x3. Pour l'utiliser : `pip install rubik_solver`

### [Snake Cube](https://fr.wikipedia.org/wiki/Cube_serpent) ([`snakecube.ipynb`](./python/snakecube/snakecube.ipynb)) 
Un [Cube-Serpent](./python/snakecube/cobra-bleu-dev.png) étant donné, calcul de ses [solutions](./python/snakecube/cobra-bleu.png).

## Sage

### Utilisation d'un noteboook jupyter avec un noyau [SageMath](https://www.sagemath.org/)

Télécharger le notebook  `xxx.ipynb`.
- Pour une utilisation basique du programme, téléverser `xxx.ipynb` sur [ce site](https://dahn-research.eu/nbplayer/). 
- Sinon, 
    - si SageMath est installé sur votre machine, utiliser la commande `sage -n jupyter` dans un répertoire qui contient `xxx.ipynb`
    - ou vous pouvez ouvrir un compte sur [`sage.syzygy.ca`](https://sage.syzygy.ca/) ou sur [cocalc](https://cocalc.com/).

### Rubik's Cube 3x3x3 ([`rubikcube.ipynb`](./sage/rubikcube/rubikcube.ipynb))
Interface avec les solveurs de Rubik's Cube fournis par Sage (si le package externe [`rubiks`](https://doc.sagemath.org/html/en/reference/spkg/rubiks.html) est installé [^1]) et [affichage graphique](./sage/rubikcube/exemple.png) des solutions.

### [Rubik's Snake](https://fr.wikipedia.org/wiki/Rubik%27s_Snake) ([`rubiksnake.ipynb`](./sage/rubiksnake/rubiksnake.ipynb))
Etude d'un Rubik's Snake donné par son code, par exemple [000000220220220102202200](https://raw.githack.com/YvesLemaire/images/main/cat.html) et [aide à sa réalisation](./sage/rubiksnake/cat.png)

### Algorithme X ([`algorithmeX.ipynb`](./sage/algorithmeX/algorithmeX.ipynb))
Applications de l'algorithme X à la résolution de [puzzles](./sage/algorithmeX/puzzle.png). L'algorithme est implémenté efficacement avec la méthode, incluse dans Sage, des [liens dansants](https://arxiv.org/pdf/cs/0011047.pdf) de [Donald Knuth](https://www-cs-faculty.stanford.edu/~knuth/). 

[^1]: `rubiks` est pré-installé sur  [`sage.syzygy.ca`](https://sage.syzygy.ca/) et [cocalc](https://cocalc.com/) mais pas sur [nbplayer](https://dahn-research.eu/nbplayer/)
