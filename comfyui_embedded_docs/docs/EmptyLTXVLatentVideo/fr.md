# EmptyLTXVLatentVideo

Le nœud EmptyLTXVLatentVideo crée un tenseur latent vide pour la génération vidéo. Il produit une représentation latente remplie de zéros avec la largeur, la hauteur, la longueur et la taille de lot spécifiées, prête à être utilisée comme point de départ dans les flux de travail vidéo LTXV. Le latent stocke la vidéo sous une forme compressée : les dimensions spatiales sont divisées par 32 et le nombre d'images est réduit d'un facteur 8.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `width` | La largeur de la vidéo latente en pixels (par défaut : 768, pas : 32) | INT | Oui | 64 à MAX_RESOLUTION |
| `height` | La hauteur de la vidéo latente en pixels (par défaut : 512, pas : 32) | INT | Oui | 64 à MAX_RESOLUTION |
| `length` | Le nombre d'images dans la vidéo latente (par défaut : 97, pas : 8) | INT | Oui | 1 à MAX_RESOLUTION |
| `batch_size` | Le nombre de vidéos latentes à générer dans un lot (par défaut : 1) | INT | Non | 1 à 4096 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `samples` | Le tenseur latent vide généré, rempli de zéros. Le latent porte également une valeur `downscale_ratio_spacial` de 32, qui décrit la réduction spatiale appliquée à la largeur et à la hauteur. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLTXVLatentVideo/fr.md)

---
**Source fingerprint (SHA-256):** `0b1e57baf9730d852b03b6bccbb8a033e2be9b9cd2420a0aa3638c31f6d3cd26`
