# VAEDecodeAudio

Ce nœud convertit une représentation latente audio en une forme d'onde audio lisible à l'aide d'un auto-encodeur variationnel (VAE). Il prend les échantillons encodés, les décode via le VAE sélectionné, puis normalise la forme d'onde résultante afin que le niveau de volume global reste constant. L'audio de sortie utilise le taux d'échantillonnage audio du VAE (44100 Hz par défaut), ou le taux d'échantillonnage stocké dans les `samples` d'entrée lorsqu'il est présent.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `samples` | Les échantillons audio encodés dans l'espace latent qui seront décodés pour redevenir une forme d'onde audio. Si les échantillons portent leur propre taux d'échantillonnage, cette valeur est utilisée pour la sortie. | LATENT | Oui | - |
| `vae` | Le modèle d'auto-encodeur variationnel utilisé pour décoder les échantillons latents en audio. Son taux d'échantillonnage de sortie audio (44100 Hz par défaut) détermine le taux d'échantillonnage de la forme d'onde résultante lorsque les échantillons d'entrée n'en spécifient pas. | VAE | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `AUDIO` | La forme d'onde audio décodée avec un volume normalisé, renvoyée avec son taux d'échantillonnage (le taux d'échantillonnage des `samples` d'entrée s'il est présent, sinon le taux d'échantillonnage audio du VAE, 44100 Hz par défaut). | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudio/fr.md)

---
**Source fingerprint (SHA-256):** `2a3f5c912d1d84eea7768979f6b8f0eaa9fe89041f3a3352434f38abd3c09fea`
