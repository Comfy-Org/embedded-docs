# WanSCAILToVideo

Le nœud WanSCAILToVideo prépare le conditionnement et un espace latent vide pour la génération vidéo avec les modèles vidéo SCAIL et SCAIL-2. Il traite des entrées facultatives telles que les images de référence, les vidéos de pose, les sorties CLIP vision, les masques d'identité colorés et les segments d’images précédentes, en les intégrant dans les conditionnements positif et négatif. Le nœud renvoie le conditionnement modifié et un tenseur latent vide aux dimensions vidéo spécifiées, prêt pour l’échantillonnage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `positif` | Le conditionnement positif d’entrée. | CONDITIONING | Oui | - |
| `négatif` | Le conditionnement négatif d’entrée. | CONDITIONING | Oui | - |
| `vae` | Le modèle VAE utilisé pour encoder les images et les images vidéo. | VAE | Oui | - |
| `largeur` | La largeur de la vidéo de sortie en pixels (par défaut : 512). Les valeurs augmentent par pas de 32. | INT | Oui | 32 to MAX_RESOLUTION |
| `hauteur` | La hauteur de la vidéo de sortie en pixels (par défaut : 896). Les valeurs augmentent par pas de 32. | INT | Oui | 32 to MAX_RESOLUTION |
| `longueur` | Le nombre d’images de la vidéo (par défaut : 81). Les valeurs augmentent par pas de 4. | INT | Oui | 1 to MAX_RESOLUTION |
| `taille_du_lot` | Le nombre de vidéos à générer dans un lot (par défaut : 1). | INT | Oui | 1 à 4096 |
| `vidéo_de_pose` | Vidéo utilisée pour le conditionnement de pose. Elle sera réduite à la moitié de la résolution de la vidéo principale. | IMAGE | Non | - |
| `pose_video_mask` | SCAIL-2 uniquement. Vidéo de masques SAM3 colorés par identité, à la même résolution que `pose_video`. | IMAGE | Non | - |
| `replacement_mode` | SCAIL-2 uniquement. False = mode Animation (`pose_video_mask` doit avoir un fond noir). True = mode Remplacement (`pose_video_mask` doit avoir un fond blanc). (par défaut : False) | BOOLEAN | Non | - |
| `force_de_pose` | Force du latent de pose. (par défaut : 1.0) | FLOAT | Oui | 0.0 à 10.0 |
| `début_de_pose` | Étape de début du conditionnement de pose. (par défaut : 0.0) | FLOAT | Oui | 0.0 à 1.0 |
| `fin_de_pose` | Étape de fin du conditionnement de pose. (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `image_de_référence` | Image de référence. La première image est la référence principale (effectuez la composition de toutes les identités sur cette image). SCAIL-2 : les images supplémentaires du lot sont utilisées comme vues additionnelles (vue arrière, gros plan, arrière-plan occulté), chacune nécessitant un `reference_image_mask` correspondant dans la couleur de cette identité. | IMAGE | Non | - |
| `reference_image_mask` | SCAIL-2 uniquement. Masque de référence coloré, correspondant par lot à `reference_image` (le premier = masque de référence principal, les autres = masques d’identité pour les `reference_image` supplémentaires). | IMAGE | Non | - |
| `clip_vision_output` | Caractéristiques CLIP vision pour le conditionnement. Le modèle est entraîné avec un redimensionnement par étirement au ratio d’aspect. | CLIP_VISION_OUTPUT | Non | - |
| `video_frame_offset` | Décalage cumulé de l’image de sortie à partir duquel ce segment commence. Reliez cette entrée à la sortie `video_frame_offset` du segment précédent. (par défaut : 0) | INT | Oui | 0 to MAX_RESOLUTION |
| `previous_frame_count` | Images finales de `previous_frames` à ancrer. SCAIL-2 est entraîné avec une valeur de 5 (segments de 81 images, pas de 76 images). (par défaut : 5) | INT | Oui | 1 to MAX_RESOLUTION |
| `previous_frames` | SCAIL-2 uniquement. Sortie décodée complète du segment précédent. Seules les `previous_frame_count` dernières images sont utilisées comme ancrage d’extension. | IMAGE | Non | - |

**Remarque :** Les entrées `pose_video` et `pose_video_mask` sont tronquées ensemble à la longueur de la plus courte des deux, et ne sont traitées que pour les `length` premières images. Si l’une des entrées est plus courte ou égale à `video_frame_offset`, elle est entièrement ignorée. `pose_video` est réduite à la moitié de la résolution de la vidéo principale avant l’encodage, et le latent de pose encodé est multiplié par `pose_strength` puis appliqué au conditionnement uniquement entre les pas de temps `pose_start` et `pose_end`. Si `pose_video_mask` est fournie, la vidéo de masques colorés est réduite à la moitié de la résolution et convertie en un masque de pilotage à 28 canaux, qui est ajouté aux conditionnements positif et négatif.

**Remarque :** Lorsque `reference_image` est fournie, chaque image du lot est encodée individuellement en un latent puis intégrée aux conditionnements positif et négatif. La première image est la référence principale ; les images supplémentaires sont utilisées comme vues additionnelles, chacune nécessitant un `reference_image_mask` correspondant. `reference_image_mask` n’est utilisé que lorsque `reference_image` est également fournie ; lorsque les deux sont fournis, un masque de référence à 28 canaux qui lie les images de référence aux identités est également construit à partir des masques et ajouté au conditionnement. En mode Remplacement (`replacement_mode=True`), l’image de référence est composée sur un fond noir en utilisant le masque de référence comme cache alpha. Lorsque `clip_vision_output` est fourni, il est appliqué aux conditionnements positif et négatif.

**Remarque :** Lorsque `previous_frames` est fourni, seules les `previous_frame_count` dernières images sont utilisées comme ancrage d’extension, et `video_frame_offset` est ajusté en conséquence (réduit du nombre d’images ancrées, limité à 0). Les images ancrées sont encodées et écrites au début du latent de sortie, et un masque de bruit est inclus afin que ces images restent inchangées pendant la génération.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positif` | Le conditionnement positif modifié, contenant potentiellement des latents d’image de référence intégrés, la sortie CLIP vision, des latents de vidéo de pose, des masques de pilotage, des masques de référence ou des latents d’images précédentes. | CONDITIONING |
| `négatif` | Le conditionnement négatif modifié, contenant potentiellement des latents d’image de référence intégrés, la sortie CLIP vision, des latents de vidéo de pose, des masques de pilotage, des masques de référence ou des latents d’images précédentes. | CONDITIONING |
| `latent` | Un tenseur latent vide de forme `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]`. Lorsque `previous_frames` est fourni, le latent est partiellement rempli avec les images précédentes encodées et un masque de bruit est inclus. | LATENT |
| `video_frame_offset` | Décalage ajusté + longueur. Reliez-le au segment suivant pour la génération vidéo séquentielle. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSCAILToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `4a1a2201dfa94bd2f1330db02ec18a5e0a6aae9e9ac5ae97d456b7af1aa84b7b`
