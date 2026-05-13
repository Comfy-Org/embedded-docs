> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVEmptyLatentAudio/fr.md)

Le nœud LTXV Empty Latent Audio crée un lot de tenseurs audio latents vides (remplis de zéros). Il utilise la configuration d'un modèle Audio VAE fourni pour déterminer les dimensions correctes de l'espace latent, telles que le nombre de canaux et les bandes de fréquences. Ce latent vide sert de point de départ pour les workflows de génération ou de manipulation audio dans ComfyUI.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `frames_number` | INT | Oui | 1 à 1000 | Nombre d'images. La valeur par défaut est 97. |
| `frame_rate` | INT | Oui | 1 à 1000 | Nombre d'images par seconde. La valeur par défaut est 25. |
| `batch_size` | INT | Oui | 1 à 4096 | Le nombre d'échantillons audio latents dans le lot. La valeur par défaut est 1. |
| `audio_vae` | VAE | Oui | N/A | Le modèle Audio VAE pour obtenir la configuration. Ce paramètre est obligatoire. |

**Remarque :** L'entrée `audio_vae` est obligatoire. Le nœud générera une erreur si elle n'est pas fournie.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `Latent` | LATENT | Un tenseur audio latent vide avec la structure (batch_size, z_channels, num_audio_latents, audio_freq) configurée pour correspondre à l'Audio VAE d'entrée. La sortie inclut également un champ `type` défini sur "audio". |

---
**Source fingerprint (SHA-256):** `1a8bfea98f14de014069016652b39542cfd9290cae2d870ab4e381e46aa1e08f`
