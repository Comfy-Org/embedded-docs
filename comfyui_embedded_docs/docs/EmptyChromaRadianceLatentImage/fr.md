# EmptyChromaRadianceLatentImage

Le nœud `EmptyChromaRadianceLatentImage` crée une image latente vide avec des dimensions spécifiées pour une utilisation dans les workflows de radiance chromatique. Il génère un tenseur rempli de zéros (contenant 3 canaux de couleur) qui sert de point de départ pour les opérations dans l'espace latent. Ce nœud vous permet de définir la largeur, la hauteur et la taille du lot de l'image latente vide.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `width` | La largeur de l'image latente en pixels (par défaut : 1024, doit être divisible par 16) | INT | Oui | 16 to MAX_RESOLUTION |
| `height` | La hauteur de l'image latente en pixels (par défaut : 1024, doit être divisible par 16) | INT | Oui | 16 to MAX_RESOLUTION |
| `batch_size` | Le nombre d'images latentes à générer dans un lot (par défaut : 1) | INT | Non | 1 to 4096 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `samples` | Le tenseur d'image latente vide généré avec les dimensions spécifiées, rempli de zéros | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyChromaRadianceLatentImage/fr.md)

---
**Source fingerprint (SHA-256):** `870cc89fb021c258c214db153cda0a32a63da1b6bf92f09cbd3b8498c363096b`
