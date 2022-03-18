## nyan_cat

### Présentation

Représentation du célèbre mème [Nyan Cat](https://fr.wikipedia.org/wiki/Nyan_Cat) en Python affichable sur calculatrice *NumWorks*.

Développé par Ilyas R. à l'occasation du DM21 **"💖 … Les mathématiques sont belles !"** édition 2021-2022. [#nsi_xyz](https://twitter.com/nsi_xyz)

### Fonctionnement

Les différents objets de l'image sont embriqués comme des pièces de puzzle afin d'obtenir un résultat similaire au mème d'origine.

Les différents objets sont dessinés par des fonctions :
```py
drawStar(x, y, type)
drawRainbow(x, y)
drawCatHead(x, y)
drawCatBody(x, y)
drawCatLeg(x, y)
```
La fonction `drawCatHead(x, y)` va par exemple créer la tête du chat. Les paramètres `x` et `y` permettent de positioner la tête du chat dans l'écran. Cela signifie les objets n'ont pas de positions fixes. Les positions sont personnalisables. Il est par conséquent possible d'animer un peu l'image.

### Ressources

Ressources utilisées :
- https://pypi.org/project/kandinsky/
- https://www.begeek.fr/wp-content/uploads/2021/02/Nyan-Cat.jpg
- https://imagecolorpicker.com/
