> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMeshBasic/fr.md)

Le nœud VoxelToMeshBasic convertit des données voxel 3D en géométrie maillée. Il traite les volumes voxel en appliquant une valeur de seuil pour déterminer quelles parties du volume deviennent des surfaces solides dans le maillage résultant. Le nœud produit une structure maillée complète avec des sommets et des faces qui peut être utilisée pour le rendu et la modélisation 3D.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `voxel` | VOXEL | Oui | - | Les données voxel 3D à convertir en maillage |
| `seuil` | FLOAT | Oui | -1.0 à 1.0 | La valeur de seuil utilisée pour déterminer quels voxels font partie de la surface du maillage (par défaut : 0.6) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `MESH` | MESH | Le maillage 3D généré contenant les sommets et les faces |