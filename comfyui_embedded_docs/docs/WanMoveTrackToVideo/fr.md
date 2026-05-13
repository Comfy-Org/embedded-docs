> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTrackToVideo/fr.md)

Le nœud WanMoveTrackToVideo prépare les données de conditionnement et d'espace latent pour la génération vidéo, en intégrant éventuellement des informations de suivi de mouvement. Il encode une séquence d'images de départ en une représentation latente et peut fusionner des données de position provenant de pistes d'objets pour guider le mouvement dans la vidéo générée. Le nœud produit un conditionnement positif et négatif modifié, ainsi qu'un tenseur latent vide prêt pour un modèle vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `positif` | CONDITIONING | Oui | - | L'entrée de conditionnement positif à modifier. |
| `négatif` | CONDITIONING | Oui | - | L'entrée de conditionnement négatif à modifier. |
| `vae` | VAE | Oui | - | Le modèle VAE utilisé pour encoder l'image de départ dans l'espace latent. |
| `pistes` | TRACKS | Non | - | Données de suivi de mouvement facultatives contenant les trajectoires d'objets. |
| `force` | FLOAT | Non | 0,0 - 100,0 | Force du conditionnement par pistes. (par défaut : 1,0) |
| `largeur` | INT | Non | 16 - RÉSOLUTION_MAX | La largeur de la vidéo de sortie. Doit être divisible par 16. (par défaut : 832) |
| `hauteur` | INT | Non | 16 - RÉSOLUTION_MAX | La hauteur de la vidéo de sortie. Doit être divisible par 16. (par défaut : 480) |
| `longueur` | INT | Non | 1 - RÉSOLUTION_MAX | Le nombre d'images dans la séquence vidéo. (par défaut : 81) |
| `taille_du_lot` | INT | Non | 1 - 4096 | La taille du lot pour la sortie latente. (par défaut : 1) |
| `image_de_départ` | IMAGE | Oui | - | L'image ou la séquence d'images de départ à encoder. |
| `clip_vision_output` | CLIPVISIONOUTPUT | Non | - | Sortie facultative du modèle de vision CLIP à ajouter au conditionnement. |

**Remarque :** Le paramètre `strength` n'a d'effet que lorsque des `tracks` sont fournies. Si aucune piste n'est fournie ou si `strength` est à 0,0, le conditionnement par pistes n'est pas appliqué. L'image de départ (`start_image`) est utilisée pour créer une image latente et un masque pour le conditionnement ; si elle n'est pas fournie, le nœud se contente de transmettre le conditionnement et produit un tenseur latent vide.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `négatif` | CONDITIONING | Le conditionnement positif modifié, pouvant contenir `concat_latent_image`, `concat_mask` et `clip_vision_output`. |
| `latent` | CONDITIONING | Le conditionnement négatif modifié, pouvant contenir `concat_latent_image`, `concat_mask` et `clip_vision_output`. |
| `latent` | LATENT | Un tenseur latent vide dont les dimensions sont définies par les entrées `taille_du_lot`, `longueur`, `hauteur` et `largeur`. |

---
**Source fingerprint (SHA-256):** `9677addf5b94b42efd3015f51380c1fa9b16d4a5105cc7f24de0be34c0042bbc`
