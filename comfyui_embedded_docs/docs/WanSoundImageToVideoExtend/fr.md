> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideoExtend/fr.md)

Le nœud WanSoundImageToVideoExtend étend un latent vidéo existant en générant des trames supplémentaires, guidé optionnellement par un fichier audio, une image de référence et une vidéo de contrôle. Il prend un latent vidéo de départ et produit une séquence vidéo plus longue, en utilisant les conditionnements et les indices audio fournis pour influencer le nouveau contenu.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `positive` | CONDITIONING | Oui | - | Prompts de conditionnement positif qui guident le contenu de la vidéo |
| `negative` | CONDITIONING | Oui | - | Prompts de conditionnement négatif qui spécifient ce que la vidéo doit éviter |
| `vae` | VAE | Oui | - | Autoencodeur variationnel utilisé pour encoder et décoder les trames vidéo |
| `length` | INT | Oui | 1 à MAX_RESOLUTION | Nombre total de trames à générer pour la séquence vidéo (par défaut : 77, pas : 4) |
| `video_latent` | LATENT | Oui | - | Représentation latente vidéo initiale servant de point de départ pour l'extension |
| `audio_encoder_output` | AUDIOENCODEROUTPUT | Non | - | Plongements audio optionnels pouvant influencer la génération vidéo en fonction des caractéristiques sonores |
| `ref_image` | IMAGE | Non | - | Image de référence optionnelle fournissant un guidage visuel pour la génération vidéo |
| `control_video` | IMAGE | Non | - | Vidéo de contrôle optionnelle pouvant guider le mouvement et le style de la vidéo générée |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `positive` | CONDITIONING | Conditionnement positif traité avec le contexte vidéo appliqué |
| `negative` | CONDITIONING | Conditionnement négatif traité avec le contexte vidéo appliqué |
| `latent` | LATENT | Représentation latente vidéo générée contenant la séquence vidéo étendue |

---
**Source fingerprint (SHA-256):** `fc9aee5d51e96b864da7d75f592f07691be8b970346998b209b3ad8a72308ecb`
