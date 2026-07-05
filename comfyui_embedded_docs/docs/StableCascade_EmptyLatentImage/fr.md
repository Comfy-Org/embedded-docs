# StableCascade_EmptyLatentImage

Le nœud `StableCascade_EmptyLatentImage` crée des tenseurs latents vides pour les modèles Stable Cascade. Il génère deux représentations latentes distinctes - une pour l'étape C et une autre pour l'étape B - avec des dimensions appropriées basées sur la résolution d'entrée et les paramètres de compression. Ce nœud fournit le point de départ pour le pipeline de génération Stable Cascade.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `largeur` | La largeur de l'image de sortie en pixels (par défaut : 1024, pas : 8) | INT | Oui | 256 à MAX_RESOLUTION |
| `hauteur` | La hauteur de l'image de sortie en pixels (par défaut : 1024, pas : 8) | INT | Oui | 256 à MAX_RESOLUTION |
| `compression` | Le facteur de compression qui détermine les dimensions latentes pour l'étape C (par défaut : 42, pas : 1) | INT | Oui | 4 à 128 |
| `taille_du_lot` | Le nombre d'échantillons latents à générer dans un lot (par défaut : 1) | INT | Non | 1 à 4096 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `stage_b` | Le tenseur latent de l'étape C avec les dimensions [batch_size, 16, hauteur//compression, largeur//compression] | LATENT |
| `stage_b` | Le tenseur latent de l'étape B avec les dimensions [batch_size, 4, hauteur//4, largeur//4] | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_EmptyLatentImage/fr.md)

---
**Source fingerprint (SHA-256):** `ba5347f522b661993e540bc5775737cae88bd5f7a87c1b91715f8c1858e8e81a`
