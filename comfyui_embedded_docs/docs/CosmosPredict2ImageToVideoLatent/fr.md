> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/fr.md)

Le nœud CosmosPredict2ImageToVideoLatent crée des représentations latentes vidéo à partir d'images pour la génération de vidéos. Il peut générer une vidéo latente vierge ou incorporer des images de début et de fin pour créer des séquences vidéo avec des dimensions et une durée spécifiées. Le nœud gère l'encodage des images dans le format d'espace latent approprié pour le traitement vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `vae` | VAE | Oui | - | Le modèle VAE utilisé pour encoder les images dans l'espace latent |
| `width` | INT | Non | 16 à MAX_RESOLUTION | La largeur de la vidéo de sortie en pixels (par défaut : 848, doit être divisible par 16) |
| `height` | INT | Non | 16 à MAX_RESOLUTION | La hauteur de la vidéo de sortie en pixels (par défaut : 480, doit être divisible par 16) |
| `length` | INT | Non | 1 à MAX_RESOLUTION | Le nombre d'images dans la séquence vidéo (par défaut : 93, pas : 4) |
| `batch_size` | INT | Non | 1 à 4096 | Le nombre de séquences vidéo à générer (par défaut : 1) |
| `start_image` | IMAGE | Non | - | Image de début optionnelle pour la séquence vidéo |
| `end_image` | IMAGE | Non | - | Image de fin optionnelle pour la séquence vidéo |

**Note :** Lorsque ni `start_image` ni `end_image` ne sont fournis, le nœud génère une vidéo latente vierge. Lorsque des images sont fournies, elles sont encodées et positionnées au début et/ou à la fin de la séquence vidéo avec un masquage approprié.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `samples` | LATENT | La représentation latente vidéo générée contenant la séquence vidéo encodée |
| `noise_mask` | LATENT | Un masque indiquant quelles parties du latent doivent être préservées pendant la génération |