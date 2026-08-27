# StableCascade_EmptyLatentImage

Le nœud StableCascade_EmptyLatentImage crée des tenseurs latents vides pour les modèles Stable Cascade. Il génère deux représentations latentes distinctes — une pour l'étape C et une pour l'étape B — avec des dimensions appropriées basées sur la résolution d'entrée et les paramètres de compression. Ce nœud fournit le point de départ du pipeline de génération Stable Cascade.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `largeur` | La largeur de l'image de sortie en pixels (défaut : 1024, pas : 8) | INT | Oui | 256 à MAX_RESOLUTION |
| `hauteur` | La hauteur de l'image de sortie en pixels (défaut : 1024, pas : 8) | INT | Oui | 256 à MAX_RESOLUTION |
| `compression` | Le facteur de compression qui détermine les dimensions latentes de l'étape C (défaut : 42, pas : 1). Il s'agit d'un paramètre avancé. | INT | Oui | 4 à 128 |
| `taille_du_lot` | Le nombre d'échantillons latents à générer dans un lot (défaut : 1) | INT | Non | 1 à 4096 |

Remarque : La valeur de `compression` contrôle la taille du latent de l'étape C : sa hauteur et sa largeur correspondent à la `height` et à la `width` d'entrée divisées par `compression`. Le latent de l'étape B utilise toujours une compression fixe de 4.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `stage_c` | Le tenseur latent de l'étape C avec les dimensions [batch_size, 16, height//compression, width//compression] | LATENT |
| `stage_b` | Le tenseur latent de l'étape B avec les dimensions [batch_size, 4, height//4, width//4] | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_EmptyLatentImage/fr.md)

---
**Source fingerprint (SHA-256):** `f336f87d0ec14b3716efda2cfaa194b1f80707d64821bb56ade7d88d9bd5b53f`
