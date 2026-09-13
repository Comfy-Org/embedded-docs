# WanSCAILToVideo

Le nœud WanSCAILToVideo prépare le conditionnement et un espace latent vide pour la génération vidéo avec les modèles vidéo SCAIL et SCAIL-2. Il traite des entrées facultatives telles que des images de référence, des vidéos de pose, des sorties de vision CLIP, des masques d'identité colorés et des segments de trames précédentes, en les intégrant dans le conditionnement positif et négatif. Le nœud produit le conditionnement modifié et un tenseur latent vide aux dimensions vidéo spécifiées, prêt pour l'échantillonnage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `positive` | L'entrée de conditionnement positive. | CONDITIONING | Oui | - |
| `negative` | L'entrée de conditionnement négative. | CONDITIONING | Oui | - |
| `vae` | Le modèle VAE utilisé pour encoder les images et les trames vidéo. | VAE | Oui | - |
| `width` | La largeur de la vidéo de sortie en pixels (par défaut : 512). Les valeurs augmentent par pas de 32. | INT | Oui | 32 à MAX_RESOLUTION |
| `height` | La hauteur de la vidéo de sortie en pixels (par défaut : 896). Les valeurs augmentent par pas de 32. | INT | Oui | 32 à MAX_RESOLUTION |
| `length` | Le nombre de trames dans la vidéo (par défaut : 81). Les valeurs augmentent par pas de 4. | INT | Oui | 1 à MAX_RESOLUTION |
| `batch_size` | Le nombre de vidéos à générer dans un lot (par défaut : 1). | INT | Oui | 1 à 4096 |
| `pose_video` | Vidéo utilisée pour le conditionnement de pose. Sera réduite à la moitié de la résolution de la vidéo principale. | IMAGE | Non | - |
| `pose_video_mask` | SCAIL-2 uniquement. Vidéo de masque SAM3 coloré par identité à la même résolution que `pose_video`. | IMAGE | Non | - |
| `replacement_mode` | SCAIL-2 uniquement. False = Mode Animation (`pose_video_mask` doit avoir un fond noir). True = Mode Remplacement (`pose_video_mask` doit avoir un fond blanc). (par défaut : False) | BOOLEAN | Non | - |
| `pose_strength` | Force du latent de pose. (par défaut : 1.0) | FLOAT | Oui | 0.0 à 10.0 |
| `pose_start` | Étape de début du conditionnement de pose. (par défaut : 0.0) | FLOAT | Oui | 0.0 à 1.0 |
| `pose_end` | Étape de fin du conditionnement de pose. (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `reference_image` | Image de référence. La première image est la référence principale (y composer toutes les identités). SCAIL-2 : les images supplémentaires du lot sont utilisées comme vues additionnelles (vue arrière, gros plan, arrière-plan occulté), chacune nécessitant un `reference_image_mask` correspondant dans la couleur de cette identité. | IMAGE | Non | - |
| `reference_image_mask` | SCAIL-2 uniquement. Masque de référence coloré, lot correspondant à `reference_image` (le premier = masque de référence principal, les autres = masques d'identité pour les images `reference_image` supplémentaires). | IMAGE | Non | - |
| `clip_vision_output` | Caractéristiques de vision CLIP pour le conditionnement. Le modèle est entraîné avec un redimensionnement étiré selon le rapport d'aspect. | CLIP_VISION_OUTPUT | Non | - |
| `video_frame_offset` | Trame de sortie cumulée à laquelle ce bloc commence. À connecter depuis la sortie `video_frame_offset` du bloc précédent. (par défaut : 0) | INT | Oui | 0 à MAX_RESOLUTION |
| `previous_frame_count` | Trames de fin de `previous_frames` à ancrer. SCAIL-2 entraîné avec 5 (blocs de 81 trames, pas de 76 trames). (par défaut : 5). Les valeurs augmentent par pas de 4. | INT | Oui | 1 à MAX_RESOLUTION |
| `previous_frames` | SCAIL-2 uniquement. Sortie décodée complète du bloc précédent. Seules les dernières `previous_frame_count` trames sont utilisées comme ancrage d'extension. | IMAGE | Non | - |

**Remarque :** Les entrées `pose_video` et `pose_video_mask` sont tronquées ensemble à la plus courte des deux, et ne sont traitées que pour les premières `length` trames. Si l'une des entrées est plus courte ou égale à `video_frame_offset`, elle est entièrement ignorée. Le `pose_video` est réduit à la moitié de la résolution de la vidéo principale avant l'encodage, et le latent de pose encodé est multiplié par `pose_strength` puis appliqué au conditionnement uniquement entre les étapes temporelles `pose_start` et `pose_end`. Si `pose_video_mask` est fourni, la vidéo de masque coloré est réduite à demi-résolution et convertie en masque de guidage à 28 canaux, qui est ajouté à la fois au conditionnement positif et négatif.

**Remarque :** Lorsque `reference_image` est fourni, chaque image du lot est encodée individuellement dans un latent et intégrée à la fois au conditionnement positif et négatif. La première image est la référence principale ; les images supplémentaires sont utilisées comme vues supplémentaires, chacune nécessitant un `reference_image_mask` correspondant. `reference_image_mask` n'est utilisé que lorsque `reference_image` est également fourni ; lorsque les deux sont donnés, un masque de référence à 28 canaux qui lie les trames de référence aux identités est également construit à partir des masques et ajouté au conditionnement. En Mode Remplacement (`replacement_mode=True`), l'image de référence est composée sur un fond noir en utilisant le masque d'image de référence comme masque alpha. Lorsque `clip_vision_output` est fourni, il est appliqué à la fois au conditionnement positif et négatif.

**Remarque :** Lorsque `previous_frames` est fourni, seules les dernières `previous_frame_count` trames sont utilisées comme ancrage d'extension, et `video_frame_offset` est ajusté en conséquence (réduit du nombre de trames ancrées, avec un minimum de 0). Les trames ancrées sont encodées et écrites au début du latent de sortie, et un masque de bruit est inclus afin que ces trames restent inchangées pendant la génération.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positive` | Le conditionnement positif modifié, pouvant contenir des latents d'images de référence intégrés, la sortie de vision CLIP, des latents de vidéo de pose, des masques de guidage, des masques de référence ou des latents de trames précédentes. | CONDITIONING |
| `negative` | Le conditionnement négatif modifié, pouvant contenir des latents d'images de référence intégrés, la sortie de vision CLIP, des latents de vidéo de pose, des masques de guidage, des masques de référence ou des latents de trames précédentes. | CONDITIONING |
| `latent` | Un tenseur latent vide de forme `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]`. Lorsque `previous_frames` est fourni, le latent est partiellement rempli avec les trames précédentes encodées et un masque de bruit est inclus. | LATENT |
| `video_frame_offset` | Offset ajusté + longueur. À connecter dans le bloc suivant pour la génération vidéo séquentielle. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSCAILToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `4a1a2201dfa94bd2f1330db02ec18a5e0a6aae9e9ac5ae97d456b7af1aa84b7b`
