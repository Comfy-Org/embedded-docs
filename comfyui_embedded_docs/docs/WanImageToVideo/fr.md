# WanImageVersVidéo

Voici la traduction en français de la documentation du nœud WanImageToVideo :

Le nœud WanImageToVideo prépare les représentations de conditionnement et latentes pour les tâches de génération vidéo. Il crée un espace latent vide pour la génération vidéo et peut éventuellement intégrer des images de départ et des sorties CLIP vision pour guider le processus de génération vidéo. Le nœud modifie les entrées de conditionnement positives et négatives en fonction de l'image et des données visuelles fournies.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Entrée de conditionnement positive pour guider la génération | CONDITIONING | Oui | - |
| `négatif` | Entrée de conditionnement négative pour guider la génération | CONDITIONING | Oui | - |
| `vae` | Modèle VAE pour encoder les images dans l'espace latent | VAE | Oui | - |
| `largeur` | Largeur de la vidéo de sortie (par défaut : 832, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | Hauteur de la vidéo de sortie (par défaut : 480, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `longueur` | Nombre d'images dans la vidéo (par défaut : 81, pas : 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `taille_du_lot` | Nombre de vidéos à générer dans un lot (par défaut : 1) | INT | Oui | 1 à 4096 |
| `sortie_vision_clip` | Sortie CLIP vision facultative pour un conditionnement supplémentaire | CLIP_VISION_OUTPUT | Non | - |
| `image_de_départ` | Image de départ facultative pour initialiser la génération vidéo | IMAGE | Non | - |

**Remarque :** Lorsque `start_image` est fourni, le nœud encode la séquence d'images et applique un masquage aux entrées de conditionnement. Le paramètre `clip_vision_output`, lorsqu'il est fourni, ajoute un conditionnement basé sur la vision aux entrées positives et négatives.


| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif modifié avec les données d'image et visuelles intégrées | CONDITIONING |
| `negative` | Conditionnement négatif modifié avec les données d'image et visuelles intégrées | CONDITIONING |
| `latent` | Tenseur d'espace latent vide prêt pour la génération vidéo | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `e9f4350c43e48351523c04d82675c24f868df7b2109530c32b8e752a3ab61e8b`
