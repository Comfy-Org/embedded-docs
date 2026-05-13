> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/fr.md)

Voici la traduction en français de la documentation du nœud ComfyUI :

Le nœud CosmosPredict2ImageToVideoLatent crée des représentations latentes vidéo à partir d'images pour la génération vidéo. Il peut générer une vidéo latente vierge ou intégrer des images de début et de fin pour créer des séquences vidéo avec des dimensions et une durée spécifiées. Le nœud gère l'encodage des images dans le format d'espace latent approprié pour le traitement vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `vae` | VAE | Oui | - | Le modèle VAE utilisé pour encoder les images dans l'espace latent |
| `largeur` | INT | Non | 16 à MAX_RESOLUTION | La largeur de la vidéo de sortie en pixels (défaut : 848, doit être divisible par 16) |
| `hauteur` | INT | Non | 16 à MAX_RESOLUTION | La hauteur de la vidéo de sortie en pixels (défaut : 480, doit être divisible par 16) |
| `longueur` | INT | Non | 1 à MAX_RESOLUTION | Le nombre d'images dans la séquence vidéo (défaut : 93, pas : 4) |
| `taille_du_lot` | INT | Non | 1 à 4096 | Le nombre de séquences vidéo à générer (défaut : 1) |
| `image_de_départ` | IMAGE | Non | - | Image de début optionnelle pour la séquence vidéo |
| `image_de_fin` | IMAGE | Non | - | Image de fin optionnelle pour la séquence vidéo |

**Remarque :** Lorsque ni `start_image` ni `end_image` ne sont fournis, le nœud génère une vidéo latente vierge. Lorsque des images sont fournies, elles sont encodées et positionnées au début et/ou à la fin de la séquence vidéo avec un masquage approprié.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `samples` | LATENT | La représentation latente vidéo générée contenant la séquence vidéo encodée |
| `noise_mask` | LATENT | Un masque indiquant les parties du latent à préserver lors de la génération |

---
**Source fingerprint (SHA-256):** `55fab16180c0e3fa254bcc77694dbc666810b28522e61b9c613f720fae66bd0c`
