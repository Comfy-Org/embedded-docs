# Audio latent vide LTXV

Le nœud LTXV Empty Latent Audio crée un lot de tenseurs latents audio vides (remplis de zéros). Il utilise la configuration d'un modèle Audio VAE fourni pour déterminer les dimensions correctes de l'espace latent, telles que le nombre de canaux et les bins de fréquence. Le nombre de latents audio est calculé à partir du nombre d'images et de la fréquence d'images à l'aide du modèle Audio VAE. Ce latent vide sert de point de départ pour les flux de travail de génération ou de manipulation audio dans ComfyUI.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `frames_number` | Nombre d'images. Par défaut : 97. | INT | Oui | 1 à 1000 |
| `frame_rate` | Nombre d'images par seconde. Accepte des valeurs flottantes ou entières. Par défaut : 25.0. | FLOAT (ou INT) | Oui | 1.0 à 1000.0 |
| `batch_size` | Le nombre d'échantillons latents audio dans le lot. Par défaut : 1. | INT | Oui | 1 à 4096 |
| `audio_vae` | Le modèle Audio VAE à partir duquel obtenir la configuration. | VAE | Oui | N/A |

**Remarque :** Le paramètre `audio_vae` est obligatoire. Le nœud lèvera une erreur s'il n'est pas fourni.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `Latent` | Un tenseur latent audio vide avec la structure (batch_size, z_channels, num_audio_latents, audio_freq), configuré pour correspondre à l'Audio VAE d'entrée. La sortie inclut également un champ `type` défini sur "audio". | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVEmptyLatentAudio/fr.md)

---
**Source fingerprint (SHA-256):** `3ac1bf17ebdba7c3a73bdd795f561b7bee31798d8a1efc11b972db1944f873a4`
