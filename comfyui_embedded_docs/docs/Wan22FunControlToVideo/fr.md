> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22FunControlToVideo/fr.md)

Le nœud Wan22FunControlToVideo prépare les représentations de conditionnement et latentes pour la génération vidéo en utilisant l'architecture du modèle vidéo Wan. Il traite les entrées de conditionnement positif et négatif, ainsi que des images de référence et des vidéos de contrôle optionnelles, pour créer les représentations latentes nécessaires à la synthèse vidéo. Le nœud gère la mise à l'échelle spatiale et les dimensions temporelles afin de générer des données de conditionnement adaptées aux modèles vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `positif` | CONDITIONING | Oui | - | Entrée de conditionnement positif pour guider la génération vidéo |
| `négatif` | CONDITIONING | Oui | - | Entrée de conditionnement négatif pour guider la génération vidéo |
| `vae` | VAE | Oui | - | Modèle VAE utilisé pour encoder les images dans l'espace latent |
| `largeur` | INT | Oui | 16 à MAX_RESOLUTION | Largeur de la vidéo de sortie en pixels (défaut : 832, pas : 16) |
| `hauteur` | INT | Oui | 16 à MAX_RESOLUTION | Hauteur de la vidéo de sortie en pixels (défaut : 480, pas : 16) |
| `longueur` | INT | Oui | 1 à MAX_RESOLUTION | Nombre d'images dans la séquence vidéo (défaut : 81, pas : 4) |
| `taille_du_lot` | INT | Oui | 1 à 4096 | Nombre de séquences vidéo à générer (défaut : 1) |
| `image_de_référence` | IMAGE | Non | - | Image de référence optionnelle pour fournir un guidage visuel |
| `vidéo_de_contrôle` | IMAGE | Non | - | Vidéo de contrôle optionnelle pour guider le processus de génération |

**Remarque :** Le paramètre `length` est traité par blocs de 4 images, et le nœud gère automatiquement la mise à l'échelle temporelle pour l'espace latent. Lorsque `ref_image` est fourni, il influence le conditionnement via les latentes de référence. Lorsque `control_video` est fourni, il affecte directement la représentation latente concaténée utilisée dans le conditionnement. Le paramètre `start_image` n'est pas exposé en tant qu'entrée dans le schéma de ce nœud, mais est référencé dans la logique d'exécution.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `négatif` | CONDITIONING | Conditionnement positif modifié avec des données latentes spécifiques à la vidéo, incluant la latente concaténée, le masque et les latentes de référence optionnelles |
| `latent` | CONDITIONING | Conditionnement négatif modifié avec des données latentes spécifiques à la vidéo, incluant la latente concaténée, le masque et les latentes de référence optionnelles |
| `latent` | LATENT | Tenseur latent vide avec des dimensions appropriées pour la génération vidéo, basé sur la taille du lot, les canaux latents et la mise à l'échelle spatiale/temporelle |

---
**Source fingerprint (SHA-256):** `8b24058f06aa9f779371a402c41cffc95d13ad0131d23d1438067d77755c73e2`
