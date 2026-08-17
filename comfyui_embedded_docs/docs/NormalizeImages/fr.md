# Normaliser les images

Ce nœud normalise une image d’entrée en soustrayant une valeur moyenne spécifiée à chaque pixel, puis en divisant le résultat par un écart type spécifié. Il s’agit d’une étape de prétraitement courante pour standardiser les valeurs des pixels et préparer les données d’image pour un traitement ultérieur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L’image d’entrée à normaliser. | IMAGE | Oui | - |
| `mean` | Valeur moyenne pour la normalisation (par défaut : 0,5). | FLOAT | Non | 0.0 - 1.0 |
| `std` | Écart type pour la normalisation (par défaut : 0,5). | FLOAT | Non | 0.001 - 1.0 |

Remarque : La normalisation est appliquée à l’ensemble du lot d’images en une seule fois, et toute taille de lot est prise en charge.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L’image résultante après application du processus de normalisation. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/fr.md)

---
**Source fingerprint (SHA-256):** `927451ed275254d87e42b52919143ee2f3d9833a2aa5b43c7315d798871f9a2d`
