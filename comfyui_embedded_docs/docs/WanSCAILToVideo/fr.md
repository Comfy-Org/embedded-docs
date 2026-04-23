> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSCAILToVideo/fr.md)

Le nœud WanSCAILToVideo prépare le conditionnement et un espace latent vide pour la génération vidéo. Il traite des entrées optionnelles telles que les images de référence, les vidéos de pose et les sorties de vision CLIP, en les intégrant dans le conditionnement positif et négatif pour un modèle vidéo. Le nœud produit le conditionnement modifié ainsi qu'un tenseur latent vide aux dimensions vidéo spécifiées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `positive` | CONDITIONING | Oui | - | L'entrée de conditionnement positif. |
| `negative` | CONDITIONING | Oui | - | L'entrée de conditionnement négatif. |
| `vae` | VAE | Oui | - | Le modèle VAE utilisé pour encoder les images et les trames vidéo. |
| `width` | INT | Oui | 32 à MAX_RESOLUTION | La largeur de la vidéo de sortie en pixels (par défaut : 512). Doit être divisible par 8. |
| `height` | INT | Oui | 32 à MAX_RESOLUTION | La hauteur de la vidéo de sortie en pixels (par défaut : 896). Doit être divisible par 8. |
| `length` | INT | Oui | 1 à MAX_RESOLUTION | Le nombre de trames dans la vidéo (par défaut : 81). |
| `batch_size` | INT | Oui | 1 à 4096 | Le nombre de vidéos à générer par lot (par défaut : 1). |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Non | - | Sortie de vision CLIP optionnelle pour le conditionnement. |
| `reference_image` | IMAGE | Non | - | Image de référence optionnelle pour le conditionnement. |
| `pose_video` | IMAGE | Non | - | Vidéo utilisée pour le conditionnement de pose. Seront réduites à la moitié de la résolution de la vidéo principale. |
| `pose_strength` | FLOAT | Oui | 0,0 à 10,0 | Force du latent de pose (par défaut : 1,0). |
| `pose_start` | FLOAT | Oui | 0,0 à 1,0 | Étape de début pour utiliser le conditionnement de pose (par défaut : 0,0). |
| `pose_end` | FLOAT | Oui | 0,0 à 1,0 | Étape de fin pour utiliser le conditionnement de pose (par défaut : 1,0). |

**Remarque :** L'entrée `pose_video` n'est traitée que pour les premières trames `length`. L'entrée `reference_image` n'est traitée que pour la première image du lot.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `positive` | CONDITIONING | Le conditionnement positif modifié, contenant potentiellement des latents d'image de référence intégrés, la sortie de vision CLIP ou les latents de vidéo de pose. |
| `negative` | CONDITIONING | Le conditionnement négatif modifié, contenant potentiellement des latents d'image de référence intégrés, la sortie de vision CLIP ou les latents de vidéo de pose. |
| `latent` | LATENT | Un tenseur latent vide de forme `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]`. |