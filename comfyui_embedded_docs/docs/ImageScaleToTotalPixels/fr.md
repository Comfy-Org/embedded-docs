Le nœud ImageScaleToTotalPixels est conçu pour redimensionner les images à un nombre total de pixels spécifié tout en maintenant le rapport d'aspect. Il propose diverses méthodes pour agrandir l'image afin d'atteindre le nombre de pixels souhaité.

## Entrées

| Paramètre       | Data Type | Description                                                                |
|-----------------|-------------|----------------------------------------------------------------------------|
| `image`         | `IMAGE`     | L'image d'entrée à agrandir au nombre total de pixels spécifié.            |
| `upscale_method`| COMBO[STRING] | La méthode utilisée pour agrandir l'image. Elle affecte la qualité et les caractéristiques de l'image agrandie. |
| `megapixels`    | `FLOAT`     | La taille cible de l'image en mégapixels. Cela détermine le nombre total de pixels dans l'image agrandie. |

## Sorties

| Paramètre | Data Type | Description                                                           |
|-----------|-------------|-----------------------------------------------------------------------|
| `image`   | `IMAGE`     | L'image agrandie avec le nombre total de pixels spécifié, tout en maintenant le rapport d'aspect original. |
