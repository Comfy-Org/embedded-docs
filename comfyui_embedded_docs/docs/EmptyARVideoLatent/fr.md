# EmptyARVideoLatent

Le nœud EmptyARVideoLatent crée une représentation latente vide pour la génération vidéo. Il construit un tenseur de zéros en utilisant la largeur, la hauteur, le nombre d’images et la taille de lot demandés, qui peut ensuite servir à initialiser un processus de génération vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `width` | Largeur des images de la vidéo en pixels (par défaut : 832) | INT | Oui | 16 à 8192 (pas : 16) |
| `height` | Hauteur des images de la vidéo en pixels (par défaut : 480) | INT | Oui | 16 à 8192 (pas : 16) |
| `length` | Nombre d’images dans la vidéo (par défaut : 81) | INT | Oui | 1 à 1024 (pas : 4) |
| `batch_size` | Nombre de vidéos à générer dans un seul lot (par défaut : 1) | INT | Oui | 1 à 64 |

Remarque : la taille latente interne est dérivée de ces entrées. `width` et `height` sont divisés par 8, et le nombre de pas de temps latents est calculé comme `((length - 1) // 4) + 1`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `LATENT` | Un tenseur latent rempli de zéros, représentant un espace latent vidéo vide avec les dimensions, la longueur et la taille de lot spécifiées. La forme du tenseur est [batch_size, 16, lat_t, height/8, width/8], où lat_t = ((length - 1) // 4) + 1 correspond au nombre de pas de temps latents dérivés de la longueur demandée. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyARVideoLatent/fr.md)

---
**Source fingerprint (SHA-256):** `02ed3c96d94f2a3df9fb5315a5312e5280b9bee280369eb1218ba10bc122e609`
