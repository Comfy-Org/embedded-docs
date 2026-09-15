# VOIDInpaintConditioning

Le nœud VOIDInpaintConditioning prépare les données de conditionnement nécessaires pour l'inpainting avec les modèles CogVideoX. Il prend une vidéo source et un quadmask prétraité, les encode via le VAE, puis les combine en un signal de conditionnement à 32 canaux (16 canaux issus du masque + 16 canaux issus de la vidéo masquée) que le modèle utilise pour remplir les zones masquées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Le conditionnement positif à enrichir avec les informations latentes d'inpainting | CONDITIONING | Oui | - |
| `negative` | Le conditionnement négatif à enrichir avec les informations latentes d'inpainting | CONDITIONING | Oui | - |
| `vae` | Le modèle VAE utilisé pour encoder le masque et la vidéo masquée dans l'espace latent | VAE | Oui | - |
| `video` | Images de la vidéo source [T, H, W, 3] | IMAGE | Oui | - |
| `quadmask` | Quadmask prétraité issu de VOIDQuadmaskPreprocess [T, H, W] | MASK | Oui | - |
| `width` | Largeur vers laquelle redimensionner la vidéo et le masque (par défaut : 672) | INT | Oui | 16 à MAX_RESOLUTION (pas : 8) |
| `height` | Hauteur vers laquelle redimensionner la vidéo et le masque (par défaut : 384) | INT | Oui | 16 à MAX_RESOLUTION (pas : 8) |
| `length` | Nombre d'images en pixels à traiter. Pour CogVideoX-Fun-V1.5 (patch_size_t=2), latent_t doit être pair — les longueurs qui produisent un latent_t impair sont arrondies à l'entier inférieur (par ex. 49 → 45) (par défaut : 45) | INT | Oui | 1 à MAX_RESOLUTION (pas : 1) |
| `batch_size` | Taille du lot pour le latent de bruit en sortie (par défaut : 1) | INT | Oui | 1 à 64 |

**Remarque :** Comme CogVideoX-Fun-V1.5 utilise `patch_size_t=2`, le latent encodé doit avoir une dimension temporelle paire. Si `length` devait produire un `latent_t` impair, le nœud l'arrondit automatiquement à la valeur valide la plus proche inférieure et consigne un avertissement. Utiliser un `latent_t` impair corrompt la dernière image via le remplissage circulaire, ce qui peut provoquer un tremblement visible ou la disparition de sujets vers la fin de la vidéo décodée.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Le conditionnement positif avec les informations latentes d'inpainting ajoutées | CONDITIONING |
| `negative` | Le conditionnement négatif avec les informations latentes d'inpainting ajoutées | CONDITIONING |
| `latent` | Un tenseur latent de bruit rempli de zéros de forme [batch_size, 16, latent_t, latent_h, latent_w] | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDInpaintConditioning/fr.md)

---
**Source fingerprint (SHA-256):** `885e462c0f17a3e9610146a05ba3b9c879db0112d3961c95a83f63ba2cd511f1`
