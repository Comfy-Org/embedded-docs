> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SVD_img2vid_Conditioning/fr.md)

## Entrées

| Paramètre | Type de données | Obligatoire | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `clip_vision` | CLIP_VISION | Oui | - | Modèle de vision CLIP pour encoder l'image d'entrée |
| `init_image` | IMAGE | Oui | - | Image initiale utilisée comme point de départ pour la génération vidéo |
| `vae` | VAE | Oui | - | Modèle VAE pour encoder l'image dans l'espace latent |
| `largeur` | INT | Oui | 16 à MAX_RESOLUTION | Largeur de la vidéo de sortie (par défaut : 1024, pas : 8) |
| `hauteur` | INT | Oui | 16 à MAX_RESOLUTION | Hauteur de la vidéo de sortie (par défaut : 576, pas : 8) |
| `cadres_vidéo` | INT | Oui | 1 à 4096 | Nombre d'images à générer dans la vidéo (par défaut : 14) |
| `id_seau_de_mouvement` | INT | Oui | 1 à 1023 | Contrôle la quantité de mouvement dans la vidéo générée (par défaut : 127) |
| `fps` | INT | Oui | 1 à 1024 | Images par seconde pour la vidéo générée (par défaut : 6) |
| `niveau_d'augmentation` | FLOAT | Oui | 0.0 à 10.0 | Niveau de bruit d'augmentation à appliquer à l'image d'entrée (par défaut : 0.0, pas : 0.01) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `négatif` | CONDITIONING | Données de conditionnement positives contenant les embeddings d'image et les paramètres vidéo |
| `latent` | CONDITIONING | Données de conditionnement négatives avec des embeddings mis à zéro et paramètres vidéo |
| `latent` | LATENT | Tenseur d'espace latent vide prêt pour la génération vidéo |
