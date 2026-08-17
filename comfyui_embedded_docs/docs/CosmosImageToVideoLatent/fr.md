# CosmosImageVersVidéoLatent

Le nœud CosmosImageToVideoLatent crée un latent vidéo pour la génération image-vers-vidéo. Il commence avec un latent vide et peut éventuellement encoder une image de début et/ou une image de fin dans les premières ou dernières images de la séquence vidéo. Lorsque des images sont fournies, il génère également un masque de bruit qui marque les images encodées comme fixes pendant la génération.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `vae` | Le modèle VAE utilisé pour encoder les images d'entrée dans l'espace latent | VAE | Oui | - |
| `width` | La largeur de la vidéo de sortie en pixels (par défaut : 1280) | INT | Oui | 16 à MAX_RESOLUTION (pas de 16) |
| `height` | La hauteur de la vidéo de sortie en pixels (par défaut : 704) | INT | Oui | 16 à MAX_RESOLUTION (pas de 16) |
| `length` | Le nombre d'images dans la séquence vidéo (par défaut : 121) | INT | Oui | 1 à MAX_RESOLUTION (pas de 8) |
| `batch_size` | Le nombre de latents vidéo à générer dans le lot de sortie (par défaut : 1) | INT | Oui | 1 à 4096 |
| `start_image` | Image ou séquence d'images facultative à encoder au début de la séquence vidéo | IMAGE | Non | - |
| `end_image` | Image ou séquence d'images facultative à encoder à la fin de la séquence vidéo | IMAGE | Non | - |

**Remarque :** Lorsque ni `start_image` ni `end_image` n'est fourni, le nœud renvoie un latent vide sans masque de bruit. Lorsqu'au moins une image est fournie, un `noise_mask` est inclus : les images latentes encodées à partir des images fournies ont une valeur de masque de 0 (conservées fixes), tandis que les images restantes ont une valeur de masque de 1 (à générer). Les images sont redimensionnées aux dimensions `width` et `height` cibles avant l'encodage, et le nombre d'images extraites d'une image d'entrée est égal à sa dimension de lot, jusqu'à un maximum de `length`. Le latent a 16 canaux, des dimensions spatiales `width / 8` et `height / 8`, et `((length - 1) // 8) + 1` images. Lorsque des images sont fournies, le latent et son masque de bruit sont répétés `batch_size` fois pour former le lot de sortie.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `latent` | Un LATENT contenant les `samples` du latent vidéo et, lorsque `start_image` ou `end_image` est fourni, un `noise_mask` qui marque les images encodées comme fixes | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosImageToVideoLatent/fr.md)

---
**Source fingerprint (SHA-256):** `0b06ccfcb14c27c81eeebbbff519da1e187970d4cfc19c8796fc3da20688245c`
