# Wan22ImageToVideoLatent

Wan22ImageToVideoLatent crée des représentations latentes vidéo à partir d'images. Il génère un espace latent vidéo vierge avec la largeur, la hauteur, la longueur de trame et la taille de lot spécifiées, et peut éventuellement encoder une séquence d'images de départ dans les premières trames. Lorsqu'une image de départ est fournie, le nœud l'encode dans l'espace latent et crée un masque de bruit correspondant qui indique quelles régions doivent être débruitées pendant la génération.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `vae` | Le modèle VAE utilisé pour encoder l'image de départ dans l'espace latent | VAE | Oui | - |
| `largeur` | La largeur de la vidéo de sortie en pixels (défaut : 1280, pas : 32) | INT | Oui | 32 à MAX_RESOLUTION |
| `hauteur` | La hauteur de la vidéo de sortie en pixels (défaut : 704, pas : 32) | INT | Oui | 32 à MAX_RESOLUTION |
| `longueur` | Le nombre de trames dans la séquence vidéo (défaut : 49, pas : 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `taille_du_lot` | Le nombre de latents vidéo à générer (défaut : 1) | INT | Oui | 1 à 4096 |
| `image_de_départ` | Séquence d'images de départ facultative à encoder dans les premières trames du latent vidéo (utilise les `length` premières trames) | IMAGE | Non | - |

**Remarque :** Lorsque `start_image` est fourni, la séquence d'images est redimensionnée aux dimensions `width` et `height` cibles, encodée avec le VAE, puis placée dans les premières trames du latent. Le masque de bruit pour ces trames est défini à 0 (préservé), tandis que les trames restantes ont une valeur de masque de 1 (à débruiter). Le latent a toujours 48 canaux, des dimensions spatiales de `height / 16` par `width / 16`, et une dimension temporelle de `((length - 1) // 4) + 1`. `width` et `height` doivent être divisibles par 16 (imposé par le pas de 32), et `length` augmente la dimension temporelle par pas de 4.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `samples` | La représentation latente vidéo générée, répétée pour chaque élément du lot | LATENT |
| `noise_mask` | Le masque de bruit indiquant quelles régions doivent être débruitées (valeur 1) et lesquelles conservent l'image de départ encodée (valeur 0) | LATENT |

Les deux champs sont renvoyés ensemble dans une seule sortie LATENT.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22ImageToVideoLatent/fr.md)

---
**Source fingerprint (SHA-256):** `3d05980641eeef2e86df7a845aa8b2bd703882db98fe71adef2746ab34a9d717`
