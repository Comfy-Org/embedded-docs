# CosmosPredict2ImageToVideoLatent

Crée des latents vidéo pour le workflow image-vers-vidéo de Cosmos Predict2. Le nœud peut produire un latent vidéo vide d'une taille et d'une longueur données, ou insérer des images de début et/ou de fin encodées dans la séquence afin que ces trames soient conservées pendant la génération. Toute image fournie est redimensionnée aux `width` et `height` demandés et encodée avec le VAE fourni avant d'être placée au début et/ou à la fin de la séquence latente.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `vae` | Modèle VAE utilisé pour encoder les images de début et de fin dans l'espace latent | VAE | Oui | - |
| `largeur` | Largeur de la vidéo de sortie en pixels (par défaut : 848, doit être un multiple de 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | Hauteur de la vidéo de sortie en pixels (par défaut : 480, doit être un multiple de 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `longueur` | Nombre de trames dans la séquence vidéo (par défaut : 93) | INT | Oui | 1 à MAX_RESOLUTION |
| `taille_du_lot` | Nombre de séquences vidéo à générer (par défaut : 1) | INT | Oui | 1 à 4096 |
| `image_de_départ` | Image de début facultative pour la séquence vidéo | IMAGE | Non | - |
| `image_de_fin` | Image de fin facultative pour la séquence vidéo | IMAGE | Non | - |

**Remarque :** Lorsque ni `start_image` ni `end_image` ne sont fournis, le nœud renvoie simplement un latent vide de la taille et de la longueur demandées. Lorsqu'une ou les deux images sont fournies, elles sont redimensionnées à `width` et `height`, encodées avec le `vae`, puis placées au début et/ou à la fin de la séquence latente. Les régions correspondantes sont marquées dans le masque de bruit afin qu'elles soient préservées pendant la génération. Les latents encodés sont convertis avec le format latent Wan 2.1, et le latent et le masque résultants sont répétés `batch_size` fois.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `LATENT` | Le latent vidéo généré contenant `samples` (la séquence latente vidéo) et, lorsqu'au moins l'une des entrées `start_image` ou `end_image` est fournie, un `noise_mask` marquant les trames qui doivent être préservées pendant la génération | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/fr.md)

---
**Source fingerprint (SHA-256):** `842bd2b8cda438e7b938439d4eba280478939e3302dc1846d52595d40082ff05`
