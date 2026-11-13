# MiniMax H3 Image

Génère des images à partir de texte avec MiniMax H3 Image, ou édite et combine jusqu'à 16 images de référence. Le prompt désigne les images de référence selon leur ordre de connexion : `@Image1`, `@Image2`, etc.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | `MiniMax-H3-Image`, ou `MiniMax-H3-Image-Highspeed` pour des exécutions plus rapides. Par défaut : `"MiniMax-H3-Image"`. | COMBO | Oui | `"MiniMax-H3-Image"`<br>`"MiniMax-H3-Image-Highspeed"` |
| `prompt` | Ce qu'il faut générer, ou comment éditer les images de référence. Lorsque des images de référence sont connectées, il peut contenir au maximum 8 000 caractères. Par défaut : vide. | STRING | Oui | 1 à 8000 caractères |
| `size` | `2K` et `4K` déduisent la taille à partir d'un rapport d'aspect ; `custom` définit une largeur et une hauteur exactes. Par défaut : `"2K"`. | DYNAMIC_COMBO | Oui | `"2K"`<br>`"4K"`<br>`"custom"` |
| `enhance_prompt` | MiniMax réécrit le prompt en une description détaillée de la scène avant la génération. Les éditions d'image sont toujours améliorées. Lorsque cette option est désactivée, choisissez un rapport d'aspect fixe ou une taille personnalisée. Par défaut : true. | BOOLEAN | Non | true<br>false |
| `seed` | Contrôle si le nœud est réexécuté ; les résultats ne sont pas déterministes, quelle que soit la valeur de `seed`. Par défaut : 42. | INT | Non | 0 à 2147483647 |
| `images` | Images de référence à éditer ou à combiner, désignées dans le prompt par `@Image1` à `@Image16` selon leur ordre de connexion. | AUTOGROW | Non | Jusqu'à 16 images |

### Entrées pour la taille "2K" et "4K"

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | Avec `auto`, MiniMax choisit le rapport à partir du prompt, ou suit l'image de référence lorsqu'une est connectée. La génération texte-vers-image avec `enhance_prompt` désactivé nécessite un rapport fixe. Par défaut : `"auto"`. | COMBO | Oui | Plusieurs options disponibles |

### Entrées pour la taille "custom"

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `width` | Largeur de sortie en pixels. Par défaut : 2048. | INT | Oui | 512 à 7680 (pas : 16) |
| `height` | Hauteur de sortie en pixels. Par défaut : 2048. | INT | Oui | 512 à 7680 (pas : 16) |

Remarque : pour une taille personnalisée, le produit de la largeur par la hauteur doit être compris entre 655 360 et 20 000 000 pixels, avec un rapport d'aspect maximal de 3:1.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image générée ou éditée, au format PNG. | IMAGE |
| `revised_prompt` | Le prompt réécrit utilisé par MiniMax, lorsque l'amélioration du prompt était activée. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxH3ImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `723eb4c2d3b303ece041f98bd5b773c669affb9a7b3da0c08ffcac4ee89f8e11`
