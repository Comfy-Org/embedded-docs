> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImageMaskNode/fr.md)

Le nœud Redimensionner Image/Masque propose plusieurs méthodes pour modifier les dimensions d'une image ou d'un masque en entrée. Il peut mettre à l'échelle par un multiplicateur, définir des dimensions spécifiques, correspondre à la taille d'une autre entrée, ou ajuster en fonction du nombre de pixels, en utilisant diverses méthodes d'interpolation pour la qualité.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `input` | IMAGE ou MASK | Oui | N/A | L'image ou le masque à redimensionner. |
| `resize_type` | COMBO | Oui | `SCALE_BY`<br>`SCALE_DIMENSIONS`<br>`SCALE_LONGER_DIMENSION`<br>`SCALE_SHORTER_DIMENSION`<br>`SCALE_WIDTH`<br>`SCALE_HEIGHT`<br>`SCALE_TOTAL_PIXELS`<br>`MATCH_SIZE` | La méthode utilisée pour déterminer la nouvelle taille. Les paramètres requis changent en fonction du type sélectionné. |
| `multiplier` | FLOAT | Non | 0.01 à 8.0 | Le facteur d'échelle. Requis lorsque `resize_type` est `SCALE_BY` (par défaut : 1.00). |
| `width` | INT | Non | 0 à 8192 | La largeur cible en pixels. Requis lorsque `resize_type` est `SCALE_DIMENSIONS` ou `SCALE_WIDTH` (par défaut : 512). |
| `height` | INT | Non | 0 à 8192 | La hauteur cible en pixels. Requis lorsque `resize_type` est `SCALE_DIMENSIONS` ou `SCALE_HEIGHT` (par défaut : 512). |
| `crop` | COMBO | Non | `"disabled"`<br>`"center"` | La méthode de recadrage à appliquer lorsque les dimensions ne correspondent pas au rapport d'aspect. Disponible uniquement lorsque `resize_type` est `SCALE_DIMENSIONS` ou `MATCH_SIZE` (par défaut : "center"). |
| `longer_size` | INT | Non | 0 à 8192 | La taille cible pour le côté le plus long de l'image. Requis lorsque `resize_type` est `SCALE_LONGER_DIMENSION` (par défaut : 512). |
| `shorter_size` | INT | Non | 0 à 8192 | La taille cible pour le côté le plus court de l'image. Requis lorsque `resize_type` est `SCALE_SHORTER_DIMENSION` (par défaut : 512). |
| `megapixels` | FLOAT | Non | 0.01 à 16.0 | Le nombre total cible de mégapixels. Requis lorsque `resize_type` est `SCALE_TOTAL_PIXELS` (par défaut : 1.0). |
| `match` | IMAGE ou MASK | Non | N/A | Une image ou un masque dont les dimensions serviront de référence pour redimensionner l'entrée. Requis lorsque `resize_type` est `MATCH_SIZE`. |
| `scale_method` | COMBO | Oui | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"lanczos"` | L'algorithme d'interpolation utilisé pour la mise à l'échelle (par défaut : "area"). |

**Note :** Le paramètre `crop` n'est disponible et pertinent que lorsque `resize_type` est défini sur `SCALE_DIMENSIONS` ou `MATCH_SIZE`. Lors de l'utilisation de `SCALE_WIDTH` ou `SCALE_HEIGHT`, l'autre dimension est automatiquement mise à l'échelle pour conserver le rapport d'aspect original.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `resized` | IMAGE ou MASK | L'image ou le masque redimensionné, correspondant au type de données de l'entrée. |
