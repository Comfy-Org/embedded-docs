# WanDancerVideo

Le nœud WanDancerVideo prépare les données de conditionnement et un tenseur latent vide pour la génération vidéo avec le modèle WanDancer. Il combine le conditionnement positif et négatif avec des entrées optionnelles comme une image de départ, un masque, des embeddings CLIP vision et des caractéristiques audio pour contrôler la vidéo générée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | Le conditionnement positif pour guider la génération vidéo. | CONDITIONING | Oui |  |
| `négatif` | Le conditionnement négatif pour guider la génération vidéo. | CONDITIONING | Oui |  |
| `vae` | Le VAE utilisé pour encoder l'image de départ dans l'espace latent. | VAE | Oui |  |
| `largeur` | La largeur de la vidéo générée en pixels (par défaut : 480). | INT | Oui | 16 à MAX_RESOLUTION (pas : 16) |
| `hauteur` | La hauteur de la vidéo générée en pixels (par défaut : 832). | INT | Oui | 16 à MAX_RESOLUTION (pas : 16) |
| `longueur` | Le nombre d'images dans la vidéo générée. Doit rester à 149 pour WanDancer (par défaut : 149). | INT | Oui | 1 à MAX_RESOLUTION (pas : 4) |
| `clip_vision_output` | Les embeddings CLIP vision pour la première image. | CLIP_VISION_OUTPUT | Non |  |
| `clip_vision_output_ref` | Les embeddings CLIP vision pour l'image de référence. | CLIP_VISION_OUTPUT | Non |  |
| `image_de_départ` | La ou les images initiales à encoder. Peut être n'importe quel nombre d'images, jusqu'à la `longueur` spécifiée. | IMAGE | Non |  |
| `masque` | Masque de conditionnement d'image pour la ou les images de départ. Les zones blanches sont conservées, les zones noires sont générées. Utilisé pour les générations locales. | MASK | Non |  |
| `audio_encoder_output` | La sortie d'un encodeur audio, fournissant les caractéristiques audio, le fps et l'échelle d'injection pour la génération conditionnée par l'audio. | AUDIO_ENCODER_OUTPUT | Non |  |

**Remarque sur les contraintes des paramètres :**
- Les entrées `start_image` et `mask` sont optionnelles mais peuvent être utilisées ensemble. Lorsque `start_image` est fournie, elle est encodée et concaténée avec le latent. Si `mask` est également fourni, il contrôle les parties de l'image de départ qui sont conservées (blanc) et celles qui sont régénérées (noir). Si `mask` n'est pas fourni, toute la zone de l'image de départ est utilisée comme guide de conditionnement.
- Les entrées `clip_vision_output` et `clip_vision_output_ref` sont optionnelles et peuvent être utilisées ensemble pour fournir un contexte visuel pour la première image et une image de référence.
- L'entrée `audio_encoder_output` est optionnelle et fournit des caractéristiques audio pour la génération conditionnée par l'audio.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `négatif` | Le conditionnement positif avec toutes les données supplémentaires (concat latent, CLIP vision, audio) attachées. | CONDITIONING |
| `latent` | Le conditionnement négatif avec toutes les données supplémentaires (concat latent, CLIP vision, audio) attachées. | CONDITIONING |
| `latent` | Un tenseur latent vide avec des dimensions correspondant à la longueur, hauteur et largeur vidéo spécifiées. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerVideo/fr.md)

---
**Source fingerprint (SHA-256):** `7ab1b4662eb8d780295ea3a3e3139c64d81e03a979a293a481f82deaf1fc2f7e`
