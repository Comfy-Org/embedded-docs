> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanImageLatent/fr.md)

Le nœud EmptyHunyuanImageLatent crée un tenseur latent vide avec des dimensions spécifiques pour une utilisation avec les modèles de génération d'images Hunyuan. Il génère un point de départ vierge qui peut être traité par les nœuds suivants dans le flux de travail. Ce nœud permet de spécifier la largeur, la hauteur et la taille du lot de l'espace latent.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | Oui | 64 à MAX_RESOLUTION | La largeur de l'image latente générée en pixels (par défaut : 2048, pas : 32) |
| `height` | INT | Oui | 64 à MAX_RESOLUTION | La hauteur de l'image latente générée en pixels (par défaut : 2048, pas : 32) |
| `batch_size` | INT | Oui | 1 à 4096 | Le nombre d'échantillons latents à générer dans un lot (par défaut : 1) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `LATENT` | LATENT | Un tenseur latent vide avec les dimensions spécifiées pour le traitement d'images Hunyuan |