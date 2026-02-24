> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVLatentUpsampler/fr.md)

## Vue d'ensemble

Le nœud LTXVLatentUpsampler augmente la résolution spatiale d'une représentation latente vidéo d'un facteur deux. Il utilise un modèle de suréchantillonnage spécialisé pour traiter les données latentes, qui sont d'abord dé-normalisées puis re-normalisées en utilisant les statistiques des canaux du VAE fourni. Ce nœud est conçu pour les flux de travail vidéo dans l'espace latent.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `samples` | LATENT | Oui | | La représentation latente d'entrée de la vidéo à suréchantillonner. |
| `upscale_model` | LATENT_UPSCALE_MODEL | Oui | | Le modèle chargé utilisé pour effectuer le suréchantillonnage 2x sur les données latentes. |
| `vae` | VAE | Oui | | Le modèle VAE utilisé pour dé-normaliser les latents d'entrée avant le suréchantillonnage et pour normaliser les latents de sortie par la suite. |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `LATENT` | LATENT | La représentation latente suréchantillonnée, dont les dimensions spatiales sont doublées par rapport à l'entrée. |
