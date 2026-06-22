# TextEncodeBooguEdit

Ce nœud prépare le conditionnement pour l'édition d'images avec Boogu. Il traite les images de référence pour produire à la fois un conditionnement positif et négatif. L'image de référence est utilisée deux fois : les tokens visuels de l'image sont ajoutés uniquement au conditionnement positif pour amplifier l'instruction d'édition, tandis qu'un latent de référence VAE est ajouté aux conditionnements positif et négatif afin de s'annuler sous CFG, préservant ainsi l'identité de l'image d'origine.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `clip` | Le modèle CLIP utilisé pour l'encodage de texte | CLIP | Oui | |
| `prompt` | Le prompt textuel décrivant l'édition souhaitée | STRING | Oui | |
| `negative_prompt` | Le prompt textuel décrivant ce qu'il faut éviter dans l'édition | STRING | Non | |
| `vae` | Le modèle VAE utilisé pour encoder les images de référence dans l'espace latent | VAE | Non | |
| `images` | Image(s) de référence à éditer. Boogu se concentre sur une référence par échantillon ; plusieurs sont autorisées. | IMAGE | Non | Jusqu'à 16 images |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `negative` | Conditionnement contenant à la fois le prompt textuel avec les tokens visuels et les latents de référence | CONDITIONING |
| `negative` | Conditionnement contenant le prompt textuel négatif et les latents de référence | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeBooguEdit/fr.md)

---
**Source fingerprint (SHA-256):** `170979acf5b2e9f25f96231a4b23a4376cfddcd4bda2fdd6e03528417e6931b0`
