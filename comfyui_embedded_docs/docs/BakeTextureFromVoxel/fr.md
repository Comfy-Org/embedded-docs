# Pré-calculer la texture depuis le voxel

Ce nœud effectue le baking de textures PBR sur un maillage 3D en utilisant la disposition UV existante du maillage. Il rastérise le maillage dans l’espace UV et échantillonne les attributs de couleur et de matériau à partir d’un volume de voxels épars à chaque texel, produisant une image de couleur de base ainsi que des cartes métallique et de rugosité. Il ne déplie pas le maillage ; un nœud de dépliage UV doit donc être connecté en amont ; les images résultantes sont destinées à être associées au même maillage dans ApplyTextureToMesh pour être enregistrées au format GLB.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `mesh` | Le maillage 3D sur lequel appliquer les textures par baking. Doit déjà disposer d’une disposition UV ; un nœud de dépliage UV doit être connecté en amont. | MESH | Oui | |
| `voxel_colors` | Volume de voxels épars contenant les couleurs par voxel et des attributs PBR facultatifs (canaux métallique et rugosité). | VOXEL | Oui | |
| `texture_size` | Résolution carrée de l’atlas UV (nom affiché : « resolution », par défaut : 2048). | INT | Oui | 64 à 8192 |
| `reference_mesh` | Maillage dense pré-décimation facultatif ; reprojette chaque texel sur sa surface réelle avant l’échantillonnage, supprimant le baking facetté sur les maillages grossiers. | MESH | Non | |

Remarques :

- Le maillage d’entrée doit avoir des UV. Si aucune UV n’est présente, le nœud déclenche une erreur. Les UV doivent être 1:1 avec les sommets (une UV par sommet).
- Lorsque le maillage et les coordonnées de voxels contiennent une dimension de lot, chaque élément du lot fait l’objet d’un baking séparé. Si un élément du lot n’a pas de voxels ou pas de faces, il est ignoré et une texture noire est émise pour lui.
- Lorsque `reference_mesh` est fourni pour un lot, il est apparié par indice de lot, sauf s’il ne contient qu’un seul maillage, auquel cas ce maillage est utilisé pour tous les éléments.
- Les texels qui ne sont couverts par aucun triangle UV sont remplis à partir du texel couvert le plus proche afin que les coutures de texture ne fassent pas apparaître de noir.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `base_color` | Carte de texture de couleur de base RVB. Les valeurs sont de type float dans la plage 0–1. | IMAGE |
| `metallic` | Carte métallique en niveaux de gris (float, 0–1). Noire lorsque les couleurs de voxels ne contiennent aucun canal métallique. | IMAGE |
| `roughness` | Carte de rugosité en niveaux de gris (float, 0–1). Noire lorsque les couleurs de voxels ne contiennent aucun canal de rugosité. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeTextureFromVoxel/fr.md)

---
**Source fingerprint (SHA-256):** `080dcb670620f1cb97523d04fc45293e03d139e513845d0fa7b1c4d2f8bdf32d`
