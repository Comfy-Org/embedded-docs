> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ScaleROPE/fr.md)

Le nœud ScaleROPE vous permet de modifier l'encodage positionnel rotatif (ROPE) d'un modèle en appliquant des facteurs de mise à l'échelle et de décalage distincts à ses composantes X, Y et T (temps). Il s'agit d'un nœud expérimental avancé utilisé pour ajuster le comportement de l'encodage positionnel du modèle.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle dont les paramètres ROPE seront modifiés. |
| `scale_x` | FLOAT | Non | 0.0 - 100.0 | Le facteur de mise à l'échelle à appliquer à la composante X du ROPE (par défaut : 1.0). |
| `shift_x` | FLOAT | Non | -256.0 - 256.0 | La valeur de décalage à appliquer à la composante X du ROPE (par défaut : 0.0). |
| `scale_y` | FLOAT | Non | 0.0 - 100.0 | Le facteur de mise à l'échelle à appliquer à la composante Y du ROPE (par défaut : 1.0). |
| `shift_y` | FLOAT | Non | -256.0 - 256.0 | La valeur de décalage à appliquer à la composante Y du ROPE (par défaut : 0.0). |
| `scale_t` | FLOAT | Non | 0.0 - 100.0 | Le facteur de mise à l'échelle à appliquer à la composante T (temps) du ROPE (par défaut : 1.0). |
| `shift_t` | FLOAT | Non | -256.0 - 256.0 | La valeur de décalage à appliquer à la composante T (temps) du ROPE (par défaut : 0.0). |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle avec les nouveaux paramètres de mise à l'échelle et de décalage du ROPE appliqués. |
