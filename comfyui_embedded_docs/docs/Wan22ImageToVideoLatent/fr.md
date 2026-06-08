Le nœud Wan22ImageToVideoLatent crée des représentations latentes vidéo à partir d'images. Il génère un espace latent vidéo vierge avec des dimensions spécifiées et peut éventuellement encoder une séquence d'images de départ dans les premières trames. Lorsqu'une image de départ est fournie, il encode l'image dans l'espace latent et crée un masque de bruit correspondant pour les régions à peindre.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `vae` | Le modèle VAE utilisé pour encoder les images dans l'espace latent | VAE | Oui | - |
| `largeur` | La largeur de la vidéo de sortie en pixels (par défaut : 1280, pas : 32) | INT | Oui | 32 à MAX_RESOLUTION |
| `hauteur` | La hauteur de la vidéo de sortie en pixels (par défaut : 704, pas : 32) | INT | Oui | 32 à MAX_RESOLUTION |
| `longueur` | Le nombre de trames dans la séquence vidéo (par défaut : 49, pas : 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `taille_du_lot` | Le nombre de lots à générer (par défaut : 1) | INT | Oui | 1 à 4096 |
| `image_de_départ` | Séquence d'images de départ facultative à encoder dans la vidéo latente | IMAGE | Non | - |

**Remarque :** Lorsque `start_image` est fourni, le nœud encode la séquence d'images dans les premières trames de l'espace latent et génère un masque de bruit correspondant. Les paramètres de largeur et de hauteur doivent être divisibles par 16 pour des dimensions d'espace latent appropriées. Le paramètre `length` détermine le nombre de trames dans la vidéo latente ; la dimension temporelle de l'espace latent est calculée comme suit : `((length - 1) // 4) + 1`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `samples` | La représentation latente vidéo générée | LATENT |
| `noise_mask` | Le masque de bruit indiquant les régions à débruitiser lors de la génération | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22ImageToVideoLatent/fr.md)

---
**Source fingerprint (SHA-256):** `0f27e20bcc63f0dd224cda0fa26ee676c42898ac74fcfbe0a2b591def933689c`
