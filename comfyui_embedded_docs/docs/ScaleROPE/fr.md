# ÉchelleROPE

Le nœud ScaleROPE vous permet de modifier le plongement de position rotatif (ROPE) d'un modèle en appliquant des facteurs d'échelle et de décalage distincts à ses composantes X, Y et T (temps). Il s'agit d'un nœud avancé et expérimental utilisé pour ajuster le comportement de l'encodage positionnel du modèle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle dont les paramètres ROPE seront modifiés. | MODEL | Oui | - |
| `échelle_x` | Le facteur d'échelle à appliquer à la composante X du ROPE (par défaut : 1.0). | FLOAT | Oui | 0.0 - 100.0 (step 0.1) |
| `décalage_x` | La valeur de décalage à appliquer à la composante X du ROPE (par défaut : 0.0). | FLOAT | Oui | -256.0 - 256.0 (step 0.1) |
| `échelle_y` | Le facteur d'échelle à appliquer à la composante Y du ROPE (par défaut : 1.0). | FLOAT | Oui | 0.0 - 100.0 (step 0.1) |
| `décalage_y` | La valeur de décalage à appliquer à la composante Y du ROPE (par défaut : 0.0). | FLOAT | Oui | -256.0 - 256.0 (step 0.1) |
| `échelle_t` | Le facteur d'échelle à appliquer à la composante T (temps) du ROPE (par défaut : 1.0). | FLOAT | Oui | 0.0 - 100.0 (step 0.1) |
| `décalage_t` | La valeur de décalage à appliquer à la composante T (temps) du ROPE (par défaut : 0.0). | FLOAT | Oui | -256.0 - 256.0 (step 0.1) |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle avec les nouveaux paramètres d'échelle et de décalage ROPE appliqués. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ScaleROPE/fr.md)

---
**Source fingerprint (SHA-256):** `5d5ab0182b78c8c12ceaf44685a91e666ce15fa099fd194e3605bbdb9cc3c961`
