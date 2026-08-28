# HunyuanVideo15SuperResolution

Le nœud HunyuanVideo15SuperResolution prépare les données de conditionnement pour un processus de super-résolution vidéo. Il prend une représentation latente d'une vidéo et, éventuellement, une image de départ, et les regroupe avec l'augmentation de bruit et les données CLIP vision dans un format pouvant être utilisé par un modèle pour générer une sortie en plus haute résolution.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | L'entrée de conditionnement positive à modifier avec les données latentes et d'augmentation. | CONDITIONING | Oui | N/A |
| `négatif` | L'entrée de conditionnement négative à modifier avec les données latentes et d'augmentation. | CONDITIONING | Oui | N/A |
| `vae` | Le VAE utilisé pour encoder l'`start_image` facultative. Requis si `start_image` est fournie. | VAE | Non | N/A |
| `image_de_départ` | Une image de départ facultative pour guider la super-résolution. Si fournie, elle est agrandie et encodée dans le latent de conditionnement. | IMAGE | Non | N/A |
| `clip_vision_output` | Embeddings CLIP vision facultatifs à ajouter au conditionnement. | CLIP_VISION_OUTPUT | Non | N/A |
| `latent` | La représentation latente vidéo d'entrée qui est incorporée dans le conditionnement. | LATENT | Oui | N/A |
| `augmentation_du_bruit` | La force de l'augmentation de bruit à appliquer au conditionnement (par défaut : 0,70). C'est un paramètre avancé. | FLOAT | Non | 0.0 - 1.0 (pas 0.01) |

**Remarque :** Si vous fournissez une `start_image`, vous devez également connecter un `vae` pour pouvoir l'encoder. L'`start_image` est automatiquement agrandie à 16 fois les dimensions spatiales (largeur et hauteur) du `latent` d'entrée, puis encodée et placée dans le latent de conditionnement. Seuls les canaux RVB de l'`start_image` sont utilisés pour l'encodage.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positif` | Le conditionnement positif modifié, contenant désormais le latent concaténé, l'augmentation de bruit et les éventuelles données CLIP vision. | CONDITIONING |
| `négatif` | Le conditionnement négatif modifié, contenant désormais le latent concaténé, l'augmentation de bruit et les éventuelles données CLIP vision. | CONDITIONING |
| `latent` | Le latent d'entrée est transmis tel quel, sans modification. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15SuperResolution/fr.md)

---
**Source fingerprint (SHA-256):** `c9e64092e78423f5e0dc43446a77240e09100242c25e4fccc91491049fe76be5`
