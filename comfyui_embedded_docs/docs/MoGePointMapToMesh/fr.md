Voici la traduction de la documentation technique du nœud ComfyUI, en respectant toutes les règles spécifiées :

---

## Aperçu

Ce nœud convertit une carte de points MoGe en un maillage 3D. Il prend les données géométriques produites par un nœud d'estimation de profondeur MoGe et les triangule en un maillage avec des coordonnées UV et une texture optionnelle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `moge_geometry` | Les données géométriques MoGe contenant les cartes de points, la profondeur et éventuellement l'image source. | MOGE_GEOMETRY | Oui | N/D |
| `batch_index` | Quelle image d'une géométrie MoGe par lots transformer en maillage. Les nombres de sommets par image diffèrent, donc les lots ne peuvent pas être empilés en un seul MESH (par défaut : 0). | INT | Oui | 0 à 4096 |
| `décimation` | Pas de sommet ; 1 = pleine résolution (par défaut : 1). | INT | Oui | 1 à 8 |
| `seuil_de_discontinuité` | Supprime les pixels dont l'étendue de profondeur 3x3 dépasse cette fraction. 0 = désactivé (par défaut : 0.04). | FLOAT | Oui | 0.0 à 1.0 |
| `texture` | Transmet l'image source comme texture baseColor (par défaut : Vrai). | BOOLEAN | Oui | Vrai/Faux |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `MESH` | Un maillage 3D avec sommets, faces, coordonnées UV et une texture optionnelle provenant de l'image source. | MESH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePointMapToMesh/fr.md)

---
**Source fingerprint (SHA-256):** `65c43d64050d1c63d9efbb6c2bb96123f94c6d356d6341f2975537ac24ace29f`
