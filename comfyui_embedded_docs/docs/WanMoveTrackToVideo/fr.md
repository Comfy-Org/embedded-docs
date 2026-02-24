> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTrackToVideo/fr.md)

Le nœud WanMoveTrackToVideo prépare les données de conditionnement et d'espace latent pour la génération vidéo, en intégrant éventuellement des informations de suivi de mouvement. Il encode une séquence d'image de départ en une représentation latente et peut intégrer des données positionnelles provenant de pistes d'objets pour guider le mouvement dans la vidéo générée. Le nœud renvoie un conditionnement positif et négatif modifié ainsi qu'un tenseur latent vide prêt pour un modèle vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Oui | - | L'entrée de conditionnement positif à modifier. |
| `negative` | CONDITIONING | Oui | - | L'entrée de conditionnement négatif à modifier. |
| `vae` | VAE | Oui | - | Le modèle VAE utilisé pour encoder l'image de départ dans l'espace latent. |
| `tracks` | TRACKS | Non | - | Données de suivi de mouvement optionnelles contenant les trajectoires d'objets. |
| `strength` | FLOAT | Non | 0.0 - 100.0 | Intensité du conditionnement par les pistes. (par défaut : 1.0) |
| `width` | INT | Non | 16 - MAX_RESOLUTION | La largeur de la vidéo de sortie. Doit être divisible par 16. (par défaut : 832) |
| `height` | INT | Non | 16 - MAX_RESOLUTION | La hauteur de la vidéo de sortie. Doit être divisible par 16. (par défaut : 480) |
| `length` | INT | Non | 1 - MAX_RESOLUTION | Le nombre d'images dans la séquence vidéo. (par défaut : 81) |
| `batch_size` | INT | Non | 1 - 4096 | La taille du lot pour la sortie latente. (par défaut : 1) |
| `start_image` | IMAGE | Oui | - | L'image ou séquence d'images de départ à encoder. |
| `clip_vision_output` | CLIPVISIONOUTPUT | Non | - | Sortie optionnelle du modèle de vision CLIP à ajouter au conditionnement. |

**Note :** Le paramètre `strength` n'a d'effet que si des `tracks` sont fournies. Si aucune `tracks` n'est fournie ou si `strength` est à 0.0, le conditionnement par les pistes n'est pas appliqué. L'`start_image` est utilisée pour créer une image latente et un masque pour le conditionnement ; si elle n'est pas fournie, le nœud se contente de transmettre le conditionnement et renvoie un latent vide.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Le conditionnement positif modifié, contenant potentiellement `concat_latent_image`, `concat_mask` et `clip_vision_output`. |
| `negative` | CONDITIONING | Le conditionnement négatif modifié, contenant potentiellement `concat_latent_image`, `concat_mask` et `clip_vision_output`. |
| `latent` | LATENT | Un tenseur latent vide dont les dimensions sont définies par les entrées `batch_size`, `length`, `height` et `width`. |
