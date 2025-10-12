> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudio/fr.md)

Le nœud VAEDecodeAudio convertit les représentations latentes en formes d'onde audio en utilisant un Autoencodeur Variationnel. Il prend des échantillons audio encodés et les traite à travers le VAE pour reconstruire l'audio original, en appliquant une normalisation pour assurer des niveaux de sortie cohérents. L'audio résultant est retourné avec un taux d'échantillonnage standard de 44100 Hz.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `samples` | LATENT | Oui | - | Les échantillons audio encodés dans l'espace latent qui seront décodés en forme d'onde audio |
| `vae` | VAE | Oui | - | Le modèle d'Autoencodeur Variationnel utilisé pour décoder les échantillons latents en audio |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `AUDIO` | AUDIO | La forme d'onde audio décodée avec volume normalisé et taux d'échantillonnage de 44100 Hz |