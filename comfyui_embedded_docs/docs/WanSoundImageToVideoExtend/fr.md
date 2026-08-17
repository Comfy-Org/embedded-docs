# Extension WanSoundImageToVideo

Le nœud WanSoundImageToVideoExtend étend un latent vidéo existant en générant des images supplémentaires, éventuellement guidé par l’audio, une image de référence et une vidéo de contrôle. Il prend un latent vidéo initial et produit une séquence vidéo plus longue, en utilisant le conditionnement fourni et les indices audio pour influencer le nouveau contenu.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `positive` | Invites de conditionnement positives qui guident le contenu vidéo souhaité | CONDITIONING | Oui | - |
| `negative` | Invites de conditionnement négatives qui précisent ce que la vidéo doit éviter | CONDITIONING | Oui | - |
| `vae` | Autoencodeur variationnel utilisé pour encoder et décoder les images vidéo | VAE | Oui | - |
| `length` | Nombre total d’images à générer pour la séquence vidéo (par défaut : 77, pas : 4) | INT | Oui | 1 to MAX_RESOLUTION |
| `video_latent` | Représentation latente vidéo initiale servant de point de départ pour l’extension. La largeur, la hauteur, la taille du lot et le décalage d’image sont dérivés de ce latent. Les 19 dernières images de ce latent sont également utilisées comme mouvement de référence pour la nouvelle séquence. | LATENT | Oui | - |
| `audio_encoder_output` | Plongements audio facultatifs pouvant influencer la génération vidéo en fonction des caractéristiques sonores. Lorsqu’ils sont fournis, l’audio est interpolé et utilisé pour créer un bucket de plongements audio qui est ajouté au conditionnement. | AUDIO_ENCODER_OUTPUT | Non | - |
| `ref_image` | Image de référence facultative fournissant un guidage visuel pour la génération vidéo. L’image est mise à l’échelle pour correspondre aux dimensions cibles puis encodée en un latent, qui est ensuite ajouté au conditionnement positif et négatif. Seule la première image du lot est utilisée. | IMAGE | Non | - |
| `control_video` | Vidéo de contrôle facultative pouvant guider le mouvement et le style de la vidéo générée. La vidéo est mise à l’échelle, encodée, puis ajoutée au conditionnement positif et négatif. La vidéo de contrôle est tronquée à la longueur spécifiée `length`. | IMAGE | Non | - |

Remarque : Lorsque `audio_encoder_output` est fourni, les plongements audio sont ajoutés au conditionnement positif, tandis que le conditionnement négatif reçoit les mêmes plongements mis à zéro. Le décalage d’image dérivé de `video_latent` détermine où les nouvelles images commencent dans la séquence audio. Si la séquence audio ne contient pas assez d’images pour couvrir l’extension demandée, aucun conditionnement audio n’est appliqué.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positive` | Conditionnement positif traité avec le contexte vidéo appliqué, y compris les plongements audio, les latents de référence, le mouvement de référence et la vidéo de contrôle si fournie | CONDITIONING |
| `negative` | Conditionnement négatif traité avec le contexte vidéo appliqué, y compris les plongements audio (mis à zéro), les latents de référence, le mouvement de référence et la vidéo de contrôle si fournie | CONDITIONING |
| `latent` | Représentation latente vidéo générée contenant la séquence vidéo étendue, initialisée à zéro avec des dimensions dérivées du `video_latent` d’entrée et de la `length` cible | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideoExtend/fr.md)

---
**Source fingerprint (SHA-256):** `32b58aaba566f346a0388ba804fc92e7ad426bf2e9e7039e5fdb0bf6a746e972`
