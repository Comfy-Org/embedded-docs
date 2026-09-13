# Kandinsky5ImageToVideo

Le nœud Kandinsky5ImageToVideo prépare les données de conditionnement et les données latentes pour la génération vidéo à l'aide du modèle Kandinsky. Il crée un latent vidéo vide dimensionné selon la largeur, la hauteur, la longueur et la taille de lot demandées, et peut éventuellement encoder une image de départ pour guider les premières images de la vidéo générée en mettant à jour les conditionnements positif et négatif.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Les invites de conditionnement positives pour guider la génération vidéo. | CONDITIONING | Oui | N/A |
| `negative` | Les invites de conditionnement négatives pour éloigner la génération vidéo de certains concepts. | CONDITIONING | Oui | N/A |
| `vae` | Le modèle VAE utilisé pour encoder l'image de départ facultative dans l'espace latent. | VAE | Oui | N/A |
| `width` | La largeur de la vidéo de sortie en pixels (par défaut : 768). | INT | Oui | 16 à 16384 (pas de 16) |
| `height` | La hauteur de la vidéo de sortie en pixels (par défaut : 512). | INT | Oui | 16 à 16384 (pas de 16) |
| `length` | Le nombre d'images dans la vidéo (par défaut : 121). | INT | Oui | 1 à 16384 (pas de 4) |
| `batch_size` | Le nombre de séquences vidéo à générer simultanément (par défaut : 1). | INT | Oui | 1 à 4096 |
| `start_image` | Une image de départ facultative ou un lot d'images. Si elle est fournie, elle est encodée et utilisée pour remplacer le début bruité des latents de sortie du modèle. | IMAGE | Non | N/A |

**Remarque :** Lorsqu'une `start_image` est fournie, elle est automatiquement redimensionnée pour correspondre à la `width` et à la `height` spécifiées à l'aide d'une interpolation bilinéaire. Seules les `length` premières images du lot d'images sont utilisées pour l'encodage ; toutes les images supplémentaires sont ignorées. Si le lot d'images contient moins de `length` images, seules ces images sont utilisées. Seuls les canaux RVB de l'image sont encodés. Le latent encodé est ensuite injecté dans les conditionnements positif et négatif pour guider l'apparence initiale de la vidéo, et les images encodées propres remplacent le début bruité des latents de sortie du modèle.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Le conditionnement positif modifié, mis à jour avec les données d'image de départ encodées lorsqu'une `start_image` est fournie. | CONDITIONING |
| `negative` | Le conditionnement négatif modifié, mis à jour avec les données d'image de départ encodées lorsqu'une `start_image` est fournie. | CONDITIONING |
| `latent` | Latent vidéo vide. Un tenseur latent rempli de zéros, dimensionné selon les dimensions spécifiées. | LATENT |
| `cond_latent` | Images de départ encodées propres, utilisées pour remplacer le début bruité des latents de sortie du modèle. Vide lorsqu'aucune `start_image` n'est fournie. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kandinsky5ImageToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `7212f0ea912578d3b72dddf1333a20054a881e3f22c2b8abd9645fc21e75a08b`
