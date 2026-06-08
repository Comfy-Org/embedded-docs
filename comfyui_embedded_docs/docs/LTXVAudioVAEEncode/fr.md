Le nœud LTXV Audio VAE Encode prend une entrée audio et la compresse en une représentation latente plus petite à l'aide d'un modèle Audio VAE spécifié. Ce processus est essentiel pour générer ou manipuler de l'audio dans un workflow d'espace latent, car il convertit les données audio brutes en un format que les autres nœuds du pipeline peuvent comprendre et traiter.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `audio` | L'audio à encoder. | AUDIO | Oui | - |
| `audio_vae` | Le modèle Audio VAE à utiliser pour l'encodage. | VAE | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `Audio Latent` | La représentation latente compressée de l'audio d'entrée. La sortie inclut les échantillons latents, le taux d'échantillonnage du modèle VAE et un identifiant de type. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEEncode/fr.md)

---
**Source fingerprint (SHA-256):** `fc10d8bbdca5150b7c87adb52960b8690397c3d003c89f9ec6a8410c541a347f`
