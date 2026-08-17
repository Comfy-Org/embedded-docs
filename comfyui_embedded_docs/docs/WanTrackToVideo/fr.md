# WanTrackToVideo

Le nœud WanTrackToVideo utilise les données de suivi de mouvement (trajectoires de points) pour guider la génération vidéo. Il traite les pistes, les combine éventuellement avec une image de départ, et produit des sorties conditionnées positives et négatives ainsi qu'un tenseur latent pour le modèle vidéo Wan. Lorsqu'aucune piste valide n'est fournie, il revient à la conversion standard d'image en vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Conditionnement positif pour la génération vidéo | CONDITIONING | Oui | - |
| `negative` | Conditionnement négatif pour la génération vidéo | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder les images vidéo | VAE | Oui | - |
| `tracks` | Données de suivi au format JSON sous forme de chaîne multiligne (défaut : "[]") | STRING | Oui | - |
| `width` | Largeur de la vidéo de sortie en pixels (défaut : 832, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `height` | Hauteur de la vidéo de sortie en pixels (défaut : 480, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `length` | Nombre de frames dans la vidéo de sortie (défaut : 81, pas : 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `batch_size` | Nombre de vidéos à générer simultanément (défaut : 1) | INT | Oui | 1 à 4096 |
| `temperature` | Paramètre de température avancé pour le patch de mouvement (défaut : 220.0, pas : 0.1) | FLOAT | Oui | 1.0 à 1000.0 |
| `topk` | Valeur top-k avancée pour le patch de mouvement (défaut : 2) | INT | Oui | 1 à 10 |
| `start_image` | Image de départ utilisée pour la première frame de la génération vidéo | IMAGE | Oui | - |
| `clip_vision_output` | Sortie de vision CLIP pour un conditionnement supplémentaire | CLIP_VISION_OUTPUT | Non | - |

**Remarques :**
- L'entrée `tracks` attend une chaîne JSON ou une liste de chaînes JSON contenant des données de suivi de points. Si `tracks` est vide ou ne peut pas être analysée, le nœud revient au comportement de WanImageToVideo.
- Lorsque `start_image` est présente, elle est redimensionnée pour correspondre à `width` et `height` et utilisée comme première frame de la séquence vidéo.
- Lorsque `clip_vision_output` est fourni, il est ajouté au conditionnement positif et négatif.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif avec les informations de piste de mouvement et d'image facultative appliquées | CONDITIONING |
| `negative` | Conditionnement négatif avec les informations de piste de mouvement et d'image facultative appliquées | CONDITIONING |
| `latent` | Tenseur latent rempli de zéros dimensionné pour les dimensions, la longueur et la taille de lot de la vidéo demandée | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTrackToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `e67fe326dd7e5ae63ddc35946d8144138d04d9523ec1ad2e08ea6bc1dc9325da`
