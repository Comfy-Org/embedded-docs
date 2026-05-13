> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/fr.md)

Voici la traduction en français de la documentation du nœud WanImageToVideo :

Le nœud WanImageToVideo prépare les représentations de conditionnement et latentes pour les tâches de génération vidéo. Il crée un espace latent vide pour la génération vidéo et peut éventuellement intégrer des images de départ et des sorties CLIP vision pour guider le processus de génération vidéo. Le nœud modifie les entrées de conditionnement positives et négatives en fonction de l'image et des données visuelles fournies.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `positive` | CONDITIONING | Oui | - | Entrée de conditionnement positive pour guider la génération |
| `negative` | CONDITIONING | Oui | - | Entrée de conditionnement négative pour guider la génération |
| `vae` | VAE | Oui | - | Modèle VAE pour encoder les images dans l'espace latent |
| `width` | INT | Oui | 16 à MAX_RESOLUTION | Largeur de la vidéo de sortie (par défaut : 832, pas : 16) |
| `height` | INT | Oui | 16 à MAX_RESOLUTION | Hauteur de la vidéo de sortie (par défaut : 480, pas : 16) |
| `length` | INT | Oui | 1 à MAX_RESOLUTION | Nombre d'images dans la vidéo (par défaut : 81, pas : 4) |
| `batch_size` | INT | Oui | 1 à 4096 | Nombre de vidéos à générer dans un lot (par défaut : 1) |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Non | - | Sortie CLIP vision facultative pour un conditionnement supplémentaire |
| `start_image` | IMAGE | Non | - | Image de départ facultative pour initialiser la génération vidéo |

**Remarque :** Lorsque `start_image` est fourni, le nœud encode la séquence d'images et applique un masquage aux entrées de conditionnement. Le paramètre `clip_vision_output`, lorsqu'il est fourni, ajoute un conditionnement basé sur la vision aux entrées positives et négatives.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `positive` | CONDITIONING | Conditionnement positif modifié avec les données d'image et visuelles intégrées |
| `negative` | CONDITIONING | Conditionnement négatif modifié avec les données d'image et visuelles intégrées |
| `latent` | LATENT | Tenseur d'espace latent vide prêt pour la génération vidéo |

---
**Source fingerprint (SHA-256):** `e9f4350c43e48351523c04d82675c24f868df7b2109530c32b8e752a3ab61e8b`
