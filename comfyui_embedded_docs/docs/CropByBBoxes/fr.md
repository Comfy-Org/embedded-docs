> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CropByBBoxes/fr.md)

Le nœud CropByBBoxes extrait et redimensionne des régions rectangulaires spécifiques d'un lot d'images d'entrée. Il utilise les coordonnées de boîtes englobantes fournies pour définir la zone à recadrer dans chaque image. Les régions recadrées sont ensuite redimensionnées à une dimension de sortie spécifiée, avec des options pour étirer le recadrage ou le compléter pour préserver son ratio d'aspect original.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | Le lot d'images d'entrée à recadrer. |
| `bboxes` | BOUNDINGBOX | Oui | - | La liste des boîtes englobantes définissant les régions à recadrer. Cette entrée est forcée, ce qui signifie qu'elle doit être connectée. |
| `output_width` | INT | Non | 64 - 4096 | La largeur à laquelle chaque recadrage est redimensionné (par défaut : 512). |
| `output_height` | INT | Non | 64 - 4096 | La hauteur à laquelle chaque recadrage est redimensionné (par défaut : 512). |
| `padding` | INT | Non | 0 - 1024 | Marge supplémentaire en pixels ajoutée de chaque côté de la boîte englobante avant le recadrage (par défaut : 0). |
| `keep_aspect` | COMBO | Non | `"stretch"`<br>`"pad"` | Indique s'il faut étirer le recadrage pour l'adapter à la taille de sortie, ou le compléter avec des pixels noirs pour préserver son ratio d'aspect (par défaut : "stretch"). |

**Note :** Le nœud traite une image à la fois. Si plusieurs boîtes englobantes sont fournies pour une seule image, il calcule une seule région de recadrage qui est l'union (le plus petit rectangle contenant toutes les boîtes) de toutes les boîtes fournies. Si une région de recadrage calculée est invalide (par exemple, largeur ou hauteur nulle), le nœud créera un recadrage de secours à partir du centre-haut de l'image.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | Toutes les régions recadrées et redimensionnées, empilées en un seul lot d'images. |