Le nœud `ImageCrop` est conçu pour recadrer des images selon une largeur et une hauteur spécifiées, à partir de coordonnées x et y données. Cette fonctionnalité est essentielle pour se concentrer sur des zones spécifiques d'une image ou pour ajuster sa taille afin de répondre à certaines exigences.

## Entrées

| Champ | Description | Type de données |
| --- | --- | --- |
| `image` | L'image d'entrée à recadrer. Ce paramètre est crucial car il définit l'image source à partir de laquelle une région sera extraite en fonction des dimensions et coordonnées spécifiées. | `IMAGE` |
| `largeur` | Spécifie la largeur de l'image recadrée. Ce paramètre détermine la largeur de l'image résultante après recadrage. | `INT` |
| `hauteur` | Spécifie la hauteur de l'image recadrée. Ce paramètre détermine la hauteur de l'image résultante après recadrage. | `INT` |
| `x` | La coordonnée x du coin supérieur gauche de la zone de recadrage. Ce paramètre définit le point de départ pour la dimension de largeur du recadrage. | `INT` |
| `y` | La coordonnée y du coin supérieur gauche de la zone de recadrage. Ce paramètre définit le point de départ pour la dimension de hauteur du recadrage. | `INT` |

## Sorties

| Champ | Description | Type de données |
| --- | --- | --- |
| `image` | L'image recadrée résultant de l'opération de recadrage. Cette sortie est importante pour un traitement ou une analyse ultérieure de la région d'image spécifiée. | `IMAGE` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCrop/fr.md)
