# WanVaceToVideo

Le nœud WanVaceToVideo traite les données de conditionnement vidéo pour les modèles de génération vidéo. Il accepte des entrées de conditionnement positives et négatives ainsi que des données de contrôle vidéo, et prépare des représentations latentes pour la génération vidéo. Le nœud gère la mise à l'échelle vidéo, le masquage et l'encodage VAE pour créer la structure de conditionnement appropriée pour les modèles vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Entrée de conditionnement positive pour guider la génération | CONDITIONING | Oui | - |
| `negative` | Entrée de conditionnement négative pour guider la génération | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder les images et les trames vidéo | VAE | Oui | - |
| `width` | Largeur de la vidéo de sortie en pixels (défaut : 832, pas : 16) | INT | Oui | 16 to MAX_RESOLUTION |
| `height` | Hauteur de la vidéo de sortie en pixels (défaut : 480, pas : 16) | INT | Oui | 16 to MAX_RESOLUTION |
| `length` | Nombre de trames dans la vidéo (défaut : 81, pas : 4) | INT | Oui | 1 to MAX_RESOLUTION |
| `batch_size` | Nombre de vidéos à générer simultanément (défaut : 1) | INT | Oui | 1 to 4096 |
| `strength` | Force de conditionnement pour le contrôle VACE (défaut : 1.0, pas : 0.01). Il ne s'agit pas d'une force LoRA. Les poids LoRA sont appliqués via des nœuds LoRA séparés. | FLOAT | Oui | 0.0 to 1000.0 |
| `control_video` | Vidéo d'entrée facultative pour le conditionnement de contrôle. Si elle n'est pas fournie, une vidéo gris neutre est créée automatiquement. Lorsqu'elle est fournie, elle est redimensionnée à `width` × `height` et limitée aux premières `length` trames ; si elle contient moins de trames, les trames manquantes sont complétées par du gris neutre. | IMAGE | Non | - |
| `control_masks` | Masques facultatifs pour contrôler les parties de la vidéo à modifier. Si aucun n'est fourni, un masque entièrement blanc est utilisé. Lorsqu'ils sont fournis, le masque est redimensionné à `width` × `height`, limité à `length` trames, et complété par du blanc s'il contient moins de trames. | MASK | Non | - |
| `reference_image` | Image de référence facultative pour un conditionnement supplémentaire. Lorsqu'elle est fournie, elle est redimensionnée à `width` × `height`, encodée par le VAE, et ajoutée au début de la séquence latente. | IMAGE | Non | - |

**Remarque :** Lorsque `control_video` est fourni, il est redimensionné aux dimensions `width` et `height` spécifiées. Si des `control_masks` sont fournis, ils sont redimensionnés pour correspondre aux mêmes dimensions. L'`reference_image` est encodée via le VAE et ajoutée au début de la séquence latente lorsqu'elle est fournie. Le paramètre `length` détermine le nombre de trames, et la longueur latente est calculée comme `((length - 1) // 4) + 1`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif avec données de contrôle vidéo (vace_frames, vace_mask, vace_strength) appliquées | CONDITIONING |
| `negative` | Conditionnement négatif avec données de contrôle vidéo (vace_frames, vace_mask, vace_strength) appliquées | CONDITIONING |
| `latent` | Tenseur latent vide prêt pour la génération vidéo avec la forme [batch_size, 16, latent_length, height/8, width/8] | LATENT |
| `trim_latent` | Nombre de trames latentes à rogner lorsque l'image de référence est utilisée (0 si aucune image de référence n'est fournie) | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanVaceToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `2039b7509ce5b731e9e41d9cd2dad022d4c5004751f571a4cf88c1ba0cae405b`
