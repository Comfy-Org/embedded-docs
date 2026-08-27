# Wan22FunControlToVideo

Le nœud Wan22FunControlToVideo prépare les données de conditionnement et un tenseur latent vide pour la génération de vidéos avec le modèle vidéo Wan. Il encode les images de référence et les vidéos de contrôle optionnelles dans l'espace latent, les attache au conditionnement positif et négatif, et crée un tenseur latent rempli de zéros avec les dimensions spatiales et temporelles correctes pour la vidéo demandée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | Conditionnement positif pour guider la génération vidéo | CONDITIONING | Oui | - |
| `négatif` | Conditionnement négatif pour guider la génération vidéo | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder les images dans l'espace latent | VAE | Oui | - |
| `largeur` | Largeur de la vidéo de sortie en pixels (défaut : 832, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | Hauteur de la vidéo de sortie en pixels (défaut : 480, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `longueur` | Nombre d'images dans la séquence vidéo (défaut : 81, pas : 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `taille_du_lot` | Nombre de séquences vidéo à générer (défaut : 1) | INT | Oui | 1 à 4096 |
| `image_de_référence` | Image de référence facultative fournissant un guidage visuel pour la génération | IMAGE | Non | - |
| `vidéo_de_contrôle` | Vidéo de contrôle facultative qui guide le processus de génération | IMAGE | Non | - |

**Remarque :** Le paramètre `length` est traité par pas de 4 images, et le nœud applique automatiquement une mise à l'échelle temporelle lors de la construction de l'espace latent. Lorsque `ref_image` est fourni, seule sa première image est encodée et attachée au conditionnement comme latents de référence. Lorsque `control_video` est fournie, elle est tronquée à `length` images, encodée, puis placée dans le latent concaténé utilisé par le conditionnement. Le paramètre `start_image` est référencé dans la logique d'exécution mais n'est pas exposé dans le schéma d'entrées du nœud.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positif` | Conditionnement positif avec les données latentes spécifiques à la vidéo ajoutées, y compris le latent concaténé, le masque et les latents de référence facultatifs | CONDITIONING |
| `négatif` | Conditionnement négatif avec les données latentes spécifiques à la vidéo ajoutées, y compris le latent concaténé, le masque et les latents de référence facultatifs | CONDITIONING |
| `latent` | Tenseur latent vide préparé pour la génération vidéo, dimensionné selon la taille du lot, les canaux latents, la longueur, la hauteur et la largeur | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22FunControlToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `731b848f15c13ddc662f19230acb55d195f934bad7d9ae516a288e0ed8f8d899`
