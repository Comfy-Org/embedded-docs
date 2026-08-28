# WanImageVersVidéo

Le nœud WanImageToVideo prépare les représentations de conditionnement et latentes pour les tâches de génération vidéo. Il crée un espace latent vide pour la génération vidéo et peut éventuellement incorporer des images de départ et des sorties de vision CLIP pour guider le processus de génération. Le nœud modifie à la fois les entrées de conditionnement positive et négative en fonction de l'image et des données de vision fournies.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Entrée de conditionnement positive pour guider la génération | CONDITIONING | Oui | - |
| `négatif` | Entrée de conditionnement négative pour guider la génération | CONDITIONING | Oui | - |
| `vae` | Modèle VAE pour encoder les images vers l'espace latent | VAE | Oui | - |
| `largeur` | Largeur de la vidéo de sortie (défaut : 832, pas : 16) | INT | Oui | 16 to MAX_RESOLUTION |
| `hauteur` | Hauteur de la vidéo de sortie (défaut : 480, pas : 16) | INT | Oui | 16 to MAX_RESOLUTION |
| `longueur` | Nombre d'images dans la vidéo (défaut : 81, pas : 4) | INT | Oui | 1 to MAX_RESOLUTION |
| `taille_du_lot` | Nombre de vidéos à générer dans un lot (défaut : 1) | INT | Oui | 1 à 4096 |
| `sortie_vision_clip` | Sortie de vision CLIP facultative pour un conditionnement supplémentaire | CLIP_VISION_OUTPUT | Non | - |
| `image_de_départ` | Image de départ facultative pour initialiser la génération vidéo. Lorsqu'elle est fournie, l'image est redimensionnée pour correspondre à la largeur et à la hauteur spécifiées, et les premières images de la vidéo sont initialisées à partir de cette image. Les images restantes sont remplies avec des valeurs de gris neutre (0,5). Toutes les images au-delà de `length` sont ignorées. | IMAGE | Non | - |

**Remarque :** Lorsque `start_image` est fourni, le nœud encode la séquence d'images à l'aide du VAE et applique un masque aux entrées de conditionnement. Le masque couvre toutes les images sauf celles initialisées par l'image de départ, ce qui permet à la génération de s'appuyer sur l'image fournie. Seuls les trois premiers canaux de couleur (RVB) de l'image sont utilisés lors de l'encodage. Le paramètre `clip_vision_output`, lorsqu'il est fourni, ajoute un conditionnement basé sur la vision aux entrées positive et négative.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif modifié avec incorporation des données d'image et de vision | CONDITIONING |
| `négatif` | Conditionnement négatif modifié avec incorporation des données d'image et de vision | CONDITIONING |
| `latent` | Tenseur d'espace latent vide prêt pour la génération vidéo, avec la forme [batch_size, 16, ((length-1)//4)+1, height//8, width//8] | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `46779f9f2f3da16826b7b547761a96597a3b6b43ce51a9c13367987642f3d5b7`
