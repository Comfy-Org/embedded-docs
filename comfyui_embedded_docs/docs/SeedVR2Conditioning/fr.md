# Appliquer le Conditionnement SeedVR2

Ce nœud construit un conditionnement positif et négatif à partir d'un latent VAE pour une utilisation avec le modèle SeedVR2. Il prépare les données de conditionnement qui guident le processus de génération d'image ou de vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle SeedVR2. | MODEL | Oui | - |
| `vae_conditioning` | Le latent VAE à partir duquel construire le conditionnement. | LATENT | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model` | Le modèle SeedVR2. | MODEL |
| `positive` | Le conditionnement positif pour guider la génération. | CONDITIONING |
| `negative` | Le conditionnement négatif pour guider la génération. | CONDITIONING |
| `latent` | Les échantillons latents traités. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Conditioning/fr.md)

---
**Source fingerprint (SHA-256):** `8f99c0e712c5c6fc76261d6d72c5c08b7202c77827ecf2549240fc530c1b65bd`
