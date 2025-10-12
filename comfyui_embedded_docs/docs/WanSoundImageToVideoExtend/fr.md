> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideoExtend/fr.md)

Le nœud WanSoundImageToVideoExtend étend la génération d'image-à-vidéo en incorporant un conditionnement audio et des images de référence. Il prend des conditionnements positifs et négatifs ainsi que des données latentes vidéo et des embeddings audio optionnels pour générer des séquences vidéo étendues. Le nœud traite ces entrées pour créer des sorties vidéo cohérentes qui peuvent être synchronisées avec des repères audio.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Oui | - | Conditionnements positifs qui guident ce que la vidéo doit inclure |
| `negative` | CONDITIONING | Oui | - | Conditionnements négatifs qui spécifient ce que la vidéo doit éviter |
| `vae` | VAE | Oui | - | Autoencodeur variationnel utilisé pour l'encodage et le décodage des images vidéo |
| `length` | INT | Oui | 1 à MAX_RESOLUTION | Nombre d'images à générer pour la séquence vidéo (par défaut : 77, pas : 4) |
| `video_latent` | LATENT | Oui | - | Représentation latente vidéo initiale qui sert de point de départ pour l'extension |
| `audio_encoder_output` | AUDIOENCODEROUTPUT | Non | - | Embeddings audio optionnels qui peuvent influencer la génération vidéo en fonction des caractéristiques sonores |
| `ref_image` | IMAGE | Non | - | Image de référence optionnelle qui fournit un guide visuel pour la génération vidéo |
| `control_video` | IMAGE | Non | - | Vidéo de contrôle optionnelle qui peut guider le mouvement et le style de la vidéo générée |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Conditionnement positif traité avec le contexte vidéo appliqué |
| `negative` | CONDITIONING | Conditionnement négatif traité avec le contexte vidéo appliqué |
| `latent` | LATENT | Représentation latente vidéo générée contenant la séquence vidéo étendue |
