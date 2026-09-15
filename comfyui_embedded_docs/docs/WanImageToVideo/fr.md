# WanImageVersVidéo

Le nœud WanImageToVideo prépare les représentations de conditionnement et latentes pour la génération vidéo. Il crée un espace latent vide pour la vidéo et peut éventuellement intégrer une image de départ et une sortie de vision CLIP pour guider la génération. Les entrées de conditionnement positive et négative sont toutes deux mises à jour avec l’image et les données de vision fournies.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Entrée de conditionnement positive utilisée pour guider la génération | CONDITIONING | Oui | - |
| `négatif` | Entrée de conditionnement négative utilisée pour guider la génération | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder les images dans l’espace latent | VAE | Oui | - |
| `largeur` | Largeur de la vidéo générée (par défaut : 832, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | Hauteur de la vidéo générée (par défaut : 480, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `longueur` | Nombre d’images dans la vidéo (par défaut : 81, pas : 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `taille_du_lot` | Nombre de vidéos à générer dans un lot (par défaut : 1) | INT | Oui | 1 à 4096 |
| `sortie_vision_clip` | Sortie de vision CLIP facultative ajoutée comme conditionnement supplémentaire aux entrées positive et négative | CLIP_VISION_OUTPUT | Non | - |
| `image_de_départ` | Image de départ facultative utilisée pour initialiser la vidéo. Lorsqu’elle est fournie, elle est redimensionnée aux `width` et `height` spécifiés et placée au début de la séquence d’images ; toutes les images au-delà de `length` sont ignorées. Les images restantes sont remplies avec des valeurs de gris neutre (0,5). | IMAGE | Non | - |

**Remarque :** Lorsque `start_image` est fournie, la séquence d’images est encodée avec le VAE et un masque est appliqué au conditionnement. Le masque est défini à 0 pour les images couvertes par l’image de départ et à 1 pour les images restantes, afin que la génération se poursuive à partir de l’image fournie. Seuls les trois premiers canaux de couleur (RVB) de l’image sont utilisés lors de l’encodage. Les conditionnements positif et négatif reçoivent tous deux la même image latente concaténée, le masque et (si fournie) la sortie de vision CLIP.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif, mis à jour avec l’image et les données de vision | CONDITIONING |
| `negative` | Conditionnement négatif, mis à jour avec l’image et les données de vision | CONDITIONING |
| `latent` | Tenseur latent vide prêt pour la génération vidéo, de forme [batch_size, 16, ((length-1)//4)+1, height//8, width//8] | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `46779f9f2f3da16826b7b547761a96597a3b6b43ce51a9c13367987642f3d5b7`
