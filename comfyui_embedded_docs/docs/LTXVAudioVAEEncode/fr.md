> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEEncode/fr.md)

Le nœud LTXV Audio VAE Encode prend une entrée audio et la compresse en une représentation latente plus petite à l'aide d'un modèle Audio VAE spécifié. Ce processus est essentiel pour générer ou manipuler de l'audio dans un workflow d'espace latent, car il convertit les données audio brutes en un format que les autres nœuds du pipeline peuvent comprendre et traiter.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `audio` | AUDIO | Oui | - | L'audio à encoder. |
| `audio_vae` | VAE | Oui | - | Le modèle Audio VAE à utiliser pour l'encodage. |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `Audio Latent` | LATENT | La représentation latente compressée de l'audio d'entrée. La sortie inclut les échantillons latents, le taux d'échantillonnage du modèle VAE et un identifiant de type. |

---
**Source fingerprint (SHA-256):** `fc10d8bbdca5150b7c87adb52960b8690397c3d003c89f9ec6a8410c541a347f`
