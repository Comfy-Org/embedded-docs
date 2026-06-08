Le nœud de recadrage d'image extrait une section rectangulaire d'une image d'entrée. Vous définissez la région à conserver en spécifiant les coordonnées de son coin supérieur gauche ainsi que sa largeur et sa hauteur. Le nœud renvoie ensuite la partie recadrée de l'image d'origine.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée à recadrer. | IMAGE | Oui | N/A |
| `crop_region` | Définit la zone rectangulaire à extraire de l'image. Elle est spécifiée par `x` (départ horizontal), `y` (départ vertical), `width` (largeur) et `height` (hauteur). Si la région définie dépasse les bords de l'image, elle sera automatiquement ajustée pour s'adapter aux dimensions de l'image. | BOUNDINGBOX | Oui | N/A |

**Remarque sur les contraintes de région :** La région de recadrage est automatiquement limitée pour rester dans les limites de l'image d'entrée. Si la coordonnée `x` ou `y` spécifiée est supérieure à la largeur ou à la hauteur de l'image, elle sera définie à la position valide maximale. La largeur et la hauteur du recadrage résultant seront ajustées pour que la région ne dépasse pas les bords de l'image.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `image` | La section recadrée de l'image d'entrée d'origine. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCropV2/fr.md)

---
**Source fingerprint (SHA-256):** `9d3543aa8396ae2ab0353accc3c89ae6be6495f6fdcefbb5439fa865a5d3059f`
