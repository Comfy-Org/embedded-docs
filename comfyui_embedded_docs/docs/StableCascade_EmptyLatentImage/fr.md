> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_EmptyLatentImage/fr.md)

Le nœud StableCascade_EmptyLatentImage crée des tenseurs latents vides pour les modèles Stable Cascade. Il génère deux représentations latentes distinctes - une pour l'étape C et une autre pour l'étape B - avec des dimensions appropriées basées sur la résolution d'entrée et les paramètres de compression. Ce nœud fournit le point de départ pour le pipeline de génération Stable Cascade.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `largeur` | INT | Oui | 256 à MAX_RESOLUTION | La largeur de l'image de sortie en pixels (par défaut : 1024, pas : 8) |
| `hauteur` | INT | Oui | 256 à MAX_RESOLUTION | La hauteur de l'image de sortie en pixels (par défaut : 1024, pas : 8) |
| `compression` | INT | Oui | 4 à 128 | Le facteur de compression qui détermine les dimensions latentes pour l'étape C (par défaut : 42, pas : 1) |
| `taille_du_lot` | INT | Non | 1 à 4096 | Le nombre d'échantillons latents à générer dans un lot (par défaut : 1) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `stage_b` | LATENT | Le tenseur latent de l'étape C avec les dimensions [batch_size, 16, height//compression, width//compression] |
| `stage_b` | LATENT | Le tenseur latent de l'étape B avec les dimensions [batch_size, 4, height//4, width//4] |
