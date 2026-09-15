# Wan22FunControlToVideo

Le nœud Wan22FunControlToVideo prépare les données de conditionnement et un tenseur latent vide pour la génération vidéo avec le modèle vidéo Wan. Il encode les images de référence optionnelles et les vidéos de contrôle dans l'espace latent, les attache aux conditionnements positif et négatif, et crée un tenseur latent rempli de zéros avec les dimensions spatiales et temporelles correctes pour la vidéo demandée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | Entrée de conditionnement positive pour guider la génération vidéo | CONDITIONING | Oui | - |
| `négatif` | Entrée de conditionnement négative pour guider la génération vidéo | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder les images dans l'espace latent | VAE | Oui | - |
| `largeur` | Largeur de la vidéo de sortie en pixels (par défaut : 832, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | Hauteur de la vidéo de sortie en pixels (par défaut : 480, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `longueur` | Nombre d'images dans la séquence vidéo (par défaut : 81, pas : 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `taille_du_lot` | Nombre de séquences vidéo à générer (par défaut : 1) | INT | Oui | 1 à 4096 |
| `image_de_référence` | Image de référence optionnelle qui fournit une indication visuelle pour la génération | IMAGE | Non | - |
| `vidéo_de_contrôle` | Vidéo de contrôle optionnelle qui guide le processus de génération | IMAGE | Non | - |

**Remarque :** Le paramètre `length` est traité par pas de 4 images, et le nœud applique automatiquement une mise à l'échelle temporelle lors de la construction de l'espace latent. Lorsque `ref_image` est fourni, seule sa première image est encodée (redimensionnée à `width` x `height`) et attachée au conditionnement comme latents de référence. Lorsque `control_video` est fourni, il est rogné à `length` images, redimensionné, encodé et placé dans le latent concaténé utilisé par le conditionnement. Le latent concaténé est dupliqué le long de la dimension des canaux et sa disposition des canaux dépend du nombre de canaux latents du VAE (48 canaux utilise le format Wan 2.2, sinon le format Wan 2.1). Le paramètre `start_image` est référencé dans la logique d'exécution mais n'est pas exposé dans le schéma d'entrée du nœud, il ne peut donc pas être défini depuis l'interface du nœud.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif avec des données latentes spécifiques à la vidéo ajoutées, incluant le latent concaténé, le masque et les latents de référence optionnels | CONDITIONING |
| `negative` | Conditionnement négatif avec des données latentes spécifiques à la vidéo ajoutées, incluant le latent concaténé, le masque et les latents de référence optionnels | CONDITIONING |
| `latent` | Tenseur latent vide préparé pour la génération vidéo, dimensionné selon la taille du lot, les canaux latents, la longueur, la hauteur et la largeur | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22FunControlToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `731b848f15c13ddc662f19230acb55d195f934bad7d9ae516a288e0ed8f8d899`
