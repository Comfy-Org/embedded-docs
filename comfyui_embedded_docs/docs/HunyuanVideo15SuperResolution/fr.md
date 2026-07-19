# HunyuanVideo15SuperResolution

Le nœud HunyuanVideo15SuperResolution prépare les données de conditionnement pour un processus de super-résolution vidéo. Il prend une représentation latente d'une vidéo et, éventuellement, une image de départ, puis les assemble avec une augmentation de bruit et des données de vision CLIP dans un format utilisable par un modèle pour générer une sortie en résolution plus élevée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | L'entrée de conditionnement positif à modifier avec les données latentes et d'augmentation. | CONDITIONING | Oui | N/A |
| `négatif` | L'entrée de conditionnement négatif à modifier avec les données latentes et d'augmentation. | CONDITIONING | Oui | N/A |
| `vae` | Le VAE utilisé pour encoder l'`image_de_départ` facultative. Requis si `image_de_départ` est fourni. | VAE | Non | N/A |
| `image_de_départ` | Une image de départ facultative pour guider la super-résolution. Si fournie, elle sera mise à l'échelle et encodée dans le latent de conditionnement. | IMAGE | Non | N/A |
| `clip_vision_output` | Plongements de vision CLIP facultatifs à ajouter au conditionnement. | CLIP_VISION_OUTPUT | Non | N/A |
| `latent` | La représentation vidéo latente d'entrée qui sera intégrée dans le conditionnement. | LATENT | Oui | N/A |
| `augmentation_du_bruit` | La force de l'augmentation de bruit à appliquer au conditionnement (par défaut : 0.70). | FLOAT | Non | 0.0 - 1.0 |

**Remarque :** Si vous fournissez une `start_image`, vous devez également connecter un `vae` pour qu'elle soit encodée. L'`start_image` sera automatiquement mise à l'échelle pour correspondre aux dimensions implicites du `latent` d'entrée.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positif` | Le conditionnement positif modifié, contenant désormais le latent concaténé, l'augmentation de bruit et les données de vision CLIP facultatives. | CONDITIONING |
| `négatif` | Le conditionnement négatif modifié, contenant désormais le latent concaténé, l'augmentation de bruit et les données de vision CLIP facultatives. | CONDITIONING |
| `latent` | Le latent d'entrée est transmis sans modification. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15SuperResolution/fr.md)

---
**Source fingerprint (SHA-256):** `f913327a81d034997fa8a485ca4b3691f75ba1d3c5c6e2e73ab107021b58a52a`
