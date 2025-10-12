> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/fr.md)

Le nœud WanImageToVideo prépare les conditionnements et les représentations latentes pour les tâches de génération vidéo. Il crée un espace latent vide pour la génération vidéo et peut optionnellement incorporer des images de départ et des sorties de vision CLIP pour guider le processus de génération vidéo. Le nœud modifie à la fois les entrées de conditionnement positives et négatives en fonction des données d'image et de vision fournies.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Oui | - | Conditionnement positif pour guider la génération |
| `négatif` | CONDITIONING | Oui | - | Conditionnement négatif pour guider la génération |
| `vae` | VAE | Oui | - | Modèle VAE pour encoder les images dans l'espace latent |
| `largeur` | INT | Oui | 16 à MAX_RESOLUTION | Largeur de la vidéo en sortie (par défaut : 832, pas : 16) |
| `hauteur` | INT | Oui | 16 à MAX_RESOLUTION | Hauteur de la vidéo en sortie (par défaut : 480, pas : 16) |
| `longueur` | INT | Oui | 1 à MAX_RESOLUTION | Nombre d'images dans la vidéo (par défaut : 81, pas : 4) |
| `taille_du_lot` | INT | Oui | 1 à 4096 | Nombre de vidéos à générer dans un lot (par défaut : 1) |
| `sortie_vision_clip` | CLIP_VISION_OUTPUT | Non | - | Sortie de vision CLIP optionnelle pour un conditionnement supplémentaire |
| `image_de_départ` | IMAGE | Non | - | Image de départ optionnelle pour initialiser la génération vidéo |

**Note :** Lorsque `start_image` est fournie, le nœud encode la séquence d'images et applique un masquage aux entrées de conditionnement. Le paramètre `clip_vision_output`, lorsqu'il est fourni, ajoute un conditionnement basé sur la vision aux entrées positives et négatives.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `négatif` | CONDITIONING | Conditionnement positif modifié avec incorporation des données d'image et de vision |
| `latent` | CONDITIONING | Conditionnement négatif modifié avec incorporation des données d'image et de vision |
| `latent` | LATENT | Tenseur d'espace latent vide prêt pour la génération vidéo |
