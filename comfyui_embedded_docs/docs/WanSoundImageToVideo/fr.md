# WanSoundImageToVideo

Le nœud WanSoundImageToVideo génère du contenu vidéo à partir d'images avec un conditionnement audio optionnel. Il utilise des prompts de conditionnement positifs et négatifs ainsi qu'un modèle VAE pour créer des latents vidéo, et peut intégrer des images de référence, un encodage audio, des vidéos de contrôle et des références de mouvement pour guider le processus de génération vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | Prompts de conditionnement positifs qui guident le contenu à faire apparaître dans la vidéo générée | CONDITIONING | Oui | - |
| `négatif` | Prompts de conditionnement négatifs qui spécifient le contenu à éviter dans la vidéo générée | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder et décoder les représentations latentes vidéo | VAE | Oui | - |
| `largeur` | Largeur de la vidéo de sortie en pixels (par défaut : 832, doit être divisible par 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | Hauteur de la vidéo de sortie en pixels (par défaut : 480, doit être divisible par 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `longueur` | Nombre d'images dans la vidéo générée (par défaut : 77, doit être divisible par 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `taille_lot` | Nombre de vidéos à générer simultanément (par défaut : 1) | INT | Oui | 1 à 4096 |
| `sortie_encodeur_audio` | Encodage audio optionnel pouvant influencer la génération vidéo en fonction des caractéristiques sonores | AUDIOENCODEROUTPUT | Non | - |
| `image_référence` | Image de référence optionnelle fournissant un guide visuel pour le contenu vidéo | IMAGE | Non | - |
| `vidéo de contrôle` | Vidéo de contrôle optionnelle guidant le mouvement et la structure de la vidéo générée | IMAGE | Non | - |
| `mouvement de référence` | Référence de mouvement optionnelle fournissant un guide pour les schémas de déplacement dans la vidéo | IMAGE | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `négatif` | Conditionnement positif traité et modifié pour la génération vidéo | CONDITIONING |
| `latent` | Conditionnement négatif traité et modifié pour la génération vidéo | CONDITIONING |
| `latent` | Représentation vidéo générée dans l'espace latent, pouvant être décodée en images vidéo finales | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `f80f82b8671294a14ecfecf91bc13febae0c91c5efa438467a4413d52dc82d3f`
