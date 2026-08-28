# MoGe Point Map vers Mesh

Ce nœud convertit une carte de points MoGe en maillage 3D. Il prend les données de géométrie produites par un nœud d'estimation de profondeur MoGe et les triangule en un maillage avec des coordonnées UV et une texture facultative.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `moge_geometry` | Les données de géométrie MoGe contenant les cartes de points, la profondeur et éventuellement l'image source. | MOGE_GEOMETRY | Oui | N/A |
| `batch_index` | Quelle image d'une géométrie MoGe groupée convertir en maillage. Le nombre de sommets varie selon l'image, donc les lots ne peuvent pas être empilés dans un seul MESH (défaut : 0). | INT | Oui | 0 à 4096 |
| `décimation` | Pas de sommet ; 1 = pleine résolution (défaut : 1). | INT | Oui | 1 à 8 |
| `seuil_de_discontinuité` | Supprime les pixels dont l'étendue de profondeur 3x3 dépasse cette fraction. 0 = désactivé (défaut : 0,04). | FLOAT | Oui | 0.0 à 1.0 |
| `texture` | Transmet l'image source en tant que texture baseColor (défaut : True). | BOOLEAN | Oui | True/False |

Remarque : `batch_index` doit être inférieur à la taille du lot de `moge_geometry` ; la sélection d'un index hors plage déclenche une erreur. Si la triangulation produit un maillage vide, le nœud déclenche une erreur — définir `discontinuity_threshold` sur 0 désactive le filtre de discontinuité de profondeur. Le maillage de sortie est converti en coordonnées glTF : les données MoGe en perspective (X à droite, Y vers le bas, Z vers l'avant) sont inversées pour correspondre à glTF (Y vers le haut, Z vers l'arrière), et les données panoramiques sont pivotées en conséquence. Lorsque `texture` est activé, l'image source de `moge_geometry` est utilisée comme texture baseColor.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `MESH` | Un maillage 3D avec des sommets, des faces, des coordonnées UV et une texture baseColor facultative provenant de l'image source. | MESH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePointMapToMesh/fr.md)

---
**Source fingerprint (SHA-256):** `626925866eed6805d2ce87529909fc76b9484cd2e8118fdd1669a237d44b9b0b`
