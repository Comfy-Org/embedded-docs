# CosmosPredict2ImageToVideoLatent

Le nœud CosmosPredict2ImageToVideoLatent crée des représentations latentes vidéo à partir d'images pour la génération vidéo. Il peut générer un latent vidéo vide ou intégrer des images de début et de fin pour créer des séquences vidéo avec des dimensions et une durée spécifiées. Le nœud gère l'encodage des images dans le format d'espace latent approprié pour le traitement vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `vae` | Le modèle VAE utilisé pour encoder les images dans l'espace latent | VAE | Oui | - |
| `width` | La largeur de la vidéo de sortie en pixels (défaut : 848, doit être divisible par 16) | INT | Oui | 16 to MAX_RESOLUTION (step 16) |
| `height` | La hauteur de la vidéo de sortie en pixels (défaut : 480, doit être divisible par 16) | INT | Oui | 16 to MAX_RESOLUTION (step 16) |
| `length` | Le nombre d'images dans la séquence vidéo (défaut : 93) | INT | Oui | 1 to MAX_RESOLUTION (step 4) |
| `batch_size` | Le nombre de séquences vidéo à générer (défaut : 1) | INT | Oui | 1 to 4096 |
| `start_image` | Image de départ facultative pour la séquence vidéo | IMAGE | Non | - |
| `end_image` | Image de fin facultative pour la séquence vidéo | IMAGE | Non | - |

**Remarque :** Lorsque ni `start_image` ni `end_image` ne sont fournis, le nœud génère un latent vidéo vide. Lorsque des images sont fournies, elles sont encodées et positionnées au début et/ou à la fin de la séquence vidéo avec un masquage approprié.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `samples` | La représentation latente vidéo générée contenant la séquence vidéo encodée | LATENT |
| `noise_mask` | Un masque indiquant les parties du latent à préserver pendant la génération | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/fr.md)

---
**Source fingerprint (SHA-256):** `842bd2b8cda438e7b938439d4eba280478939e3302dc1846d52595d40082ff05`
