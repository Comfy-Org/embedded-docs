# WanSCAILToVideo

Le nœud WanSCAILToVideo prépare le conditionnement et un espace latent vide pour la génération vidéo. Il traite les entrées optionnelles comme les images de référence, les vidéos de pose et les sorties CLIP vision, en les intégrant dans le conditionnement positif et négatif pour un modèle vidéo. Le nœud produit le conditionnement modifié ainsi qu'un tenseur latent vierge aux dimensions vidéo spécifiées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | L'entrée de conditionnement positive. | CONDITIONING | Oui | - |
| `négatif` | L'entrée de conditionnement négative. | CONDITIONING | Oui | - |
| `vae` | Le modèle VAE utilisé pour encoder les images et les trames vidéo. | VAE | Oui | - |
| `largeur` | La largeur de la vidéo de sortie en pixels (par défaut : 512). Doit être divisible par 8. | INT | Oui | 32 à MAX_RESOLUTION |
| `hauteur` | La hauteur de la vidéo de sortie en pixels (par défaut : 896). Doit être divisible par 8. | INT | Oui | 32 à MAX_RESOLUTION |
| `longueur` | Le nombre de trames dans la vidéo (par défaut : 81). Doit être divisible par 4. | INT | Oui | 1 à MAX_RESOLUTION |
| `taille_du_lot` | Le nombre de vidéos à générer par lot (par défaut : 1). | INT | Oui | 1 à 4096 |
| `clip_vision_output` | Sortie CLIP vision optionnelle pour le conditionnement. | CLIP_VISION_OUTPUT | Non | - |
| `image_de_référence` | Image de référence optionnelle pour le conditionnement. | IMAGE | Non | - |
| `vidéo_de_pose` | Vidéo utilisée pour le conditionnement de pose. Sera réduite à la moitié de la résolution de la vidéo principale. | IMAGE | Non | - |
| `force_de_pose` | Force du latent de pose (par défaut : 1,0). | FLOAT | Oui | 0,0 à 10,0 |
| `début_de_pose` | Étape de début pour utiliser le conditionnement de pose (par défaut : 0,0). | FLOAT | Oui | 0,0 à 1,0 |
| `fin_de_pose` | Étape de fin pour utiliser le conditionnement de pose (par défaut : 1,0). | FLOAT | Oui | 0,0 à 1,0 |

**Remarque :** L'entrée `pose_video` n'est traitée que pour les premières trames `length`. L'image `reference_image` n'est traitée que pour la première image du lot. Lorsque `reference_image` est fournie, un latent rempli de zéros de la même taille est utilisé pour le conditionnement négatif. Lorsque `clip_vision_output` est fourni, il est appliqué à la fois au conditionnement positif et négatif.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `négatif` | Le conditionnement positif modifié, contenant potentiellement des latents d'image de référence intégrés, une sortie CLIP vision ou des latents de vidéo de pose. | CONDITIONING |
| `latent` | Le conditionnement négatif modifié, contenant potentiellement des latents d'image de référence intégrés, une sortie CLIP vision ou des latents de vidéo de pose. | CONDITIONING |
| `video_frame_offset` | Un tenseur latent vide de forme `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]`. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSCAILToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `63de4b6fe41fc23ea81c21965a2dbfc82120bb1bad6785b2130af824e015fbcb`
