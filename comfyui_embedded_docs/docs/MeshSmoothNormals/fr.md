# MeshSmoothNormals

Calcule des normales lisses par sommet pour un maillage et les attache. Les maillages sans normales sont ombrés de façon plate (par face) par les visionneuses glTF ; ce nœud permet un ombrage lisse. Avec un angle de pli inférieur à 180, les arêtes plus vives que le seuil restent nettes en divisant les sommets le long de celles-ci.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `mesh` | Le maillage d'entrée à traiter. | MESH | Oui | - |
| `crease_angle` | Les arêtes dont l'angle dièdre dépasse cette valeur (en degrés) restent vives (les sommets sont divisés). 180 = entièrement lisse ; une valeur inférieure préserve les arêtes vives (par ex. ~30-60 pour les surfaces dures). Défaut : 180.0. | FLOAT | Oui | 0.0 à 180.0 (pas de 1.0) |

Quand `crease_angle` est égal à 180 ou plus, la topologie du maillage est inchangée. Quand elle est inférieure à 180, les sommets sont divisés le long des arêtes vives, ce qui peut augmenter le nombre de sommets.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `mesh` | Le maillage d'entrée avec les données de normales lisses attachées, ou avec des sommets divisés et des normales lorsqu'un angle de pli est défini. | MESH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshSmoothNormals/fr.md)

---
**Source fingerprint (SHA-256):** `bbe9c0fba68369d8e9d3fb68e635869233804f3aac458e7c217d94977e77b9be`
