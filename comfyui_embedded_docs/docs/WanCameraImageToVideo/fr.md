> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/fr.md)

Le nœud WanCameraImageToVideo convertit des images en séquences vidéo en générant des représentations latentes pour la création vidéo. Il traite les entrées de conditionnement et les images de départ optionnelles pour créer des latents vidéo qui peuvent être utilisés avec des modèles vidéo. Le nœud prend en charge les conditions de caméra et les sorties de vision CLIP pour un contrôle amélioré de la génération vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Oui | - | Prompts de conditionnement positifs pour la génération vidéo |
| `negative` | CONDITIONING | Oui | - | Prompts de conditionnement négatifs à éviter dans la génération vidéo |
| `vae` | VAE | Oui | - | Modèle VAE pour encoder les images dans l'espace latent |
| `width` | INT | Oui | 16 à MAX_RESOLUTION | Largeur de la vidéo en pixels (par défaut : 832, pas : 16) |
| `height` | INT | Oui | 16 à MAX_RESOLUTION | Hauteur de la vidéo en pixels (par défaut : 480, pas : 16) |
| `length` | INT | Oui | 1 à MAX_RESOLUTION | Nombre d'images dans la séquence vidéo (par défaut : 81, pas : 4) |
| `batch_size` | INT | Oui | 1 à 4096 | Nombre de vidéos à générer simultanément (par défaut : 1) |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Non | - | Sortie de vision CLIP optionnelle pour un conditionnement supplémentaire |
| `start_image` | IMAGE | Non | - | Image de départ optionnelle pour initialiser la séquence vidéo |
| `camera_conditions` | WAN_CAMERA_EMBEDDING | Non | - | Conditions d'embedding de caméra optionnelles pour la génération vidéo |

**Note :** Lorsqu'une `start_image` est fournie, le nœud l'utilise pour initialiser la séquence vidéo et applique un masquage pour fusionner les images de départ avec le contenu généré. Les paramètres `camera_conditions` et `clip_vision_output` sont optionnels mais, lorsqu'ils sont fournis, modifient le conditionnement pour les prompts positifs et négatifs.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Conditionnement positif modifié avec application des conditions de caméra et des sorties de vision CLIP |
| `negative` | CONDITIONING | Conditionnement négatif modifié avec application des conditions de caméra et des sorties de vision CLIP |
| `latent` | LATENT | Représentation latente vidéo générée pour utilisation avec des modèles vidéo |