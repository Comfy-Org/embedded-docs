Le nœud ScaleROPE vous permet de modifier l'encodage positionnel rotatif (ROPE) d'un modèle en appliquant des facteurs d'échelle et de décalage distincts à ses composantes X, Y et T (temporelle). Il s'agit d'un nœud expérimental avancé utilisé pour ajuster le comportement d'encodage positionnel du modèle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle dont les paramètres ROPE seront modifiés. | MODEL | Oui | - |
| `échelle_x` | Facteur d'échelle à appliquer à la composante X du ROPE (par défaut : 1.0). | FLOAT | Non | 0.0 - 100.0 |
| `décalage_x` | Valeur de décalage à appliquer à la composante X du ROPE (par défaut : 0.0). | FLOAT | Non | -256.0 - 256.0 |
| `échelle_y` | Facteur d'échelle à appliquer à la composante Y du ROPE (par défaut : 1.0). | FLOAT | Non | 0.0 - 100.0 |
| `décalage_y` | Valeur de décalage à appliquer à la composante Y du ROPE (par défaut : 0.0). | FLOAT | Non | -256.0 - 256.0 |
| `échelle_t` | Facteur d'échelle à appliquer à la composante T (temporelle) du ROPE (par défaut : 1.0). | FLOAT | Non | 0.0 - 100.0 |
| `décalage_t` | Valeur de décalage à appliquer à la composante T (temporelle) du ROPE (par défaut : 0.0). | FLOAT | Non | -256.0 - 256.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `modèle` | Le modèle avec les nouveaux paramètres d'échelle et de décalage ROPE appliqués. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ScaleROPE/fr.md)

---
**Source fingerprint (SHA-256):** `c5ca193a46faa9477a2e6c99b905205685e8add8faa2f2d161c7c384b3dc2441`
