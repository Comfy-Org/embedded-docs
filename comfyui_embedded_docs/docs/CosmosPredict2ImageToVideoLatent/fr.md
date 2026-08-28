# CosmosPredict2ImageToVideoLatent

CosmosPredict2ImageToVideoLatent crée des représentations latentes vidéo à partir d'images pour la génération vidéo. Il peut générer un latent vidéo vierge ou incorporer des images de début et de fin pour créer des séquences vidéo avec des dimensions et une durée spécifiées. Le nœud gère l'encodage des images dans le format d'espace latent approprié pour le traitement vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `vae` | Le modèle VAE utilisé pour encoder les images dans l'espace latent | VAE | Oui | - |
| `largeur` | La largeur de la vidéo de sortie en pixels (défaut : 848, doit être divisible par 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | La hauteur de la vidéo de sortie en pixels (défaut : 480, doit être divisible par 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `longueur` | Le nombre d'images de la séquence vidéo (défaut : 93, pas : 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `taille_du_lot` | Le nombre de séquences vidéo à générer (défaut : 1) | INT | Oui | 1 à 4096 |
| `image_de_départ` | Image de début facultative pour la séquence vidéo | IMAGE | Non | - |
| `image_de_fin` | Image de fin facultative pour la séquence vidéo | IMAGE | Non | - |

**Remarque :** Lorsque ni `start_image` ni `end_image` ne sont fournis, le nœud génère un latent vidéo vierge. Lorsqu'une ou les deux images sont fournies, elles sont redimensionnées à `width` et `height`, encodées dans l'espace latent, puis placées au début et/ou à la fin de la séquence vidéo, les régions correspondantes étant marquées dans le masque de bruit afin qu'elles soient préservées pendant la génération. Le latent et le masque résultants sont répétés `batch_size` fois.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `samples` | La représentation latente vidéo générée contenant la séquence vidéo encodée | LATENT |
| `noise_mask` | Un masque indiquant les parties du latent à préserver pendant la génération. Présent uniquement lorsqu'au moins une des images `start_image` ou `end_image` est fournie. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/fr.md)

---
**Source fingerprint (SHA-256):** `842bd2b8cda438e7b938439d4eba280478939e3302dc1846d52595d40082ff05`
