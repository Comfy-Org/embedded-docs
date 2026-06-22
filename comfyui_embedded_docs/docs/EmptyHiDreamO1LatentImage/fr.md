# Image latente HiDream-O1 vide

Voici la traduction en français de la documentation du nœud ComfyUI `EmptyHiDreamO1LatentImage` :

## Aperçu

Ce nœud crée une image latente vide dans l'espace pixel, spécialement conçue pour le modèle HiDream-O1-Image. Il génère un tenseur vide de zéros qui sert de point de départ pour la génération d'images, avec des dimensions définies par les entrées de largeur, hauteur et taille de lot.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `largeur` | La largeur de l'image latente en pixels (par défaut : 2048). Le modèle a été entraîné à environ 4 mégapixels ; des résolutions plus faibles s'écartent de la distribution et la qualité régresse de manière notable. | INT | Oui | 64 à 4096 (pas : 32) |
| `hauteur` | La hauteur de l'image latente en pixels (par défaut : 2048). Le modèle a été entraîné à environ 4 mégapixels ; des résolutions plus faibles s'écartent de la distribution et la qualité régresse de manière notable. | INT | Oui | 64 à 4096 (pas : 32) |
| `taille_lot` | Le nombre d'images latentes à générer en un seul lot (par défaut : 1). | INT | Non | 1 à 64 |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `samples` | Un tenseur rempli de zéros représentant l'image latente vide, avec la forme (batch_size, 3, height, width). | LATENT |

## Remarques

- Le modèle HiDream-O1-Image a été entraîné à environ 4 mégapixels. L'utilisation de résolutions nettement inférieures peut entraîner une qualité d'image réduite.
- Les résolutions d'entraînement incluent : 2048x2048, 2304x1728, 1728x2304, 2560x1440, 1440x2560, 2496x1664, 1664x2496, 3104x1312, 1312x3104, 2304x1792, 1792x2304.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHiDreamO1LatentImage/fr.md)

---
**Source fingerprint (SHA-256):** `fca32bbeddf120b4a7f9a9b88814f5345db133b35252c4d86079397be350c15e`
