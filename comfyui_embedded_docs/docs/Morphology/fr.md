Le nœud Morphology applique diverses opérations morphologiques aux images, qui sont des opérations mathématiques utilisées pour traiter et analyser les formes dans les images. Il peut effectuer des opérations comme l'érosion, la dilatation, l'ouverture, la fermeture, et plus encore, en utilisant une taille de noyau personnalisable pour contrôler l'intensité de l'effet.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée à traiter | IMAGE | Oui | - |
| `opération` | L'opération morphologique à appliquer (par défaut : "erode") | STRING | Oui | `"erode"`<br>`"dilate"`<br>`"open"`<br>`"close"`<br>`"gradient"`<br>`"bottom_hat"`<br>`"top_hat"` |
| `taille_noyau` | La taille du noyau de l'élément structurant (par défaut : 3). Doit être un nombre impair. | INT | Oui | 3-999 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image traitée après application de l'opération morphologique | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Morphology/fr.md)

---
**Source fingerprint (SHA-256):** `7f6224a0e58fbb7263267b377394e119c6f8d65d16af4ce492ca9504654af7b4`
