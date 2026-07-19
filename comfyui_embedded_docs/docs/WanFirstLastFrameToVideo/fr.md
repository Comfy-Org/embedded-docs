# WanFirstLastFrameToVideo

Le nœud WanFirstLastFrameToVideo crée un conditionnement vidéo en combinant des images de début et de fin avec des invites textuelles. Il génère une représentation latente pour la génération vidéo en encodant la première et la dernière image, en appliquant des masques pour guider le processus de génération, et en incorporant les caractéristiques visuelles CLIP lorsqu'elles sont disponibles. Ce nœud prépare à la fois un conditionnement positif et négatif pour les modèles vidéo afin de générer des séquences cohérentes entre les points de début et de fin spécifiés.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | Conditionnement textuel positif pour guider la génération vidéo | CONDITIONING | Oui | - |
| `négatif` | Conditionnement textuel négatif pour guider la génération vidéo | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder les images dans l'espace latent | VAE | Oui | - |
| `largeur` | Largeur de la vidéo de sortie (par défaut : 832, pas : 16) | INT | Oui | 16 à RÉSOLUTION_MAX |
| `hauteur` | Hauteur de la vidéo de sortie (par défaut : 480, pas : 16) | INT | Oui | 16 à RÉSOLUTION_MAX |
| `longueur` | Nombre d'images dans la séquence vidéo (par défaut : 81, pas : 4) | INT | Oui | 1 à RÉSOLUTION_MAX |
| `taille_du_lot` | Nombre de vidéos à générer simultanément (par défaut : 1) | INT | Oui | 1 à 4096 |
| `clip_vision_image_de_départ` | Caractéristiques visuelles CLIP extraites de l'image de début | CLIP_VISION_OUTPUT | Non | - |
| `clip_vision_image_de_fin` | Caractéristiques visuelles CLIP extraites de l'image de fin | CLIP_VISION_OUTPUT | Non | - |
| `image_de_départ` | Image du cadre de départ pour la séquence vidéo | IMAGE | Non | - |
| `image_de_fin` | Image du cadre de fin pour la séquence vidéo | IMAGE | Non | - |

**Remarque :** Lorsque `start_image` et `end_image` sont tous deux fournis, le nœud crée une séquence vidéo qui effectue une transition entre ces deux images. Les paramètres `clip_vision_start_image` et `clip_vision_end_image` sont facultatifs, mais lorsqu'ils sont fournis, leurs caractéristiques visuelles CLIP sont concaténées et appliquées au conditionnement positif et négatif. L'image `start_image` est recadrée aux premières images `length`, et l'image `end_image` est recadrée aux dernières images `length` avant le traitement.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positif` | Conditionnement positif avec encodage d'images vidéo appliqué et caractéristiques visuelles CLIP | CONDITIONING |
| `négatif` | Conditionnement négatif avec encodage d'images vidéo appliqué et caractéristiques visuelles CLIP | CONDITIONING |
| `latent` | Tenseur latent vide dont les dimensions correspondent aux paramètres vidéo spécifiés | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFirstLastFrameToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `8cfca692fc4975bb5238ce749d2102fad4b6cd84e96ef74c3eff2b297ee60c3c`
