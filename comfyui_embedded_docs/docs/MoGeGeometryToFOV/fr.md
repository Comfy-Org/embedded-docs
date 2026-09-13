# Obtenir le champ de vision à partir de la géométrie MoGe

Ce nœud déduit le champ de vision et la distance focale à partir des paramètres intrinsèques de la caméra stockés dans un objet de géométrie MoGe. Il peut renvoyer le FOV vertical, horizontal ou diagonal, en degrés ou en radians. La sortie FOV vertical peut être utilisée, par exemple, pour alimenter le nœud SAM3DBody_Predict.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `moge_geometry` | L'objet de géométrie MoGe. Il doit contenir une matrice intrinsèque et au moins une des données `image`, `points` ou `depth`, qui est utilisée pour lire la hauteur en pixels pour la conversion de la distance focale. | MOGE_GEOMETRY | Oui | — |
| `axis` | L'axe selon lequel le FOV est calculé : "vertical" (fov_y), "horizontal" (fov_x) ou "diagonal" (par défaut : "vertical"). | COMBO | Oui | "vertical"<br>"horizontal"<br>"diagonal" |
| `unit` | Unité de sortie pour le FOV (par défaut : "degrees"). | COMBO | Oui | "degrees"<br>"radians" |

Remarque : Le nœud lève une erreur si `moge_geometry` ne contient aucun paramètre intrinsèque (la géométrie panorama n'en contient aucun) ou s'il ne contient ni `image`, ni `points`, ni `depth`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `fov` | Le champ de vision le long de l'axe sélectionné, dans l'unité sélectionnée (degrés ou radians). | FLOAT |
| `focal_pixels` | La distance focale de l'objectif en pixels, déduite du paramètre intrinsèque vertical et de la hauteur en pixels. | FLOAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeGeometryToFOV/fr.md)

---
**Source fingerprint (SHA-256):** `983dc984847f93a8e002c73982571ecb38b7bae9c3dc4c201d9be17f785dcaed`
