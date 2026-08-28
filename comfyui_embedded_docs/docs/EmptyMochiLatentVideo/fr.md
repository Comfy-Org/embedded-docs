# EmptyMochiLatentVideo

EmptyMochiLatentVideo crée un tenseur de vidéo latente vide avec les dimensions que vous spécifiez. Il génère une représentation latente remplie de zéros qui peut être utilisée comme point de départ pour les flux de travail de génération vidéo. Le nœud vous permet de définir la largeur, la hauteur, la longueur et la taille du lot du tenseur de vidéo latente.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `largeur` | La largeur de la vidéo latente en pixels (par défaut : 848, doit être divisible par 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | La hauteur de la vidéo latente en pixels (par défaut : 480, doit être divisible par 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `longueur` | Le nombre d'images dans la vidéo latente (par défaut : 25, doit satisfaire que `(length - 1)` soit divisible par 6) | INT | Oui | 7 à MAX_RESOLUTION |
| `taille_du_lot` | Le nombre de vidéos latentes à générer dans un lot (par défaut : 1) | INT | Non | 1 à 4096 |

**Remarque :** Les dimensions latentes réelles sont calculées comme width/8 et height/8, la dimension temporelle est calculée comme `((length - 1) // 6) + 1`, et le tenseur possède 12 canaux. Le paramètre `length` doit satisfaire que `(length - 1)` soit divisible par 6, ce qui signifie que les valeurs valides sont 7, 13, 19, 25, etc.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `samples` | Un tenseur de vidéo latente vide avec les dimensions spécifiées, contenant uniquement des zéros | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMochiLatentVideo/fr.md)

---
**Source fingerprint (SHA-256):** `1774e1b54b429a946172ba9f609b433d99c0ca2ced2d9e0e3b0b85c82e5141b2`
