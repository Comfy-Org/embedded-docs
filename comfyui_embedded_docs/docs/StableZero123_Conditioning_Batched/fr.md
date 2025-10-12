> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning_Batched/fr.md)

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `clip_vision` | CLIP_VISION | Oui | - | Le modèle CLIP vision utilisé pour encoder l'image d'entrée |
| `init_image` | IMAGE | Oui | - | L'image d'entrée initiale à traiter et encoder |
| `vae` | VAE | Oui | - | Le modèle VAE utilisé pour encoder les pixels de l'image dans l'espace latent |
| `width` | INT | Non | 16 à MAX_RESOLUTION | La largeur de sortie pour l'image traitée (par défaut : 256, doit être divisible par 8) |
| `height` | INT | Non | 16 à MAX_RESOLUTION | La hauteur de sortie pour l'image traitée (par défaut : 256, doit être divisible par 8) |
| `batch_size` | INT | Non | 1 à 4096 | Le nombre d'échantillons de conditionnement à générer dans le lot (par défaut : 1) |
| `elevation` | FLOAT | Non | -180.0 à 180.0 | L'angle d'élévation initial de la caméra en degrés (par défaut : 0.0) |
| `azimuth` | FLOAT | Non | -180.0 à 180.0 | L'angle d'azimut initial de la caméra en degrés (par défaut : 0.0) |
| `elevation_batch_increment` | FLOAT | Non | -180.0 à 180.0 | L'incrément d'élévation pour chaque élément du lot (par défaut : 0.0) |
| `azimuth_batch_increment` | FLOAT | Non | -180.0 à 180.0 | L'incrément d'azimut pour chaque élément du lot (par défaut : 0.0) |

**Note :** Les paramètres `width` et `height` doivent être divisibles par 8 car le nœud divise ces dimensions par 8 en interne pour la génération de l'espace latent.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Les données de conditionnement positives contenant les embeddings d'image et les paramètres de caméra |
| `negative` | CONDITIONING | Les données de conditionnement négatives avec des embeddings initialisés à zéro |
| `latent` | LATENT | La représentation latente de l'image traitée avec les informations d'indexation du lot |