# LTXVImgToVideo

Le nœud LTXVImgToVideo convertit une image d'entrée en une représentation latente vidéo destinée aux modèles de génération vidéo. Il prend une image unique et l'étend en une séquence d'images à l'aide de l'encodeur VAE, puis applique un conditionnement avec contrôle de l'intensité pour déterminer la part du contenu de l'image d'origine qui est préservée ou modifiée lors de la génération vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Invites de conditionnement positives pour guider la génération vidéo | CONDITIONING | Oui | - |
| `negative` | Invites de conditionnement négatives pour éviter certains éléments dans la vidéo | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder l'image d'entrée dans l'espace latent | VAE | Oui | - |
| `image` | Image d'entrée à convertir en images vidéo | IMAGE | Oui | - |
| `width` | Largeur de la vidéo de sortie en pixels (par défaut : 768, pas : 32) | INT | Non | 64 à MAX_RESOLUTION |
| `height` | Hauteur de la vidéo de sortie en pixels (par défaut : 512, pas : 32) | INT | Non | 64 à MAX_RESOLUTION |
| `length` | Nombre d'images dans la vidéo générée (par défaut : 97, pas : 8) | INT | Non | 9 à MAX_RESOLUTION |
| `batch_size` | Nombre de vidéos à générer simultanément (par défaut : 1) | INT | Non | 1 à 4096 |
| `force` | Contrôle de la part du contenu de l'image d'origine préservée dans la première image de la vidéo générée. Une valeur de 1.0 préserve intégralement l'image d'origine, tandis que 0.0 permet une modification maximale (par défaut : 1.0) | FLOAT | Non | 0.0 à 1.0 |


| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif traité avec masquage d'image vidéo appliqué | CONDITIONING |
| `negative` | Conditionnement négatif traité avec masquage d'image vidéo appliqué | CONDITIONING |
| `latent` | Représentation latente vidéo contenant les images encodées et le masque de bruit pour la génération vidéo | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `fbd35623cd71bf917f39108d388986c9604138fbfb9380bdf936deff6d775cb9`
