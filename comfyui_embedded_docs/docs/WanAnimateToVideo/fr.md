# WanAnimateToVideo

WanAnimateToVideo prépare les données de conditionnement et un latent initial pour générer des vidéos animées avec Wan, en utilisant des entrées telles qu'une image de référence, une pose, un visage, un arrière-plan et un mouvement facultatif provenant d'un segment précédent. Il prend également en charge la génération de vidéos plus longues par segments en lisant et en mettant à jour une valeur `video_frame_offset`. Ce nœud est marqué comme expérimental.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | Conditionnement positif pour guider la génération vers le contenu souhaité. | CONDITIONING | Oui | - |
| `négatif` | Conditionnement négatif pour éloigner la génération du contenu indésirable. | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder les entrées d'image et de vidéo dans l'espace latent. | VAE | Oui | - |
| `largeur` | Largeur de la vidéo générée en pixels (défaut : 832, pas : 16). | INT | Oui | 16 to MAX_RESOLUTION |
| `hauteur` | Hauteur de la vidéo générée en pixels (défaut : 480, pas : 16). | INT | Oui | 16 to MAX_RESOLUTION |
| `longueur` | Nombre d'images à générer (défaut : 77, pas : 4). | INT | Oui | 1 to MAX_RESOLUTION |
| `taille_du_lot` | Nombre de vidéos à générer en un seul lot (défaut : 1). | INT | Oui | 1 à 4096 |
| `sortie_vision_clip` | Sortie CLIP vision facultative ajoutée au conditionnement positif et négatif. | CLIP_VISION_OUTPUT | Non | - |
| `image_de_référence` | Image de référence utilisée comme point de départ d'apparence pour la vidéo générée. Si elle n'est pas fournie, une image noire est utilisée. | IMAGE | Non | - |
| `vidéo_visage` | Entrée vidéo fournissant des indications sur l'expression faciale. Elle est redimensionnée en 512x512 et mise à l'échelle dans la plage de -1.0 à 1.0 en interne. | IMAGE | Non | - |
| `vidéo_pose` | Entrée vidéo fournissant des indications de pose et de mouvement. | IMAGE | Non | - |
| `images_max_poursuite_mouvement` | Nombre maximal d'images reportées d'une séquence de mouvement précédente (défaut : 5, pas : 4). | INT | Oui | 1 to MAX_RESOLUTION |
| `vidéo_arrière_plan` | Vidéo d'arrière-plan utilisée pour remplir les parties hors personnage des images. | IMAGE | Non | - |
| `masque_personnage` | Masque définissant les régions du personnage, utilisé pour séparer le personnage de l'arrière-plan. | MASK | Non | - |
| `poursuite_mouvement` | Images de mouvement précédentes à partir desquelles continuer, afin de préserver la cohérence temporelle avec les segments générés précédemment. | IMAGE | Non | - |
| `décalage_image_vidéo` | Nombre d'images à rechercher dans toutes les vidéos d'entrée. Utilisé pour générer des vidéos plus longues par segments. Connectez-le à la sortie `video_frame_offset` du nœud précédent pour prolonger une vidéo. (défaut : 0, pas : 1) | INT | Oui | 0 to MAX_RESOLUTION |

**Contraintes des paramètres :**

- Lorsque `continue_motion` est fourni, seules ses dernières images `continue_motion_max_frames` sont utilisées.
- Les vidéos d'entrée (`face_video`, `pose_video`, `background_video`, `character_mask`) sont décalées de `video_frame_offset` avant utilisation. Si le décalage est supérieur ou égal au nombre d'images de l'entrée, cette entrée est ignorée, sauf pour un `character_mask` à image unique.
- Si `character_mask` ne possède qu'une seule image, cette image est répétée pour chaque image de la sortie.
- Lorsque `pose_video` est plus courte que `length`, sa dernière image est répétée pour remplir les images restantes ; la longueur de sortie n'est pas modifiée.
- Si `clip_vision_output` est fourni, il est ajouté au conditionnement positif et négatif.
- Si `reference_image` n'est pas fournie, une image noire (toutes les valeurs à zéro) est utilisée comme référence par défaut.
- Si `continue_motion` n'est pas fourni, les images de mouvement initiales sont remplies d'images grises constantes (intensité 0,5).
- Lorsque `continue_motion` est utilisé, `video_frame_offset` est réduit du nombre d'images reportées avant le calcul du décalage du segment suivant, afin que les images qui se chevauchent ne soient pas traitées deux fois.
- `background_video` remplit les images de mouvement après la partie mouvement de référence ; il ne remplace pas l'image de référence ni les images `continue_motion` reportées.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positif` | Conditionnement positif modifié avec contexte vidéo supplémentaire, comprenant la sortie CLIP vision, le latent de la vidéo de pose, les pixels de la vidéo de visage, l'image latente concaténée et le masque concaténé. | CONDITIONING |
| `négatif` | Conditionnement négatif modifié avec contexte vidéo supplémentaire, comprenant la sortie CLIP vision, le latent de la vidéo de pose, les pixels de visage vierges, l'image latente concaténée et le masque concaténé. | CONDITIONING |
| `latent` | Tenseur latent initial (échantillons tous à zéro) pour la vidéo générée, avec la forme `[batch_size, 16, latent_length + trim_latent, latent_height, latent_width]`. | LATENT |
| `latent_rogné` | Nombre d'images latentes à supprimer au début du latent, correspondant aux images de l'image de référence. | INT |
| `image_rognée` | Nombre d'images à supprimer au début, correspondant aux images du mouvement de référence. | INT |
| `décalage de trame vidéo` | Décalage d'images mis à jour à utiliser pour le segment suivant, basé sur le décalage d'entrée et le nombre d'images traitées. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimateToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `a95bae4c7ae4ddc8a95bc9dafa2ca920b1d2166802615189537dce16949bfc03`
