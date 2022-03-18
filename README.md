## nyan_cat

### Présentation

Représentation du célèbre mème [Nyan Cat](https://fr.wikipedia.org/wiki/Nyan_Cat) en Python affichable sur calculatrice *NumWorks*.

Développé par Ilyas R. à l'occasation du DM21 **"💖 … Les mathématiques sont belles !"** édition 2021-2022. [#nsi_xyz](https://twitter.com/nsi_xyz)

### Fonctionnement

Les différents objets de l'image sont embriqués comme des pièces de puzzle afin d'obtenir un résultat similaire au mème d'origine.

Les différents objets sont dessinés par des fonctions :
```py
draw_star(x, y, variety)
draw_rainbow(x, y)
draw_cat_head(x, y)
draw_cat_body(x, y)
draw_cat_leg(x, y)
```
La fonction `draw_cat_head(x, y)` va par exemple créer la tête du chat. Les paramètres `x` et `y` permettent de positioner la tête du chat dans l'écran. Cela signifie les objets n'ont pas de positions fixes. Les positions sont personnalisables. Il est par conséquent possible d'animer un peu l'image.

Ce qui ressemble à des pixels dans la réalisation finale sont en réalité des carrés de 5 pixels sur 5 pixels.

### Ressources

Ressources utilisées :
- https://pypi.org/project/kandinsky/
- https://www.begeek.fr/wp-content/uploads/2021/02/Nyan-Cat.jpg
- https://imagecolorpicker.com/
