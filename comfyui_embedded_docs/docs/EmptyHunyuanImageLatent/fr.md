# EmptyHunyuanImageLatent

Le nœud EmptyHunyuanImageLatent crée un tenseur latent vide avec des dimensions spécifiques pour une utilisation avec les modèles de génération d'images Hunyuan. Il génère un point de départ vierge qui peut être traité via les nœuds suivants dans le workflow. Ce nœud permet de spécifier la largeur, la hauteur et la taille du lot de l'espace latent.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `largeur` | La largeur de l'image latente générée en pixels (par défaut : 2048, pas : 32) | INT | Oui | 64 à MAX_RESOLUTION |
| `hauteur` | La hauteur de l'image latente générée en pixels (par défaut : 2048, pas : 32) | INT | Oui | 64 à MAX_RESOLUTION |
| `taille_du_lot` | Le nombre d'échantillons latents à générer dans un lot (par défaut : 1) | INT | Oui | 1 à 4096 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `LATENT` | Un tenseur latent vide avec les dimensions spécifiées pour le traitement d'images Hunyuan | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanImageLatent/fr.md)

---
**Source fingerprint (SHA-256):** `18e920527c88be2648d8cbe4255f693123be4e70a9e21dd379310088a1470834`
