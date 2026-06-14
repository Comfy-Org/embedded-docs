# Convertir DA3 Geometry en Maillage

Ce nœud convertit un paquet DA3_GEOMETRY en un maillage 3D en déprojetant la carte de profondeur et en triangulant le nuage de points résultant. Il traite une seule image d'un lot et produit un maillage texturé ou non texturé adapté au rendu 3D.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `da3_geometry` | Le paquet DA3_GEOMETRY contenant la carte de profondeur, la carte de confiance optionnelle, la carte de ciel optionnelle et l'image source | DA3_GEOMETRY | Oui | - |
| `batch_index` | Quelle image d'un lot convertir. Les nombres de sommets par image diffèrent, donc les lots ne peuvent pas être empilés (par défaut : 0) | INT | Oui | 0 à 4096 |
| `decimation` | Pas de sommet. 1 = pleine résolution, 2 = moitié, etc. (par défaut : 1) | INT | Oui | 1 à 8 |
| `discontinuity_threshold` | Supprimer les triangles dont l'étendue de profondeur 3x3 dépasse cette fraction. 0 = désactivé (par défaut : 0,04) | FLOAT | Oui | 0,0 à 1,0 |
| `confidence_threshold` | Exclure les pixels dont la confiance normalisée par image est inférieure à cette valeur. 0 = tout conserver, 1 = ne conserver que le pixel le plus fiable. Utilisé lorsque la géométrie possède une carte de confiance (modèles Small/Base) (par défaut : 0,1) | FLOAT | Oui | 0,0 à 1,0 |
| `use_sky_mask` | Exclure les pixels de probabilité de ciel (ciel >= 0,5) du maillage. Utilisé lorsque la géométrie possède une carte de ciel (modèles Mono/Metric) (par défaut : Vrai) | BOOLEAN | Oui | Vrai ou Faux |
| `texture` | Utiliser l'image source comme texture de couleur de base (par défaut : Vrai) | BOOLEAN | Oui | Vrai ou Faux |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `MESH` | Un maillage 3D triangulé avec sommets, faces, coordonnées UV et texture optionnelle | MESH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DA3GeometryToMesh/fr.md)

---
**Source fingerprint (SHA-256):** `1d311223a8d131030bcd4930d21852a21ac9dd5758e7f8b8d20b1cf68698893b`
