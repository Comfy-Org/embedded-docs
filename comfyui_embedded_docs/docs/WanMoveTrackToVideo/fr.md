# WanMoveTrackToVideo

Le nœud WanMoveTrackToVideo prépare les données de conditionnement et d'espace latent pour la génération vidéo, en intégrant éventuellement des informations de suivi de mouvement. Il encode une séquence d'images de départ en une représentation latente et peut fusionner des données de position provenant de pistes d'objets pour guider le mouvement dans la vidéo générée. Le nœud produit un conditionnement positif et négatif modifié, ainsi qu'un tenseur latent vide prêt pour un modèle vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | L'entrée de conditionnement positif à modifier. | CONDITIONING | Oui | - |
| `négatif` | L'entrée de conditionnement négatif à modifier. | CONDITIONING | Oui | - |
| `vae` | Le modèle VAE utilisé pour encoder l'image de départ dans l'espace latent. | VAE | Oui | - |
| `pistes` | Données de suivi de mouvement facultatives contenant les trajectoires d'objets. | TRACKS | Non | - |
| `force` | Force du conditionnement par pistes. (par défaut : 1,0) | FLOAT | Non | 0,0 - 100,0 |
| `largeur` | La largeur de la vidéo de sortie. Doit être divisible par 16. (par défaut : 832) | INT | Non | 16 - RÉSOLUTION_MAX |
| `hauteur` | La hauteur de la vidéo de sortie. Doit être divisible par 16. (par défaut : 480) | INT | Non | 16 - RÉSOLUTION_MAX |
| `longueur` | Le nombre d'images dans la séquence vidéo. (par défaut : 81) | INT | Non | 1 - RÉSOLUTION_MAX |
| `taille_du_lot` | La taille du lot pour la sortie latente. (par défaut : 1) | INT | Non | 1 - 4096 |
| `image_de_départ` | L'image ou la séquence d'images de départ à encoder. | IMAGE | Oui | - |
| `clip_vision_output` | Sortie facultative du modèle de vision CLIP à ajouter au conditionnement. | CLIPVISIONOUTPUT | Non | - |

**Remarque :** Le paramètre `strength` n'a d'effet que lorsque des `tracks` sont fournies. Si aucune piste n'est fournie ou si `strength` est à 0,0, le conditionnement par pistes n'est pas appliqué. L'image de départ (`start_image`) est utilisée pour créer une image latente et un masque pour le conditionnement ; si elle n'est pas fournie, le nœud se contente de transmettre le conditionnement et produit un tenseur latent vide.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `négatif` | Le conditionnement positif modifié, pouvant contenir `concat_latent_image`, `concat_mask` et `clip_vision_output`. | CONDITIONING |
| `latent` | Le conditionnement négatif modifié, pouvant contenir `concat_latent_image`, `concat_mask` et `clip_vision_output`. | CONDITIONING |
| `latent` | Un tenseur latent vide dont les dimensions sont définies par les entrées `taille_du_lot`, `longueur`, `hauteur` et `largeur`. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTrackToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `9677addf5b94b42efd3015f51380c1fa9b16d4a5105cc7f24de0be34c0042bbc`
