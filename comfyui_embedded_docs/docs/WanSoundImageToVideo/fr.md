# WanSoundImageToVideo

Le nœud WanSoundImageToNode génère du contenu vidéo à partir d’images avec un conditionnement audio facultatif. Il accepte des inviteurs de conditionnement positive et négative ainsi qu’un modèle VAE pour créer des latents vidéo, et peut intégrer des images de référence, un encodage audio, des vidéos de contrôle et des références de mouvement pour guider le processus de génération vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | Invites de conditionnement positives qui guident le contenu qui doit apparaître dans la vidéo générée | CONDITIONING | Oui | - |
| `négatif` | Invites de conditionnement négatives qui spécifient le contenu à éviter dans la vidéo générée | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder et décoder les représentations latentes de la vidéo | VAE | Oui | - |
| `largeur` | Largeur de la vidéo de sortie en pixels (par défaut : 832, doit être divisible par 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | Hauteur de la vidéo de sortie en pixels (par défaut : 480, doit être divisible par 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `longueur` | Nombre d’images dans la vidéo générée (par défaut : 77, doit être divisible par 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `taille_lot` | Nombre de vidéos à générer simultanément (par défaut : 1) | INT | Oui | 1 à 4096 |
| `sortie_encodeur_audio` | Encodage audio facultatif pouvant influencer la génération vidéo en fonction des caractéristiques sonores. Lorsqu’il est fourni, les caractéristiques audio sont interpolées et utilisées pour conditionner la génération vidéo. | AUDIO_ENCODER_OUTPUT | Non | - |
| `image_référence` | Image de référence facultative fournissant un guidage visuel pour le contenu vidéo. L’image est agrandie pour correspondre à la largeur et à la hauteur spécifiées, puis encodée en une représentation latente. Seule la première image de l’entrée est utilisée comme référence. | IMAGE | Non | - |
| `vidéo de contrôle` | Vidéo de contrôle facultative qui guide le mouvement et la structure de la vidéo générée. La vidéo est agrandie et encodée, puis utilisée pour conditionner la sortie. Seules les premières images `length` sont utilisées. | IMAGE | Non | - |
| `mouvement de référence` | Référence de mouvement facultative fournissant un guidage pour les schémas de mouvement dans la vidéo. Si l’entrée contient plus de 73 images, seules les 73 dernières sont utilisées. Si moins de 73 images sont fournies, la séquence est complétée par des images neutres. | IMAGE | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positif` | Conditionnement positif traité et modifié pour la génération vidéo, incluant les plongements audio, les latents de référence, les références de mouvement et le conditionnement par vidéo de contrôle | CONDITIONING |
| `négatif` | Conditionnement négatif traité et modifié pour la génération vidéo, incluant les plongements audio (mis à zéro), les latents de référence, les références de mouvement et le conditionnement par vidéo de contrôle | CONDITIONING |
| `latent` | Représentation vidéo générée dans l’espace latent, pouvant être décodée en images vidéo finales. Le tenseur latent a la forme [batch_size, 16, latent_t, height/8, width/8] où latent_t est dérivé du paramètre `length` | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `b1148cd00d8999dd6842e3c2fb13655fda8f20d5befed975a6d1652688b2807c`
