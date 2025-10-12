> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideo/fr.md)

Le nœud LTXVImgToVideo convertit une image d'entrée en une représentation latente vidéo pour les modèles de génération vidéo. Il prend une seule image et l'étend en une séquence de trames à l'aide de l'encodeur VAE, puis applique un conditionnement avec un contrôle de l'intensité pour déterminer dans quelle mesure le contenu original de l'image est préservé ou modifié pendant la génération vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Oui | - | Conditionnements positifs pour guider la génération vidéo |
| `negative` | CONDITIONING | Oui | - | Conditionnements négatifs pour éviter certains éléments dans la vidéo |
| `vae` | VAE | Oui | - | Modèle VAE utilisé pour encoder l'image d'entrée dans l'espace latent |
| `image` | IMAGE | Oui | - | Image d'entrée à convertir en trames vidéo |
| `width` | INT | Non | 64 à MAX_RESOLUTION | Largeur de la vidéo de sortie en pixels (par défaut : 768, pas : 32) |
| `height` | INT | Non | 64 à MAX_RESOLUTION | Hauteur de la vidéo de sortie en pixels (par défaut : 512, pas : 32) |
| `length` | INT | Non | 9 à MAX_RESOLUTION | Nombre de trames dans la vidéo générée (par défaut : 97, pas : 8) |
| `batch_size` | INT | Non | 1 à 4096 | Nombre de vidéos à générer simultanément (par défaut : 1) |
| `force` | FLOAT | Non | 0.0 à 1.0 | Contrôle de la modification de l'image originale pendant la génération vidéo, où 1.0 préserve la majeure partie du contenu original et 0.0 permet une modification maximale (par défaut : 1.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `negative` | CONDITIONING | Conditionnement positif traité avec application d'un masque de trame vidéo |
| `latent` | CONDITIONING | Conditionnement négatif traité avec application d'un masque de trame vidéo |
| `latent` | LATENT | Représentation latente vidéo contenant les trames encodées et le masque de bruit pour la génération vidéo |