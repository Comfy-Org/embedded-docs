> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateAVLatent/fr.md)

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `av_latent` | LATENT | Oui | N/A | La représentation latente audio-visuelle combinée à séparer. |

**Note :** Le tenseur `samples` du latent d'entrée doit comporter au moins deux éléments le long de la première dimension (dimension du lot). Le premier élément est utilisé pour le latent vidéo, et le second élément est utilisé pour le latent audio. Si un `noise_mask` est présent, il est divisé de la même manière.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `video_latent` | LATENT | La représentation latente contenant les données vidéo séparées. |
| `audio_latent` | LATENT | La représentation latente contenant les données audio séparées. |
