> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Morphology/fr.md)

Le nœud Morphologie applique diverses opérations morphologiques aux images, qui sont des opérations mathématiques utilisées pour traiter et analyser les formes dans les images. Il peut effectuer des opérations comme l'érosion, la dilatation, l'ouverture, la fermeture, et plus encore en utilisant une taille de noyau personnalisable pour contrôler l'intensité de l'effet.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée à traiter |
| `opération` | STRING | Oui | `"erode"`<br>`"dilate"`<br>`"open"`<br>`"close"`<br>`"gradient"`<br>`"bottom_hat"`<br>`"top_hat"` | L'opération morphologique à appliquer |
| `taille_noyau` | INT | Non | 3-999 | La taille du noyau de l'élément structurant (par défaut : 3) |

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | L'image traitée après application de l'opération morphologique |
