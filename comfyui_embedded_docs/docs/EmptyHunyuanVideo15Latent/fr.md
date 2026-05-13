> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanVideo15Latent/fr.md)

Ce nœud crée un tenseur latent vide spécialement formaté pour être utilisé avec le modèle HunyuanVideo 1.5. Il génère un point de départ vierge pour la génération vidéo en allouant un tenseur de zéros avec le nombre correct de canaux et les dimensions spatiales adaptées à l'espace latent du modèle.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `largeur` | INT | Oui | - | La largeur de l'image vidéo en pixels. |
| `hauteur` | INT | Oui | - | La hauteur de l'image vidéo en pixels. |
| `longueur` | INT | Oui | - | Le nombre d'images dans la séquence vidéo. |
| `taille_lot` | INT | Non | - | Le nombre d'échantillons vidéo à générer dans un lot (par défaut : 1). |

**Remarque :** Les dimensions spatiales du tenseur latent généré sont calculées en divisant la `width` et la `height` d'entrée par 16. La dimension temporelle (images) est calculée comme suit : `((length - 1) // 4) + 1`.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `samples` | LATENT | Un tenseur latent vide avec des dimensions adaptées au modèle HunyuanVideo 1.5. Le tenseur a une forme de `[batch_size, 32, frames, height//16, width//16]`. La sortie inclut également une valeur `downscale_ratio_spacial` de 16. |

---
**Source fingerprint (SHA-256):** `eebc131adfe63f6bc8367f2a96b3ac7f3f3223c5b1fb308eda3ec09c94fff2ee`
