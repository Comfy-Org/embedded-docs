# CosmosImageVersVidéoLatent

Le nœud CosmosImageToVideoLatent crée une représentation latente vidéo à partir d'images d'entrée. Il construit un latent vidéo vierge avec la largeur, la hauteur et le nombre d'images demandés, puis encode éventuellement une image de début dans les premières images et/ou une image de fin dans les dernières images. Lorsque des images sont fournies, il génère également un masque de bruit afin que les images encodées restent fixes pendant la génération.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `vae` | Le modèle VAE utilisé pour encoder les images dans l'espace latent vidéo. | VAE | Oui | - |
| `largeur` | La largeur de la vidéo de sortie en pixels (par défaut : 1280). | INT | Oui | 16 à MAX_RESOLUTION (pas : 16) |
| `hauteur` | La hauteur de la vidéo de sortie en pixels (par défaut : 704). | INT | Oui | 16 à MAX_RESOLUTION (pas : 16) |
| `longueur` | Le nombre total d'images dans la vidéo (par défaut : 121). | INT | Oui | 1 à MAX_RESOLUTION (pas : 8) |
| `taille_du_lot` | Le nombre de latents vidéo à générer (par défaut : 1). | INT | Oui | 1 à 4096 |
| `image_de_départ` | Image ou séquence d'images optionnelle à encoder au début de la vidéo. | IMAGE | Non | - |
| `image_de_fin` | Image ou séquence d'images optionnelle à encoder à la fin de la vidéo. | IMAGE | Non | - |

**Remarque :**
- Lorsque ni `start_image` ni `end_image` n'est fourni, le nœud renvoie un latent vierge sans masque de bruit.
- Lorsque `start_image` est fourni, il est encodé dans les premières images du latent et ces images sont marquées avec la valeur 0 du masque de bruit (préservées). Lorsque `end_image` est fourni, il est encodé dans les dernières images et ces images sont marquées avec la valeur 0 du masque de bruit. Les images restantes conservent une valeur de masque de 1.
- Le latent possède 16 canaux et ses dimensions spatiales sont `height / 8` par `width / 8`. Le nombre d'images latentes est `((length - 1) // 8) + 1`.
- `batch_size` répète le latent et, le cas échéant, le masque de bruit.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `latent` | Le latent vidéo généré contenant les éventuelles images de début et/ou de fin encodées et, lorsque des images sont fournies, un masque de bruit correspondant avec la valeur 0 sur les images préservées. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosImageToVideoLatent/fr.md)

---
**Source fingerprint (SHA-256):** `0b06ccfcb14c27c81eeebbbff519da1e187970d4cfc19c8796fc3da20688245c`
