# StableCascade_SuperResolutionControlnet

Ce nœud fait partie du groupe expérimental Stable Cascade. Il prépare les entrées pour le traitement de super-résolution Stable Cascade en encodant une image d'entrée avec un VAE pour créer une entrée ControlNet, et en générant des espaces réservés latents vides (remplis de zéros) pour l'étape C et l'étape B du pipeline Stable Cascade.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée à traiter pour la super-résolution. Seuls les 3 premiers canaux de couleur (RGB) de l'image sont utilisés pour l'encodage. | IMAGE | Oui | - |
| `vae` | Le modèle VAE utilisé pour encoder l'image d'entrée | VAE | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `controlnet_input` | La représentation d'image encodée par le VAE, adaptée à une entrée ControlNet | IMAGE |
| `stage_c` | Représentation latente d'espace réservé (remplie de zéros) pour l'étape C du traitement Stable Cascade, avec 16 canaux et des dimensions basées sur la taille de l'image d'entrée divisée par 16 | LATENT |
| `stage_b` | Représentation latente d'espace réservé (remplie de zéros) pour l'étape B du traitement Stable Cascade, avec 4 canaux et des dimensions basées sur la taille de l'image d'entrée divisée par 2 | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/fr.md)

---
**Source fingerprint (SHA-256):** `d9eff373ac7736f2e2f9788d1b43c04bb3212422aa1703d1d58ac512ce476925`
