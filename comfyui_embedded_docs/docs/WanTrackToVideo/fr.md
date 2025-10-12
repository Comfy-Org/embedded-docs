> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTrackToVideo/fr.md)

Le nœud WanTrackToVideo convertit des données de suivi de mouvement en séquences vidéo en traitant les points de piste et en générant les images vidéo correspondantes. Il prend en entrée des coordonnées de suivi et produit un conditionnement vidéo ainsi que des représentations latentes qui peuvent être utilisées pour la génération vidéo. Lorsqu'aucune piste n'est fournie, il revient à une conversion image-à-vidéo standard.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Oui | - | Conditionnement positif pour la génération vidéo |
| `negative` | CONDITIONING | Oui | - | Conditionnement négatif pour la génération vidéo |
| `vae` | VAE | Oui | - | Modèle VAE pour l'encodage et le décodage |
| `tracks` | STRING | Oui | - | Données de suivi au format JSON sous forme de chaîne multiligne (par défaut : "[]") |
| `width` | INT | Oui | 16 à MAX_RESOLUTION | Largeur de la vidéo en pixels (par défaut : 832, pas : 16) |
| `height` | INT | Oui | 16 à MAX_RESOLUTION | Hauteur de la vidéo en pixels (par défaut : 480, pas : 16) |
| `length` | INT | Oui | 1 à MAX_RESOLUTION | Nombre d'images dans la vidéo de sortie (par défaut : 81, pas : 4) |
| `batch_size` | INT | Oui | 1 à 4096 | Nombre de vidéos à générer simultanément (par défaut : 1) |
| `temperature` | FLOAT | Oui | 1.0 à 1000.0 | Paramètre de température pour l'application du mouvement (par défaut : 220.0, pas : 0.1) |
| `topk` | INT | Oui | 1 à 10 | Valeur top-k pour l'application du mouvement (par défaut : 2) |
| `start_image` | IMAGE | Non | - | Image de départ pour la génération vidéo |
| `clip_vision_output` | CLIPVISIONOUTPUT | Non | - | Sortie CLIP vision pour un conditionnement supplémentaire |

**Note :** Lorsque `tracks` contient des données de suivi valides, le nœud traite les pistes de mouvement pour générer la vidéo. Lorsque `tracks` est vide, il bascule en mode image-à-vidéo standard. Si `start_image` est fournie, elle initialise la première image de la séquence vidéo.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Conditionnement positif avec les informations de piste de mouvement appliquées |
| `negative` | CONDITIONING | Conditionnement négatif avec les informations de piste de mouvement appliquées |
| `latent` | LATENT | Représentation latente de la vidéo générée |