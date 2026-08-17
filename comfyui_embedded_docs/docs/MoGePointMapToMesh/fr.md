# MoGe Point Map vers Mesh

Ce nœud convertit une carte de points MoGe en maillage 3D. Il prend les données géométriques produites par un nœud d'estimation de profondeur MoGe et en triangule une image en un maillage avec coordonnées UV et une texture optionnelle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `moge_geometry` | Les données géométriques MoGe contenant les cartes de points, la profondeur et, éventuellement, l'image source. | MOGE_GEOMETRY | Oui | N/A |
| `batch_index` | Quelle image d'une géométrie MoGe groupée convertir en maillage. Les nombres de sommets par image diffèrent, donc les lots ne peuvent pas être empilés en un seul MESH (par défaut : 0). | INT | Oui | 0 à 4096 |
| `decimation` | Pas de sommet ; 1 = pleine résolution (par défaut : 1). | INT | Oui | 1 à 8 |
| `discontinuity_threshold` | Supprime les pixels dont l'étendue de profondeur 3x3 dépasse cette fraction. 0 = désactivé (par défaut : 0.04). | FLOAT | Oui | 0.0 à 1.0 |
| `texture` | Transmettre l'image source comme texture baseColor (par défaut : True). | BOOLEAN | Oui | True/False |

Remarque : `batch_index` doit être inférieur à la taille du lot de la `moge_geometry` fournie. La géométrie d'entrée doit contenir des données de points, et si le maillage généré est vide, le nœud renvoie une erreur suggérant `discontinuity_threshold = 0`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `MESH` | Un maillage 3D avec sommets, faces, coordonnées UV et une texture optionnelle provenant de l'image source. | MESH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePointMapToMesh/fr.md)

---
**Source fingerprint (SHA-256):** `626925866eed6805d2ce87529909fc76b9484cd2e8118fdd1669a237d44b9b0b`
