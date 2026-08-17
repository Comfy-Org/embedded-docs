# WanAnimateToVideo

Ce nœud expérimental prépare la génération vidéo Wan en combinant une image de référence avec des vidéos facultatives de pose, de visage et d’arrière-plan. Il construit les données de conditionnement et un tenseur vidéo latent vide pour la génération ultérieure, et il renvoie des informations de décalage de frames qui aident à étendre des vidéos existantes par segments.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Conditionnement positif pour guider la génération vers le contenu souhaité. | CONDITIONING | Oui | - |
| `negative` | Conditionnement négatif pour éloigner la génération du contenu indésirable. | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder et décoder les données d’image. | VAE | Oui | - |
| `width` | Largeur de la vidéo de sortie en pixels (défaut : 832, pas : 16). | INT | Oui | 16 à MAX_RESOLUTION |
| `height` | Hauteur de la vidéo de sortie en pixels (défaut : 480, pas : 16). | INT | Oui | 16 à MAX_RESOLUTION |
| `length` | Nombre de frames à générer (défaut : 77, pas : 4). | INT | Oui | 1 à MAX_RESOLUTION |
| `batch_size` | Nombre de vidéos à générer en un seul lot (défaut : 1). | INT | Oui | 1 à 4096 |
| `clip_vision_output` | Sortie facultative du modèle de vision CLIP utilisée comme conditionnement supplémentaire pour les conditionnements positif et négatif. | CLIP_VISION_OUTPUT | Non | - |
| `reference_image` | Image de référence utilisée comme point de départ pour la génération. Si aucune n’est fournie, une image noire (tous les zéros) est utilisée. | IMAGE | Non | - |
| `face_video` | Vidéo fournissant des indications d’expressions faciales. Une fois traitée, elle est redimensionnée à 512x512 et normalisée dans la plage -1.0 à 1.0. | IMAGE | Non | - |
| `pose_video` | Vidéo fournissant des indications de pose et de mouvement. Si elle est plus courte que `length`, elle est complétée par sa dernière frame. | IMAGE | Non | - |
| `continue_motion_max_frames` | Nombre maximal de frames à poursuivre à partir d’un mouvement précédent. Seules les dernières frames de `continue_motion`, à hauteur de cette valeur, sont utilisées (défaut : 5, pas : 4). | INT | Oui | 1 à MAX_RESOLUTION |
| `background_video` | Vidéo d’arrière-plan à composer avec le contenu généré. | IMAGE | Non | - |
| `character_mask` | Masque définissant les zones des personnages pour un traitement sélectif. Si le masque ne contient qu’une seule frame, il est répété sur toutes les frames. | MASK | Non | - |
| `continue_motion` | Séquence de mouvement précédente utilisée pour maintenir la cohérence temporelle lors de l’extension d’une vidéo. Seules les dernières `continue_motion_max_frames` frames sont utilisées. | IMAGE | Non | - |
| `video_frame_offset` | Nombre de frames de décalage à appliquer dans toutes les vidéos d’entrée. Utilisé pour générer des vidéos plus longues par segments. Connectez cette entrée à la sortie `video_frame_offset` du nœud précédent pour étendre une vidéo. (défaut : 0, pas : 1) | INT | Oui | 0 à MAX_RESOLUTION |

**Contraintes des paramètres :**

- Lorsque `pose_video` est fournie, une vidéo de pose plus courte est complétée par sa dernière frame pour correspondre à `length`. Le code source contient un indicateur `trim_to_pose_video`, actuellement désactivé, qui raccourcirait plutôt la sortie pour correspondre à la longueur de la vidéo de pose.
- `face_video` est redimensionnée à 512x512 et normalisée dans la plage -1.0 à 1.0.
- `continue_motion` est limitée aux dernières `continue_motion_max_frames` frames. Lorsque `continue_motion` est utilisée, `video_frame_offset` est réduit du nombre de frames retenues, mais jamais en dessous de 0.
- Les vidéos d’entrée (`face_video`, `pose_video`, `background_video`, `character_mask`) sont décalées de `video_frame_offset`. Si le décalage est supérieur ou égal à leur longueur, l’entrée est ignorée, sauf pour un `character_mask` à une seule frame, qui est toujours répété.
- Lorsque `clip_vision_output` est fournie, elle est appliquée aux conditionnements positif et négatif.
- Si `reference_image` n’est pas fournie, une image noire (tous les zéros) est utilisée comme référence.
- Si `continue_motion` n’est pas fournie, des frames grises avec une valeur de pixel de 0,5 sont utilisées pour la partie mouvement.
- `width` et `height` utilisent un pas de 16 ; les dimensions latentes correspondantes sont `width / 8` et `height / 8`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif modifié qui inclut toujours l’image latente concaténée et le masque concaténé. Si `clip_vision_output`, `pose_video` ou `face_video` sont fournies, leurs valeurs sont également ajoutées. | CONDITIONING |
| `negative` | Conditionnement négatif modifié qui inclut toujours l’image latente concaténée et le masque concaténé. Si `clip_vision_output`, `pose_video` ou `face_video` sont fournies, leurs valeurs sont également ajoutées ; les pixels de la vidéo de visage sont définis à -1.0. | CONDITIONING |
| `latent` | Tenseur latent vide initialisé à zéro, de forme `[batch_size, 16, latent_length + trim_latent, latent_height, latent_width]`. | LATENT |
| `trim_latent` | Nombre de frames latentes à retirer au début, correspondant aux frames latentes de l’image de référence. | INT |
| `trim_image` | Nombre de frames d’image à retirer au début, correspondant aux frames de mouvement de référence. | INT |
| `video_frame_offset` | Décalage de frames mis à jour pour la génération vidéo par segments, égal au décalage d’entrée ajusté plus la longueur générée. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimateToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `a95bae4c7ae4ddc8a95bc9dafa2ca920b1d2166802615189537dce16949bfc03`
