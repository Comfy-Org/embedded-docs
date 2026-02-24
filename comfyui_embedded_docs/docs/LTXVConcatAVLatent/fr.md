> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConcatAVLatent/fr.md)

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `video_latent` | LATENT | Oui | | La représentation latente des données vidéo. |
| `audio_latent` | LATENT | Oui | | La représentation latente des données audio. |

**Note :** Les tenseurs `samples` des entrées `video_latent` et `audio_latent` sont concaténés. Si l'une des entrées contient un `noise_mask`, il sera utilisé ; si l'un est manquant, un masque de valeurs un (de même forme que le `samples` correspondant) est créé pour celui-ci. Les masques résultants sont ensuite également concaténés.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `latent` | LATENT | Un dictionnaire latent unique contenant les `samples` concaténés et, le cas échéant, le `noise_mask` concaténé provenant des entrées vidéo et audio. |
