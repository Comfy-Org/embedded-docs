# WanVaceToVideo

Le nœud WanVaceToVideo prépare les données de conditionnement vidéo pour les modèles de génération vidéo contrôlés par VACE. Il combine un conditionnement positif et négatif avec une vidéo de contrôle facultative, des masques de contrôle et une image de référence, les encode via un VAE, et produit un conditionnement mis à jour, un tenseur latent vide et une valeur de rognage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | Entrée de conditionnement positif pour guider la génération | CONDITIONING | Oui | - |
| `négatif` | Entrée de conditionnement négatif pour guider la génération | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder les images et les trames vidéo | VAE | Oui | - |
| `largeur` | Largeur de la vidéo de sortie en pixels (par défaut : 832, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | Hauteur de la vidéo de sortie en pixels (par défaut : 480, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `longueur` | Nombre de trames dans la vidéo (par défaut : 81, pas : 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `taille_lot` | Nombre de vidéos à générer simultanément (par défaut : 1) | INT | Oui | 1 à 4096 |
| `intensité` | Force du conditionnement pour le contrôle VACE (par défaut : 1.0, pas : 0.01). Il ne s'agit pas d'une force LoRA. Les poids LoRA sont appliqués via des nœuds LoRA distincts. | FLOAT | Oui | 0.0 à 1000.0 |
| `contrôle_vidéo` | Vidéo d'entrée facultative utilisée pour le conditionnement de contrôle. Si elle n'est pas fournie, une vidéo gris neutre est créée automatiquement. | IMAGE | Non | - |
| `masques_de_contrôle` | Masques facultatifs qui déterminent quelles parties de la vidéo de contrôle sont actives. S'ils ne sont pas fournis, un masque blanc complet est utilisé. | MASK | Non | - |
| `image_de_référence` | Image de référence facultative pour un conditionnement supplémentaire. Lorsqu'elle est fournie, elle est encodée et ajoutée au début de la séquence latente. Seule la première image est utilisée. | IMAGE | Non | - |

**Remarque :** Lorsque `control_video` est fourni, il est tronqué à `length` trames et mis à l'échelle vers les `width` et `height` spécifiés ; s'il contient moins de trames que `length`, les trames manquantes sont complétées par du gris neutre (valeur 0.5). Lorsqu'il n'est pas fourni, une vidéo gris neutre de `length` trames est créée automatiquement. `control_masks` sont mis à l'échelle vers les `width` et `height` spécifiés, tronqués à `length` trames, et complétés par la valeur 1.0 s'ils sont plus courts. Le masque sépare la vidéo de contrôle en parties inactive et réactive, chacune étant encodée par le VAE et concaténée selon la dimension des canaux ; le masque est également sous-échantillonné à la résolution latente. Lorsque `reference_image` est fournie, sa première image est encodée par le VAE et ajoutée au début de la séquence latente, et `trim_latent` indique le nombre de trames latentes ajoutées. Le nombre de trames latentes est calculé comme `((length - 1) // 4) + 1`, et les dimensions spatiales latentes sont `height / 8` et `width / 8`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif avec les données de contrôle vidéo (vace_frames, vace_mask, vace_strength) appliquées | CONDITIONING |
| `negative` | Conditionnement négatif avec les données de contrôle vidéo (vace_frames, vace_mask, vace_strength) appliquées | CONDITIONING |
| `latent` | Tenseur latent vide prêt pour la génération vidéo avec la forme [batch_size, 16, latent_length, height/8, width/8] | LATENT |
| `trim_latent` | Nombre de trames latentes à rogner lorsqu'une image de référence est utilisée ; 0 si aucune image de référence n'est fournie | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanVaceToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `2039b7509ce5b731e9e41d9cd2dad022d4c5004751f571a4cf88c1ba0cae405b`
