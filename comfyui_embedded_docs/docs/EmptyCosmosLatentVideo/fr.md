# VidéoLatenteCosmosVide

Le nœud EmptyCosmosLatentVideo crée un tenseur vidéo latent vide avec des dimensions spécifiées. Il génère une représentation latente remplie de zéros pouvant être utilisée comme point de départ pour des workflows de génération vidéo, avec des paramètres configurables de largeur, hauteur, longueur et taille de lot. Les dimensions spatiales du latent sont sous-échantillonnées par un facteur 8.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `width` | La largeur de la vidéo latente en pixels (défaut : 1280, doit être divisible par 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `height` | La hauteur de la vidéo latente en pixels (défaut : 704, doit être divisible par 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `length` | Le nombre d’images de la vidéo latente (défaut : 121, doit être divisible par 8) | INT | Oui | 1 à MAX_RESOLUTION |
| `batch_size` | Le nombre de vidéos latentes à générer dans un lot (défaut : 1) | INT | Oui | 1 à 4096 |

Le tenseur latent utilise 16 canaux. Les dimensions spatiales sont divisées par 8 par rapport aux dimensions en pixels (hauteur // 8, largeur // 8), et le nombre d’images est compressé en ((length - 1) // 8) + 1 images latentes.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `samples` | Le tenseur vidéo latent vide généré, avec des valeurs nulles. Forme : (batch_size, 16, ((length - 1) // 8) + 1, hauteur // 8, largeur // 8) | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyCosmosLatentVideo/fr.md)

---
**Source fingerprint (SHA-256):** `7ee194324b02367ed853f6d36bc51742081bac6a9469c4a619586e0560a1b33b`
