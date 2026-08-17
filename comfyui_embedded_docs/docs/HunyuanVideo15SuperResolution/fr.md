# HunyuanVideo15SuperResolution

Le nœud HunyuanVideo15SuperResolution prépare les données de conditionnement pour un processus de super-résolution vidéo. Il prend une représentation latente d'une vidéo et, éventuellement, une image de départ, et les regroupe avec une valeur d'augmentation du bruit et des données de vision CLIP facultatives dans un format qu'un modèle peut utiliser pour générer une sortie en plus haute résolution.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | L'entrée de conditionnement positive à modifier avec les données latentes concaténées et d'augmentation du bruit. | CONDITIONING | Oui | N/A |
| `negative` | L'entrée de conditionnement négative à modifier avec les données latentes concaténées et d'augmentation du bruit. | CONDITIONING | Oui | N/A |
| `vae` | Le VAE utilisé pour encoder le `start_image` facultatif. Requis si `start_image` est fourni. | VAE | Non | N/A |
| `start_image` | Une image de départ facultative qui guide le processus de super-résolution. Si elle est fournie, elle est agrandie, encodée avec le `vae`, et placée au début du latent de conditionnement. | IMAGE | Non | N/A |
| `clip_vision_output` | Plongements de vision CLIP facultatifs. Lorsqu'ils sont fournis, ils sont ajoutés à la fois au conditionnement positif et négatif. | CLIP_VISION_OUTPUT | Non | N/A |
| `latent` | La représentation vidéo latente à incorporer dans le conditionnement. | LATENT | Oui | N/A |
| `noise_augmentation` | L'intensité de l'augmentation du bruit à appliquer au conditionnement (par défaut : 0.70). Ceci est un paramètre avancé. | FLOAT | Oui | 0.0 - 1.0 (step 0.01) |

**Remarque :** Si vous fournissez un `start_image`, vous devez également connecter un `vae` pour qu'il soit encodé. Le `start_image` est automatiquement agrandi pour correspondre aux dimensions impliquées par le `latent` d'entrée, et seuls ses trois premiers canaux de couleur (RVB) sont utilisés par le VAE.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Le conditionnement positif modifié, contenant désormais le latent concaténé, l'augmentation du bruit et les éventuelles données de vision CLIP. | CONDITIONING |
| `negative` | Le conditionnement négatif modifié, contenant désormais le latent concaténé, l'augmentation du bruit et les éventuelles données de vision CLIP. | CONDITIONING |
| `latent` | Le latent d'entrée, transmis inchangé. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15SuperResolution/fr.md)

---
**Source fingerprint (SHA-256):** `c9e64092e78423f5e0dc43446a77240e09100242c25e4fccc91491049fe76be5`
