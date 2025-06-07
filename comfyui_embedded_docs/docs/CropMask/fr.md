Le nœud CropMask est conçu pour recadrer une zone spécifiée à partir d'un masque donné. Il permet aux utilisateurs de définir la région d'intérêt en spécifiant des coordonnées et des dimensions, extrayant ainsi efficacement une partie du masque pour un traitement ou une analyse ultérieure.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `mask`    | MASK        | L'entrée du masque représente l'image du masque à recadrer. Elle est essentielle pour définir la zone à extraire en fonction des coordonnées et des dimensions spécifiées. |
| `x`       | INT         | La coordonnée x spécifie le point de départ sur l'axe horizontal à partir duquel le recadrage doit commencer. |
| `y`       | INT         | La coordonnée y détermine le point de départ sur l'axe vertical pour l'opération de recadrage. |
| `width`   | INT         | La largeur définit l'étendue horizontale de la zone de recadrage à partir du point de départ. |
| `height`  | INT         | La hauteur spécifie l'étendue verticale de la zone de recadrage à partir du point de départ. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `mask`    | MASK        | La sortie est un masque recadré, qui est une portion du masque original définie par les coordonnées et dimensions spécifiées. |
