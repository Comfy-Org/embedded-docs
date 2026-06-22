# Redimensionner l'image en fonction du nombre total de pixels

Le nœud ImageScaleToTotalPixels est conçu pour redimensionner des images à un nombre total de pixels spécifié tout en conservant le rapport hauteur/largeur. Il propose différentes méthodes de suréchantillonnage pour atteindre le nombre de pixels souhaité.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `image` | L'image d'entrée à suréchantillonner au nombre total de pixels spécifié. | `IMAGE` |
| `méthode_d'agrandissement` | La méthode utilisée pour le suréchantillonnage de l'image. Elle affecte la qualité et les caractéristiques de l'image suréchantillonnée. | COMBO[STRING] |
| `mégapixels` | La taille cible de l'image en mégapixels. Cela détermine le nombre total de pixels dans l'image suréchantillonnée. | `FLOAT` |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `image` | L'image suréchantillonnée avec le nombre total de pixels spécifié, en conservant le rapport hauteur/largeur d'origine. | `IMAGE` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleToTotalPixels/fr.md)
