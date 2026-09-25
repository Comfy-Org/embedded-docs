# Text Encode Ming Image Edit

Text Encode Ming Image Edit encode un prompt texte en conditionnement pour l'édition d'image Ming, en mélangeant éventuellement des images de référence. Le prompt et les images de référence sont tokenisés par un modèle CLIP, et lorsqu'un VAE est connecté, les images de référence sont également encodées en trames latentes qui sont ajoutées au conditionnement.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `clip` | Le modèle CLIP utilisé pour tokeniser le prompt et les images de référence. | CLIP | Oui | - |
| `vae` | VAE facultatif qui encode les images de référence en trames latentes ajoutées au conditionnement. Sans VAE, les images ne conditionnent l'encodeur de texte que via la tour de vision. | VAE | Non | - |
| `prompt` | Prompt texte à encoder. Prend en charge l'entrée multiligne et les prompts dynamiques. | STRING | Oui | Texte multiligne |
| `images` | Emplacement extensible : images de référence facultatives vues par l'encodeur de texte et ajoutées à la séquence latente en tant que trames propres. Connecter 1..8 images (`image_1`, `image_2`, ...) ; les images suivantes sont redimensionnées à la taille de la première et le latent échantillonné doit correspondre à sa taille. Seuls les canaux RVB sont utilisés. | IMAGE | Non | 0 à 8 |

**Remarque :** Les images de référence sont lues dans l'ordre numérique de leurs noms d'emplacement, et les emplacements vides sont ignorés. Les latents de référence ne sont produits que lorsque `vae` et au moins une image sont fournis.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `CONDITIONING` | Conditionnement contenant le prompt encodé, ainsi que les latents de référence lorsqu'un VAE et des images de référence sont fournis. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMingImageEdit/fr.md)

---
**Source fingerprint (SHA-256):** `675fb3cc0af006e1284fdb2a5ca2c268c540ee92e1ede90b2359f4e3fc8ba5ea`
