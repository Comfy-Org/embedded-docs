# WanDancerVideo

WanDancerVideo prépare les données de conditionnement et un tenseur latent vide pour la génération vidéo avec le modèle WanDancer. Il prend un conditionnement positif et négatif et les combine facultativement avec une image de départ, un masque, des embeddings de vision CLIP et des caractéristiques audio pour contrôler la vidéo générée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Le conditionnement positif pour guider la génération vidéo. | CONDITIONING | Oui |  |
| `negative` | Le conditionnement négatif pour guider la génération vidéo. | CONDITIONING | Oui |  |
| `vae` | Le VAE utilisé pour encoder l'image de départ dans l'espace latent. | VAE | Oui |  |
| `width` | La largeur de la vidéo générée en pixels (défaut : 480). | INT | Oui | 16 à MAX_RESOLUTION (pas : 16) |
| `height` | La hauteur de la vidéo générée en pixels (défaut : 832). | INT | Oui | 16 à MAX_RESOLUTION (pas : 16) |
| `length` | Le nombre d'images (frames) de la vidéo générée. Doit rester 149 pour WanDancer (défaut : 149). | INT | Oui | 1 à MAX_RESOLUTION (pas : 4) |
| `clip_vision_output` | Les embeddings de vision CLIP pour la première image. | CLIP_VISION_OUTPUT | Non |  |
| `clip_vision_output_ref` | Les embeddings de vision CLIP pour l'image de référence. | CLIP_VISION_OUTPUT | Non |  |
| `start_image` | L'image ou les images initiales à encoder, peut être un nombre quelconque d'images. | IMAGE | Non |  |
| `mask` | Masque de conditionnement d'image pour la ou les images de départ. Le blanc est conservé, le noir est généré. Utilisé pour les générations locales. | MASK | Non |  |
| `audio_encoder_output` | La sortie d'un encodeur audio, fournissant les caractéristiques audio, le FPS et l'échelle d'injection audio pour la génération conditionnée par l'audio. | AUDIO_ENCODER_OUTPUT | Non |  |

**Remarque sur les contraintes des paramètres :**
- Lorsque `start_image` est fourni, l'image est redimensionnée à `width` × `height`, limitée à `length` images, et encodée en un latent qui est ajouté aux deux conditionnements avec un masque de concaténation.
- `mask` n'a d'effet que lorsque `start_image` est également fourni. Dans le masque, les zones blanches sont conservées et les zones noires sont générées. Quand `mask` n'est pas fourni, la zone de l'image de départ est utilisée comme guide de conditionnement et les images restantes sont générées.
- `clip_vision_output_ref` n'est appliqué que lorsque `clip_vision_output` est fourni.
- `audio_encoder_output` ajoute les caractéristiques audio, le FPS et une échelle d'injection audio (défaut 1.0) aux deux conditionnements.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Le conditionnement positif avec toutes les données supplémentaires (latent concaténé, vision CLIP, audio) ajoutées. | CONDITIONING |
| `negative` | Le conditionnement négatif avec toutes les données supplémentaires (latent concaténé, vision CLIP, audio) ajoutées. | CONDITIONING |
| `latent` | Un tenseur latent vide dont les dimensions correspondent à la longueur, la hauteur et la largeur de la vidéo spécifiées. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerVideo/fr.md)

---
**Source fingerprint (SHA-256):** `086a0ec361cf7f7ae7ce9505b55d31d92b025c6c7c9cde192009e6664011ad05`
