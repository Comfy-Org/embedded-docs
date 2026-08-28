# BakeNormalMapFromMesh

Ce nœud génère une carte de normales tangentielles à partir d’un maillage haute résolution sur le layout UV d’un maillage basse résolution, capturant ainsi les détails de surface perdus lors de la décimation. Connectez le maillage basse résolution déplié en UV et le maillage haute résolution dont il provient, et le nœud produit une image prête pour l’entrée `normal_map` du nœud Apply Texture To Mesh.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `low_poly` | Le maillage basse résolution déplié en UV qui reçoit les détails générés. Il doit avoir des UV existants ; le nœud ne déplie jamais le maillage. | MESH | Oui | — |
| `high_poly` | Le maillage haute résolution dont les détails de surface sont transférés dans le layout UV du maillage basse résolution. | MESH | Oui | — |
| `resolution` | Longueur de côté en pixels de la carte de normales carrée en sortie (défaut : 1024). | INT | Oui | 64 à 8192 (pas de 64) |
| `cage_distance` | Bande de recherche de surface, exprimée en fraction de la diagonale de la boîte englobante. Augmentez-la en cas de zones incorrectes ou manquantes après une forte décimation ; diminuez-la si elle capture des éléments à travers les interstices. Défaut : 0.05. | FLOAT | Oui | 0.001 à 0.5 (pas de 0.001) |
| `ignore_backfaces` | Ignore les surfaces haute résolution orientées à l’opposé du texel, afin que les crevasses et les espaces clos ne capturent pas la paroi opposée. Ne désactivez cette option que si l’orientation des faces du maillage haute résolution est incohérente. Défaut : true. | BOOLEAN | Oui | true / false |

Remarque : `low_poly` doit avoir des coordonnées UV. S’il n’en a pas, le nœud lève une erreur car il effectue le transfert sur le layout UV existant et ne déplie pas le maillage. Lorsque `low_poly` est un lot, chaque élément est traité dans l’ordre ; si `high_poly` ne contient qu’un seul élément, celui-ci est réutilisé pour chaque élément du lot. Les maillages vides du lot sont ignorés avec un avertissement et produisent une carte de normales gris moyen uniforme (0,5).

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `normal_map` | La carte de normales tangentielles générée (convention glTF/OpenGL +Y) sous forme d’une image RVB carrée de résolution × résolution avec des valeurs dans [0,1]. Connectez-la à l’entrée `normal_map` du nœud Apply Texture To Mesh. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeNormalMapFromMesh/fr.md)

---
**Source fingerprint (SHA-256):** `29df10014b5998b741d71db21d0c982d7bca85ad966a720063af15062e203322`
