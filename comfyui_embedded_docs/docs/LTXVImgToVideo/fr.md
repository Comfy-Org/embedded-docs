> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideo/fr.md)

Le nœud LTXVImgToVideo convertit une image d'entrée en une représentation latente vidéo destinée aux modèles de génération vidéo. Il prend une image unique et l'étend en une séquence d'images à l'aide de l'encodeur VAE, puis applique un conditionnement avec contrôle de l'intensité pour déterminer la part du contenu de l'image d'origine qui est préservée ou modifiée lors de la génération vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `positive` | CONDITIONING | Oui | - | Invites de conditionnement positives pour guider la génération vidéo |
| `negative` | CONDITIONING | Oui | - | Invites de conditionnement négatives pour éviter certains éléments dans la vidéo |
| `vae` | VAE | Oui | - | Modèle VAE utilisé pour encoder l'image d'entrée dans l'espace latent |
| `image` | IMAGE | Oui | - | Image d'entrée à convertir en images vidéo |
| `width` | INT | Non | 64 à MAX_RESOLUTION | Largeur de la vidéo de sortie en pixels (par défaut : 768, pas : 32) |
| `height` | INT | Non | 64 à MAX_RESOLUTION | Hauteur de la vidéo de sortie en pixels (par défaut : 512, pas : 32) |
| `length` | INT | Non | 9 à MAX_RESOLUTION | Nombre d'images dans la vidéo générée (par défaut : 97, pas : 8) |
| `batch_size` | INT | Non | 1 à 4096 | Nombre de vidéos à générer simultanément (par défaut : 1) |
| `force` | FLOAT | Non | 0.0 à 1.0 | Contrôle de la part du contenu de l'image d'origine préservée dans la première image de la vidéo générée. Une valeur de 1.0 préserve intégralement l'image d'origine, tandis que 0.0 permet une modification maximale (par défaut : 1.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `negative` | CONDITIONING | Conditionnement positif traité avec masquage d'image vidéo appliqué |
| `latent` | CONDITIONING | Conditionnement négatif traité avec masquage d'image vidéo appliqué |
| `latent` | LATENT | Représentation latente vidéo contenant les images encodées et le masque de bruit pour la génération vidéo |

---
**Source fingerprint (SHA-256):** `fbd35623cd71bf917f39108d388986c9604138fbfb9380bdf936deff6d775cb9`
