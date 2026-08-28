# MoGeGeometryToFOV

Ce nœud dérive le champ de vision et la longueur focale à partir des intrinsèques de caméra stockés dans un objet géométrique MoGe. Il peut retourner le FOV vertical, horizontal ou diagonal, en degrés ou en radians. La sortie FOV vertical peut être utilisée, par exemple, pour alimenter le nœud SAM3DBody_Predict.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `moge_geometry` | L'objet géométrique MoGe. Il doit contenir une matrice d'intrinsèques et au moins l'une des données suivantes : image, points ou profondeur, qui est utilisée pour lire la hauteur de pixel lors de la conversion de la longueur focale. | MOGE_GEOMETRY | Oui | — |
| `axe` | L'axe le long duquel le FOV est calculé : « vertical » (fov_y), « horizontal » (fov_x) ou « diagonal » (par défaut : « vertical »). | COMBO | Oui | "vertical"<br>"horizontal"<br>"diagonal" |
| `unité` | Unité de sortie pour le FOV (par défaut : « degrees »). | COMBO | Oui | "degrees"<br>"radians" |

Remarque : Le nœud lève une erreur si `moge_geometry` ne contient pas d'intrinsèques (la géométrie panoramique n'en a pas) ou s'il ne contient ni données d'image, ni points, ni profondeur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `fov` | Le champ de vision le long de l'axe sélectionné, dans l'unité choisie (degrees ou radians). | FLOAT |
| `focal_pixels` | La longueur focale de l'objectif en pixels, dérivée de l'intrinsèque vertical et de la hauteur de pixel. | FLOAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeGeometryToFOV/fr.md)

---
**Source fingerprint (SHA-256):** `983dc984847f93a8e002c73982571ecb38b7bae9c3dc4c201d9be17f785dcaed`
