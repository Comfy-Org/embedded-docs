Le nœud EmptyLTXVLatentVideo crée un tenseur latent vide pour le traitement vidéo. Il génère un point de départ vierge avec des dimensions spécifiées, pouvant être utilisé comme entrée pour les workflows de génération vidéo. Ce nœud produit une représentation latente remplie de zéros avec la largeur, la hauteur, la longueur et la taille de lot configurées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `largeur` | La largeur du tenseur vidéo latent (par défaut : 768, pas : 32) | INT | Oui | 64 à MAX_RESOLUTION |
| `hauteur` | La hauteur du tenseur vidéo latent (par défaut : 512, pas : 32) | INT | Oui | 64 à MAX_RESOLUTION |
| `longueur` | Le nombre d'images dans la vidéo latente (par défaut : 97, pas : 8) | INT | Oui | 1 à MAX_RESOLUTION |
| `taille_du_lot` | Le nombre de vidéos latentes à générer dans un lot (par défaut : 1) | INT | Non | 1 à 4096 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `samples` | Le tenseur latent vide généré avec des valeurs nulles dans les dimensions spécifiées | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLTXVLatentVideo/fr.md)

---
**Source fingerprint (SHA-256):** `c3ee9374210e100a074b238ce7ac8b5d2d2d415efd3318c9a6a7c8f7e20bda84`
