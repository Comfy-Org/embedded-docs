> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22FunControlToVideo/fr.md)

Le nœud Wan22FunControlToVideo prépare les conditionnements et les représentations latentes pour la génération vidéo en utilisant l'architecture de modèle vidéo Wan. Il traite les entrées de conditionnement positives et négatives ainsi que les images de référence et les vidéos de contrôle optionnelles pour créer les représentations d'espace latent nécessaires à la synthèse vidéo. Le nœud gère la mise à l'échelle spatiale et les dimensions temporelles pour générer des données de conditionnement appropriées pour les modèles vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Oui | - | Conditionnement positif pour guider la génération vidéo |
| `negative` | CONDITIONING | Oui | - | Conditionnement négatif pour guider la génération vidéo |
| `vae` | VAE | Oui | - | Modèle VAE utilisé pour encoder les images en espace latent |
| `width` | INT | Non | 16 à MAX_RESOLUTION | Largeur de la vidéo en pixels (par défaut : 832, pas : 16) |
| `height` | INT | Non | 16 à MAX_RESOLUTION | Hauteur de la vidéo en pixels (par défaut : 480, pas : 16) |
| `length` | INT | Non | 1 à MAX_RESOLUTION | Nombre d'images dans la séquence vidéo (par défaut : 81, pas : 4) |
| `batch_size` | INT | Non | 1 à 4096 | Nombre de séquences vidéo à générer (par défaut : 1) |
| `ref_image` | IMAGE | Non | - | Image de référence optionnelle pour fournir un guidage visuel |
| `control_video` | IMAGE | Non | - | Vidéo de contrôle optionnelle pour guider le processus de génération |

**Note :** Le paramètre `length` est traité par blocs de 4 images, et le nœud gère automatiquement la mise à l'échelle temporelle pour l'espace latent. Lorsque `ref_image` est fournie, elle influence le conditionnement via les latents de référence. Lorsque `control_video` est fournie, elle affecte directement la représentation latente de concaténation utilisée dans le conditionnement.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Conditionnement positif modifié avec des données latentes spécifiques à la vidéo |
| `negative` | CONDITIONING | Conditionnement négatif modifié avec des données latentes spécifiques à la vidéo |
| `latent` | LATENT | Tenseur latent vide avec les dimensions appropriées pour la génération vidéo |