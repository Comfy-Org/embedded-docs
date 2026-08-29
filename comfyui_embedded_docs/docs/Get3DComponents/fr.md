# Obtenir les composants 3D

Get3DComponents analyse un fichier de modèle 3D (GLB, GLTF, OBJ ou STL) en un maillage éditable pouvant être utilisé par des nœuds de traitement de maillage tels que decimate, remesh, UV unwrap et bake. Tous les nœuds et primitives de la scène sont fusionnés en un seul maillage avec leurs transformations appliquées, et les textures et paramètres de matériau proviennent du premier matériau. C'est la contrepartie du nœud MeshToFile3D.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_3d` | Fichier de modèle 3D provenant du nœud Load 3D ou d'un autre nœud 3D. Les fichiers FBX/USDZ ne sont pas pris en charge - convertissez-les en GLB d'abord. | File3DGLB<br>File3DGLTF<br>File3DOBJ<br>File3DSTL<br>File3DAny | Oui | GLB<br>GLTF<br>OBJ<br>STL |

Remarque : Les fichiers FBX et USDZ ne sont pas pris en charge et provoquent une erreur ; convertissez-les d'abord en GLB ou GLTF. Si le fichier 3D contient plusieurs matériaux, seules les textures et les facteurs de matériau du premier matériau sont conservés (un avertissement est journalisé). Toutes les primitives de la scène sont fusionnées en un seul maillage avec leurs transformations appliquées. Ce nœud est expérimental.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `mesh` | Maillage éditable contenant les sommets, les faces, les UV, les couleurs de sommets, les normales, les tangentes et les informations de matériau (texture, rugosité-métallique, carte de normales, émissif, drapeau unlit) extraits du fichier de modèle. | MESH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Get3DComponents/fr.md)

---
**Source fingerprint (SHA-256):** `f2cdc9767a50503988484f09d2b3d110caf086b8cd84f65034a4a1e17a94405e`
