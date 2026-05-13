> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosImageToVideoLatent/fr.md)

Voici la traduction de la documentation du nœud CosmosImageToVideoLatent :

Le nœud CosmosImageToVideoLatent crée des représentations latentes vidéo à partir d'images d'entrée. Il génère une latente vidéo vierge et encode éventuellement des images de début et/ou de fin dans les premières et/ou dernières images de la séquence vidéo. Lorsque des images sont fournies, il crée également des masques de bruit correspondants pour indiquer quelles parties de la latente doivent être préservées lors de la génération.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `vae` | VAE | Oui | - | Le modèle VAE utilisé pour encoder les images dans l'espace latent |
| `width` | INT | Oui | 16 à MAX_RESOLUTION | La largeur de la vidéo de sortie en pixels (par défaut : 1280) |
| `height` | INT | Oui | 16 à MAX_RESOLUTION | La hauteur de la vidéo de sortie en pixels (par défaut : 704) |
| `length` | INT | Oui | 1 à MAX_RESOLUTION | Le nombre d'images dans la séquence vidéo (par défaut : 121) |
| `batch_size` | INT | Oui | 1 à 4096 | Le nombre de lots de latentes à générer (par défaut : 1) |
| `start_image` | IMAGE | Non | - | Image facultative à encoder au début de la séquence vidéo |
| `end_image` | IMAGE | Non | - | Image facultative à encoder à la fin de la séquence vidéo |

**Remarque :** Lorsque ni `start_image` ni `end_image` ne sont fournis, le nœud renvoie une latente vierge sans aucun masque de bruit. Lorsqu'une image est fournie, les sections correspondantes de la latente sont encodées et masquées en conséquence.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `latent` | LATENT | La représentation latente vidéo générée avec les images encodées facultatives et les masques de bruit correspondants |

---
**Source fingerprint (SHA-256):** `31ce4dc577c672e0b3dc0bfb6644b2ef7ab737f6c4ee5e0677973b6a4efdd66d`
