Le nœud WanCameraImageToVideo convertit des images en séquences vidéo en générant des représentations latentes pour la génération vidéo. Il traite les entrées de conditionnement et les images de départ optionnelles pour créer des latents vidéo utilisables avec des modèles vidéo. Le nœud prend en charge les conditions de caméra et les sorties CLIP vision pour un contrôle amélioré de la génération vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | Prompts de conditionnement positifs pour la génération vidéo | CONDITIONING | Oui | - |
| `négatif` | Prompts de conditionnement négatifs à éviter dans la génération vidéo | CONDITIONING | Oui | - |
| `vae` | Modèle VAE pour encoder les images dans l'espace latent | VAE | Oui | - |
| `largeur` | Largeur de la vidéo de sortie en pixels (par défaut : 832, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | Hauteur de la vidéo de sortie en pixels (par défaut : 480, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `longueur` | Nombre d'images dans la séquence vidéo (par défaut : 81, pas : 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `taille du lot` | Nombre de vidéos à générer simultanément (par défaut : 1) | INT | Oui | 1 à 4096 |
| `sortie de vision de clip` | Sortie CLIP vision optionnelle pour un conditionnement supplémentaire | CLIP_VISION_OUTPUT | Non | - |
| `image de départ` | Image de départ optionnelle pour initialiser la séquence vidéo. Lorsqu'elle est fournie, les premières images de la vidéo seront basées sur cette image, avec un masque appliqué pour fusionner les images de départ avec le contenu généré. L'image est redimensionnée pour correspondre à la largeur et à la hauteur spécifiées. | IMAGE | Non | - |
| `conditions de caméra` | Conditions d'encastrement de caméra optionnelles pour la génération vidéo. Lorsqu'elles sont fournies, ces conditions sont appliquées au conditionnement positif et négatif. | WAN_CAMERA_EMBEDDING | Non | - |

**Remarque :** Lorsque `start_image` est fourni, le nœud l'utilise pour initialiser la séquence vidéo et applique un masquage pour fusionner les images de départ avec le contenu généré. Les paramètres `camera_conditions` et `clip_vision_output` sont optionnels, mais lorsqu'ils sont fournis, ils modifient le conditionnement pour les prompts positifs et négatifs.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `négatif` | Conditionnement positif modifié avec les conditions de caméra et les sorties CLIP vision appliquées | CONDITIONING |
| `latent` | Conditionnement négatif modifié avec les conditions de caméra et les sorties CLIP vision appliquées | CONDITIONING |
| `latent` | Représentation latente vidéo générée pour utilisation avec des modèles vidéo. Le tenseur latent a des dimensions [batch_size, 16, images, hauteur/8, largeur/8] où images est calculé comme ((longueur - 1) // 4) + 1. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `19d76097d580b14663afd0aab58810f9dc1685cd32e8f67aa43c820be65239e7`
