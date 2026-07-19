# VAEDecodeAudio

Le nœud VAEDecodeAudio convertit les représentations latentes en formes d'onde audio à l'aide d'un autoencodeur variationnel (VAE). Il prend des échantillons audio encodés et les traite via le VAE pour reconstruire l'audio original, en appliquant une normalisation pour garantir des niveaux de sortie cohérents. L'audio résultant est renvoyé avec une fréquence d'échantillonnage standard de 44100 Hz.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `échantillons` | Les échantillons audio encodés dans l'espace latent qui seront décodés en forme d'onde audio | LATENT | Oui | - |
| `vae` | Le modèle d'autoencodeur variationnel utilisé pour décoder les échantillons latents en audio | VAE | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `AUDIO` | La forme d'onde audio décodée avec volume normalisé et fréquence d'échantillonnage de 44100 Hz | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudio/fr.md)

---
**Source fingerprint (SHA-256):** `15848d3763324cbae986949146d57352c68369713cd99a27d216797560836824`
