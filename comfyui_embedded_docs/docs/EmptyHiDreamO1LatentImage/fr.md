# Image latente HiDream-O1 vide

Ce nœud crée une image latente vide dans l’espace des pixels, spécialement conçue pour le modèle HiDream-O1-Image. Il génère un tenseur de zéros qui sert de point de départ à la génération d’image, avec des dimensions définies par les entrées `width`, `height` et `batch_size`.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `largeur` | La largeur de l’image latente en pixels (par défaut : 2048). Le modèle a été entraîné à environ 4 mégapixels ; les résolutions inférieures sortent de la distribution et la qualité régresse sensiblement. | INT | Oui | 64 à 4096 (step: 32) |
| `hauteur` | La hauteur de l’image latente en pixels (par défaut : 2048). Le modèle a été entraîné à environ 4 mégapixels ; les résolutions inférieures sortent de la distribution et la qualité régresse sensiblement. | INT | Oui | 64 à 4096 (step: 32) |
| `taille_lot` | Le nombre d’images latentes à générer en un seul lot (par défaut : 1). | INT | Non | 1 à 64 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `samples` | Un tenseur rempli de zéros représentant l’image latente vide, avec une forme (batch_size, 3, height, width). | LATENT |

## Remarques

- Le modèle HiDream-O1-Image a été entraîné à environ 4 mégapixels. L’utilisation de résolutions nettement inférieures peut entraîner une qualité d’image réduite.
- Les résolutions d’entraînement incluent : 2048x2048, 2304x1728, 1728x2304, 2560x1440, 1440x2560, 2496x1664, 1664x2496, 3104x1312, 1312x3104, 2304x1792, 1792x2304.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHiDreamO1LatentImage/fr.md)

---
**Source fingerprint (SHA-256):** `7412639e261512d9174e60009143c8c06c354e2a20ada7271837d72053426be5`
