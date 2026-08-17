# StableCascade_StageC_VAEEncode

Le nœud StableCascade_StageC_VAEEncode traite une image d'entrée via un encodeur VAE pour générer des représentations latentes pour le modèle Stable Cascade. Il redimensionne d'abord l'image en fonction d'un facteur de compression et du taux de réduction du VAE, puis encode l'image redimensionnée. Le nœud produit deux tenseurs latents : un pour l'étape C (le résultat réellement encodé) et un pour l'étape B (un espace réservé rempli de zéros).

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée à encoder dans l'espace latent | IMAGE | Oui | - |
| `vae` | Le modèle VAE utilisé pour encoder l'image | VAE | Oui | - |
| `compression` | Le facteur de compression appliqué à l'image avant l'encodage. Les dimensions de l'image sont divisées par cette valeur, puis multipliées par le taux de réduction du VAE. (défaut : 42) | INT | Non | 4-128 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `stage_c` | La représentation latente encodée pour l'étape C du modèle Stable Cascade | LATENT |
| `stage_b` | Une représentation latente de remplacement pour l'étape B. Renvoie actuellement un tenseur rempli de zéros dont les dimensions sont calculées à partir de la taille de l'image d'entrée. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageC_VAEEncode/fr.md)

---
**Source fingerprint (SHA-256):** `1679aaac77057fcc359e5428906d5227f6c2dde721aabbfb5a32c08738ac376c`
