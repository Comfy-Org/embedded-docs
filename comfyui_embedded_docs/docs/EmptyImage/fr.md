Le nœud `EmptyImage` est conçu pour générer des images vides de dimensions et de couleur spécifiées. Il permet la création d'images de couleur uniforme pouvant servir de fonds ou de réserves dans diverses tâches de traitement d'image.

## Entrées

| Paramètre   | Data Type | Description |
|-------------|-------------|-------------|
| `width`     | `INT`       | Spécifie la largeur de l'image générée. Cela détermine la largeur de l'image. |
| `height`    | `INT`       | Détermine la hauteur de l'image générée. Cela affecte la taille verticale de l'image. |
| `batch_size`| `INT`       | Indique le nombre d'images à générer en un seul lot. Cela permet la création de plusieurs images à la fois. |
| `color`     | `INT`       | Définit la couleur de l'image générée en utilisant une valeur hexadécimale, permettant la personnalisation de l'apparence de l'image. Ce paramètre permet la sélection d'une large gamme de couleurs. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | La sortie est un tenseur représentant l'image ou les images générées, avec les dimensions et la couleur spécifiées. |
