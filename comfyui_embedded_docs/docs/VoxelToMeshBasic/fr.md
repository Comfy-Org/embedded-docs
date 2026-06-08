Le nœud **VoxelToMeshBasic** convertit des données voxel 3D en géométrie de maillage. Il traite les volumes voxel en appliquant une valeur de seuil pour déterminer quelles parties du volume deviennent des surfaces solides dans le maillage résultant. Le nœud produit une structure de maillage complète avec des sommets et des faces, utilisable pour le rendu et la modélisation 3D.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `voxel` | Les données voxel 3D à convertir en maillage | VOXEL | Oui | - |
| `seuil` | La valeur de seuil utilisée pour déterminer quels voxels font partie de la surface du maillage (par défaut : 0.6) | FLOAT | Oui | -1.0 à 1.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `MESH` | Le maillage 3D généré contenant les sommets et les faces | MESH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMeshBasic/fr.md)

---
**Source fingerprint (SHA-256):** `36df962c84c99a83f243a59b6387874e42e7d05323bd84079dbab112d2f1b67c`
