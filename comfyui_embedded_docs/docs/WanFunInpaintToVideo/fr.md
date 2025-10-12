> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/fr.md)

Le nœud WanFunInpaintToVideo crée des séquences vidéo en effectuant un inpainting entre des images de début et de fin. Il utilise des conditionnements positifs et négatifs ainsi que des images de frames optionnelles pour générer des latents vidéo. Le nœud gère la génération vidéo avec des paramètres de dimensions et de longueur configurables.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `positif` | CONDITIONING | Oui | - | Conditionnements positifs pour la génération vidéo |
| `négatif` | CONDITIONING | Oui | - | Conditionnements négatifs à éviter dans la génération vidéo |
| `vae` | VAE | Oui | - | Modèle VAE pour les opérations d'encodage/décodage |
| `largeur` | INT | Oui | 16 à MAX_RESOLUTION | Largeur de la vidéo en pixels (par défaut : 832, pas : 16) |
| `hauteur` | INT | Oui | 16 à MAX_RESOLUTION | Hauteur de la vidéo en pixels (par défaut : 480, pas : 16) |
| `longueur` | INT | Oui | 1 à MAX_RESOLUTION | Nombre de frames dans la séquence vidéo (par défaut : 81, pas : 4) |
| `taille_du_lot` | INT | Oui | 1 à 4096 | Nombre de vidéos à générer en lot (par défaut : 1) |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Non | - | Sortie CLIP vision optionnelle pour un conditionnement supplémentaire |
| `image_de_départ` | IMAGE | Non | - | Image de frame de début optionnelle pour la génération vidéo |
| `image_de_fin` | IMAGE | Non | - | Image de frame de fin optionnelle pour la génération vidéo |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `négatif` | CONDITIONING | Conditionnement positif traité en sortie |
| `latent` | CONDITIONING | Conditionnement négatif traité en sortie |
| `latent` | LATENT | Représentation latente vidéo générée |