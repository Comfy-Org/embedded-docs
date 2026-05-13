> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudioTiled/fr.md)

Ce nœud convertit une représentation audio compressée (échantillons latents) en une forme d'onde audio à l'aide d'un autoencodeur variationnel (VAE). Il traite les données en sections plus petites et chevauchantes (tuiles) pour gérer l'utilisation de la mémoire, ce qui le rend adapté au traitement de séquences audio plus longues.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `échantillons` | LATENT | Oui | N/D | La représentation latente compressée de l'audio à décoder. |
| `vae` | VAE | Oui | N/D | Le modèle d'autoencodeur variationnel utilisé pour effectuer le décodage. |
| `taille de tuile` | INT | Oui | 32 à 8192 | La taille de chaque tuile de traitement. L'audio est décodé en sections de cette longueur pour économiser la mémoire (par défaut : 512). |
| `chevauchement` | INT | Oui | 0 à 1024 | Le nombre d'échantillons sur lesquels les tuiles adjacentes se chevauchent. Cela permet de réduire les artefacts aux limites entre les tuiles (par défaut : 64). |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | AUDIO | La forme d'onde audio décodée. |

---
**Source fingerprint (SHA-256):** `d989f0cd0e4b4bf992d6860e27c25b8e814df52763c82909a61c58f418306352`
