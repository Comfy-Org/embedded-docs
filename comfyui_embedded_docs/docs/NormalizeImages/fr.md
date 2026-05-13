> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/fr.md)

Ce nœud ajuste les valeurs des pixels d'une image d'entrée en utilisant un processus de normalisation mathématique. Il soustrait une valeur moyenne spécifiée de chaque pixel, puis divise le résultat par un écart type spécifié. Il s'agit d'une étape de prétraitement courante pour préparer les données d'image à d'autres modèles d'apprentissage automatique.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée à normaliser. |
| `mean` | FLOAT | Non | 0,0 - 1,0 | Valeur moyenne pour la normalisation (par défaut : 0,5). |
| `std` | FLOAT | Non | 0,001 - 1,0 | Écart type pour la normalisation (par défaut : 0,5). |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `image` | IMAGE | L'image résultante après l'application du processus de normalisation. |

---
**Source fingerprint (SHA-256):** `9d08c8dba7d13c6f255ed786d3d2d3005bce425dc04b14b7199d868c3fc81fd9`
