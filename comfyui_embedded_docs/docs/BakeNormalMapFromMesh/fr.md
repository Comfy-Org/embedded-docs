# BakeNormalMapFromMesh

Ce nœud cuit une carte normale tangentielle à partir d’un maillage haute poly sur la disposition UV d’un maillage basse poly, capturant les détails de surface perdus lors de la décimation. Connectez le maillage basse poly avec UV déroulés et le maillage haute poly dont il est issu, et le nœud génère une image prête pour l’entrée `normal_map` de Apply Texture To Mesh.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `low_poly` | Le maillage basse poly avec UV déroulés qui reçoit le détail cuit. Doit avoir des UV existants ; le nœud ne déroule jamais. | MESH | Oui | — |
| `high_poly` | Le maillage haute poly dont les détails de surface sont cuits dans la disposition UV du basse poly. | MESH | Oui | — |
| `resolution` | Longueur de côté en pixels de la carte normale carrée de sortie (par défaut : 1024). | INT | Oui | 64 à 8192 (pas de 64) |
| `cage_distance` | Bande de recherche de surface, en fraction de la diagonale de la boîte englobante. Augmentez-la pour les zones incorrectes ou manquantes après une décimation importante ; diminuez-la si elle capture à travers les espaces. Par défaut : 0.05. | FLOAT | Oui | 0.001 à 0.5 (pas de 0.001) |
| `ignore_backfaces` | Ignore les surfaces haute poly orientées à l’opposé du texel, afin que les crevasses/espaces fermés ne capturent pas la paroi opposée. Désactivez uniquement si l’orientation des faces du maillage haute poly est incohérente. Par défaut : true. | BOOLEAN | Oui | true / false |

Note : `low_poly` doit avoir des coordonnées UV. S’il n’en a pas, le nœud lève une erreur car il cuit sur la disposition UV existante et ne déroule pas le maillage. Lorsque `low_poly` est un lot, chaque élément est cuit dans l’ordre ; si `high_poly` ne contient qu’un seul élément, cet élément est réutilisé pour chaque élément du lot. Les maillages vides du lot sont ignorés avec un avertissement et produisent une carte normale gris moyen (0.5) uniforme.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `normal_map` | La carte normale tangentielle cuite (convention glTF/OpenGL +Y) sous forme d’image RGB carrée de résolution × résolution avec des valeurs dans [0,1]. Connectez-la à l’entrée `normal_map` de Apply Texture To Mesh. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeNormalMapFromMesh/fr.md)

---
**Source fingerprint (SHA-256):** `29df10014b5998b741d71db21d0c982d7bca85ad966a720063af15062e203322`
