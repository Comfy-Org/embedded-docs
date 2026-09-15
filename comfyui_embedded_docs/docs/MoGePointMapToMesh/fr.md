# MoGe Point Map vers Mesh

This node converts a MoGe point map into a 3D mesh. It takes geometry data produced by a MoGe depth estimation node and triangulates it into a mesh with UV coordinates and an optional texture.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `moge_geometry` | Les données de géométrie MoGe contenant les cartes de points, la profondeur et éventuellement l'image source. | MOGE_GEOMETRY | Oui | N/A |
| `batch_index` | Quelle image d'une géométrie MoGe traitée par lots doit être convertie en maillage. Le nombre de sommets diffère d'une image à l'autre, donc les lots ne peuvent pas être empilés en un seul MESH (par défaut : 0). | INT | Oui | 0 à 4096 |
| `décimation` | Pas des sommets ; 1 = pleine résolution (par défaut : 1). | INT | Oui | 1 à 8 |
| `seuil_de_discontinuité` | Supprime les pixels dont l'étendue de profondeur 3x3 dépasse cette fraction. 0 = désactivé (par défaut : 0.04). | FLOAT | Oui | 0.0 à 1.0 |
| `texture` | Transmet l'image source comme texture baseColor (par défaut : True). | BOOLEAN | Oui | True/False |

Remarque : `batch_index` doit être inférieur à la taille du lot de l'entrée `moge_geometry` ; sélectionner un index hors plage déclenche une erreur. L'entrée doit contenir une sortie points, sinon le nœud déclenche une erreur. Si la triangulation produit un maillage vide, le nœud déclenche une erreur — définir `discontinuity_threshold` sur 0 désactive le filtre de discontinuité de profondeur. Le maillage de sortie est converti en coordonnées glTF : les données MoGe en perspective (X à droite, Y vers le bas, Z vers l'avant) sont retournées pour correspondre à glTF (Y vers le haut, Z vers l'arrière), et les données panoramiques (géométrie sans paramètres intrinsèques) sont tournées en conséquence avec un enroulement corrigé. Lorsque `texture` est activé, l'image source issue de `moge_geometry` est utilisée comme texture baseColor.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `MESH` | Un maillage 3D avec des sommets, des faces, des coordonnées UV et une texture baseColor facultative issue de l'image source. | MESH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePointMapToMesh/fr.md)

---
**Source fingerprint (SHA-256):** `626925866eed6805d2ce87529909fc76b9484cd2e8118fdd1669a237d44b9b0b`
