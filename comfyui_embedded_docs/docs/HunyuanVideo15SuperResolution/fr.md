> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15SuperResolution/fr.md)

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Oui | N/A | L'entrée de conditionnement positive à modifier avec les données latentes et d'augmentation. |
| `negative` | CONDITIONING | Oui | N/A | L'entrée de conditionnement négative à modifier avec les données latentes et d'augmentation. |
| `vae` | VAE | Non | N/A | Le VAE utilisé pour encoder l'`start_image` optionnelle. Requis si `start_image` est fournie. |
| `start_image` | IMAGE | Non | N/A | Une image de départ optionnelle pour guider la super-résolution. Si elle est fournie, elle sera suréchantillonnée et encodée dans le latent de conditionnement. |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Non | N/A | Les embeddings de vision CLIP optionnels à ajouter au conditionnement. |
| `latent` | LATENT | Oui | N/A | La représentation latente vidéo d'entrée qui sera incorporée dans le conditionnement. |
| `noise_augmentation` | FLOAT | Non | 0.0 - 1.0 | L'intensité de l'augmentation par bruit à appliquer au conditionnement (par défaut : 0.70). |

**Remarque :** Si vous fournissez une `start_image`, vous devez également connecter un `vae` pour qu'elle soit encodée. L'`start_image` sera automatiquement suréchantillonnée pour correspondre aux dimensions impliquées par le `latent` d'entrée.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Le conditionnement positif modifié, contenant désormais le latent concaténé, l'augmentation par bruit et les données de vision CLIP optionnelles. |
| `negative` | CONDITIONING | Le conditionnement négatif modifié, contenant désormais le latent concaténé, l'augmentation par bruit et les données de vision CLIP optionnelles. |
| `latent` | LATENT | Le latent d'entrée est transmis inchangé. |
