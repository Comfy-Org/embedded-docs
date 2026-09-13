# Image vers vidéo WanCamera

Le nœud WanCameraImageToVideo prépare les données de conditionnement et latentes pour la génération vidéo contrôlée par caméra à partir d’images. Il prend des prompts de conditionnement positifs et négatifs, ainsi que des entrées facultatives telles qu’une image de départ, une sortie de vision CLIP et des conditions de caméra, et produit un conditionnement mis à jour ainsi qu’un tenseur latent vide prêt à être rempli par un modèle vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Prompts de conditionnement positifs pour la génération vidéo | CONDITIONING | Oui | - |
| `negative` | Prompts de conditionnement négatifs à éviter dans la génération vidéo | CONDITIONING | Oui | - |
| `vae` | Modèle VAE pour encoder les images dans l’espace latent | VAE | Oui | - |
| `width` | Largeur de la vidéo de sortie en pixels (valeur par défaut : 832, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `height` | Hauteur de la vidéo de sortie en pixels (valeur par défaut : 480, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `length` | Nombre d’images dans la séquence vidéo (valeur par défaut : 81, pas : 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `batch_size` | Nombre de vidéos à générer simultanément (valeur par défaut : 1) | INT | Oui | 1 à 4096 |
| `clip_vision_output` | Sortie de vision CLIP facultative pour un conditionnement supplémentaire | CLIP_VISION_OUTPUT | Non | - |
| `start_image` | Image de départ facultative pour initialiser la séquence vidéo. Lorsqu’elle est fournie, seules les premières `length` images sont utilisées, et l’image est redimensionnée pour correspondre à la `width` et à la `height` spécifiées. Les premières images de la séquence sont encodées dans le latent et un masque est appliqué pour mélanger les images de départ avec le contenu généré. | IMAGE | Non | - |
| `camera_conditions` | Conditions d’embedding de caméra facultatives pour la génération vidéo. Lorsqu’elles sont fournies, ces conditions sont appliquées à la fois au conditionnement positif et négatif. | WAN_CAMERA_EMBEDDING | Non | - |

**Remarque :** Lorsque `start_image` est fournie, le nœud définit les valeurs `concat_latent_image` et `concat_mask` sur les conditionnements `positive` et `negative`. Les paramètres `camera_conditions` et `clip_vision_output` sont facultatifs, mais lorsqu’ils sont fournis, ils modifient le conditionnement à la fois pour les prompts positif et négatif.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif modifié avec application des conditions de caméra, de la sortie de vision CLIP et/ou des données d’image de départ | CONDITIONING |
| `negative` | Conditionnement négatif modifié avec application des conditions de caméra, de la sortie de vision CLIP et/ou des données d’image de départ | CONDITIONING |
| `latent` | Représentation latente vidéo vide à utiliser avec les modèles vidéo. Le tenseur latent a les dimensions [batch_size, 16, frames, height/8, width/8], où frames est calculé comme ((length - 1) // 4) + 1. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `467a82be0dfd6ac1c3b2dd2a6cb02e0d0749de4536a7fbdb000456b817b20ebb`
