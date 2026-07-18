Le nœud `StableCascade_StageC_VAEEncode` traite les images via un encodeur VAE pour générer des représentations latentes destinées aux modèles Stable Cascade. Il prend une image en entrée et la compresse à l'aide du modèle VAE spécifié, puis produit deux représentations latentes : une pour l'étape C et un espace réservé pour l'étape B. Le paramètre de compression contrôle le facteur de réduction de l'image avant l'encodage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée à encoder dans l'espace latent | IMAGE | Oui | - |
| `vae` | Le modèle VAE utilisé pour encoder l'image | VAE | Oui | - |
| `compression` | Le facteur de compression appliqué à l'image avant l'encodage (par défaut : 42) | INT | Non | 4-128 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `stage_c` | La représentation latente encodée pour l'étape C du modèle Stable Cascade | LATENT |
| `stage_b` | Un espace réservé pour la représentation latente de l'étape B (retourne actuellement des zéros) | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageC_VAEEncode/fr.md)

---
**Source fingerprint (SHA-256):** `e7b9bd83d263903567ab06c00324575e01b79b50881fa807cd6f006955935c63`
