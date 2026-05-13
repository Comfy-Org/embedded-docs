> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/fr.md)

Le nœud **StableCascade_SuperResolutionControlnet** prépare les entrées pour le traitement de super-résolution Stable Cascade. Il prend une image d'entrée et l'encode à l'aide d'un VAE pour créer une entrée de controlnet, tout en générant des représentations latentes de substitution pour l'étape C et l'étape B du pipeline Stable Cascade.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée à traiter pour la super-résolution |
| `vae` | VAE | Oui | - | Le modèle VAE utilisé pour encoder l'image d'entrée |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `étape_c` | IMAGE | La représentation encodée de l'image adaptée à l'entrée du controlnet |
| `étape_b` | LATENT | Représentation latente de substitution pour l'étape C du traitement Stable Cascade |
| `stage_b` | LATENT | Représentation latente de substitution pour l'étape B du traitement Stable Cascade |

---
**Source fingerprint (SHA-256):** `78b6e5a02c48ac37a205ef9d8532a3aca19134de4ec7be98b2ee55969dab7b53`
