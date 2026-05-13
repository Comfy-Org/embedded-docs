> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanVaceToVideo/fr.md)

Le nœud WanVaceToVideo traite les données de conditionnement vidéo pour les modèles de génération vidéo. Il prend en entrée des conditionnements positifs et négatifs, ainsi que des données de contrôle vidéo, et prépare des représentations latentes pour la génération vidéo. Ce nœud gère le redimensionnement vidéo, le masquage et l'encodage VAE afin de créer la structure de conditionnement appropriée pour les modèles vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `positif` | CONDITIONING | Oui | - | Conditionnement positif guidant la génération |
| `négatif` | CONDITIONING | Oui | - | Conditionnement négatif guidant la génération |
| `vae` | VAE | Oui | - | Modèle VAE utilisé pour encoder les images et les trames vidéo |
| `largeur` | INT | Oui | 16 à MAX_RESOLUTION | Largeur de la vidéo de sortie en pixels (par défaut : 832, pas : 16) |
| `hauteur` | INT | Oui | 16 à MAX_RESOLUTION | Hauteur de la vidéo de sortie en pixels (par défaut : 480, pas : 16) |
| `longueur` | INT | Oui | 1 à MAX_RESOLUTION | Nombre de trames dans la vidéo (par défaut : 81, pas : 4) |
| `taille_lot` | INT | Oui | 1 à 4096 | Nombre de vidéos à générer simultanément (par défaut : 1) |
| `intensité` | FLOAT | Oui | 0.0 à 1000.0 | Force de contrôle pour le conditionnement vidéo (par défaut : 1.0, pas : 0.01) |
| `contrôle_vidéo` | IMAGE | Non | - | Vidéo d'entrée optionnelle pour le conditionnement de contrôle |
| `masques_de_contrôle` | MASK | Non | - | Masques optionnels pour contrôler les parties de la vidéo à modifier |
| `image_de_référence` | IMAGE | Non | - | Image de référence optionnelle pour un conditionnement supplémentaire |

**Remarque :** Lorsque `control_video` est fourni, il sera redimensionné pour correspondre à la largeur et à la hauteur spécifiées. Si `control_masks` sont fournis, ils doivent correspondre aux dimensions de la vidéo de contrôle. L'`reference_image` est encodée via le VAE et ajoutée au début de la séquence latente lorsqu'elle est fournie.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `négatif` | CONDITIONING | Conditionnement positif avec les données de contrôle vidéo appliquées |
| `latent` | CONDITIONING | Conditionnement négatif avec les données de contrôle vidéo appliquées |
| `latent_coupé` | LATENT | Tenseur latent vide prêt pour la génération vidéo |
| `trim_latent` | INT | Nombre de trames latentes à supprimer lors de l'utilisation d'une image de référence |

---
**Source fingerprint (SHA-256):** `66e50a360dc99ac49cac8f3f1c8649bf4298da2934c1bd9a0bc7cfbec620b291`
