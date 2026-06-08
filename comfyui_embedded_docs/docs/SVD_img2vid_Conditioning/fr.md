Le nœud **SVD_img2vid_Conditioning** prépare les données de conditionnement pour la génération vidéo à l'aide de Stable Video Diffusion. Il prend une image initiale et la traite via les encodeurs CLIP vision et VAE pour créer des paires de conditionnement positives et négatives, ainsi qu'un espace latent vide pour la génération vidéo. Ce nœud configure les paramètres nécessaires pour contrôler le mouvement, la fréquence d'images et le niveau d'augmentation dans la vidéo générée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip_vision` | Modèle de vision CLIP pour encoder l'image d'entrée | CLIP_VISION | Oui | - |
| `init_image` | Image initiale utilisée comme point de départ pour la génération vidéo | IMAGE | Oui | - |
| `vae` | Modèle VAE pour encoder l'image dans l'espace latent | VAE | Oui | - |
| `largeur` | Largeur de la vidéo de sortie (par défaut : 1024, pas : 8) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | Hauteur de la vidéo de sortie (par défaut : 576, pas : 8) | INT | Oui | 16 à MAX_RESOLUTION |
| `cadres_vidéo` | Nombre d'images à générer dans la vidéo (par défaut : 14) | INT | Oui | 1 à 4096 |
| `id_seau_de_mouvement` | Contrôle la quantité de mouvement dans la vidéo générée (par défaut : 127) | INT | Oui | 1 à 1023 |
| `fps` | Images par seconde pour la vidéo générée (par défaut : 6) | INT | Oui | 1 à 1024 |
| `niveau_d'augmentation` | Niveau d'augmentation du bruit à appliquer à l'image d'entrée (par défaut : 0,0, pas : 0,01) | FLOAT | Oui | 0,0 à 10,0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `négatif` | Données de conditionnement positives contenant les embeddings d'image et les paramètres vidéo | CONDITIONING |
| `latent` | Données de conditionnement négatives avec des embeddings et paramètres vidéo mis à zéro | CONDITIONING |
| `latent` | Tenseur d'espace latent vide prêt pour la génération vidéo | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SVD_img2vid_Conditioning/fr.md)

---
**Source fingerprint (SHA-256):** `33b295b6f2e459852aaa95d9dca26c724aa2e9ad0f884a1c7760766530a00a09`
