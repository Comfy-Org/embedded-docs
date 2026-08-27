# WanVaceToVideo

Le nœud WanVaceToVideo prépare les données de conditionnement vidéo pour les modèles de génération vidéo. Il prend des entrées de conditionnement positive et négative ainsi qu’une vidéo de contrôle facultative, des masques et une image de référence, et les encode en représentations latentes qui guident la génération vidéo. Le nœud gère la mise à l’échelle, le remplissage, le masquage et l’encodage VAE pour construire la structure de conditionnement appropriée pour les modèles vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | Entrée de conditionnement positive pour guider la génération | CONDITIONING | Oui | - |
| `négatif` | Entrée de conditionnement négative pour guider la génération | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder les images et les frames vidéo | VAE | Oui | - |
| `largeur` | Largeur de la vidéo de sortie en pixels (par défaut : 832, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | Hauteur de la vidéo de sortie en pixels (par défaut : 480, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `longueur` | Nombre de frames dans la vidéo (par défaut : 81, pas : 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `taille_lot` | Nombre de vidéos à générer simultanément (par défaut : 1) | INT | Oui | 1 à 4096 |
| `intensité` | Force de conditionnement pour le contrôle VACE (par défaut : 1.0, pas : 0.01). Ce n’est pas une force LoRA. Les poids LoRA sont appliqués via des nœuds LoRA séparés. | FLOAT | Oui | 0.0 à 1000.0 |
| `contrôle_vidéo` | Vidéo d’entrée facultative utilisée pour le conditionnement de contrôle. Si elle n’est pas fournie, une vidéo gris neutre est créée automatiquement. | IMAGE | Non | - |
| `masques_de_contrôle` | Masques facultatifs qui déterminent quelles parties de la vidéo de contrôle sont actives. S’ils ne sont pas fournis, un masque entièrement blanc est utilisé. | MASK | Non | - |
| `image_de_référence` | Image de référence facultative pour un conditionnement supplémentaire. Lorsqu’elle est fournie, elle est encodée et ajoutée au début de la séquence latente. | IMAGE | Non | - |

**Remarque :** Lorsque `control_video` est fourni, il est tronqué à `length` frames et redimensionné à la `width` et `height` spécifiées ; s’il a moins de frames que `length`, les frames manquantes sont remplies avec du gris neutre (valeur 0.5). Lorsqu’il n’est pas fourni, une vidéo gris neutre de `length` frames est créée automatiquement. `control_masks` sont redimensionnés à la `width` et `height` spécifiées, tronqués à `length` frames, et remplis avec la valeur 1.0 s’ils sont plus courts. Le masque sépare la vidéo de contrôle en parties inactives et réactives, chacune encodée par VAE et concaténée le long de la dimension des canaux ; le masque est également sous-échantillonné à la résolution latente. Lorsque `reference_image` est fournie, elle est encodée par VAE et ajoutée au début de la séquence latente. Le nombre de frames latentes est calculé comme `((length - 1) // 4) + 1`, et les dimensions spatiales latentes sont `height / 8` et `width / 8`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positif` | Conditionnement positif avec données de contrôle vidéo (vace_frames, vace_mask, vace_strength) appliquées | CONDITIONING |
| `négatif` | Conditionnement négatif avec données de contrôle vidéo (vace_frames, vace_mask, vace_strength) appliquées | CONDITIONING |
| `latent` | Tenseur latent vide prêt pour la génération vidéo avec la forme [batch_size, 16, latent_length, height/8, width/8] | LATENT |
| `latent_coupé` | Nombre de frames latentes à supprimer lorsqu’une image de référence est utilisée ; 0 si aucune image de référence n’est fournie | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanVaceToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `2039b7509ce5b731e9e41d9cd2dad022d4c5004751f571a4cf88c1ba0cae405b`
