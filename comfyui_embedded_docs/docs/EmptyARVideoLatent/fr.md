# EmptyARVideoLatent

Le nœud EmptyARVideoLatent crée une représentation latente vide pour la génération vidéo. Il est utilisé pour initialiser un processus de génération vidéo en fournissant un tenseur de zéros avec les dimensions, le rapport hauteur/largeur et la longueur spécifiés.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `width` | La largeur des images vidéo en pixels (défaut : 832) | INT | Oui | 16 to 8192 (step: 16) |
| `height` | La hauteur des images vidéo en pixels (défaut : 480) | INT | Oui | 16 to 8192 (step: 16) |
| `length` | Le nombre d'images de la vidéo (défaut : 81) | INT | Oui | 1 to 1024 (step: 4) |
| `batch_size` | Le nombre de vidéos à générer dans un même lot (défaut : 1) | INT | Oui | 1 to 64 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `LATENT` | Un tenseur latent rempli de zéros, représentant un espace latent vidéo vide avec les dimensions, la longueur et la taille du lot spécifiées. La forme du tenseur est [batch_size, 16, lat_t, height/8, width/8], où lat_t est calculé à partir de la longueur. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyARVideoLatent/fr.md)

---
**Source fingerprint (SHA-256):** `02ed3c96d94f2a3df9fb5315a5312e5280b9bee280369eb1218ba10bc122e609`
