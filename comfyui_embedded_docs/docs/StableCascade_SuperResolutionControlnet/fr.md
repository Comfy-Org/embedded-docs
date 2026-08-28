# StableCascade_SuperResolutionControlnet

Le nœud StableCascade_SuperResolutionControlnet prépare les entrées pour le traitement de super-résolution Stable Cascade. Il prend une image d'entrée et l'encode à l'aide d'un VAE pour créer une entrée controlnet, tout en générant également des représentations latentes d'espace réservé pour les étapes C et B du pipeline Stable Cascade.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée à traiter pour la super-résolution. Seuls les 3 premiers canaux de couleur (RVB) de l'image sont utilisés pour l'encodage. | IMAGE | Oui | - |
| `vae` | Le modèle VAE utilisé pour encoder l'image d'entrée | VAE | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `entrée_controlnet` | Représentation d'image encodée par VAE, adaptée à l'entrée controlnet | IMAGE |
| `étape_c` | Représentation latente d'espace réservé (remplie de zéros) pour l'étape C du traitement Stable Cascade, avec 16 canaux et des dimensions basées sur la taille de l'image d'entrée divisée par 16 | LATENT |
| `étape_b` | Représentation latente d'espace réservé (remplie de zéros) pour l'étape B du traitement Stable Cascade, avec 4 canaux et des dimensions basées sur la taille de l'image d'entrée divisée par 2 | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/fr.md)

---
**Source fingerprint (SHA-256):** `d9eff373ac7736f2e2f9788d1b43c04bb3212422aa1703d1d58ac512ce476925`
