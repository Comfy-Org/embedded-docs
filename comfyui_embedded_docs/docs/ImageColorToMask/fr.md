
Le nœud `ImageColorToMask` est conçu pour convertir une couleur spécifiée dans une image en un masque. Il traite une image et une couleur cible, générant un masque où la couleur spécifiée est mise en évidence, facilitant des opérations telles que la segmentation basée sur la couleur ou l'isolement d'objets.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | Le paramètre 'image' représente l'image d'entrée à traiter. Il est crucial pour déterminer les zones de l'image qui correspondent à la couleur spécifiée à convertir en masque. |
| `color`   | `INT`       | Le paramètre 'color' spécifie la couleur cible dans l'image à convertir en masque. Il joue un rôle clé dans l'identification des zones de couleur spécifiques à mettre en évidence dans le masque résultant. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `mask`    | `MASK`      | La sortie est un masque mettant en évidence les zones de l'image d'entrée qui correspondent à la couleur spécifiée. Ce masque peut être utilisé pour d'autres tâches de traitement d'image, telles que la segmentation ou l'isolement d'objets. |
