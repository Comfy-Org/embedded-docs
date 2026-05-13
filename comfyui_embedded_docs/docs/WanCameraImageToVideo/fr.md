> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/fr.md)

Le nœud WanCameraImageToVideo convertit des images en séquences vidéo en générant des représentations latentes pour la génération vidéo. Il traite les entrées de conditionnement et les images de départ optionnelles pour créer des latents vidéo utilisables avec des modèles vidéo. Le nœud prend en charge les conditions de caméra et les sorties CLIP vision pour un contrôle amélioré de la génération vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `positif` | CONDITIONING | Oui | - | Prompts de conditionnement positifs pour la génération vidéo |
| `négatif` | CONDITIONING | Oui | - | Prompts de conditionnement négatifs à éviter dans la génération vidéo |
| `vae` | VAE | Oui | - | Modèle VAE pour encoder les images dans l'espace latent |
| `largeur` | INT | Oui | 16 à MAX_RESOLUTION | Largeur de la vidéo de sortie en pixels (par défaut : 832, pas : 16) |
| `hauteur` | INT | Oui | 16 à MAX_RESOLUTION | Hauteur de la vidéo de sortie en pixels (par défaut : 480, pas : 16) |
| `longueur` | INT | Oui | 1 à MAX_RESOLUTION | Nombre d'images dans la séquence vidéo (par défaut : 81, pas : 4) |
| `taille du lot` | INT | Oui | 1 à 4096 | Nombre de vidéos à générer simultanément (par défaut : 1) |
| `sortie de vision de clip` | CLIP_VISION_OUTPUT | Non | - | Sortie CLIP vision optionnelle pour un conditionnement supplémentaire |
| `image de départ` | IMAGE | Non | - | Image de départ optionnelle pour initialiser la séquence vidéo. Lorsqu'elle est fournie, les premières images de la vidéo seront basées sur cette image, avec un masque appliqué pour fusionner les images de départ avec le contenu généré. L'image est redimensionnée pour correspondre à la largeur et à la hauteur spécifiées. |
| `conditions de caméra` | WAN_CAMERA_EMBEDDING | Non | - | Conditions d'encastrement de caméra optionnelles pour la génération vidéo. Lorsqu'elles sont fournies, ces conditions sont appliquées au conditionnement positif et négatif. |

**Remarque :** Lorsque `start_image` est fourni, le nœud l'utilise pour initialiser la séquence vidéo et applique un masquage pour fusionner les images de départ avec le contenu généré. Les paramètres `camera_conditions` et `clip_vision_output` sont optionnels, mais lorsqu'ils sont fournis, ils modifient le conditionnement pour les prompts positifs et négatifs.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `négatif` | CONDITIONING | Conditionnement positif modifié avec les conditions de caméra et les sorties CLIP vision appliquées |
| `latent` | CONDITIONING | Conditionnement négatif modifié avec les conditions de caméra et les sorties CLIP vision appliquées |
| `latent` | LATENT | Représentation latente vidéo générée pour utilisation avec des modèles vidéo. Le tenseur latent a des dimensions [batch_size, 16, images, hauteur/8, largeur/8] où images est calculé comme ((longueur - 1) // 4) + 1. |

---
**Source fingerprint (SHA-256):** `19d76097d580b14663afd0aab58810f9dc1685cd32e8f67aa43c820be65239e7`
