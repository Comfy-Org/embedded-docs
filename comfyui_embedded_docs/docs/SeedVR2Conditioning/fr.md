# Appliquer le conditionnement SeedVR2

Construit un conditionnement positif et négatif à partir d'un latent VAE pour une utilisation avec le modèle SeedVR2. Il valide le latent d'entrée et la structure du modèle, ajoute un canal de masque au latent et renvoie les deux sorties de conditionnement.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle SeedVR2. | MODEL | Oui | - |
| `vae_conditioning` | Le latent VAE SeedVR2 à partir duquel construire le conditionnement (nom d'affichage : latent). | LATENT | Oui | - |

Remarque : le latent `vae_conditioning` doit être un tenseur 5-D dans la disposition Comfy channel-first (B, C, T, H, W), où C correspond au nombre de canaux attendu pour le VAE SeedVR2. Le nœud lève une erreur si le latent n'est pas 5-D, si le nombre de canaux ne correspond pas, ou si le tenseur semble être dans une disposition channel-last. L'entrée `model` doit avoir la structure SeedVR2 attendue ; le nœud résout son modèle de diffusion interne et lit ses conditionnements positif et négatif. En interne, le nœud ajoute un canal de masque constant au latent et attache le conditionnement résultant aux sorties de conditionnement positif et négatif.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positive` | Le conditionnement positif pour l'échantillonnage. | CONDITIONING |
| `negative` | Le conditionnement négatif pour l'échantillonnage. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Conditioning/fr.md)

---
**Source fingerprint (SHA-256):** `28e508bdd776e2e3f5f2f93bfc29a1a1d1c34a11dbdc7f421d197ddbfa85f0f5`
