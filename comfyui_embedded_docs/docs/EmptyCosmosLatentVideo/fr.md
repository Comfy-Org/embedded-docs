# VidéoLatenteCosmosVide

Le nœud EmptyCosmosLatentVideo crée un tenseur vidéo latent vide avec des dimensions spécifiées. Il génère une représentation latente remplie de zéros qui peut être utilisée comme point de départ pour les workflows de génération vidéo, avec des paramètres configurables pour la largeur, la hauteur, la longueur et la taille du lot.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `largeur` | La largeur de la vidéo latente en pixels (par défaut : 1280, doit être divisible par 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | La hauteur de la vidéo latente en pixels (par défaut : 704, doit être divisible par 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `longueur` | Le nombre d'images dans la vidéo latente (par défaut : 121, doit être divisible par 8) | INT | Oui | 1 à MAX_RESOLUTION |
| `taille_du_lot` | Le nombre de vidéos latentes à générer dans un lot (par défaut : 1) | INT | Non | 1 à 4096 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `samples` | Le tenseur vidéo latent vide généré avec des valeurs nulles | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyCosmosLatentVideo/fr.md)

---
**Source fingerprint (SHA-256):** `f473820af3faf7cb6992ff1959089801e333df395b4007abeb9b504962bfc73b`
