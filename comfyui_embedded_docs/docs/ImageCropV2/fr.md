> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCropV2/fr.md)

Le nœud Image Crop extrait une section rectangulaire d'une image d'entrée. Vous définissez la région à conserver en spécifiant les coordonnées de son coin supérieur gauche ainsi que sa largeur et sa hauteur. Le nœud renvoie ensuite la partie recadrée de l'image originale.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | N/A | L'image d'entrée à recadrer. |
| `crop_region` | BOUNDINGBOX | Oui | N/A | Définit la zone rectangulaire à extraire de l'image. Elle est spécifiée par `x` (début horizontal), `y` (début vertical), `width` (largeur) et `height` (hauteur). Si la région définie dépasse les bords de l'image, elle sera automatiquement ajustée pour tenir dans les dimensions de l'image. |

**Note sur les contraintes de région :** La région de recadrage est automatiquement contrainte pour rester à l'intérieur des limites de l'image d'entrée. Si la coordonnée `x` ou `y` spécifiée est supérieure à la largeur ou à la hauteur de l'image, elle sera définie sur la position valide maximale. La largeur et la hauteur de recadrage résultantes seront ajustées afin que la région ne dépasse pas les bords de l'image.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | La section recadrée de l'image d'entrée originale. |