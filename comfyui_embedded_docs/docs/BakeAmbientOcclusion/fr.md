# Pré-calculer l’occlusion ambiante

Calcule une carte d'occlusion ambiante à partir d'un maillage high-poly dans la disposition UV d'un maillage low-poly. La sortie est une image en niveaux de gris dans laquelle les texels blancs correspondent aux zones dégagées et les texels sombres aux creux ; elle est destinée à l'entrée occlusion du nœud Apply Texture To Mesh. Connectez le maillage low-poly déplié en UV et le maillage high-poly à partir duquel il a été décimé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `low_poly` | Le maillage low-poly déplié en UV dans lequel effectuer le baking. Doit avoir des UV ; le nœud lève une erreur si elles sont manquantes. | MESH | Oui | - |
| `high_poly` | Le maillage high-poly à partir duquel le low-poly a été décimé, utilisé comme géométrie source pour l'occlusion. | MESH | Oui | - |
| `resolution` | Résolution de la texture en pixels ; chaque texel reçoit une valeur d'occlusion. Par défaut : 1024. | INT | Oui | 64 à 8192 (pas 64) |
| `samples` | Rayons par texel. Plus il y en a = plus lisse, plus lent. Augmentez si l'image est granuleuse. Par défaut : 64. | INT | Oui | 4 à 1024 (pas 4) |
| `max_distance` | Longueur des rayons, en fraction de la diagonale de la boîte englobante. Plus petit = occlusion plus serrée et plus locale. Par défaut : 0,5. | FLOAT | Oui | 0,01 à 2,0 (pas 0,01) |
| `strength` | Met à l'échelle l'occlusion. >1 assombrit, <1 éclaircit. Par défaut : 1,0. | FLOAT | Oui | 0,0 à 2,0 (pas 0,05) |
| `bias` | Élévation de l'origine des rayons au-dessus de la surface, en fraction de la diagonale de la boîte englobante. Augmentez si même des surfaces planes montrent des taches/trous sombres. Par défaut : 0,01. | FLOAT | Oui | 0,0001 à 0,2 (pas 0,0005) |

Remarque : `low_poly` doit avoir des coordonnées UV — ce nœud ne déplie jamais le maillage. Si `high_poly` ne contient qu'un seul élément de lot, il est réutilisé pour chaque élément de lot de `low_poly` ; les éléments de lot de `low_poly` sans faces sont ignorés et remplacés par une image entièrement blanche, avec un avertissement journalisé. Si les UV de `low_poly` dépassent la plage 0-1, elles sont uniformément réajustées à l'intérieur de celle-ci, et un avertissement est journalisé lorsqu'une disposition de type tuilé/UDIM est détectée.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `occlusion` | Image d'occlusion ambiante en niveaux de gris avec des valeurs dans [0,1] (blanc = zones dégagées, sombre = creux), une image par élément de lot de `low_poly`. Destinée à l'entrée occlusion du nœud Apply Texture To Mesh (empaquetée dans la carte ORM / occlusionTexture). | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeAmbientOcclusion/fr.md)

---
**Source fingerprint (SHA-256):** `63ea6ce5289728d351fdd7d722e9a299ebb1283e1128262a817466ec6d23786a`
