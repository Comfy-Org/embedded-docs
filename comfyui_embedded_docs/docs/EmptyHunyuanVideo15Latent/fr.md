# HunyuanVideo 1.5 latent vide

Ce nœud crée un tenseur latent vide spécialement formaté pour être utilisé avec le modèle HunyuanVideo 1.5. Il génère un point de départ vide pour la génération vidéo en allouant un tenseur de zéros avec le nombre de canaux et les dimensions spatiales corrects pour l'espace latent du modèle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `largeur` | La largeur de la trame vidéo en pixels. | INT | Oui | - |
| `hauteur` | La hauteur de la trame vidéo en pixels. | INT | Oui | - |
| `longueur` | Le nombre de trames dans la séquence vidéo. | INT | Oui | - |
| `taille_lot` | Le nombre d'échantillons vidéo à générer dans un lot (par défaut : 1). | INT | Non | - |

**Remarque :** Les dimensions spatiales du tenseur latent généré sont calculées en divisant les entrées `width` et `height` par 16 (ce nœud utilise un facteur d'échelle spatial de 16 plutôt que 8). La dimension temporelle (trames) est calculée comme `((length - 1) // 4) + 1`. Ces calculs utilisent une division entière, donc `width` et `height` doivent être des multiples de 16 pour éviter toute troncature.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `samples` | Un tenseur latent vide avec des dimensions adaptées au modèle HunyuanVideo 1.5. Le tenseur a une forme de `[batch_size, 32, ((length - 1) // 4) + 1, height // 16, width // 16]`. La sortie inclut également une valeur `downscale_ratio_spacial` de 16. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanVideo15Latent/fr.md)

---
**Source fingerprint (SHA-256):** `ce7ec75e8433c778d175a3e2ea260a4397aa5507428908b9a32f50fbe9e184c6`
