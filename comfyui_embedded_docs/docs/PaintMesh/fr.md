# PaintMesh

PaintMesh applique un maillage 3D et un champ de voxels de couleur. Il assigne à chaque sommet la couleur du voxel le plus proche dans le champ, écrivant le résultat comme couleurs de sommet sur le maillage de sortie. Si le champ de voxels est vide, le maillage est peint avec des couleurs de sommet nulles (noir) par défaut.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `mesh` | Le maillage à peindre. | MESH | Oui | N/A |
| `voxel_colors` | Champ de voxels contenant les données de couleur utilisées pour la peinture. Seuls les canaux RVB de la couleur de base sont utilisés à partir du champ. | VOXEL | Oui | N/A |

Remarque : lorsque les coordonnées du champ de voxels incluent un canal d'indice de lot et que le maillage d'entrée contient plusieurs éléments de maillage, le nœud applique les couleurs séparément à chaque élément de maillage du lot. Les couleurs échantillonnées sont converties de sRGB vers RGB linéaire pour le maillage de sortie.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `mesh` | Le maillage peint avec les couleurs de sommet appliquées. | MESH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PaintMesh/fr.md)

---
**Source fingerprint (SHA-256):** `55683bef55b18487ba660fe619d6ec176f786de346be12724751b71901c14116`
