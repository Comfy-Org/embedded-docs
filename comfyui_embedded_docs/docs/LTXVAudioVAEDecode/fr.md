> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEDecode/fr.md)

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `samples` | LATENT | Oui | N/A | La représentation latente à décoder. |
| `audio_vae` | VAE | Oui | N/A | Le modèle Audio VAE utilisé pour décoder la représentation latente. |

**Note :** Si la représentation latente fournie est imbriquée (contient plusieurs latents), le nœud utilisera automatiquement le dernier latent de la séquence pour le décodage.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `Audio` | AUDIO | La forme d'onde audio décodée et sa fréquence d'échantillonnage associée. |
