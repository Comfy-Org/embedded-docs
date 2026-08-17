# WanSoundImageToVideo

Le nœud WanSoundImageToVideo prépare la génération vidéo à partir d'images avec un conditionnement audio facultatif. Il prend des invites de conditionnement positive et négative ainsi qu'un modèle VAE pour construire les entrées de conditionnement et un tenseur latent vide, et peut intégrer des images de référence, un encodage audio, des vidéos de contrôle et des références de mouvement pour guider le processus de génération vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Invites de conditionnement positif qui guident le contenu devant apparaître dans la vidéo générée | CONDITIONING | Oui | - |
| `negative` | Invites de conditionnement négatif qui spécifient le contenu à éviter dans la vidéo générée | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder et décoder les représentations latentes de la vidéo | VAE | Oui | - |
| `width` | Largeur de la vidéo de sortie en pixels (par défaut : 832, doit être divisible par 16) | INT | Oui | 16 à MAX_RESOLUTION (pas : 16) |
| `height` | Hauteur de la vidéo de sortie en pixels (par défaut : 480, doit être divisible par 16) | INT | Oui | 16 à MAX_RESOLUTION (pas : 16) |
| `length` | Nombre d'images dans la vidéo générée (par défaut : 77, doit être divisible par 4) | INT | Oui | 1 à MAX_RESOLUTION (pas : 4) |
| `batch_size` | Nombre de vidéos à générer simultanément (par défaut : 1) | INT | Oui | 1 à 4096 |
| `audio_encoder_output` | Encodage audio facultatif pouvant influencer la génération vidéo selon les caractéristiques sonores. Lorsqu'il est fourni, les caractéristiques audio sont interpolées et utilisées pour conditionner la génération vidéo. | AUDIOENCODEROUTPUT | Non | - |
| `ref_image` | Image de référence facultative fournissant des indications visuelles pour le contenu vidéo. L'image est mise à l'échelle pour correspondre à la largeur et à la hauteur spécifiées, puis encodée en une représentation latente. Seule la première image du lot d'entrée est utilisée. | IMAGE | Non | - |
| `control_video` | Vidéo de contrôle facultative guidant le mouvement et la structure de la vidéo générée. La vidéo est mise à l'échelle et encodée, puis utilisée pour conditionner la sortie. Seules les premières images `length` sont utilisées. | IMAGE | Non | - |
| `ref_motion` | Référence de mouvement facultative fournissant des indications pour les schémas de mouvement dans la vidéo. Si l'entrée comporte plus de 73 images, seules les 73 dernières sont utilisées. Si moins de 73 images sont fournies, la séquence est complétée par des images neutres. | IMAGE | Non | - |

**Remarque :** Les entrées facultatives (`audio_encoder_output`, `ref_image`, `control_video`, `ref_motion`) peuvent être utilisées indépendamment ou combinées. Le conditionnement par vidéo de contrôle est toujours appliqué ; lorsqu'aucune `control_video` n'est fournie, une vidéo de contrôle vide (zéro) est utilisée.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif traité et modifié pour la génération vidéo. Lorsque les entrées facultatives correspondantes sont fournies, il inclut les plongements audio, les latents de référence, les références de mouvement et le conditionnement par vidéo de contrôle. | CONDITIONING |
| `negative` | Conditionnement négatif traité et modifié pour la génération vidéo. Lorsque les entrées facultatives correspondantes sont fournies, il inclut les plongements audio (mis à zéro), les latents de référence, les références de mouvement et le conditionnement par vidéo de contrôle. | CONDITIONING |
| `latent` | Tenseur latent vide servant de point de départ à la génération vidéo. Le latent a la forme [batch_size, 16, latent_t, height/8, width/8], où latent_t = ((length - 1) // 4) + 1. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `b1148cd00d8999dd6842e3c2fb13655fda8f20d5befed975a6d1652688b2807c`
