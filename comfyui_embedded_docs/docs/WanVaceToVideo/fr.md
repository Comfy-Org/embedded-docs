Le nœud WanVaceToVideo traite les données de conditionnement vidéo pour les modèles de génération vidéo. Il prend en entrée des conditionnements positifs et négatifs, ainsi que des données de contrôle vidéo, et prépare des représentations latentes pour la génération vidéo. Ce nœud gère le redimensionnement vidéo, le masquage et l'encodage VAE afin de créer la structure de conditionnement appropriée pour les modèles vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | Conditionnement positif guidant la génération | CONDITIONING | Oui | - |
| `négatif` | Conditionnement négatif guidant la génération | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder les images et les trames vidéo | VAE | Oui | - |
| `largeur` | Largeur de la vidéo de sortie en pixels (par défaut : 832, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | Hauteur de la vidéo de sortie en pixels (par défaut : 480, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `longueur` | Nombre de trames dans la vidéo (par défaut : 81, pas : 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `taille_lot` | Nombre de vidéos à générer simultanément (par défaut : 1) | INT | Oui | 1 à 4096 |
| `intensité` | Force de contrôle pour le conditionnement vidéo (par défaut : 1.0, pas : 0.01) | FLOAT | Oui | 0.0 à 1000.0 |
| `contrôle_vidéo` | Vidéo d'entrée optionnelle pour le conditionnement de contrôle | IMAGE | Non | - |
| `masques_de_contrôle` | Masques optionnels pour contrôler les parties de la vidéo à modifier | MASK | Non | - |
| `image_de_référence` | Image de référence optionnelle pour un conditionnement supplémentaire | IMAGE | Non | - |

**Remarque :** Lorsque `control_video` est fourni, il sera redimensionné pour correspondre à la largeur et à la hauteur spécifiées. Si `control_masks` sont fournis, ils doivent correspondre aux dimensions de la vidéo de contrôle. L'`reference_image` est encodée via le VAE et ajoutée au début de la séquence latente lorsqu'elle est fournie.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `négatif` | Conditionnement positif avec les données de contrôle vidéo appliquées | CONDITIONING |
| `latent` | Conditionnement négatif avec les données de contrôle vidéo appliquées | CONDITIONING |
| `latent_coupé` | Tenseur latent vide prêt pour la génération vidéo | LATENT |
| `trim_latent` | Nombre de trames latentes à supprimer lors de l'utilisation d'une image de référence | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanVaceToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `66e50a360dc99ac49cac8f3f1c8649bf4298da2934c1bd9a0bc7cfbec620b291`
