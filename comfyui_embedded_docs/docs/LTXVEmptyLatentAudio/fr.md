# Audio latent vide LTXV

Le nœud LTXV Empty Latent Audio crée un lot de tenseurs audio latents vides (remplis de zéros). Il utilise la configuration d'un modèle Audio VAE fourni pour déterminer les dimensions correctes de l'espace latent, telles que le nombre de canaux et les bandes de fréquences. Ce latent vide sert de point de départ pour les workflows de génération ou de manipulation audio dans ComfyUI.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `frames_number` | Nombre d'images. La valeur par défaut est 97. | INT | Oui | 1 à 1000 |
| `frame_rate` | Nombre d'images par seconde. La valeur par défaut est 25. | INT | Oui | 1 à 1000 |
| `batch_size` | Le nombre d'échantillons audio latents dans le lot. La valeur par défaut est 1. | INT | Oui | 1 à 4096 |
| `audio_vae` | Le modèle Audio VAE pour obtenir la configuration. Ce paramètre est obligatoire. | VAE | Oui | N/A |

**Remarque :** L'entrée `audio_vae` est obligatoire. Le nœud générera une erreur si elle n'est pas fournie.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `Latent` | Un tenseur audio latent vide avec la structure (batch_size, z_channels, num_audio_latents, audio_freq) configurée pour correspondre à l'Audio VAE d'entrée. La sortie inclut également un champ `type` défini sur "audio". | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVEmptyLatentAudio/fr.md)

---
**Source fingerprint (SHA-256):** `1a8bfea98f14de014069016652b39542cfd9290cae2d870ab4e381e46aa1e08f`
