> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22ImageToVideoLatent/fr.md)

Le nœud Wan22ImageToVideoLatent crée des représentations latentes vidéo à partir d'images. Il génère un espace latent vidéo vierge avec des dimensions spécifiées et peut optionnellement encoder une séquence d'images de départ dans les premières trames. Lorsqu'une image de départ est fournie, il encode l'image dans l'espace latent et crée un masque de bruit correspondant pour les régions inpaintees.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `vae` | VAE | Oui | - | Le modèle VAE utilisé pour encoder les images dans l'espace latent |
| `width` | INT | Non | 32 à MAX_RESOLUTION | La largeur de la vidéo de sortie en pixels (par défaut : 1280, pas : 32) |
| `height` | INT | Non | 32 à MAX_RESOLUTION | La hauteur de la vidéo de sortie en pixels (par défaut : 704, pas : 32) |
| `length` | INT | Non | 1 à MAX_RESOLUTION | Le nombre de trames dans la séquence vidéo (par défaut : 49, pas : 4) |
| `batch_size` | INT | Non | 1 à 4096 | Le nombre de lots à générer (par défaut : 1) |
| `start_image` | IMAGE | Non | - | Séquence d'image de départ optionnelle à encoder dans la vidéo latente |

**Note :** Lorsque `start_image` est fourni, le nœud encode la séquence d'images dans les premières trames de l'espace latent et génère un masque de bruit correspondant. Les paramètres de largeur et de hauteur doivent être divisibles par 16 pour des dimensions d'espace latent appropriées.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `samples` | LATENT | La représentation latente vidéo générée |
| `noise_mask` | LATENT | Le masque de bruit indiquant les régions qui doivent être dé-bruitées pendant la génération |
