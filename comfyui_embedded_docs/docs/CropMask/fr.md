> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CropMask/fr.md)

Le nœud CropMask est conçu pour découper une zone spécifiée à partir d'un masque donné. Il permet aux utilisateurs de définir la région d'intérêt en précisant les coordonnées et les dimensions, extrayant ainsi une partie du masque pour un traitement ou une analyse ultérieure.

## Entrées

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `mask`    | MASK            | L'entrée du masque représente l'image du masque à découper. Elle est essentielle pour définir la zone à extraire en fonction des coordonnées et des dimensions spécifiées. |
| `x`       | INT             | La coordonnée x spécifie le point de départ sur l'axe horizontal à partir duquel le découpage doit commencer. |
| `y`       | INT             | La coordonnée y détermine le point de départ sur l'axe vertical pour l'opération de découpage. |
| `width`   | INT             | La largeur définit l'étendue horizontale de la zone de découpage à partir du point de départ. |
| `height`  | INT             | La hauteur spécifie l'étendue verticale de la zone de découpage à partir du point de départ. |

## Sorties

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `mask`    | MASK            | La sortie est un masque découpé, qui correspond à une partie du masque original définie par les coordonnées et les dimensions spécifiées. |