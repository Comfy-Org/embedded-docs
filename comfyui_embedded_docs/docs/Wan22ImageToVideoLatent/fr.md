# Wan22ImageToVideoLatent

Wan22ImageToVideoLatent crée des représentations latentes vidéo à partir d’images. Il génère un espace latent vidéo vide avec la largeur, la hauteur, le nombre d’images et la taille de lot spécifiés, et peut éventuellement encoder une séquence d’images de départ dans les premières images. Lorsqu’une image de départ est fournie, le nœud l’encode dans l’espace latent et crée un masque de bruit correspondant qui indique quelles régions doivent être débruitées pendant la génération.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `vae` | Modèle VAE utilisé pour encoder l’image de départ dans l’espace latent | VAE | Oui | - |
| `width` | Largeur de la vidéo de sortie en pixels (par défaut : 1280, pas : 32) | INT | Oui | 32 à MAX_RESOLUTION |
| `height` | Hauteur de la vidéo de sortie en pixels (par défaut : 704, pas : 32) | INT | Oui | 32 à MAX_RESOLUTION |
| `length` | Nombre d’images dans la séquence vidéo (par défaut : 49, pas : 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `batch_size` | Nombre de latents vidéo à générer (par défaut : 1) | INT | Oui | 1 à 4096 |
| `start_image` | Séquence d’images de départ facultative à encoder dans les premières images du latent vidéo (utilise les `length` premières images) | IMAGE | Non | - |

**Remarque :** Lorsque `start_image` est fourni, la séquence d’images est mise à l’échelle vers la `width` et la `height` cibles, encodée avec le VAE, puis placée dans les premières images du latent. Le masque de bruit de ces images est défini à 0 (préservé), tandis que les images restantes ont une valeur de masque de 1 (à débruiter). Le latent possède toujours 48 canaux, des dimensions spatiales de `height / 16` par `width / 16`, et une dimension temporelle de `((length - 1) // 4) + 1`. `width` et `height` doivent être divisibles par 16 (imposé par le pas de 32), et `length` augmente la dimension temporelle par pas de 4.

Lorsque `start_image` n’est pas fourni, un latent entièrement vide est renvoyé sans masque de bruit, et l’entrée `batch_size` n’est pas appliquée à ce latent vide.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `samples` | Représentation latente vidéo générée, répétée pour chaque élément du lot | LATENT |
| `noise_mask` | Masque de bruit indiquant les régions qui doivent être débruitées (valeur 1) et celles qui conservent l’image de départ encodée (valeur 0) | LATENT |

Ces deux champs sont renvoyés ensemble dans une seule sortie LATENT.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22ImageToVideoLatent/fr.md)

---
**Source fingerprint (SHA-256):** `3d05980641eeef2e86df7a845aa8b2bd703882db98fe71adef2746ab34a9d717`
