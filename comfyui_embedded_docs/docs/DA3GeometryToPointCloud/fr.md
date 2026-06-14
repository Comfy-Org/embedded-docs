# Convertir la géométrie DA3 en nuage de points

Ce nœud convertit une carte de profondeur issue d'un objet DA3_GEOMETRY en un nuage de points 3D. Il applique un filtrage basé sur la confiance et les masques de ciel, et transforme les points dans un système de coordonnées mondial commun adapté aux scènes multi-vues.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `da3_geometry` | L'objet DA3_GEOMETRY contenant les données de profondeur ainsi que les cartes optionnelles d'image, de confiance et de ciel | DA3_GEOMETRY | Oui | - |
| `batch_index` | Quelle image d'un lot convertir (par défaut : 0) | INT | Oui | 0 à 4096 |
| `confidence_threshold` | Exclure les pixels dont la confiance normalisée par image est inférieure à cette valeur (0 = tout conserver). Utilisé lorsque la géométrie possède une carte de confiance (modèles Small/Base). (par défaut : 0,1) | FLOAT | Oui | 0,0 à 1,0 |
| `use_sky_mask` | Exclure les pixels à probabilité de ciel (ciel >= 0,5). Utilisé lorsque la géométrie possède une carte de ciel (modèles Mono/Metric). (par défaut : Vrai) | BOOLEAN | Oui | Vrai ou Faux |
| `downsample` | Prendre un pixel sur N (1 = pleine résolution). Des valeurs plus élevées donnent moins de points et un traitement plus rapide. (par défaut : 1) | INT | Oui | 1 à 16 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `point_cloud` | Un objet nuage de points contenant les points 3D filtrés, les couleurs optionnelles et les valeurs de confiance optionnelles | DA3_POINT_CLOUD |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DA3GeometryToPointCloud/fr.md)

---
**Source fingerprint (SHA-256):** `3cf5bdbb8afdfcfc02f9832a8cbc5a3df49da755dea6df01792aa6ef9e5d7287`
