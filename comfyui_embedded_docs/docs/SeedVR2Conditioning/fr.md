# Appliquer le conditionnement SeedVR2

Ce nœud construit un conditionnement positif et négatif à partir d'un latent VAE pour une utilisation avec le modèle SeedVR2. Il ajoute un canal de masque au latent, puis l'associe aux plongements de conditionnement positifs et négatifs intégrés du modèle afin de produire les valeurs de conditionnement nécessaires à l'échantillonnage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `model` | Le modèle SeedVR2. | MODEL | Oui | - |
| `vae_conditioning` | Le latent VAE à partir duquel construire le conditionnement. Nom affiché : latent. | LATENT | Oui | - |

Le latent `vae_conditioning` doit être un tenseur 5D dans la disposition canal-en-premier de Comfy (B, C, T, H, W) avec le nombre de canaux attendu par le VAE SeedVR2. Les latents canal-en-dernier sont rejetés avec une erreur. L'entrée `model` doit être un modèle SeedVR2 valide avec la structure interne attendue.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `positive` | Le conditionnement positif pour l'échantillonnage. | CONDITIONING |
| `negative` | Le conditionnement négatif pour l'échantillonnage. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Conditioning/fr.md)

---
**Source fingerprint (SHA-256):** `28e508bdd776e2e3f5f2f93bfc29a1a1d1c34a11dbdc7f421d197ddbfa85f0f5`
