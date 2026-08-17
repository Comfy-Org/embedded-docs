# WanMoveTrackToVideo

Le nœud WanMoveTrackToVideo prépare les données de conditionnement et latentes pour la génération vidéo. Il encode une séquence d'images de départ dans l'espace latent à l'aide d'un VAE et peut éventuellement intégrer des informations de suivi de mouvement pour guider le déplacement des objets dans la vidéo générée. Le nœud génère un conditionnement positif et négatif modifié ainsi qu'un tenseur latent vide prêt pour un modèle de génération vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | L'entrée de conditionnement positif à modifier. | CONDITIONING | Oui | - |
| `negative` | L'entrée de conditionnement négatif à modifier. | CONDITIONING | Oui | - |
| `vae` | Le modèle VAE utilisé pour encoder l'image de départ dans l'espace latent. | VAE | Oui | - |
| `tracks` | Données de suivi de mouvement facultatives contenant les trajectoires d'objets. | TRACKS | Non | - |
| `strength` | Force du conditionnement de suivi. N'a d'effet que lorsque `tracks` est fourni et que la valeur est supérieure à 0.0. (défaut : 1.0) | FLOAT | Oui | 0.0 - 100.0 |
| `width` | La largeur de la vidéo de sortie. Définie par incréments de 16. (défaut : 832) | INT | Oui | 16 - MAX_RESOLUTION |
| `height` | La hauteur de la vidéo de sortie. Définie par incréments de 16. (défaut : 480) | INT | Oui | 16 - MAX_RESOLUTION |
| `length` | Le nombre d'images de la séquence vidéo. Défini par incréments de 4. (défaut : 81) | INT | Oui | 1 - MAX_RESOLUTION |
| `batch_size` | La taille du lot pour la sortie latente. (défaut : 1) | INT | Oui | 1 - 4096 |
| `start_image` | L'image de départ ou la séquence d'images à encoder avec le VAE. | IMAGE | Oui | - |
| `clip_vision_output` | Sortie facultative du modèle de vision CLIP à ajouter au conditionnement. | CLIP_VISION_OUTPUT | Non | - |

Remarque : le mouvement basé sur le suivi n'est appliqué que lorsque `tracks` est fourni et que `strength` est supérieur à 0.0. Sinon, le conditionnement reçoit l'image de départ encodée non modifiée. `start_image` est utilisé pour créer une image latente et un masque pour le conditionnement ; s'il n'est pas disponible, le nœud transmet simplement le conditionnement et produit un latent vide.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Le conditionnement positif modifié, contenant potentiellement `concat_latent_image`, `concat_mask` et `clip_vision_output`. | CONDITIONING |
| `negative` | Le conditionnement négatif modifié, contenant potentiellement `concat_latent_image`, `concat_mask` et `clip_vision_output`. | CONDITIONING |
| `latent` | Un tenseur latent vide dont les dimensions sont définies par les entrées `batch_size`, `length`, `height` et `width`. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTrackToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `b02a1a359d349a0136d84ed77a510c46cb2c8b565650ed54d5fca6c87cd0ab1f`
