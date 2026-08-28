# Appliquer le conditionnement SeedVR2

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle SeedVR2. | MODEL | Oui | - |
| `vae_conditioning` | Le latent VAE SeedVR2 à partir duquel construire le conditionnement (nom d’affichage : latent). | LATENT | Oui | - |

Note : Le latent `vae_conditioning` doit être un tenseur 5D dans la disposition de Comfy avec les canaux en premier (B, C, T, H, W), où C correspond au nombre de canaux attendu du VAE SeedVR2. Le nœud génère une erreur si le latent n’est pas en 5D, si son nombre de canaux ne correspond pas, ou s’il semble être dans une disposition avec les canaux en dernier. L’entrée `model` doit être un modèle avec la structure SeedVR2 attendue. En interne, le nœud ajoute un canal de masque constant au latent et attache le conditionnement résultant aux deux ensembles de conditionnement positif et négatif.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positive` | Le conditionnement positif pour l’échantillonnage. | CONDITIONING |
| `negative` | Le conditionnement négatif pour l’échantillonnage. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Conditioning/fr.md)

---
**Source fingerprint (SHA-256):** `28e508bdd776e2e3f5f2f93bfc29a1a1d1c34a11dbdc7f421d197ddbfa85f0f5`
