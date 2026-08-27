# WanMoveTrackToVideo

Le nœud WanMoveTrackToVideo prépare les données de conditionnement et d'espace latent pour la génération vidéo, en intégrant des informations optionnelles de suivi de mouvement. Il encode une séquence d'images de départ en une représentation latente et peut y combiner les données de position des pistes d'objets pour guider le mouvement dans la vidéo générée. Le nœud produit un conditionnement positif et négatif modifié ainsi qu'un tenseur latent vide prêt pour un modèle vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | L'entrée de conditionnement positif à modifier. | CONDITIONING | Oui | - |
| `négatif` | L'entrée de conditionnement négatif à modifier. | CONDITIONING | Oui | - |
| `vae` | Le modèle VAE utilisé pour encoder l'image de départ dans l'espace latent. | VAE | Oui | - |
| `pistes` | Données optionnelles de suivi de mouvement contenant les trajectoires d'objets. | TRACKS | Non | - |
| `force` | Force du conditionnement par pistes. (défaut : 1.0) | FLOAT | Oui | 0.0 - 100.0 |
| `largeur` | La largeur de la vidéo de sortie. Doit être divisible par 16. (défaut : 832) | INT | Oui | 16 - MAX_RESOLUTION |
| `hauteur` | La hauteur de la vidéo de sortie. Doit être divisible par 16. (défaut : 480) | INT | Oui | 16 - MAX_RESOLUTION |
| `longueur` | Le nombre de frames dans la séquence vidéo, par incréments de 4. (défaut : 81) | INT | Oui | 1 - MAX_RESOLUTION |
| `taille_du_lot` | La taille du lot pour la sortie latente. (défaut : 1) | INT | Oui | 1 - 4096 |
| `image_de_départ` | L'image de départ ou la séquence d'images à encoder. | IMAGE | Oui | - |
| `clip_vision_output` | Sortie optionnelle du modèle de vision CLIP à ajouter au conditionnement. | CLIP_VISION_OUTPUT | Non | - |

**Remarque :** Le paramètre `strength` n'a d'effet que lorsque `tracks` est fourni et que `strength` est supérieur à 0,0 ; le conditionnement par pistes n'est appliqué que si `start_image` est également fourni. Si `tracks` n'est pas fourni ou si `strength` vaut 0,0, le mélange des pistes est ignoré. Lorsque le mélange des pistes est actif, le conditionnement positif reçoit l'image latente fusionnée avec les pistes, tandis que le conditionnement négatif reçoit l'image latente non modifiée. Si `start_image` n'est pas fourni, aucun conditionnement d'image latente ni de masque n'est créé ; le conditionnement positif et négatif est transmis tel quel (sauf que `clip_vision_output` est toujours ajouté s'il est fourni), et le nœud produit un latent vide.

**Remarque :** Lorsque `start_image` est fourni, la séquence d'images est redimensionnée à la `width` et à la `height` cibles et tronquée aux `length` premières frames. Si la séquence est plus courte que `length`, les frames restantes sont remplies avec des frames gris neutres (valeur 0,5) avant l'encodage VAE. Le conditionnement résultant inclut un `concat_mask` avec la valeur 0 aux positions temporelles correspondant aux frames de l'image de départ et 1 ailleurs.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positif` | Le conditionnement positif modifié, contenant potentiellement `concat_latent_image`, `concat_mask` et `clip_vision_output`. | CONDITIONING |
| `négatif` | Le conditionnement négatif modifié, contenant potentiellement `concat_latent_image`, `concat_mask` et `clip_vision_output`. | CONDITIONING |
| `latent` | Un tenseur latent vide de forme `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]`, déterminé par les entrées `batch_size`, `length`, `height` et `width`. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTrackToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `b02a1a359d349a0136d84ed77a510c46cb2c8b565650ed54d5fca6c87cd0ab1f`
