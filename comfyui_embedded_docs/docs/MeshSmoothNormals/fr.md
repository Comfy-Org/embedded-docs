# MeshSmoothNormals

Calcule des normales lisses par sommet pour un maillage et les attache. Les maillages sans normales sont ombrés en facettes (par face) par les visionneuses glTF ; ce nœud les rend lisses. Avec un angle de pli inférieur à 180, les arêtes dont l'angle dièdre dépasse le seuil restent vives ; les sommets sont alors scindés le long de ces arêtes.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `mesh` | Le maillage d'entrée à traiter. | MESH | Oui | - |
| `crease_angle` | Les arêtes dont l'angle dièdre dépasse cette valeur (en degrés) restent vives (les sommets sont scindés). 180 = entièrement lisse ; une valeur plus basse préserve les arêtes vives (p. ex. ~30-60 pour les surfaces dures). Défaut : 180.0. | FLOAT | Oui | 0.0 à 180.0 (step 1.0) |

Lorsque `crease_angle` est supérieur ou égal à 180, la topologie du maillage est inchangée. Lorsque `crease_angle` est inférieur à 180, les sommets sont scindés le long des arêtes vives, ce qui peut augmenter le nombre de sommets.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `mesh` | Le maillage d'entrée avec les données de normales lisses attachées, ou avec les sommets scindés et les normales lorsqu'un angle de pli est défini. | MESH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshSmoothNormals/fr.md)

---
**Source fingerprint (SHA-256):** `bbe9c0fba68369d8e9d3fb68e635869233804f3aac458e7c217d94977e77b9be`
