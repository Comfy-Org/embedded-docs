> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanVideo15Latent/fr.md)

Ce nœud crée un tenseur latent vide spécifiquement formaté pour une utilisation avec le modèle HunyuanVideo 1.5. Il génère un point de départ vierge pour la création vidéo en allouant un tenseur de zéros avec le nombre de canaux et les dimensions spatiales corrects pour l'espace latent du modèle.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | Oui | - | La largeur de la trame vidéo en pixels. |
| `height` | INT | Oui | - | La hauteur de la trame vidéo en pixels. |
| `length` | INT | Oui | - | Le nombre de trames dans la séquence vidéo. |
| `batch_size` | INT | Non | - | Le nombre d'échantillons vidéo à générer dans un lot (par défaut : 1). |

**Note :** Les dimensions spatiales du tenseur latent généré sont calculées en divisant les entrées `width` et `height` par 16. La dimension temporelle (trames) est calculée comme `((length - 1) // 4) + 1`.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `samples` | LATENT | Un tenseur latent vide avec des dimensions adaptées au modèle HunyuanVideo 1.5. Le tenseur a une forme de `[batch_size, 32, frames, height//16, width//16]`. |
