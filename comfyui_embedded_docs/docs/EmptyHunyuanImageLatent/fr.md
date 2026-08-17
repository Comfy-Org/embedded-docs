# EmptyHunyuanImageLatent

Le nœud EmptyHunyuanImageLatent crée un tenseur latent vide avec des dimensions spécifiques pour une utilisation avec les modèles de génération d'images Hunyuan. Il génère un point de départ vide qui peut être traité par les nœuds suivants du flux de travail. Ce nœud vous permet de spécifier la largeur, la hauteur et la taille du lot de l'espace latent.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `width` | La largeur de l'image latente générée en pixels (par défaut : 2048, pas : 32) | INT | Oui | de 64 à MAX_RESOLUTION |
| `height` | La hauteur de l'image latente générée en pixels (par défaut : 2048, pas : 32) | INT | Oui | de 64 à MAX_RESOLUTION |
| `batch_size` | Le nombre d'échantillons latents à générer dans un lot (par défaut : 1) | INT | Oui | de 1 à 4096 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `LATENT` | Un tenseur latent vide avec les dimensions spécifiées pour le traitement d'images Hunyuan. Le tenseur possède 64 canaux et ses dimensions spatiales correspondent à un trente-deuxième (1/32) de la largeur et de la hauteur demandées. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanImageLatent/fr.md)

---
**Source fingerprint (SHA-256):** `31fc10d43c224810709870cf40256b6fccd4743445ea9d98d148d443bc591d7a`
