# VoxelToMesh

Le nœud VoxelToMesh convertit des données de voxels 3D en une géométrie de maillage en extrayant une surface à une valeur de seuil spécifiée. Il propose deux algorithmes d'extraction de surface : une méthode de base qui crée des faces simples en forme de boîtes, et une méthode surface net qui produit des maillages plus lisses et plus détaillés. Le nœud traite chaque grille de voxels en entrée et génère des sommets et des faces qui forment une représentation de maillage 3D.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `voxel` | Les données de voxels d'entrée à convertir en géométrie de maillage | VOXEL | Oui | - |
| `algorithm` | L'algorithme utilisé pour l'extraction de surface. "surface net" produit des maillages plus lisses, tandis que "basic" crée des faces simples en forme de boîtes (par défaut : "surface net") | COMBO | Oui | `"surface net"`<br>`"basic"` |
| `threshold` | La valeur de seuil pour l'extraction de surface. Les voxels dont les valeurs sont supérieures à ce seuil sont considérés comme solides (par défaut : 0.6) | FLOAT | Oui | -1.0 à 1.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `MESH` | Le maillage 3D généré contenant les sommets et les faces de toutes les grilles de voxels d'entrée. Si toutes les grilles de voxels produisent des maillages de formes identiques, la sortie est un tenseur empilé ; sinon, un lot de longueur variable est renvoyé | MESH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMesh/fr.md)

---
**Source fingerprint (SHA-256):** `b600be13f1a484d8c0cc1f9c3918630d00c15d35008bcac0f677b21ef64b5d98`
