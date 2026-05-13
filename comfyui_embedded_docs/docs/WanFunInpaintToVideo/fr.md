> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/fr.md)

Voici la traduction en français de la documentation du nœud WanFunInpaintToVideo :

Le nœud WanFunInpaintToVideo crée des séquences vidéo en effectuant de l'infilling entre des images de début et de fin. Il prend en entrée un conditionnement positif et négatif ainsi que des images d'image facultatives pour générer des latents vidéo. Le nœud gère la génération vidéo avec des paramètres de dimensions et de longueur configurables.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `positif` | CONDITIONING | Oui | - | Prompts de conditionnement positif pour la génération vidéo |
| `négatif` | CONDITIONING | Oui | - | Prompts de conditionnement négatif à éviter dans la génération vidéo |
| `vae` | VAE | Oui | - | Modèle VAE pour les opérations d'encodage/décodage |
| `largeur` | INT | Oui | 16 à MAX_RESOLUTION | Largeur de la vidéo de sortie en pixels (par défaut : 832, pas : 16) |
| `hauteur` | INT | Oui | 16 à MAX_RESOLUTION | Hauteur de la vidéo de sortie en pixels (par défaut : 480, pas : 16) |
| `longueur` | INT | Oui | 1 à MAX_RESOLUTION | Nombre d'images dans la séquence vidéo (par défaut : 81, pas : 4) |
| `taille_du_lot` | INT | Oui | 1 à 4096 | Nombre de vidéos à générer par lot (par défaut : 1) |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Non | - | Sortie de vision CLIP facultative pour un conditionnement supplémentaire |
| `image_de_départ` | IMAGE | Non | - | Image de début facultative pour la génération vidéo |
| `image_de_fin` | IMAGE | Non | - | Image de fin facultative pour la génération vidéo |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `négatif` | CONDITIONING | Sortie de conditionnement positif traitée |
| `latent` | CONDITIONING | Sortie de conditionnement négatif traitée |
| `latent` | LATENT | Représentation latente vidéo générée |

---
**Source fingerprint (SHA-256):** `bbc5c2614f5fc21877345b3f01686ea57bee5108cdb253fb5dbf4b2cce9e59dd`
