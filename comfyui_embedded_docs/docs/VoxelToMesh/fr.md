# VoxelToMesh

Le nœud VoxelToMeshBasic convertit des données voxel 3D en une géométrie de maillage en extrayant une surface à une valeur de seuil spécifiée. Il traite chaque grille de voxel en entrée et génère des sommets et des faces qui forment une représentation 3D sous forme de maillage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `voxel` | Les données voxel d'entrée à convertir en géométrie de maillage | VOXEL | Oui | - |
| `seuil` | La valeur de seuil pour l'extraction de surface (par défaut : 0,6) | FLOAT | Oui | -1,0 à 1,0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `MESH` | Le maillage 3D généré contenant les sommets et faces empilés provenant de toutes les grilles de voxel en entrée | MESH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMesh/fr.md)

---
**Source fingerprint (SHA-256):** `36df962c84c99a83f243a59b6387874e42e7d05323bd84079dbab112d2f1b67c`
