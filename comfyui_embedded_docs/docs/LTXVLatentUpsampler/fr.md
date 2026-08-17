# LTXVLatentUpsampler

Le nœud LTXVLatentUpsampler augmente la résolution spatiale d'une représentation latente vidéo par un facteur de deux. Il utilise un modèle de suréchantillonnage spécialisé pour traiter les données latentes, qui sont d'abord dé-normalisées puis re-normalisées à l'aide des statistiques de canaux du VAE fourni. Ce nœud est conçu pour les flux de travail vidéo dans l'espace latent.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `samples` | La représentation latente d'entrée de la vidéo à suréchantillonner. | LATENT | Oui |  |
| `upscale_model` | Le modèle chargé utilisé pour effectuer le suréchantillonnage 2x sur les données latentes. | LATENT_UPSCALE_MODEL | Oui |  |
| `vae` | Le modèle VAE utilisé pour dé-normaliser les latents d'entrée avant le suréchantillonnage et pour normaliser les latents de sortie ensuite. | VAE | Oui |  |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `LATENT` | La représentation latente suréchantillonnée, avec des dimensions spatiales doublées par rapport à l'entrée. Le latent de sortie a la même taille de lot, le même nombre de canaux et la même longueur temporelle que l'entrée, et est reconverti au même type de données que les latents d'entrée. Le `noise_mask` de l'entrée, s'il est présent, est supprimé de la sortie. | LATENT |

Remarque : Ce nœud est marqué comme expérimental.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVLatentUpsampler/fr.md)

---
**Source fingerprint (SHA-256):** `7d7f0b733cb3758e9ec985cac30134d719b130b5b86c35bfdd14576a5b4575db`
