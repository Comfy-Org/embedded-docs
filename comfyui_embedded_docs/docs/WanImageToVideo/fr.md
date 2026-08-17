# WanImageVersVidéo

Le nœud WanImageToVideo prépare les représentations de conditionnement et latentes pour les tâches de génération vidéo. Il crée un espace latent vide pour la génération vidéo et peut éventuellement incorporer des images de départ et des sorties de vision CLIP pour guider le processus de génération vidéo. Le nœud modifie à la fois les entrées de conditionnement positive et négative en fonction de l'image et des données de vision fournies.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Entrée de conditionnement positive pour guider la génération | CONDITIONING | Oui | - |
| `negative` | Entrée de conditionnement négative pour guider la génération | CONDITIONING | Oui | - |
| `vae` | Modèle VAE pour encoder les images dans l'espace latent | VAE | Oui | - |
| `width` | Largeur de la vidéo de sortie (par défaut : 832, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `height` | Hauteur de la vidéo de sortie (par défaut : 480, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `length` | Nombre d'images dans la vidéo (par défaut : 81, pas : 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `batch_size` | Nombre de vidéos à générer par lot (par défaut : 1) | INT | Oui | 1 à 4096 |
| `clip_vision_output` | Sortie de vision CLIP optionnelle pour un conditionnement supplémentaire | CLIP_VISION_OUTPUT | Non | - |
| `start_image` | Image de départ optionnelle pour initialiser la génération vidéo. Lorsqu'elle est fournie, l'image est redimensionnée pour correspondre à la largeur et à la hauteur spécifiées, et les premières images de la vidéo sont initialisées à partir de cette image. Les images restantes sont remplies avec du gris neutre (0,5). Seules les premières `length` images de l'image sont utilisées. | IMAGE | Non | - |

**Note :** Lorsqu'une `start_image` est fournie, le nœud encode la séquence d'images à l'aide du VAE et applique un masque aux entrées de conditionnement. Le masque couvre toutes les images sauf celles initialisées par l'image de départ, permettant à la génération de s'appuyer sur l'image fournie. Le paramètre `clip_vision_output`, lorsqu'il est fourni, ajoute un conditionnement basé sur la vision à la fois aux entrées positive et négative.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif modifié intégrant les données d'image et de vision | CONDITIONING |
| `negative` | Conditionnement négatif modifié intégrant les données d'image et de vision | CONDITIONING |
| `latent` | Tenseur d'espace latent vide prêt pour la génération vidéo, avec une forme [batch_size, 16, ((length-1)//4)+1, height//8, width//8] | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `46779f9f2f3da16826b7b547761a96597a3b6b43ce51a9c13367987642f3d5b7`
