# EmptyHunyuanImageLatent

Le nœud EmptyHunyuanImageLatent crée un espace latent vide, entièrement composé de zéros, pour les modèles de génération d'images Hunyuan. Il produit un latent de départ vide à partir de la largeur, de la hauteur et de la taille de lot fournies, qui peut ensuite être transmis aux nœuds en aval du workflow. Le tenseur latent contient 64 canaux, et chaque dimension spatiale équivaut à la dimension en pixels correspondante divisée par 32.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `width` | La largeur de l'image latente générée en pixels (par défaut : 2048, pas : 32) | INT | Oui | 64 à MAX_RESOLUTION |
| `height` | La hauteur de l'image latente générée en pixels (par défaut : 2048, pas : 32) | INT | Oui | 64 à MAX_RESOLUTION |
| `batch_size` | Le nombre d'échantillons latents à générer dans un lot (par défaut : 1) | INT | Oui | 1 à 4096 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `LATENT` | Un tenseur latent vide avec 64 canaux et des dimensions de hauteur ÷ 32 par largeur ÷ 32, prêt pour le traitement d'image Hunyuan | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanImageLatent/fr.md)

---
**Source fingerprint (SHA-256):** `31fc10d43c224810709870cf40256b6fccd4743445ea9d98d148d443bc591d7a`
