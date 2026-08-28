# Normaliser les images

Ce nœud ajuste les valeurs de pixels d'une image d'entrée à l'aide d'un processus de normalisation mathématique. Il soustrait une valeur moyenne spécifiée de chaque pixel, puis divise le résultat par un écart type spécifié. Il s'agit d'une étape de prétraitement courante pour préparer les données d'image pour d'autres modèles d'apprentissage automatique.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée à normaliser. | IMAGE | Oui | - |
| `moyenne` | Valeur moyenne pour la normalisation (par défaut : 0.5). | FLOAT | Non | 0.0 - 1.0 |
| `écart_type` | Écart type pour la normalisation (par défaut : 0.5). | FLOAT | Non | 0.001 - 1.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `images` | L'image résultante après application du processus de normalisation. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/fr.md)

---
**Source fingerprint (SHA-256):** `927451ed275254d87e42b52919143ee2f3d9833a2aa5b43c7315d798871f9a2d`
