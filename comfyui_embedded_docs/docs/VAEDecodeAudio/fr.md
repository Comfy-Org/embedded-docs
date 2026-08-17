# VAEDecodeAudio

Le nœud VAEDecodeAudio convertit les représentations latentes en formes d'onde audio à l'aide d'un autoencodeur variationnel. Il prend les échantillons audio encodés et les traite via le VAE pour reconstruire l'audio d'origine, en appliquant une normalisation pour garantir des niveaux de sortie cohérents. L'audio résultant est renvoyé avec un taux d'échantillonnage standard de 44100 Hz, ou le taux d'échantillonnage des échantillons d'entrée s'il est fourni.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `samples` | Les échantillons audio encodés dans l'espace latent qui seront décodés en forme d'onde audio | LATENT | Oui | - |
| `vae` | Le modèle d'autoencodeur variationnel utilisé pour décoder les échantillons latents en audio | VAE | Oui | - |

Remarque : Si `samples` contient des données latentes imbriquées, seul le dernier élément est utilisé pour le décodage.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `AUDIO` | La forme d'onde audio décodée avec un volume normalisé et un taux d'échantillonnage (par défaut : 44100 Hz, ou le taux d'échantillonnage des `samples` d'entrée s'il est présent) | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudio/fr.md)

---
**Source fingerprint (SHA-256):** `2a3f5c912d1d84eea7768979f6b8f0eaa9fe89041f3a3352434f38abd3c09fea`
