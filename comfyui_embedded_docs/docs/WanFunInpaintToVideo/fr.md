# WanFunInpaintToVideo

Le nœud WanFunInpaintToVideo crée des séquences vidéo par inpainting entre des images de début et de fin. Il prend en entrée un conditionnement positif et négatif, ainsi que des images facultatives, pour générer des latents vidéo. Le nœud gère la génération vidéo avec des paramètres de dimensions et de longueur configurables.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Prompts de conditionnement positifs pour la génération vidéo | CONDITIONING | Oui | - |
| `negative` | Prompts de conditionnement négatifs à éviter lors de la génération vidéo | CONDITIONING | Oui | - |
| `vae` | Modèle VAE pour les opérations d'encodage/décodage | VAE | Oui | - |
| `width` | Largeur de la vidéo de sortie en pixels (défaut : 832, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `height` | Hauteur de la vidéo de sortie en pixels (défaut : 480, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `length` | Nombre d'images dans la séquence vidéo (défaut : 81, pas : 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `batch_size` | Nombre de vidéos à générer par lot (défaut : 1) | INT | Oui | 1 à 4096 |
| `clip_vision_output` | Sortie de vision CLIP facultative pour un conditionnement supplémentaire | CLIP_VISION_OUTPUT | Non | - |
| `start_image` | Image de début facultative pour la génération vidéo | IMAGE | Non | - |
| `end_image` | Image de fin facultative pour la génération vidéo | IMAGE | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Sortie de conditionnement positive traitée | CONDITIONING |
| `negative` | Sortie de conditionnement négative traitée | CONDITIONING |
| `latent` | Représentation latente vidéo générée | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `70b58e961c5df12f94183245ce320197439b2505b47d0bb3ff643b25c9fe6175`
