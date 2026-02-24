> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEEncode/fr.md)

Le nœud LTXV Audio VAE Encode prend une entrée audio et la compresse en une représentation latente plus petite en utilisant un modèle Audio VAE spécifié. Ce processus est essentiel pour générer ou manipuler de l'audio dans un flux de travail utilisant l'espace latent, car il convertit les données audio brutes en un format que les autres nœuds de la chaîne peuvent comprendre et traiter.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Oui | - | L'audio à encoder. |
| `audio_vae` | VAE | Oui | - | Le modèle Audio VAE à utiliser pour l'encodage. |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `Audio Latent` | LATENT | La représentation latente compressée de l'audio d'entrée. La sortie comprend les échantillons latents, la fréquence d'échantillonnage du modèle VAE et un identifiant de type. |
