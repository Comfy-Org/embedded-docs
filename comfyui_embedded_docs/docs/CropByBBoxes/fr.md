Le nœud CropByBBoxes extrait et redimensionne des régions rectangulaires spécifiques à partir d’un lot d’images d’entrée. Il utilise les coordonnées des boîtes englobantes fournies pour définir la zone à recadrer dans chaque image. Les régions recadrées sont ensuite redimensionnées à une dimension de sortie spécifiée, avec la possibilité d’étirer le recadrage ou de le remplir de manière à préserver son rapport hauteur/largeur d’origine.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | Le lot d’images d’entrée à recadrer. | IMAGE | Oui | - |
| `bboxes` | La liste des boîtes englobantes définissant les régions à recadrer. Cette entrée est obligatoire, ce qui signifie qu’elle doit être connectée. | BOUNDINGBOX | Oui | - |
| `output_width` | La largeur à laquelle chaque recadrage est redimensionné (par défaut : 512). | INT | Non | 64 - 4096 |
| `output_height` | La hauteur à laquelle chaque recadrage est redimensionné (par défaut : 512). | INT | Non | 64 - 4096 |
| `padding` | Remplissage supplémentaire en pixels ajouté de chaque côté de la boîte englobante avant le recadrage (par défaut : 0). | INT | Non | 0 - 1024 |
| `keep_aspect` | Indique s’il faut étirer le recadrage pour l’adapter à la taille de sortie, ou le remplir de pixels noirs pour préserver son rapport hauteur/largeur (par défaut : "stretch"). | COMBO | Non | `"stretch"`<br>`"pad"` |

**Remarque :** Le nœud traite une image à la fois. Si plusieurs boîtes englobantes sont fournies pour une seule image, il calcule une seule région de recadrage qui est l’union (le plus petit rectangle contenant toutes les boîtes) de toutes les boîtes fournies. Si une région de recadrage calculée est invalide (par exemple, largeur ou hauteur nulle), le nœud crée un recadrage de repli à partir du centre-haut de l’image.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `image` | Toutes les régions recadrées et redimensionnées, regroupées en un seul lot d’images. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CropByBBoxes/fr.md)

---
**Source fingerprint (SHA-256):** `9c0b3078405567911731c42e1873c57c77363e21ef6805769730667c811b0a0b`
