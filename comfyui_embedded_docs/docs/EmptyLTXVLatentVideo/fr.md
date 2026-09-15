# EmptyLTXVLatentVideo

Le nœud EmptyLTXVLatentVideo crée un tenseur latent vidéo vide (rempli de zéros) en utilisant les paramètres `width`, `height`, `length` et `batch_size` que vous spécifiez. Il fournit un point de départ vierge pour les flux de travail de génération vidéo LTXV, avec des dimensions latentes automatiquement compressées par rapport à la taille vidéo demandée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `largeur` | La largeur du tenseur latent vidéo (par défaut : 768, pas : 32) | INT | Oui | 64 à MAX_RESOLUTION |
| `hauteur` | La hauteur du tenseur latent vidéo (par défaut : 512, pas : 32) | INT | Oui | 64 à MAX_RESOLUTION |
| `longueur` | Le nombre d'images dans la vidéo latente (par défaut : 97, pas : 8) | INT | Oui | 1 à MAX_RESOLUTION |
| `taille_du_lot` | Le nombre de vidéos latentes à générer dans un lot (par défaut : 1) | INT | Oui | 1 à 4096 |

Remarque : la vidéo latente est compressée par rapport aux dimensions demandées : les dimensions spatiales (`width` et `height`) sont divisées par 32, et le nombre d'images (`length`) est divisé par 8 puis arrondi à l'entier supérieur. Les valeurs de pas pour `width`, `height` et `length` aident à conserver ces divisions entières.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `samples` | Le tenseur latent vide généré, avec des valeurs nulles dans les dimensions spécifiées, accompagné d'un ratio de réduction spatiale de 32 | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLTXVLatentVideo/fr.md)

---
**Source fingerprint (SHA-256):** `0b1e57baf9730d852b03b6bccbb8a033e2be9b9cd2420a0aa3638c31f6d3cd26`
