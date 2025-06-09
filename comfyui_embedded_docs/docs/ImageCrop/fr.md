Le nœud `ImageCrop` est conçu pour recadrer les images à une largeur et une hauteur spécifiées à partir d'une coordonnée x et y donnée. Cette fonctionnalité est essentielle pour se concentrer sur des régions spécifiques d'une image ou pour ajuster la taille de l'image afin de répondre à certaines exigences.

## Entrées

| Champ | Data Type | Description                                                                                   |
|-------|-------------|-----------------------------------------------------------------------------------------------|
| `image` | `IMAGE` | L'image d'entrée à recadrer. Ce paramètre est crucial car il définit l'image source à partir de laquelle une région sera extraite en fonction des dimensions et des coordonnées spécifiées. |
| `width` | `INT` | Spécifie la largeur de l'image recadrée. Ce paramètre détermine la largeur de l'image recadrée résultante. |
| `height` | `INT` | Spécifie la hauteur de l'image recadrée. Ce paramètre détermine la hauteur de l'image recadrée résultante. |
| `x` | `INT` | La coordonnée x du coin supérieur gauche de la zone de recadrage. Ce paramètre définit le point de départ pour la dimension de largeur du recadrage. |
| `y` | `INT` | La coordonnée y du coin supérieur gauche de la zone de recadrage. Ce paramètre définit le point de départ pour la dimension de hauteur du recadrage. |

## Sorties

| Champ | Data Type | Description                                                                   |
|-------|-------------|-------------------------------------------------------------------------------|
| `image` | `IMAGE` | L'image recadrée résultant de l'opération de recadrage. Cette sortie est significative pour un traitement ou une analyse ultérieure de la région d'image spécifiée. |
