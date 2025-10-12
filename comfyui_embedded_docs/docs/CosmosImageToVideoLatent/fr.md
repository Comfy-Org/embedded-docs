> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosImageToVideoLatent/fr.md)

Le nœud CosmosImageToVideoLatent crée des représentations latentes vidéo à partir d'images d'entrée. Il génère un latent vidéo vierge et encode optionnellement des images de début et/ou de fin dans les premières et/ou dernières images de la séquence vidéo. Lorsque des images sont fournies, il crée également des masques de bruit correspondants pour indiquer quelles parties du latent doivent être préservées pendant la génération.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `vae` | VAE | Oui | - | Le modèle VAE utilisé pour encoder les images dans l'espace latent |
| `largeur` | INT | Non | 16 à MAX_RESOLUTION | La largeur de la vidéo de sortie en pixels (par défaut : 1280) |
| `hauteur` | INT | Non | 16 à MAX_RESOLUTION | La hauteur de la vidéo de sortie en pixels (par défaut : 704) |
| `longueur` | INT | Non | 1 à MAX_RESOLUTION | Le nombre d'images dans la séquence vidéo (par défaut : 121) |
| `taille_du_lot` | INT | Non | 1 à 4096 | Le nombre de lots latents à générer (par défaut : 1) |
| `image_de_départ` | IMAGE | Non | - | Image optionnelle à encoder au début de la séquence vidéo |
| `image_de_fin` | IMAGE | Non | - | Image optionnelle à encoder à la fin de la séquence vidéo |

**Note :** Lorsque ni `start_image` ni `end_image` ne sont fournis, le nœud retourne un latent vierge sans aucun masque de bruit. Lorsqu'une image est fournie, les sections correspondantes du latent sont encodées et masquées en conséquence.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `latent` | LATENT | La représentation latente vidéo générée avec les images encodées optionnelles et les masques de bruit correspondants |
