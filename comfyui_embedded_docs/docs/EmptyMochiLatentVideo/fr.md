# EmptyMochiLatentVideo

Le nœud EmptyMochiLatentVideo crée un tenseur vidéo latent vide avec des dimensions spécifiées. Il génère une représentation latente remplie de zéros qui peut être utilisée comme point de départ pour des flux de travail de génération vidéo. Le nœud permet de définir la largeur, la hauteur, la longueur et la taille du lot pour le tenseur vidéo latent.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `width` | La largeur de la vidéo latente en pixels (défaut : 848, doit être divisible par 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `height` | La hauteur de la vidéo latente en pixels (défaut : 480, doit être divisible par 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `length` | Le nombre d'images dans la vidéo latente (défaut : 25, doit satisfaire la condition que `(length - 1)` soit divisible par 6) | INT | Oui | 7 à MAX_RESOLUTION |
| `batch_size` | Le nombre de vidéos latentes à générer par lot (défaut : 1) | INT | Non | 1 à 4096 |

**Remarque :** Le nœud compresse les dimensions spatiales et temporelles de l'entrée. La largeur et la hauteur latentes sont calculées comme `width / 8` et `height / 8`, et la dimension temporelle est calculée comme `((length - 1) // 6) + 1`. Le paramètre `length` doit satisfaire la condition que `(length - 1)` soit divisible par 6, ce qui signifie que les valeurs valides sont 7, 13, 19, 25, etc. Le tenseur latent obtenu possède 12 canaux et une forme finale de `(batch_size, 12, ((length - 1) // 6) + 1, height // 8, width // 8)`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `samples` | Un tenseur vidéo latent vide avec les dimensions spécifiées, rempli de zéros | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMochiLatentVideo/fr.md)

---
**Source fingerprint (SHA-256):** `1774e1b54b429a946172ba9f609b433d99c0ca2ced2d9e0e3b0b85c82e5141b2`
