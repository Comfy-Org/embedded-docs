# WeldVertices

Weld Vertices fusionne les sommets coïncidents d'un maillage 3D, de sorte que les faces qui avaient auparavant des points de coin distincts finissent par partager les mêmes sommets. Il regroupe les sommets proches à l'aide d'une quantification par grille avec une tolérance basée sur la boîte englobante du maillage, et fait la moyenne des couleurs de sommets pour chaque groupe fusionné. Cela est utile lorsqu'un maillage arrive non soudé, c'est-à-dire que chaque face possède ses propres sommets et aucune arête partagée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `mesh` | Le maillage 3D d'entrée dont les sommets coïncidents seront fusionnés. | MESH | Oui | - |
| `epsilon_rel` | Tolérance de soudure (fraction de la diagonale de la boîte englobante). 1e-5 pour la déduplication flottante ; 1e-3 pour des sommets visiblement proches mais distincts. Défaut : 1e-5. | FLOAT | Oui | 0.0 à illimité |
| `epsilon_abs` | Tolérance de soudure absolue (remplace `epsilon_rel` lorsqu'elle est > 0). Défaut : 0.0. | FLOAT | Oui | 0.0 à illimité |

Remarque : Lorsque `epsilon_abs` est supérieur à 0, elle prévaut sur `epsilon_rel` et la tolérance relative est ignorée. Lorsque `epsilon_abs` est 0, la tolérance relative `epsilon_rel` est utilisée.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `mesh` | Le maillage soudé avec les sommets fusionnés, les indices de faces mis à jour et les couleurs de sommets moyennées (si le maillage d'entrée avait des couleurs). | MESH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WeldVertices/fr.md)

---
**Source fingerprint (SHA-256):** `f8779e764b344de651b8459f6e4c28773509d9596a98fd164dc7044278856435`
