# Normaliser les images

Ce nœud ajuste les valeurs des pixels d'une image d'entrée en utilisant un processus de normalisation mathématique. Il soustrait une valeur moyenne spécifiée de chaque pixel, puis divise le résultat par un écart type spécifié. Il s'agit d'une étape de prétraitement courante pour préparer les données d'image à d'autres modèles d'apprentissage automatique.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée à normaliser. | IMAGE | Oui | - |
| `moyenne` | Valeur moyenne pour la normalisation (par défaut : 0,5). | FLOAT | Non | 0,0 - 1,0 |
| `écart_type` | Écart type pour la normalisation (par défaut : 0,5). | FLOAT | Non | 0,001 - 1,0 |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `images` | L'image résultante après l'application du processus de normalisation. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/fr.md)

---
**Source fingerprint (SHA-256):** `9d08c8dba7d13c6f255ed786d3d2d3005bce425dc04b14b7199d868c3fc81fd9`
