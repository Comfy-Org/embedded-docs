# EmptyLTXVLatentVideo

Le nœud `EmptyLTXVLatentVideo` crée un tenseur latent vide pour le traitement vidéo. Il génère un point de départ vierge avec la largeur, la hauteur, la longueur et la taille de lot spécifiées, qui peut être utilisé comme entrée pour les flux de travail de génération vidéo. Le nœud produit une représentation latente remplie de zéros dont les dimensions spatiales sont 32 fois plus petites que la largeur et la hauteur configurées, et dont le nombre d'images est compressé par un facteur de 8.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `largeur` | La largeur du tenseur vidéo latent (défaut : 768, pas : 32) | INT | Oui | 64 à MAX_RESOLUTION |
| `hauteur` | La hauteur du tenseur vidéo latent (défaut : 512, pas : 32) | INT | Oui | 64 à MAX_RESOLUTION |
| `longueur` | Le nombre d'images dans la vidéo latente (défaut : 97, pas : 8) | INT | Oui | 1 à MAX_RESOLUTION |
| `taille_du_lot` | Le nombre de vidéos latentes à générer dans un lot (défaut : 1) | INT | Oui | 1 à 4096 |

Remarque : La vidéo latente est compressée par rapport aux dimensions d'entrée : les dimensions spatiales (largeur et hauteur) sont divisées par 32, et le nombre d'images (longueur) est divisé par 8 puis arrondi au nombre entier supérieur. Les valeurs de pas pour la largeur, la hauteur et la longueur aident à maintenir ces divisions uniformes.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `samples` | Le tenseur latent vide généré avec des valeurs nulles dans les dimensions spécifiées, ainsi qu'un rapport de réduction spatiale de 32 | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLTXVLatentVideo/fr.md)

---
**Source fingerprint (SHA-256):** `0b1e57baf9730d852b03b6bccbb8a033e2be9b9cd2420a0aa3638c31f6d3cd26`
