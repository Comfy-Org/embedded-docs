> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeAudio/fr.md)

Le nœud VAEEncodeAudio convertit des données audio en une représentation latente en utilisant un Autoencodeur Variationnel (VAE). Il prend une entrée audio et la traite à travers le VAE pour générer des échantillons latents compressés qui peuvent être utilisés pour des tâches de génération ou de manipulation audio ultérieures. Le nœud rééchantillonne automatiquement l'audio à 44100 Hz si nécessaire avant l'encodage.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Oui | - | Les données audio à encoder, contenant les informations de forme d'onde et de taux d'échantillonnage |
| `vae` | VAE | Oui | - | Le modèle d'Autoencodeur Variationnel utilisé pour encoder l'audio dans l'espace latent |

**Note :** L'entrée audio est automatiquement rééchantillonnée à 44100 Hz si le taux d'échantillonnage original diffère de cette valeur.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `LATENT` | LATENT | La représentation audio encodée dans l'espace latent, contenant des échantillons compressés |