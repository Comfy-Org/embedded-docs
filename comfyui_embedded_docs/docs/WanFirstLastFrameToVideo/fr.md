# WanFirstLastFrameToVideo

Le nœud WanFirstLastFrameToVideo crée un conditionnement vidéo en combinant les images de début et de fin avec des invites textuelles. Il génère une représentation latente pour la génération vidéo en encodant les première et dernière images, en appliquant des masques pour guider le processus de génération, et en intégrant les caractéristiques visuelles CLIP lorsqu'elles sont disponibles. Ce nœud prépare un conditionnement positif et négatif pour les modèles vidéo afin de générer des séquences cohérentes entre les points de début et de fin spécifiés.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Conditionnement textuel positif pour guider la génération vidéo | CONDITIONING | Oui | - |
| `negative` | Conditionnement textuel négatif pour guider la génération vidéo | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder les images dans l'espace latent | VAE | Oui | - |
| `width` | Largeur de la vidéo de sortie (défaut : 832, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `height` | Hauteur de la vidéo de sortie (défaut : 480, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `length` | Nombre d'images dans la séquence vidéo (défaut : 81, pas : 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `batch_size` | Nombre de vidéos à générer simultanément (défaut : 1) | INT | Oui | 1 à 4096 |
| `clip_vision_start_image` | Caractéristiques visuelles CLIP extraites de l'image de début | CLIP_VISION_OUTPUT | Non | - |
| `clip_vision_end_image` | Caractéristiques visuelles CLIP extraites de l'image de fin | CLIP_VISION_OUTPUT | Non | - |
| `start_image` | Image de début de la séquence vidéo | IMAGE | Non | - |
| `end_image` | Image de fin de la séquence vidéo | IMAGE | Non | - |

**Remarque :** Lorsque `start_image` et `end_image` sont tous deux fournis, le nœud crée une séquence vidéo qui fait la transition entre ces deux images. Le `start_image` est recadré sur les premiers `length` images, et le `end_image` est recadré sur les derniers `length` images avant le traitement. Si un seul d'entre eux est fourni, le côté manquant est rempli avec des images gris neutres. Le masque est défini à 0 là où les images de début et de fin sont présentes et à 1 ailleurs. Les paramètres `clip_vision_start_image` et `clip_vision_end_image` sont facultatifs ; lorsque les deux sont fournis, leurs caractéristiques visuelles CLIP sont concaténées et appliquées aux conditionnements positif et négatif. Lorsqu'un seul est fourni, ses caractéristiques sont utilisées seules.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif avec encodage des images vidéo et caractéristiques visuelles CLIP appliqués | CONDITIONING |
| `negative` | Conditionnement négatif avec encodage des images vidéo et caractéristiques visuelles CLIP appliqués | CONDITIONING |
| `latent` | Tenseur latent vide dont les dimensions correspondent aux paramètres vidéo spécifiés | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFirstLastFrameToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `0072e441cb80334c3c961d1bbf2d081c78bc38ed1eacca840c577a2d01b36f05`
