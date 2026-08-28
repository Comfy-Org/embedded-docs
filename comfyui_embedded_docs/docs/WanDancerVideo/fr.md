# WanDancerVideo

Le nœud WanDancerVideo prépare les données de conditionnement et un tenseur latent vide pour la génération vidéo avec le modèle WanDancer. Il attache des images de départ facultatives, des masques, des plongements CLIP vision et des caractéristiques audio au conditionnement positif et négatif afin qu’ils puissent guider la vidéo générée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | Le conditionnement positif pour guider la génération vidéo. | CONDITIONING | Oui |  |
| `négatif` | Le conditionnement négatif pour guider la génération vidéo. | CONDITIONING | Oui |  |
| `vae` | Le VAE utilisé pour encoder l'image de départ dans l'espace latent. | VAE | Oui |  |
| `largeur` | La largeur de la vidéo générée en pixels (défaut : 480). | INT | Oui | 16 to MAX_RESOLUTION (step: 16) |
| `hauteur` | La hauteur de la vidéo générée en pixels (défaut : 832). | INT | Oui | 16 to MAX_RESOLUTION (step: 16) |
| `longueur` | Le nombre d'images de la vidéo générée. Doit rester à 149 pour WanDancer (défaut : 149). | INT | Oui | 1 to MAX_RESOLUTION (step: 4) |
| `clip_vision_output` | Les plongements CLIP vision pour la première image. | CLIP_VISION_OUTPUT | Non |  |
| `clip_vision_output_ref` | Les plongements CLIP vision pour l'image de référence. | CLIP_VISION_OUTPUT | Non |  |
| `image_de_départ` | L'image (ou les images) de départ à encoder, peut contenir n'importe quel nombre d'images. | IMAGE | Non |  |
| `masque` | Masque de conditionnement d'image pour le(s) image(s) de départ. Le blanc est conservé, le noir est généré. Utilisé pour les générations locales. | MASK | Non |  |
| `audio_encoder_output` | Une sortie d'encodeur audio qui fournit des caractéristiques audio, la fréquence d'images et des valeurs d'échelle d'injection, qui sont attachées au conditionnement lorsqu'elle est fournie. | AUDIO_ENCODER_OUTPUT | Non |  |

### Notes sur le comportement des paramètres

- `start_image` est facultatif. Lorsqu'il est fourni, il est redimensionné à `width` et `height`, encodé par le `vae`, et attaché au conditionnement positif et négatif. Si `start_image` a plus d'images que `length`, les images supplémentaires sont supprimées. S'il a moins d'images, les images manquantes sont remplies avec des valeurs nulles.
- `mask` n'a d'effet que lorsque `start_image` est également fourni. Les zones blanches sont conservées et les zones noires sont générées.
- `clip_vision_output_ref` n'a d'effet que lorsque `clip_vision_output` est également fourni.
- `audio_encoder_output`, lorsqu'il est fourni, attache des plongements audio, la fréquence d'images et l'échelle d'injection au conditionnement positif et négatif.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positif` | Le conditionnement positif avec tout latent d'image de départ, masque, CLIP vision ou données audio attachés. | CONDITIONING |
| `négatif` | Le conditionnement négatif avec tout latent d'image de départ, masque, CLIP vision ou données audio attachés. | CONDITIONING |
| `latent` | Un tenseur latent vide dimensionné pour la longueur, la hauteur et la largeur de vidéo demandées. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerVideo/fr.md)

---
**Source fingerprint (SHA-256):** `086a0ec361cf7f7ae7ce9505b55d31d92b025c6c7c9cde192009e6664011ad05`
