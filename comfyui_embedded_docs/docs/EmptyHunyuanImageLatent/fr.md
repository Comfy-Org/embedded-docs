# EmptyHunyuanImageLatent

Le nœud EmptyHunyuanImageLatent crée un espace latent vide (rempli de zéros) pour les modèles de génération d'images Hunyuan. Il génère un latent de départ vierge avec la largeur, la hauteur et la taille de lot spécifiées, qui peut être transmis aux nœuds en aval dans le workflow. Le tenseur latent possède 64 canaux, et ses dimensions spatiales sont la largeur et la hauteur divisées chacune par 32.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `largeur` | La largeur de l'image latente générée en pixels (défaut : 2048, pas : 32) | INT | Oui | 64 à MAX_RESOLUTION |
| `hauteur` | La hauteur de l'image latente générée en pixels (défaut : 2048, pas : 32) | INT | Oui | 64 à MAX_RESOLUTION |
| `taille_du_lot` | Le nombre d'échantillons latents à générer dans un lot (défaut : 1) | INT | Oui | 1 à 4096 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `LATENT` | Un tenseur latent vide avec 64 canaux et des dimensions de hauteur ÷ 32 par largeur ÷ 32, prêt pour le traitement d'images Hunyuan | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanImageLatent/fr.md)

---
**Source fingerprint (SHA-256):** `31fc10d43c224810709870cf40256b6fccd4743445ea9d98d148d443bc591d7a`
