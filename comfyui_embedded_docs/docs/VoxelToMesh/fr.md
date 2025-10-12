> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMesh/fr.md)

Le nœud VoxelToMesh convertit des données voxel 3D en géométrie maillée en utilisant différents algorithmes. Il traite les grilles de voxels et génère des sommets et des faces qui forment une représentation de maillage 3D. Le nœud prend en charge plusieurs algorithmes de conversion et permet d'ajuster la valeur de seuil pour contrôler l'extraction de surface.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `voxel` | VOXEL | Oui | - | Les données voxel d'entrée à convertir en géométrie maillée |
| `algorithme` | COMBO | Oui | "surface net"<br>"basic" | L'algorithme utilisé pour la conversion de maillage à partir des données voxel |
| `seuil` | FLOAT | Oui | -1.0 à 1.0 | La valeur de seuil pour l'extraction de surface (par défaut : 0.6) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `MESH` | MESH | Le maillage 3D généré contenant les sommets et les faces |