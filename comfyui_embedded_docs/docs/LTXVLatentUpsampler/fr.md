> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVLatentUpsampler/fr.md)

Le nœud LTXVLatentUpsampler augmente d’un facteur deux la résolution spatiale d’une représentation latente vidéo. Il utilise un modèle de suréchantillonnage spécialisé pour traiter les données latentes, qui sont d’abord dénormalisées puis renormalisées à l’aide des statistiques de canaux du VAE fourni. Ce nœud est conçu pour les workflows vidéo dans l’espace latent.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `échantillons` | LATENT | Oui | | La représentation latente d’entrée de la vidéo à suréchantillonner. |
| `modèle_d’agrandissement` | LATENT_UPSCALE_MODEL | Oui | | Le modèle chargé utilisé pour effectuer le suréchantillonnage 2x sur les données latentes. |
| `vae` | VAE | Oui | | Le modèle VAE utilisé pour dénormaliser les latentes d’entrée avant le suréchantillonnage et pour normaliser les latentes de sortie après. |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `LATENT` | LATENT | La représentation latente suréchantillonnée, dont les dimensions spatiales sont doublées par rapport à l’entrée. La latente de sortie conserve la même taille de lot, le même nombre de canaux et la même longueur temporelle que l’entrée. Le `noise_mask` de l’entrée, s’il est présent, est supprimé de la sortie. |

---
**Source fingerprint (SHA-256):** `b2c726d3a3e4881eee7e1d3bae8c478adf01cd87a9652be882579f4e26c1536f`
