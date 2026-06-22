# Redimensionner image/masque

Ce document a été généré par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImageMaskNode/en.md)

Le nœud Redimensionner Image/Masque propose plusieurs méthodes pour modifier les dimensions d'une image ou d'un masque d'entrée. Il peut effectuer une mise à l'échelle par multiplicateur, définir des dimensions spécifiques, adapter la taille d'une autre entrée, ou ajuster en fonction du nombre de pixels, en utilisant diverses méthodes d'interpolation pour la qualité.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `input` | L'image ou le masque à redimensionner. | IMAGE ou MASK | Oui | N/A |
| `resize_type` | La méthode utilisée pour déterminer la nouvelle taille. Les paramètres requis changent en fonction du type sélectionné. | COMBO | Oui | `SCALE_BY`<br>`SCALE_DIMENSIONS`<br>`SCALE_LONGER_DIMENSION`<br>`SCALE_SHORTER_DIMENSION`<br>`SCALE_WIDTH`<br>`SCALE_HEIGHT`<br>`SCALE_TOTAL_PIXELS`<br>`MATCH_SIZE` |
| `multiplier` | Le facteur d'échelle. Requis lorsque `resize_type` est `SCALE_BY` (par défaut : 1,00). | FLOAT | Non | 0,01 à 8,0 |
| `width` | La largeur cible en pixels. Requis lorsque `resize_type` est `SCALE_DIMENSIONS` ou `SCALE_WIDTH` (par défaut : 512). | INT | Non | 0 à 8192 |
| `height` | La hauteur cible en pixels. Requis lorsque `resize_type` est `SCALE_DIMENSIONS` ou `SCALE_HEIGHT` (par défaut : 512). | INT | Non | 0 à 8192 |
| `crop` | La méthode de recadrage à appliquer lorsque les dimensions ne correspondent pas au rapport hauteur/largeur. Disponible uniquement lorsque `resize_type` est `SCALE_DIMENSIONS` ou `MATCH_SIZE` (par défaut : "center"). | COMBO | Non | `"disabled"`<br>`"center"` |
| `longer_size` | La taille cible pour le côté le plus long de l'image. Requis lorsque `resize_type` est `SCALE_LONGER_DIMENSION` (par défaut : 512). | INT | Non | 0 à 8192 |
| `shorter_size` | La taille cible pour le côté le plus court de l'image. Requis lorsque `resize_type` est `SCALE_SHORTER_DIMENSION` (par défaut : 512). | INT | Non | 0 à 8192 |
| `megapixels` | Le nombre total cible de mégapixels. Requis lorsque `resize_type` est `SCALE_TOTAL_PIXELS` (par défaut : 1,0). | FLOAT | Non | 0,01 à 16,0 |
| `match` | Une image ou un masque dont les dimensions seront utilisées pour redimensionner l'entrée. Requis lorsque `resize_type` est `MATCH_SIZE`. | IMAGE ou MASK | Non | N/A |
| `scale_method` | L'algorithme d'interpolation utilisé pour la mise à l'échelle (par défaut : "area"). | COMBO | Oui | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"lanczos"` |

**Remarque :** Le paramètre `crop` est disponible et pertinent uniquement lorsque `resize_type` est défini sur `SCALE_DIMENSIONS` ou `MATCH_SIZE`. Lors de l'utilisation de `SCALE_WIDTH` ou `SCALE_HEIGHT`, l'autre dimension est automatiquement mise à l'échelle pour conserver le rapport hauteur/largeur d'origine.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `resized` | L'image ou le masque redimensionné, correspondant au type de données de l'entrée. | IMAGE ou MASK |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImageMaskNode/fr.md)

---
**Source fingerprint (SHA-256):** `9ac0b153608ac971bb11d9d12ebd1f0f4d6e926604e8727a1bc3a311d95fbc03`
