# MoGeGeometryToFOV

Ce nœud dérive le champ de vision et la distance focale à partir des paramètres intrinsèques de la caméra stockés dans un objet géométrique MoGe. Il peut renvoyer le FOV vertical, horizontal ou diagonal, en degrés ou en radians. La sortie du FOV vertical peut être utilisée, par exemple, pour alimenter le nœud SAM3DBody_Predict.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `moge_geometry` | L’objet géométrique MoGe. Il doit contenir une matrice intrinsèque et au moins une des données suivantes : image, points ou profondeur, utilisée pour lire la hauteur de pixel pour la conversion de distance focale. | MOGE_GEOMETRY | Oui | — |
| `axis` | L’axe le long duquel le FOV est calculé : "vertical" (fov_y), "horizontal" (fov_x), ou "diagonal" (par défaut : "vertical"). | COMBO | Oui | "vertical"<br>"horizontal"<br>"diagonal" |
| `unit` | Unité de sortie pour le FOV (par défaut : "degrees"). | COMBO | Oui | "degrees"<br>"radians" |

Remarque : le nœud génère une erreur si `moge_geometry` ne contient pas de matrice intrinsèque (la géométrie panoramique n’en a pas) ou s’il ne contient ni image, ni points, ni données de profondeur.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `fov` | Le champ de vision le long de l’axe sélectionné, dans l’unité choisie (degrés ou radians). | FLOAT |
| `focal_pixels` | La distance focale de l’objectif en pixels, dérivée du paramètre intrinsèque vertical et de la hauteur de pixel. | FLOAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeGeometryToFOV/fr.md)

---
**Source fingerprint (SHA-256):** `983dc984847f93a8e002c73982571ecb38b7bae9c3dc4c201d9be17f785dcaed`
