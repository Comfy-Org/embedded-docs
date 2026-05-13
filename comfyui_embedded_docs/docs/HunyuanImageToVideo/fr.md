> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageToVideo/fr.md)

Ce document a été généré par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageToVideo/en.md)

Le nœud HunyuanImageToVideo convertit des images en représentations latentes vidéo à l'aide du modèle vidéo Hunyuan. Il prend en entrée des conditionnements et des images de départ optionnelles pour générer des latents vidéo pouvant être traités ultérieurement par des modèles de génération vidéo. Le nœud prend en charge différents types de guidage pour contrôler l'influence de l'image de départ sur le processus de génération vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `positive` | CONDITIONING | Oui | - | Conditionnement positif pour guider la génération vidéo |
| `vae` | VAE | Oui | - | Modèle VAE utilisé pour encoder les images dans l'espace latent |
| `largeur` | INT | Oui | 16 à MAX_RESOLUTION | Largeur de la vidéo de sortie en pixels (par défaut : 848, pas : 16) |
| `hauteur` | INT | Oui | 16 à MAX_RESOLUTION | Hauteur de la vidéo de sortie en pixels (par défaut : 480, pas : 16) |
| `longueur` | INT | Oui | 1 à MAX_RESOLUTION | Nombre d'images dans la vidéo de sortie (par défaut : 53, pas : 4) |
| `taille_du_lot` | INT | Oui | 1 à 4096 | Nombre de vidéos à générer simultanément (par défaut : 1) |
| `type_de_guidage` | COMBO | Oui | "v1 (concat)"<br>"v2 (replace)"<br>"custom" | Méthode d'incorporation de l'image de départ dans la génération vidéo (par défaut : "v1 (concat)") |
| `image_de_départ` | IMAGE | Non | - | Image de départ optionnelle pour initialiser la génération vidéo |

**Remarque :** Lorsque `start_image` est fourni, le nœud utilise différentes méthodes de guidage selon le `guidance_type` sélectionné :

- "v1 (concat)" : Concatène le latent de l'image avec le latent vidéo et applique un masque pour fusionner l'image dans la vidéo
- "v2 (replace)" : Remplace les images vidéo initiales par le latent de l'image et applique un masque de bruit
- "custom" : Utilise l'image comme latent de référence pour le guidage

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `latent` | CONDITIONING | Conditionnement positif modifié avec guidage d'image appliqué lorsque start_image est fourni |
| `latent` | LATENT | Représentation latente vidéo prête pour un traitement ultérieur par des modèles de génération vidéo |

---
**Source fingerprint (SHA-256):** `e55e935b7955b28b04014359c544a230c51ee91e21170be1ae4f50705d3e7bba`
