# Pré-calculer une carte de normales depuis le maillage

Ce nœud effectue le bake d'une carte de normales en espace tangent à partir d'un maillage haute résolution vers la disposition UV d'un maillage basse résolution, capturant ainsi les détails de surface perdus lors de la décimation. Connectez le maillage basse résolution déplié en UV et le maillage haute résolution dont il est issu ; le nœud produit ensuite une image prête à être branchée sur l'entrée `normal_map` de Apply Texture To Mesh.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `low_poly` | Le maillage basse résolution déplié en UV qui reçoit les détails issus du bake. Doit posséder des coordonnées UV existantes ; le nœud ne réalise jamais de dépliage UV. | MESH | Oui | — |
| `high_poly` | Le maillage haute résolution dont les détails de surface sont intégrés par bake dans la disposition UV du maillage basse résolution. | MESH | Oui | — |
| `resolution` | Longueur d'arête en pixels de la carte de normales carrée produite en sortie (valeur par défaut : 1024). | INT | Oui | 64 à 8192 (par pas de 64) |
| `cage_distance` | Bande de recherche de surface, exprimée comme une fraction de la diagonale de la boîte englobante. Augmentez-la en cas de zones incorrectes ou manquantes sous forte décimation ; diminuez-la si elle capture des surfaces à travers des interstices. Valeur par défaut : 0.05. | FLOAT | Oui | 0.001 à 0.5 (par pas de 0.001) |
| `ignore_backfaces` | Ignorer les surfaces haute résolution orientées à l'opposé du texel, afin que les crevasses/espaces fermés ne capturent pas la paroi opposée. Désactivez cette option uniquement si l'ordre d'enroulement du maillage haute résolution est incohérent. Valeur par défaut : true. | BOOLEAN | Oui | true / false |

Remarque : `low_poly` doit posséder des coordonnées UV. S'il n'en possède aucune, le nœud lève une erreur, car le bake s'effectue sur la disposition UV existante et le nœud ne déplie pas le maillage. Lorsque `low_poly` est un lot (batch), chaque élément fait l'objet d'un bake dans l'ordre ; si `high_poly` ne contient qu'un seul élément, cet élément est réutilisé pour chaque élément du lot. Les maillages vides du lot sont ignorés avec un avertissement et produisent une carte de normales d'un gris moyen uniforme (0.5). Si les UV du maillage basse résolution dépassent l'intervalle [0,1], elles sont ajustées uniformément dans [0,1] (avec un avertissement lorsque la disposition semble tuilée/UDIM), afin que le bake et Apply Texture To Mesh utilisent les mêmes UV.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `normal_map` | La carte de normales en espace tangent issue du bake (convention glTF/OpenGL +Y) sous forme d'image RGB carrée de résolution × résolution avec des valeurs dans [0,1]. Connectez-la à l'entrée `normal_map` de Apply Texture To Mesh. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeNormalMapFromMesh/fr.md)

---
**Source fingerprint (SHA-256):** `29df10014b5998b741d71db21d0c982d7bca85ad966a720063af15062e203322`
