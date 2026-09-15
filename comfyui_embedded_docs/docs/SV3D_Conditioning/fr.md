# SV3D_Conditioning

SV3D_Conditioning prépare les données de conditionnement pour la génération de vidéo 3D à l'aide du modèle SV3D. Il prend une image initiale et la traite via les encodeurs de vision CLIP et VAE pour créer des conditionnements positif et négatif, ainsi qu'une représentation latente. Le nœud génère des séquences d'élévation et d'azimut de caméra pour la génération vidéo multi-images en fonction du nombre d'images vidéo spécifié.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
| --- | --- | --- | --- | --- |
| `clip_vision` | Modèle de vision CLIP utilisé pour encoder l'image d'entrée | CLIP_VISION | Oui | - |
| `init_image` | Image initiale servant de point de départ à la génération de vidéo 3D | IMAGE | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder l'image dans l'espace latent | VAE | Oui | - |
| `largeur` | Largeur de sortie des images vidéo générées (par défaut : 576, pas de 8) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | Hauteur de sortie des images vidéo générées (par défaut : 576, pas de 8) | INT | Oui | 16 à MAX_RESOLUTION |
| `cadres_vidéo` | Nombre d'images à générer pour la séquence vidéo (par défaut : 21) | INT | Oui | 1 à 4096 |
| `élévation` | Angle d'élévation de la caméra en degrés pour la vue 3D (par défaut : 0.0, pas de 0.1) | FLOAT | Oui | -90.0 à 90.0 |

Remarque : L'azimut de la caméra commence à 0 degré et augmente d'une quantité constante à chaque image, de sorte que la caméra effectue une orbite complète de 360 degrés autour de l'objet sur l'ensemble des images générées. L'incrément par image est calculé comme 360 divisé par (`video_frames` - 1), avec un diviseur minimum de 2 lorsqu'une seule image est demandée. La valeur `elevation` reste constante pour chaque image.

L'`init_image` est redimensionnée aux valeurs `width` et `height` spécifiées avant l'encodage VAE, et le latent renvoyé utilise des dimensions de `video_frames` x 4 x (`height` // 8) x (`width` // 8).

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Les données de conditionnement positif contenant les embeddings d'image et les paramètres de caméra pour la génération | CONDITIONING |
| `negative` | Les données de conditionnement négatif avec des embeddings et latents mis à zéro pour une génération contrastive | CONDITIONING |
| `latent` | Un tenseur latent vide dont les dimensions correspondent aux images vidéo et à la résolution spécifiées | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SV3D_Conditioning/fr.md)

---
**Source fingerprint (SHA-256):** `e28173cfa560290e66b032687088cf0b981256ca5c21f6aa608e0fdaec886665`
