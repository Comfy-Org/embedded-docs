# WanFunInpaintToVideo

Voici la traduction en français de la documentation du nœud WanFunInpaintToVideo :

Le nœud WanFunInpaintToVideo crée des séquences vidéo en effectuant de l'infilling entre des images de début et de fin. Il prend en entrée un conditionnement positif et négatif ainsi que des images d'image facultatives pour générer des latents vidéo. Le nœud gère la génération vidéo avec des paramètres de dimensions et de longueur configurables.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | Prompts de conditionnement positif pour la génération vidéo | CONDITIONING | Oui | - |
| `négatif` | Prompts de conditionnement négatif à éviter dans la génération vidéo | CONDITIONING | Oui | - |
| `vae` | Modèle VAE pour les opérations d'encodage/décodage | VAE | Oui | - |
| `largeur` | Largeur de la vidéo de sortie en pixels (par défaut : 832, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | Hauteur de la vidéo de sortie en pixels (par défaut : 480, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `longueur` | Nombre d'images dans la séquence vidéo (par défaut : 81, pas : 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `taille_du_lot` | Nombre de vidéos à générer par lot (par défaut : 1) | INT | Oui | 1 à 4096 |
| `clip_vision_output` | Sortie de vision CLIP facultative pour un conditionnement supplémentaire | CLIP_VISION_OUTPUT | Non | - |
| `image_de_départ` | Image de début facultative pour la génération vidéo | IMAGE | Non | - |
| `image_de_fin` | Image de fin facultative pour la génération vidéo | IMAGE | Non | - |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `négatif` | Sortie de conditionnement positif traitée | CONDITIONING |
| `latent` | Sortie de conditionnement négatif traitée | CONDITIONING |
| `latent` | Représentation latente vidéo générée | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `bbc5c2614f5fc21877345b3f01686ea57bee5108cdb253fb5dbf4b2cce9e59dd`
