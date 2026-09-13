# Lisser les normales du maillage

Calcule des normales lisses par sommet pour un maillage et les attache. Les maillages sans normales sont ombrés à plat (par face) par les visualiseurs glTF ; ce nœud leur permet d'être ombrés de façon lisse. Avec un angle de pli inférieur à 180, les arêtes plus vives que le seuil sont conservées dures en divisant les sommets le long de celles-ci.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `mesh` | Le maillage d'entrée à traiter. | MESH | Oui | - |
| `crease_angle` | Les arêtes dont l'angle dièdre dépasse cette valeur (en degrés) restent dures (les sommets sont divisés). 180 = entièrement lisse ; une valeur inférieure préserve les arêtes vives (par ex. ~30-60 pour les surfaces dures). Valeur par défaut : 180.0. | FLOAT | Oui | 0.0 à 180.0 (pas 1.0) |

Lorsque `crease_angle` vaut 180 ou plus, la topologie du maillage reste inchangée. Lorsqu'il est défini en dessous de 180, les sommets sont divisés le long des arêtes dures, ce qui peut augmenter le nombre de sommets. Lorsque les sommets sont divisés, les données par sommet (couleurs, UVs et tangentes) sont dupliquées pour correspondre à la nouvelle disposition des sommets, et le maillage résultant est reconstruit sous forme de lot de taille variable.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------------|
| `mesh` | Le maillage d'entrée avec des données de normales lisses attachées, ou avec des sommets et des normales divisés lorsqu'un angle de pli est défini. | MESH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshSmoothNormals/fr.md)

---
**Source fingerprint (SHA-256):** `bbe9c0fba68369d8e9d3fb68e635869233804f3aac458e7c217d94977e77b9be`
