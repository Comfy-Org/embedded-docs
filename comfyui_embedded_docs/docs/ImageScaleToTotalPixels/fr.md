> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleToTotalPixels/fr.md)

Le nœud ImageScaleToTotalPixels est conçu pour redimensionner des images à un nombre total de pixels spécifié tout en conservant le rapport hauteur/largeur. Il propose différentes méthodes de suréchantillonnage pour atteindre le nombre de pixels souhaité.

## Entrées

| Paramètre       | Type de données | Description                                                                |
|-----------------|-----------------|----------------------------------------------------------------------------|
| `image`         | `IMAGE`         | L'image d'entrée à suréchantillonner au nombre total de pixels spécifié.   |
| `upscale_method`| COMBO[STRING]   | La méthode utilisée pour le suréchantillonnage de l'image. Elle affecte la qualité et les caractéristiques de l'image suréchantillonnée. |
| `megapixels`    | `FLOAT`         | La taille cible de l'image en mégapixels. Cela détermine le nombre total de pixels dans l'image suréchantillonnée. |

## Sorties

| Paramètre | Type de données | Description                                                           |
|-----------|-----------------|-----------------------------------------------------------------------|
| `image`   | `IMAGE`         | L'image suréchantillonnée avec le nombre total de pixels spécifié, en conservant le rapport hauteur/largeur d'origine. |