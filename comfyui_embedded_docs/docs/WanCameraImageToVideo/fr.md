# Image vers vidéo WanCamera

Le nœud `WanCameraImageToVideo` prépare les données de conditionnement et latentes pour la génération de vidéos à partir d’images. Il prend en entrée des prompts de conditionnement positifs et négatifs, ainsi qu’une image de départ facultative et des contrôles de caméra facultatifs, et produit un conditionnement modifié ainsi qu’un tenseur latent vide prêt à être rempli par un modèle vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | Prompts de conditionnement positifs pour la génération vidéo | CONDITIONING | Oui | - |
| `négatif` | Prompts de conditionnement négatifs à éviter lors de la génération vidéo | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder les images dans l’espace latent | VAE | Oui | - |
| `largeur` | Largeur de la vidéo de sortie en pixels (défaut : 832, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | Hauteur de la vidéo de sortie en pixels (défaut : 480, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `longueur` | Nombre d’images de la séquence vidéo (défaut : 81, pas : 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `taille du lot` | Nombre de vidéos à générer simultanément (défaut : 1) | INT | Oui | 1 à 4096 |
| `sortie de vision de clip` | Sortie CLIP vision facultative pour un conditionnement supplémentaire | CLIP_VISION_OUTPUT | Non | - |
| `image de départ` | Image de départ facultative pour initialiser la séquence vidéo. Lorsqu’elle est fournie, les premières images de la vidéo sont basées sur cette image, avec un masque appliqué pour fusionner les images de départ avec le contenu généré. L’image est redimensionnée pour correspondre à la largeur et à la hauteur spécifiées. | IMAGE | Non | - |
| `conditions de caméra` | Conditions d’embedding caméra facultatives pour la génération vidéo. Lorsqu’elles sont fournies, ces conditions sont appliquées au conditionnement positif et négatif. | WAN_CAMERA_EMBEDDING | Non | - |

**Remarque :** Lorsque `start_image` est fourni, seules les premières `length` images de l’image d’entrée sont utilisées pour initialiser la séquence vidéo, et le nœud applique un masque pour fusionner ces images de départ avec le contenu généré. Les paramètres `camera_conditions` et `clip_vision_output` sont facultatifs, mais lorsqu’ils sont fournis, ils modifient le conditionnement pour les prompts positifs et négatifs.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positif` | Conditionnement positif modifié avec les conditions caméra, sorties CLIP vision et/ou données d’image de départ appliquées | CONDITIONING |
| `négatif` | Conditionnement négatif modifié avec les conditions caméra, sorties CLIP vision et/ou données d’image de départ appliquées | CONDITIONING |
| `latent` | Représentation latente vidéo vide générée pour une utilisation avec les modèles vidéo. Le tenseur latent a pour dimensions [batch_size, 16, frames, height/8, width/8], où frames est calculé comme ((length - 1) // 4) + 1. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `467a82be0dfd6ac1c3b2dd2a6cb02e0d0749de4536a7fbdb000456b817b20ebb`
