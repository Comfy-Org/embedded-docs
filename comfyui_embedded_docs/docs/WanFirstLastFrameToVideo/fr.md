> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFirstLastFrameToVideo/fr.md)

Le nœud WanFirstLastFrameToVideo crée un conditionnement vidéo en combinant des images de début et de fin avec des invites textuelles. Il génère une représentation latente pour la génération vidéo en encodant la première et la dernière image, en appliquant des masques pour guider le processus de génération, et en incorporant les caractéristiques visuelles CLIP lorsqu'elles sont disponibles. Ce nœud prépare à la fois un conditionnement positif et négatif pour les modèles vidéo afin de générer des séquences cohérentes entre les points de début et de fin spécifiés.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `positif` | CONDITIONING | Oui | - | Conditionnement textuel positif pour guider la génération vidéo |
| `négatif` | CONDITIONING | Oui | - | Conditionnement textuel négatif pour guider la génération vidéo |
| `vae` | VAE | Oui | - | Modèle VAE utilisé pour encoder les images dans l'espace latent |
| `largeur` | INT | Oui | 16 à RÉSOLUTION_MAX | Largeur de la vidéo de sortie (par défaut : 832, pas : 16) |
| `hauteur` | INT | Oui | 16 à RÉSOLUTION_MAX | Hauteur de la vidéo de sortie (par défaut : 480, pas : 16) |
| `longueur` | INT | Oui | 1 à RÉSOLUTION_MAX | Nombre d'images dans la séquence vidéo (par défaut : 81, pas : 4) |
| `taille_du_lot` | INT | Oui | 1 à 4096 | Nombre de vidéos à générer simultanément (par défaut : 1) |
| `clip_vision_image_de_départ` | CLIP_VISION_OUTPUT | Non | - | Caractéristiques visuelles CLIP extraites de l'image de début |
| `clip_vision_image_de_fin` | CLIP_VISION_OUTPUT | Non | - | Caractéristiques visuelles CLIP extraites de l'image de fin |
| `image_de_départ` | IMAGE | Non | - | Image du cadre de départ pour la séquence vidéo |
| `image_de_fin` | IMAGE | Non | - | Image du cadre de fin pour la séquence vidéo |

**Remarque :** Lorsque `start_image` et `end_image` sont tous deux fournis, le nœud crée une séquence vidéo qui effectue une transition entre ces deux images. Les paramètres `clip_vision_start_image` et `clip_vision_end_image` sont facultatifs, mais lorsqu'ils sont fournis, leurs caractéristiques visuelles CLIP sont concaténées et appliquées au conditionnement positif et négatif. L'image `start_image` est recadrée aux premières images `length`, et l'image `end_image` est recadrée aux dernières images `length` avant le traitement.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `négatif` | CONDITIONING | Conditionnement positif avec encodage d'images vidéo appliqué et caractéristiques visuelles CLIP |
| `latent` | CONDITIONING | Conditionnement négatif avec encodage d'images vidéo appliqué et caractéristiques visuelles CLIP |
| `latent` | LATENT | Tenseur latent vide dont les dimensions correspondent aux paramètres vidéo spécifiés |

---
**Source fingerprint (SHA-256):** `8cfca692fc4975bb5238ce749d2102fad4b6cd84e96ef74c3eff2b297ee60c3c`
