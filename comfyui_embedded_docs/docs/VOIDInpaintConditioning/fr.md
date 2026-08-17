# VOIDInpaintConditioning

Le nœud VOIDInpaintConditioning prépare les données de conditionnement nécessaires pour l'inpainting avec les modèles CogVideoX. Il prend une vidéo source et un quadmask prétraité, les encode via le VAE, et les combine en un signal de conditionnement à 32 canaux (16 canaux de masque + 16 canaux de vidéo masquée) que le modèle utilise pour remplir les zones masquées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Le conditionnement positif à augmenter avec les informations latentes d'inpainting | CONDITIONING | Oui | - |
| `negative` | Le conditionnement négatif à augmenter avec les informations latentes d'inpainting | CONDITIONING | Oui | - |
| `vae` | Le modèle VAE utilisé pour encoder le masque et la vidéo masquée dans l'espace latent | VAE | Oui | - |
| `video` | Images de la vidéo source [T, H, W, 3] | IMAGE | Oui | - |
| `quadmask` | Quadmask prétraité issu de VOIDQuadmaskPreprocess [T, H, W] | MASK | Oui | - |
| `width` | La largeur pour redimensionner la vidéo et le masque (par défaut : 672) | INT | Oui | 16 to MAX_RESOLUTION (step: 8) |
| `height` | La hauteur pour redimensionner la vidéo et le masque (par défaut : 384) | INT | Oui | 16 to MAX_RESOLUTION (step: 8) |
| `length` | Nombre de trames de pixels à traiter. Pour CogVideoX-Fun-V1.5 (patch_size_t=2), latent_t doit être pair — les longueurs qui produisent un latent_t impair sont arrondies vers le bas (par exemple 49 → 45) (par défaut : 45) | INT | Oui | 1 to MAX_RESOLUTION (step: 1) |
| `batch_size` | La taille de lot (batch size) pour le latent de bruit de sortie (par défaut : 1) | INT | Oui | 1 to 64 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Le conditionnement positif avec les informations latentes d'inpainting ajoutées | CONDITIONING |
| `negative` | Le conditionnement négatif avec les informations latentes d'inpainting ajoutées | CONDITIONING |
| `latent` | Un tenseur de bruit latent rempli de zéros avec la forme [batch_size, 16, latent_t, latent_h, latent_w] | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDInpaintConditioning/fr.md)

---
**Source fingerprint (SHA-256):** `885e462c0f17a3e9610146a05ba3b9c879db0112d3961c95a83f63ba2cd511f1`
