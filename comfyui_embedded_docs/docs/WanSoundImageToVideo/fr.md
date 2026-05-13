> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideo/fr.md)

Le nœud WanSoundImageToVideo génère du contenu vidéo à partir d'images avec un conditionnement audio optionnel. Il utilise des prompts de conditionnement positifs et négatifs ainsi qu'un modèle VAE pour créer des latents vidéo, et peut intégrer des images de référence, un encodage audio, des vidéos de contrôle et des références de mouvement pour guider le processus de génération vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `positif` | CONDITIONING | Oui | - | Prompts de conditionnement positifs qui guident le contenu à faire apparaître dans la vidéo générée |
| `négatif` | CONDITIONING | Oui | - | Prompts de conditionnement négatifs qui spécifient le contenu à éviter dans la vidéo générée |
| `vae` | VAE | Oui | - | Modèle VAE utilisé pour encoder et décoder les représentations latentes vidéo |
| `largeur` | INT | Oui | 16 à MAX_RESOLUTION | Largeur de la vidéo de sortie en pixels (par défaut : 832, doit être divisible par 16) |
| `hauteur` | INT | Oui | 16 à MAX_RESOLUTION | Hauteur de la vidéo de sortie en pixels (par défaut : 480, doit être divisible par 16) |
| `longueur` | INT | Oui | 1 à MAX_RESOLUTION | Nombre d'images dans la vidéo générée (par défaut : 77, doit être divisible par 4) |
| `taille_lot` | INT | Oui | 1 à 4096 | Nombre de vidéos à générer simultanément (par défaut : 1) |
| `sortie_encodeur_audio` | AUDIOENCODEROUTPUT | Non | - | Encodage audio optionnel pouvant influencer la génération vidéo en fonction des caractéristiques sonores |
| `image_référence` | IMAGE | Non | - | Image de référence optionnelle fournissant un guide visuel pour le contenu vidéo |
| `vidéo de contrôle` | IMAGE | Non | - | Vidéo de contrôle optionnelle guidant le mouvement et la structure de la vidéo générée |
| `mouvement de référence` | IMAGE | Non | - | Référence de mouvement optionnelle fournissant un guide pour les schémas de déplacement dans la vidéo |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `négatif` | CONDITIONING | Conditionnement positif traité et modifié pour la génération vidéo |
| `latent` | CONDITIONING | Conditionnement négatif traité et modifié pour la génération vidéo |
| `latent` | LATENT | Représentation vidéo générée dans l'espace latent, pouvant être décodée en images vidéo finales |

---
**Source fingerprint (SHA-256):** `f80f82b8671294a14ecfecf91bc13febae0c91c5efa438467a4413d52dc82d3f`
