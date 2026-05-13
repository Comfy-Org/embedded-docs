> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageSharpen/fr.md)

Le nœud ImageSharpen améliore la netteté d'une image en accentuant ses contours et ses détails. Il applique un filtre de renforcement à l'image, dont l'intensité et le rayon peuvent être ajustés, rendant ainsi l'image plus définie et plus nette.

## Entrées

| Champ           | Type de données | Description                                                                                   |
|-----------------|-----------------|-----------------------------------------------------------------------------------------------|
| `image`         | `IMAGE`         | L'image d'entrée à accentuer. Ce paramètre est crucial car il détermine l'image de base sur laquelle l'effet de renforcement sera appliqué. |
| `rayon_d'affûtage`| `INT`           | Définit le rayon de l'effet de renforcement. Un rayon plus large signifie qu'un plus grand nombre de pixels autour du contour seront affectés, ce qui conduit à un effet de renforcement plus prononcé. |
| `sigma`         | `FLOAT`         | Contrôle l'étalement de l'effet de renforcement. Une valeur sigma plus élevée entraîne une transition plus douce au niveau des contours, tandis qu'une valeur sigma plus faible rend le renforcement plus localisé. |
| `alpha`         | `FLOAT`         | Ajuste l'intensité de l'effet de renforcement. Des valeurs alpha plus élevées produisent un effet de renforcement plus fort. |

## Sorties

| Champ  | Type de données | Description                                                              |
|--------|-----------------|--------------------------------------------------------------------------|
| `image`| `IMAGE`         | L'image accentuée, avec des contours et des détails améliorés, prête pour un traitement ou un affichage ultérieur. |