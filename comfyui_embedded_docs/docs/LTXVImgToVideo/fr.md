# LTXVImgToVideo

LTXVImgToVideo convertit une image d'entrée en une représentation latente vidéo pour les modèles de génération vidéo. Il redimensionne l'image aux largeur et hauteur demandées, l'encode avec le VAE et place les images encodées au début d'un latent de taille vidéo rempli de zéros. Le contrôle `strength` détermine quelle proportion du contenu de l'image d'origine est préservée par rapport à sa modification pendant la génération vidéo.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Prompts de conditionnement positifs pour guider la génération vidéo | CONDITIONING | Oui | - |
| `negative` | Prompts de conditionnement négatifs pour éviter certains éléments dans la vidéo | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder l'image d'entrée dans l'espace latent | VAE | Oui | - |
| `image` | Image d'entrée à convertir en images vidéo | IMAGE | Oui | - |
| `width` | Largeur de la vidéo de sortie en pixels (par défaut : 768, pas : 32) | INT | Oui | 64 à MAX_RESOLUTION |
| `height` | Hauteur de la vidéo de sortie en pixels (par défaut : 512, pas : 32) | INT | Oui | 64 à MAX_RESOLUTION |
| `length` | Nombre d'images dans la vidéo générée (par défaut : 97, pas : 8) | INT | Oui | 9 à MAX_RESOLUTION |
| `batch_size` | Nombre de vidéos à générer simultanément (par défaut : 1) | INT | Oui | 1 à 4096 |
| `force` | Contrôle la proportion du contenu de l'image d'origine préservée dans les premières images de la vidéo générée. Une valeur de 1.0 préserve complètement l'image d'origine, tandis qu'une valeur de 0.0 permet une modification maximale (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |

Remarque : `width` et `height` changent par pas de 32 pixels, et `length` change par pas de 8 images, ce qui correspond à la compression latente vidéo (32x dans les dimensions spatiales et 8x dans la dimension temporelle). Le latent vidéo contient ((length - 1) // 8) + 1 images. L'image d'entrée est redimensionnée à `width` x `height` à l'aide d'une mise à l'échelle bilinéaire avec recadrage centré, et seuls les trois premiers canaux sont utilisés pour l'encodage.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Le conditionnement positif transmis inchangé pour être utilisé avec le latent généré | CONDITIONING |
| `negative` | Le conditionnement négatif transmis inchangé pour être utilisé avec le latent généré | CONDITIONING |
| `latent` | Représentation latente vidéo contenant les images encodées et un masque de bruit qui contrôle la force avec laquelle le conditionnement est appliqué pendant la génération vidéo | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `4ebc7f80b4d9ac3329e3349c7048885de22b827b5bdd102976687afd7e07a16b`
