> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeAndPadImage/fr.md)

Le nœud ResizeAndPadImage redimensionne une image pour qu'elle s'adapte aux dimensions spécifiées tout en conservant son rapport d'aspect d'origine. Il réduit proportionnellement l'image pour qu'elle tienne dans la largeur et la hauteur cibles, puis ajoute un remplissage autour des bords pour combler l'espace restant. La couleur de remplissage et la méthode d'interpolation peuvent être personnalisées pour contrôler l'apparence des zones remplies et la qualité du redimensionnement.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée à redimensionner et à remplir |
| `target_width` | INT | Oui | 1 à MAX_RESOLUTION | La largeur souhaitée de l'image de sortie (par défaut : 512) |
| `target_height` | INT | Oui | 1 à MAX_RESOLUTION | La hauteur souhaitée de l'image de sortie (par défaut : 512) |
| `padding_color` | COMBO | Oui | "white"<br>"black" | La couleur à utiliser pour les zones de remplissage autour de l'image redimensionnée |
| `interpolation` | COMBO | Oui | "area"<br>"bicubic"<br>"nearest-exact"<br>"bilinear"<br>"lanczos" | La méthode d'interpolation utilisée pour redimensionner l'image |

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | L'image de sortie redimensionnée et remplie |
