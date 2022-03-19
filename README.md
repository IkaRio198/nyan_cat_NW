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


### Ressources

Ressources utilisées :
- https://pypi.org/project/kandinsky/
- https://www.begeek.fr/wp-content/uploads/2021/02/Nyan-Cat.jpg
- https://imagecolorpicker.com/
