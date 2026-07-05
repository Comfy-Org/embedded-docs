# StableCascade_SuperResolutionControlnet

Le nœud **StableCascade_SuperResolutionControlnet** prépare les entrées pour le traitement de super-résolution Stable Cascade. Il prend une image d'entrée et l'encode à l'aide d'un VAE pour créer une entrée de controlnet, tout en générant des représentations latentes de substitution pour l'étape C et l'étape B du pipeline Stable Cascade.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée à traiter pour la super-résolution | IMAGE | Oui | - |
| `vae` | Le modèle VAE utilisé pour encoder l'image d'entrée | VAE | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `étape_c` | La représentation encodée de l'image adaptée à l'entrée du controlnet | IMAGE |
| `étape_b` | Représentation latente de substitution pour l'étape C du traitement Stable Cascade | LATENT |
| `stage_b` | Représentation latente de substitution pour l'étape B du traitement Stable Cascade | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/fr.md)

---
**Source fingerprint (SHA-256):** `78b6e5a02c48ac37a205ef9d8532a3aca19134de4ec7be98b2ee55969dab7b53`
