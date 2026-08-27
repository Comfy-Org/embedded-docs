# WanFunInpaintToVideo

Le nœud WanFunInpaintToVideo crée des séquences vidéo par inpainting entre des images de début et de fin. Il accepte un conditionnement positif et négatif ainsi que des images de trame optionnelles pour générer des latents vidéo. Le nœud gère la génération vidéo avec des paramètres de dimensions et de longueur configurables.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | Invites de conditionnement positives pour la génération vidéo | CONDITIONING | Oui | - |
| `négatif` | Invites de conditionnement négatives à éviter dans la génération vidéo | CONDITIONING | Oui | - |
| `vae` | Modèle VAE pour les opérations d'encodage/décodage | VAE | Oui | - |
| `largeur` | Largeur de la vidéo de sortie en pixels (par défaut : 832, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | Hauteur de la vidéo de sortie en pixels (par défaut : 480, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `longueur` | Nombre d'images dans la séquence vidéo (par défaut : 81, pas : 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `taille_du_lot` | Nombre de vidéos à générer dans un lot (par défaut : 1) | INT | Oui | 1 à 4096 |
| `clip_vision_output` | Sortie CLIP vision optionnelle utilisée comme conditionnement pour l'image de début | CLIP_VISION_OUTPUT | Non | - |
| `image_de_départ` | Image de trame de départ optionnelle pour la génération vidéo | IMAGE | Non | - |
| `image_de_fin` | Image de trame de fin optionnelle pour la génération vidéo | IMAGE | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positif` | Sortie de conditionnement positive traitée | CONDITIONING |
| `négatif` | Sortie de conditionnement négative traitée | CONDITIONING |
| `latent` | Représentation latente vidéo générée | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `70b58e961c5df12f94183245ce320197439b2505b47d0bb3ff643b25c9fe6175`
