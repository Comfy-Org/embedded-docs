> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22ImageToVideoLatent/fr.md)

Le nœud Wan22ImageToVideoLatent crée des représentations latentes vidéo à partir d'images. Il génère un espace latent vidéo vierge avec des dimensions spécifiées et peut éventuellement encoder une séquence d'images de départ dans les premières trames. Lorsqu'une image de départ est fournie, il encode l'image dans l'espace latent et crée un masque de bruit correspondant pour les régions à peindre.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `vae` | VAE | Oui | - | Le modèle VAE utilisé pour encoder les images dans l'espace latent |
| `largeur` | INT | Oui | 32 à MAX_RESOLUTION | La largeur de la vidéo de sortie en pixels (par défaut : 1280, pas : 32) |
| `hauteur` | INT | Oui | 32 à MAX_RESOLUTION | La hauteur de la vidéo de sortie en pixels (par défaut : 704, pas : 32) |
| `longueur` | INT | Oui | 1 à MAX_RESOLUTION | Le nombre de trames dans la séquence vidéo (par défaut : 49, pas : 4) |
| `taille_du_lot` | INT | Oui | 1 à 4096 | Le nombre de lots à générer (par défaut : 1) |
| `image_de_départ` | IMAGE | Non | - | Séquence d'images de départ facultative à encoder dans la vidéo latente |

**Remarque :** Lorsque `start_image` est fourni, le nœud encode la séquence d'images dans les premières trames de l'espace latent et génère un masque de bruit correspondant. Les paramètres de largeur et de hauteur doivent être divisibles par 16 pour des dimensions d'espace latent appropriées. Le paramètre `length` détermine le nombre de trames dans la vidéo latente ; la dimension temporelle de l'espace latent est calculée comme suit : `((length - 1) // 4) + 1`.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `samples` | LATENT | La représentation latente vidéo générée |
| `noise_mask` | LATENT | Le masque de bruit indiquant les régions à débruitiser lors de la génération |

---
**Source fingerprint (SHA-256):** `0f27e20bcc63f0dd224cda0fa26ee676c42898ac74fcfbe0a2b591def933689c`
