# SV3D_Conditioning

Le nœud SV3D_Conditioning prépare les données de conditionnement pour la génération vidéo 3D à l'aide du modèle SV3D. Il prend une image initiale et la traite via les encodeurs CLIP vision et VAE pour créer un conditionnement positif et négatif, ainsi qu'une représentation latente. Le nœud génère des séquences d'élévation et d'azimut de caméra pour la génération vidéo multi-images en fonction du nombre d'images vidéo spécifié.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `clip_vision` | Le modèle de vision CLIP utilisé pour encoder l'image d'entrée | CLIP_VISION | Oui | - |
| `init_image` | L'image initiale qui sert de point de départ pour la génération vidéo 3D | IMAGE | Oui | - |
| `vae` | Le modèle VAE utilisé pour encoder l'image dans l'espace latent | VAE | Oui | - |
| `width` | La largeur de sortie pour les images vidéo générées (par défaut : 576, doit être divisible par 8) | INT | Oui | 16 à MAX_RESOLUTION (pas de 8) |
| `height` | La hauteur de sortie pour les images vidéo générées (par défaut : 576, doit être divisible par 8) | INT | Oui | 16 à MAX_RESOLUTION (pas de 8) |
| `video_frames` | Le nombre d'images à générer pour la séquence vidéo (par défaut : 21) | INT | Oui | 1 à 4096 |
| `elevation` | L'angle d'élévation de la caméra en degrés pour la vue 3D, appliqué à chaque image (par défaut : 0,0) | FLOAT | Oui | -90,0 à 90,0 (pas de 0,1) |

Remarque : L'azimut de la caméra commence à 0 degré et augmente de 360 / (video_frames - 1) degrés par image, de sorte que la caméra effectue une orbite complète autour de l'objet sur toute la séquence. La même valeur `elevation` est appliquée à toutes les images.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positive` | Les données de conditionnement positif contenant les embeddings de l'image et les paramètres de caméra pour la génération | CONDITIONING |
| `negative` | Les données de conditionnement négatif avec des embeddings mis à zéro pour la génération contrastive | CONDITIONING |
| `latent` | Un tenseur latent vide dont les dimensions correspondent aux images vidéo et à la résolution spécifiées | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SV3D_Conditioning/fr.md)

---
**Source fingerprint (SHA-256):** `e28173cfa560290e66b032687088cf0b981256ca5c21f6aa608e0fdaec886665`
