# Image vers vidéo WanCamera

WanCameraImageToVideo prépare les données de conditionnement et les données latentes pour la génération de vidéos à partir d'images. Il prend des invites de conditionnement positives et négatives, ainsi que des images de départ et des contrôles de caméra optionnels, et renvoie un conditionnement modifié ainsi qu'un tenseur latent vide prêt à être rempli par un modèle vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Invites de conditionnement positives pour la génération vidéo | CONDITIONNING | Oui | - |
| `negative` | Invites de conditionnement négatives à éviter dans la génération vidéo | CONDITIONNING | Oui | - |
| `vae` | Modèle VAE pour encoder les images dans l'espace latent | VAE | Oui | - |
| `width` | Largeur de la vidéo de sortie en pixels (par défaut : 832, pas : 16) | INT | Oui | 16 to MAX_RESOLUTION |
| `height` | Hauteur de la vidéo de sortie en pixels (par défaut : 480, pas : 16) | INT | Oui | 16 to MAX_RESOLUTION |
| `length` | Nombre d'images dans la séquence vidéo (par défaut : 81, pas : 4) | INT | Oui | 1 to MAX_RESOLUTION |
| `batch_size` | Nombre de vidéos à générer simultanément (par défaut : 1) | INT | Oui | 1 to 4096 |
| `clip_vision_output` | Sortie CLIP Vision optionnelle pour un conditionnement supplémentaire | CLIP_VISION_OUTPUT | Non | - |
| `start_image` | Image de départ optionnelle pour initialiser la séquence vidéo. Lorsqu'elle est fournie, les premières images de la vidéo seront basées sur cette image, avec un masque appliqué pour fondre les images de départ avec le contenu généré. L'image est redimensionnée pour correspondre à la largeur et à la hauteur spécifiées. | IMAGE | Non | - |
| `camera_conditions` | Conditions d'incorporation de caméra optionnelles pour la génération vidéo. Lorsqu'elles sont fournies, ces conditions sont appliquées à la fois au conditionnement positif et négatif. | WAN_CAMERA_EMBEDDING | Non | - |

**Remarque :** Lorsque `start_image` est fourni, le nœud l'utilise pour initialiser la séquence vidéo et applique un masquage pour fondre les images de départ avec le contenu généré. Les paramètres `camera_conditions` et `clip_vision_output` sont facultatifs, mais lorsqu'ils sont fournis, ils modifient le conditionnement à la fois pour les invites positives et négatives.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif modifié avec les conditions de caméra, les sorties CLIP Vision et/ou les données d'image de départ appliquées. | CONDITIONNING |
| `negative` | Conditionnement négatif modifié avec les conditions de caméra, les sorties CLIP Vision et/ou les données d'image de départ appliquées. | CONDITIONNING |
| `latent` | Représentation latente vidéo vide générée pour une utilisation avec les modèles vidéo. Le tenseur latent a les dimensions [batch_size, 16, frames, height/8, width/8] où frames est calculé comme ((length - 1) // 4) + 1. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `467a82be0dfd6ac1c3b2dd2a6cb02e0d0749de4536a7fbdb000456b817b20ebb`
