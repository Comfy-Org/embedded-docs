Ce document a été généré par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeAudio/en.md)

Le nœud VAEEncodeAudio convertit des données audio en une représentation latente à l'aide d'un autoencodeur variationnel (VAE). Il prend une entrée audio et la traite via le VAE pour générer des échantillons latents compressés pouvant être utilisés pour d'autres tâches de génération ou de manipulation audio. Le nœud rééchantillonne automatiquement l'audio pour correspondre au taux d'échantillonnage attendu du VAE si nécessaire avant l'encodage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `audio` | Les données audio à encoder, contenant les informations de forme d'onde et de taux d'échantillonnage | AUDIO | Oui | - |
| `vae` | Le modèle d'autoencodeur variationnel utilisé pour encoder l'audio dans l'espace latent | VAE | Oui | - |

**Remarque :** L'entrée audio est automatiquement rééchantillonnée pour correspondre au taux d'échantillonnage attendu du VAE (par défaut : 44100 Hz) si le taux d'échantillonnage d'origine diffère de cette valeur.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `LATENT` | La représentation audio encodée dans l'espace latent, contenant des échantillons compressés | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeAudio/fr.md)

---
**Source fingerprint (SHA-256):** `db509ab571154c4cedbfc6cae6591bd2b67b2c6e2261766565cdb0205b2c2ecc`
