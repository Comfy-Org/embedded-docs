Le nœud Canny est conçu pour la détection des contours dans les images, en utilisant l'algorithme de Canny pour identifier et mettre en évidence les contours. Ce processus implique l'application d'une série de filtres à l'image d'entrée pour détecter les zones de fort gradient, qui correspondent aux contours, améliorant ainsi les détails structurels de l'image.

## Types d'entrée

| Paramètre | Comfy dtype | Description |
| --- | --- | --- |
| `image` | `IMAGE` | L'image d'entrée à traiter pour la détection des contours. Elle est cruciale car elle sert de base pour l'opération de détection des contours. |
| `low_threshold` | `FLOAT` | Le seuil inférieur pour la procédure d'hystérésis dans la détection des contours. Il détermine le gradient d'intensité minimum considéré pour un contour, affectant la sensibilité de la détection des contours. |
| `high_threshold` | `FLOAT` | Le seuil supérieur pour la procédure d'hystérésis dans la détection des contours. Il fixe le gradient d'intensité maximum considéré pour un contour, influençant la sélectivité de la détection des contours. |

## Types de sortie

| Paramètre | Comfy dtype | Description |
| --- | --- | --- |
| `image` | `IMAGE` | La sortie est une image avec des contours mis en évidence, où les contours sont détectés à l'aide de l'algorithme de Canny. Cela améliore les détails structurels de l'image originale. |
