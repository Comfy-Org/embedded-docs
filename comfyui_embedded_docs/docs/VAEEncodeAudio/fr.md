# VAEEncodeAudio

Le nœud VAEEncodeAudio convertit des données audio en une représentation latente à l'aide d'un autoencodeur variationnel (VAE). Il prend une entrée audio et la traite via le VAE pour générer des échantillons latents compressés pouvant être utilisés pour d'autres tâches de génération ou de manipulation audio. Le nœud rééchantillonne automatiquement l'audio pour correspondre au taux d'échantillonnage attendu par le VAE si nécessaire avant l'encodage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `audio` | Les données audio à encoder, contenant la forme d'onde et les informations de taux d'échantillonnage | AUDIO | Oui | - |
| `vae` | Le modèle d'autoencodeur variationnel utilisé pour encoder l'audio dans l'espace latent | VAE | Oui | - |

**Remarque :** L'entrée audio est automatiquement rééchantillonnée pour correspondre au taux d'échantillonnage attendu par le VAE (par défaut : 44100 Hz) si le taux d'échantillonnage d'origine diffère de cette valeur. Si l'audio d'entrée est `None` (par exemple, si la vidéo source n'a pas de piste audio), le nœud génèrera une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `LATENT` | La représentation audio encodée dans l'espace latent, contenant des échantillons compressés | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeAudio/fr.md)

---
**Source fingerprint (SHA-256):** `224563af40a377a37209b26ec8becf035560da273b18293634f684e18c5e63ed`
