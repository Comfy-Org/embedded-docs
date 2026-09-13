# EmptyMochiLatentVideo

EmptyMochiLatentVideo crée un tenseur vidéo latent vide avec les dimensions que vous spécifiez. Il génère une représentation latente remplie de zéros qui peut servir de point de départ aux workflows de génération vidéo. Le nœud vous permet de définir la largeur, la hauteur, la longueur et la taille de lot du tenseur vidéo latent.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `largeur` | La largeur de la vidéo latente en pixels (valeur par défaut : 848, les valeurs augmentent par pas de 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | La hauteur de la vidéo latente en pixels (valeur par défaut : 480, les valeurs augmentent par pas de 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `longueur` | Le nombre d’images dans la vidéo latente (valeur par défaut : 25, les valeurs augmentent par pas de 6, à partir de 7) | INT | Oui | 7 à MAX_RESOLUTION |
| `taille_du_lot` | Le nombre de vidéos latentes à générer dans un lot (valeur par défaut : 1) | INT | Non | 1 à 4096 |

**Note :** Les dimensions latentes réelles sont calculées comme width/8 et height/8, la dimension temporelle est calculée comme `((length - 1) // 6) + 1`, et le tenseur comporte 12 canaux. Comme `length` avance par pas de 6 à partir de 7, les valeurs valides sont 7, 13, 19, 25, etc.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `samples` | Un tenseur vidéo latent vide avec les dimensions spécifiées, contenant uniquement des zéros | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMochiLatentVideo/fr.md)

---
**Source fingerprint (SHA-256):** `1774e1b54b429a946172ba9f609b433d99c0ca2ced2d9e0e3b0b85c82e5141b2`
