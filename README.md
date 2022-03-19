## nyan_cat

### Présentation

Représentation du célèbre mème [Nyan Cat](https://fr.wikipedia.org/wiki/Nyan_Cat) en Python pour calculatrice *NumWorks*.

Développé par Ilyas R. à l'occasion du DM21 **"💖 … Les mathématiques sont belles !"** édition 2021-2022. [#nsi_xyz](https://twitter.com/nsi_xyz)

### Lancement

Il suffit d'importer le programme sur sa calculatrice depuis la [page du script](https://my.numworks.com/python/ikario198/dm21), l'exécuter, et laisser la magie opérer ! (bon en vrai c'est instantané)
Voici le rendu final :

![Nyan Cat](https://user-images.githubusercontent.com/58112248/159076183-714c2f6c-8875-4953-8897-c13195255c60.png)


### Fonctionnement

Les différents objets de l'image sont embriqués comme des pièces de puzzle afin d'obtenir un résultat similaire au mème d'origine.

Les différents objets sont dessinés par des fonctions :
```py
draw_star(x, y, variety)
draw_rainbow(x, y)
draw_cat_head(x, y)
draw_cat_body(x, y)
draw_cat_leg(x, y, variety)
```
La fonction `draw_cat_head(x, y)` va par exemple créer la tête du chat. Les paramètres `x` et `y` permettent de positioner la tête du chat dans l'écran. Cela signifie les objets n'ont pas de positions fixes. Les positions sont personnalisables. Il est par conséquent possible d'animer un peu l'image.

Ce qui ressemble à des pixels dans la réalisation finale sont en réalité des carrés de 5 pixels sur 5 pixels.

Les objets peuvent être dessinés de trois façons différentes, selon leur taille.

L'objet `star` par exemple, la position des carrés de 5\*5 (donc des "gros pixels") va être déterminé grâce à des listes :
```py
# En l'occurrence, ces listes sont pour positionner une étoile de variety "small"
        x_diff_s = [0, 0, 5, -5]
        y_diff_s = [5, -5, 0, 0]
```
Le nombre d'éléments dans la liste détermine le nombre de pixels à positionner ! D'ailleurs, pourquoi tous nombres sont des multiples de `5` ? Et bien, si vous avez bien suivis, les gros pixels affichés à l'écran sont encore une fois des carrés de `5`\*`5` !

Voici l'étoile qui sera dessiné avec la fonction `draw_star(x, y, "small")` (uniquement les carrés blancs, le fond bleu n'est pas généré par la fonction) :

![159114385-70254e92-3b97-4026-ba51-a6913d5dc88f](https://user-images.githubusercontent.com/58112248/159115090-296bcc16-79ed-4ce4-8fbb-0895d5059c64.png)

Les paramètres `x`, et `y` correspondent au centre de l'étoile. Étant donné qu'il n'y aucun carré de l'étoile au centre de celle-ci. Aucun carré ne sera dessiné en dans les coordonnées `x`, `y`. En revanche, le premier carré désinné sera positionné en (`x + 0` ; `y + 5`), le deuxième en (`x + 0` ; `y + -5`), le troisième en (`x + 5` ; `y + 0`), et le dernier en en (`x + -5` ; `y + 0`) ! Si vous n'avez pas compris pour ce sont ces valeurs qui sont additionnées ou soustraites, je vous renvoie aux listes `x_diff_s`, et `y_diff_s` ci-dessus. 😉

> ⚠️ Note : Les coordonnées du centre de l'écran ne sont pas `(0 ; 0)`. Le `(0 ; 0)` est positionné tout en haut à gauche de l'écran ! Si on va en bas le `y` augmente, si va à droite, le `x` augmente.


L'objet `rainbow` lui, va quoiqu'il arrive aller de gauche à droite, donc le `x` a juste à être multiplié par un nombre `k*5`, `k` qui sera égal à `0` à la première boucle, puis incrémenter à chaque boucle (on peut comparer le `k` au `i`, seulement, `k` est utilisé car `i` est déjà utilisé). Il est donc inutile de créer une liste avec la liste des positions des `x`.

Il possède donc qu'une liste qui elle, indique la position des `y`.

```py
    rainbow_colors = [colors[2], colors[3], colors[4], colors[5], colors[6], colors[7]]
    y_template = [0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5]
    for i in range(len(rainbow_colors)):
        for j in range(3):
            for k in range(len(y_template)):
                fill_rect(x + k * 5, y + y_template[k] + j * 5 + i * 5 * 3, 5, 5, rainbow_colors[i])
```

Le dernier "type" d'objet, le plus complexe, est un objet de grande taille, et n'ayant pas de pattern régulier. Comme par exemple, la tête du chat.

Dans ce cas, l'objet sera dessiné de gauche à droite et de haut en bas pour chaque couleur de l'objet. Les paramètres de la fonction `draw_cat_head(x, y)` indiquent donc la position tout en haut à gauche de la tête, et non le centre.

Le `0` affiché tout en haut à gauche correspond aux paramètres `(x, y)`

![cat](https://user-images.githubusercontent.com/58112248/159115878-935775e0-da47-494e-b685-6f302362a066.png)


Prenons l'exemple de la couleur noire. Les carrés noirs de la tête seront dessinés ligne par ligne. Quand une ligne est terminée, on incrémente `y`. Mais comment savoir si une ligne est terminée ? Et bien, analysons la liste de la couleure noire :

```py
    x_head_black = [10, 15, 60, 65, 5, 20, 55, 70, 5, 25, 50, 70, 5, 30, 35, 40, 45, 70, 5, 70, 0, 75, 0, 25, 60, 75, 0,
                    20, 25, 45, 55, 60, 75, 0, 75, 0, 25, 40, 55, 75, 5, 25, 30, 35, 40, 45, 50, 55, 70, 10, 65, 15, 20,
                    25, 30, 35, 40, 45, 50, 55, 60]
```

Combien y a t-il de carrés de `5*5` dans la première ligne ? Il y en a 4. Prenons les 4 premiers éléments de la liste `x_head_black`, soit `10`, `15`, `60`, `65`, en regardant l'image de la tête du chat ci-dessus, il ne faut pas être un génie pour comprendre à quoi ces nombres correspondent, ce sont grosso modo, la position `x` de chaque carré noir. Maintenant, regardons le 5ème élément de la liste, `5`, il correspond au premier carré noir de la deuxième ligne. Comment l'algorythme a détecté qu'on voulait un saut de ligne ? Il a comparé `65` (position `3` dans la liste), et `5` (position `3 + 1` dans la liste), et si 65 est inférieur à 5, on saute une ligne. 🙂

Donc si `x_head_black[i] > x_head_black[i + 1]`, on incrémente `y`. 😄


### Ressources

Ressources utilisées :
- https://pypi.org/project/kandinsky/
- https://www.begeek.fr/wp-content/uploads/2021/02/Nyan-Cat.jpg
- https://imagecolorpicker.com/
