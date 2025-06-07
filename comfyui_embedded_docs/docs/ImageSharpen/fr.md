Le nœud ImageSharpen améliore la clarté d'une image en accentuant ses contours et ses détails. Il applique un filtre de netteté à l'image, qui peut être ajusté en intensité et en rayon, rendant ainsi l'image plus définie et nette.

## Entrées

| Champ          | Data Type | Description                                                                                   |
|----------------|-------------|-----------------------------------------------------------------------------------------------|
| `image`        | `IMAGE`     | L'image d'entrée à améliorer. Ce paramètre est crucial car il détermine l'image de base sur laquelle l'effet de netteté sera appliqué. |
| `sharpen_radius`| `INT`       | Définit le rayon de l'effet de netteté. Un rayon plus grand signifie que plus de pixels autour du contour seront affectés, entraînant un effet de netteté plus prononcé. |
| `sigma`        | `FLOAT`     | Contrôle l'étendue de l'effet de netteté. Une valeur de sigma plus élevée entraîne une transition plus douce aux contours, tandis qu'une valeur plus basse rend la netteté plus localisée. |
| `alpha`        | `FLOAT`     | Ajuste l'intensité de l'effet de netteté. Des valeurs alpha plus élevées entraînent un effet de netteté plus fort. |

## Sorties

| Champ | Data Type | Description                                                              |
|-------|-------------|--------------------------------------------------------------------------|
| `image`| `IMAGE`     | L'image améliorée, avec des contours et des détails accentués, prête pour un traitement ou un affichage ultérieur. |
