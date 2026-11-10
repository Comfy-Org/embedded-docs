# MiniMax H3 Image Conditioning

Transforme un prompt en conditionnement et en latent vide pour une image fixe avec MiniMax H3 Image. Sans images, il s’agit de texte vers image ; avec des images connectées, il les modifie, et le prompt les désigne par `<Picture 1>`, `<Picture 2>`, etc.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP MiniMax H3 Image, qui tokenise le prompt avec les éventuelles images de référence et encode le conditionnement. | CLIP | Oui | - |
| `vae` | Le VAE MiniMax H3 Image. Avec lui, les images sont également ancrées comme latents de référence ; sans lui, elles ne conditionnent que l’encodeur de texte. | VAE | Non | - |
| `prompt` | Ce qu’il faut générer, ou comment modifier les images de référence. | STRING | Oui | Texte multiligne |
| `width` | Largeur de sortie en pixels. 0 utilise la largeur de `image_1` après sa mise à l’échelle de référence, ou 2048 sans images. Par défaut : 0. | INT | Oui | 0 à MAX_RESOLUTION (pas : 32) |
| `height` | Hauteur de sortie en pixels. 0 utilise la hauteur de `image_1` après sa mise à l’échelle de référence, ou 2048 sans images. Par défaut : 0. | INT | Oui | 0 à MAX_RESOLUTION (pas : 32) |
| `images` | Groupe extensible d’images de référence, à partir de `image_1` ; `image_1` est l’image à modifier. Le prompt les désigne par `<Picture n>`. | AUTOGROW | Non | 0 à 100 images |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement pour l’échantillonneur MiniMax H3 Image, avec les latents de référence joints lorsque des images sont connectées. | CONDITIONING |
| `latent` | Latent vide pour une image, 24 canaux à un seizième de la taille de sortie. | LATENT |

Remarque : Le modèle est calibré pour une surface de 2048x2048 pixels ; laissez donc `width` et `height` à 0, sauf si un canevas différent est nécessaire.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ImageConditioning/fr.md)

---
**Source fingerprint (SHA-256):** `b0927bbc44ac82e8a23b1edb5470c0cc8945844c326a352d75495ed801d11b1d`
