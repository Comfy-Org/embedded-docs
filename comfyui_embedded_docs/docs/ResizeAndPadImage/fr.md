Le nœud ResizeAndPadImage redimensionne une image pour qu'elle s'adapte à des dimensions spécifiées tout en conservant son rapport hauteur/largeur d'origine. Il réduit proportionnellement l'image pour qu'elle tienne dans la largeur et la hauteur cibles, puis ajoute un remplissage autour des bords pour combler l'espace restant. La couleur de remplissage et la méthode d'interpolation peuvent être personnalisées pour contrôler l'apparence des zones remplies et la qualité du redimensionnement.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée à redimensionner et à remplir | IMAGE | Oui | - |
| `largeur_cible` | La largeur souhaitée de l'image de sortie (par défaut : 512) | INT | Oui | 1 à MAX_RESOLUTION |
| `hauteur_cible` | La hauteur souhaitée de l'image de sortie (par défaut : 512) | INT | Oui | 1 à MAX_RESOLUTION |
| `couleur_rembourrage` | La couleur à utiliser pour les zones de remplissage autour de l'image redimensionnée (par défaut : "white") | COMBO | Oui | "white"<br>"black" |
| `interpolation` | La méthode d'interpolation utilisée pour redimensionner l'image (par défaut : "area") | COMBO | Oui | "area"<br>"bicubic"<br>"nearest-exact"<br>"bilinear"<br>"lanczos" |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image de sortie redimensionnée et remplie | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeAndPadImage/fr.md)

---
**Source fingerprint (SHA-256):** `01566327d46043d1ff9ce404b4df8f49e853d0b01d07cc189fb843157dac1cac`
