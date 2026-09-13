# Souder les sommets

Weld Vertices fusionne les sommets coïncidents dans un maillage 3D, de sorte que les faces qui avaient auparavant des points de coin séparés finissent par partager les mêmes sommets. Il regroupe les sommets proches en utilisant une quantification de grille avec une tolérance basée sur la boîte englobante du maillage, et moyenne les couleurs des sommets pour chaque groupe fusionné. Cela est utile lorsqu'un maillage arrive non soudé, ce qui signifie que chaque face a ses propres sommets et aucun bord partagé, et peut servir d'étape préalable avant des opérations sensibles à la topologie telles que FillHoles ou DecimateMesh.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `mesh` | Le maillage 3D d'entrée dont les sommets coïncidents seront fusionnés. | MESH | Oui | - |
| `epsilon_rel` | Tolérance de soudage (fraction de la diagonale de la boîte englobante). 1e-5 pour la déduplication de flottants ; 1e-3 pour les sommets visiblement proches mais distincts. Défaut : 1e-5. | FLOAT | Oui | 0.0 à illimité (pas 1e-6) |
| `epsilon_abs` | Tolérance de soudage absolue (remplace epsilon_rel lorsque > 0). Défaut : 0.0. | FLOAT | Oui | 0.0 à illimité (pas 1e-6) |

Remarque : Lorsque `epsilon_abs` est supérieur à 0, il a la priorité sur `epsilon_rel` et la tolérance relative est ignorée. Lorsque `epsilon_abs` est 0, la tolérance relative `epsilon_rel` est utilisée, convertie en distance absolue en la multipliant par la diagonale de la boîte englobante du maillage.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `mesh` | Le maillage soudé avec les sommets fusionnés, les indices de faces mis à jour et les couleurs de sommets moyennées (si le maillage d'entrée avait des couleurs). | MESH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WeldVertices/fr.md)

---
**Source fingerprint (SHA-256):** `f8779e764b344de651b8459f6e4c28773509d9596a98fd164dc7044278856435`
