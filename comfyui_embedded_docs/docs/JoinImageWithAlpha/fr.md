
Ce nœud est conçu pour les opérations de composition, spécifiquement pour fusionner une image avec son masque alpha correspondant afin de produire une image de sortie unique. Il combine efficacement le contenu visuel avec les informations de transparence, permettant la création d'images où certaines zones sont transparentes ou semi-transparentes.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | Le contenu visuel principal à combiner avec un masque alpha. Il représente l'image sans informations de transparence. |
| `alpha`   | `MASK`      | Le masque alpha qui définit la transparence de l'image correspondante. Il est utilisé pour déterminer quelles parties de l'image doivent être transparentes ou semi-transparentes. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | La sortie est une image unique qui combine l'image d'entrée avec le masque alpha, incorporant les informations de transparence dans le contenu visuel. |
