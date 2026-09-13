# WanFunInpaintToVideo

Le nœud WanFunInpaintToVideo prépare les données de conditionnement et de latent pour la génération vidéo de type inpainting, en s'appuyant sur une image de début et une image de fin facultatives pour guider le résultat. Il fonctionne en faisant passer le conditionnement, le VAE et les images fournis dans la même logique que celle utilisée pour la génération vidéo à première et dernière image, puis renvoie le conditionnement mis à jour ainsi qu'un latent vide pour l'échantillonnage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Invites de conditionnement positives pour la génération vidéo | CONDITIONING | Oui | - |
| `negative` | Invites de conditionnement négatives à éviter dans la génération vidéo | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour l'encodage et le décodage des images vidéo | VAE | Oui | - |
| `width` | Largeur de la vidéo de sortie en pixels (par défaut : 832, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `height` | Hauteur de la vidéo de sortie en pixels (par défaut : 480, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `length` | Nombre d'images dans la séquence vidéo (par défaut : 81, pas : 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `batch_size` | Nombre de vidéos à générer par lot (par défaut : 1) | INT | Oui | 1 à 4096 |
| `clip_vision_output` | Sortie de vision CLIP facultative utilisée comme conditionnement pour l'image de début | CLIP_VISION_OUTPUT | Non | - |
| `start_image` | Image de début facultative pour la génération vidéo | IMAGE | Non | - |
| `end_image` | Image de fin facultative pour la génération vidéo | IMAGE | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Sortie de conditionnement positif traitée | CONDITIONING |
| `negative` | Sortie de conditionnement négatif traitée | CONDITIONING |
| `latent` | Représentation latente de la vidéo générée | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `70b58e961c5df12f94183245ce320197439b2505b47d0bb3ff643b25c9fe6175`
