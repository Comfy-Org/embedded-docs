# SV3D_Conditioning

Le nœud SV3D_Conditioning prépare les données de conditionnement pour la génération vidéo 3D à l'aide du modèle SV3D. Il prend une image initiale et la traite via les encodeurs CLIP vision et VAE pour créer un conditionnement positif et négatif, accompagné d'une représentation latente. Le nœud génère des séquences d'élévation et d'azimut de caméra pour la génération vidéo multi-images en fonction du nombre d'images vidéo spécifié.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip_vision` | Le modèle de vision CLIP utilisé pour encoder l'image d'entrée | CLIP_VISION | Oui | - |
| `init_image` | L'image initiale servant de point de départ pour la génération vidéo 3D | IMAGE | Oui | - |
| `vae` | Le modèle VAE utilisé pour encoder l'image dans l'espace latent | VAE | Oui | - |
| `largeur` | La largeur de sortie pour les images vidéo générées (par défaut : 576, doit être divisible par 8) | INT | Non | 16 à MAX_RESOLUTION |
| `hauteur` | La hauteur de sortie pour les images vidéo générées (par défaut : 576, doit être divisible par 8) | INT | Non | 16 à MAX_RESOLUTION |
| `cadres_vidéo` | Le nombre d'images à générer pour la séquence vidéo (par défaut : 21) | INT | Non | 1 à 4096 |
| `élévation` | L'angle d'élévation de la caméra en degrés pour la vue 3D (par défaut : 0.0) | FLOAT | Non | -90.0 à 90.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positif` | Les données de conditionnement positif contenant les embeddings d'image et les paramètres de caméra pour la génération | CONDITIONING |
| `négatif` | Les données de conditionnement négatif avec des embeddings mis à zéro pour la génération contrastive | CONDITIONING |
| `latent` | Un tenseur latent vide dont les dimensions correspondent aux images vidéo et à la résolution spécifiées | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SV3D_Conditioning/fr.md)

---
**Source fingerprint (SHA-256):** `be02939aa4cdd1785eb445034a27d08a90e390a497fa9697fb769f0ce26e6d2f`
