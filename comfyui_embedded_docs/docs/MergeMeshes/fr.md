# MergeMeshes

MergeMeshes combine plusieurs maillages en un seul en empilant leurs sommets, faces, coordonnées UV et couleurs de sommets, et en ajustant les indices de faces afin que le résultat soit un maillage continu unique.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `meshes` | Emplacement extensible : connectez 2 à 50 objets maillage (nommés `mesh_1`, `mesh_2`, ..., `mesh_50`). Tous les maillages connectés sont fusionnés en un seul maillage de sortie. | MESH | Oui | 2 à 50 maillages |

**Remarque :** Seul le premier élément de maillage de chaque lot (batch) d’entrée est utilisé. Si un maillage d’entrée possède des données UV, la sortie inclut les UV et les maillages sans UV reçoivent des valeurs UV remplies de zéros. Si un maillage d’entrée possède des couleurs de sommets, la sortie inclut les couleurs de sommets ; les maillages sans couleurs reçoivent des couleurs blanches (valeur 1), et les canaux de couleur sont remplis de zéros jusqu’au nombre de canaux le plus élevé trouvé parmi les entrées. Seule la texture provenant du premier maillage qui en fournit une est conservée ; les textures supplémentaires sont supprimées.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `mesh` | Le maillage fusionné contenant tous les sommets, faces, UV et couleurs des entrées, combinés en un seul maillage. | MESH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeMeshes/fr.md)

---
**Source fingerprint (SHA-256):** `0ce49b522f6348d524df20d6c27eb8bd9575c4a781790f6f8e3ac4f3ee255d38`
