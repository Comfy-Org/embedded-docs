> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimateToVideo/fr.md)

Voici la traduction en français de la documentation du nœud WanAnimateToVideo :

Le nœud WanAnimateToVideo génère du contenu vidéo en combinant plusieurs entrées de conditionnement, notamment des références de pose, des expressions faciales et des éléments d'arrière-plan. Il traite diverses entrées vidéo pour créer des séquences animées cohérentes tout en maintenant la cohérence temporelle entre les images. Le nœud gère les opérations dans l'espace latent et peut prolonger des vidéos existantes en poursuivant les motifs de mouvement.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `positif` | CONDITIONING | Oui | - | Conditionnement positif pour guider la génération vers le contenu souhaité |
| `négatif` | CONDITIONING | Oui | - | Conditionnement négatif pour éloigner la génération du contenu indésirable |
| `vae` | VAE | Oui | - | Modèle VAE utilisé pour encoder et décoder les données d'image |
| `largeur` | INT | Oui | 16 à MAX_RESOLUTION | Largeur de la vidéo de sortie en pixels (par défaut : 832, pas : 16) |
| `hauteur` | INT | Oui | 16 à MAX_RESOLUTION | Hauteur de la vidéo de sortie en pixels (par défaut : 480, pas : 16) |
| `longueur` | INT | Oui | 1 à MAX_RESOLUTION | Nombre d'images à générer (par défaut : 77, pas : 4) |
| `taille_du_lot` | INT | Oui | 1 à 4096 | Nombre de vidéos à générer simultanément (par défaut : 1) |
| `sortie_vision_clip` | CLIP_VISION_OUTPUT | Non | - | Sortie facultative du modèle de vision CLIP pour un conditionnement supplémentaire |
| `image_de_référence` | IMAGE | Non | - | Image de référence utilisée comme point de départ pour la génération |
| `vidéo_visage` | IMAGE | Non | - | Entrée vidéo fournissant des indications sur les expressions faciales |
| `vidéo_pose` | IMAGE | Non | - | Entrée vidéo fournissant des indications sur la pose et le mouvement |
| `images_max_poursuite_mouvement` | INT | Oui | 1 à MAX_RESOLUTION | Nombre maximal d'images à poursuivre à partir du mouvement précédent (par défaut : 5, pas : 4) |
| `vidéo_arrière_plan` | IMAGE | Non | - | Vidéo d'arrière-plan à composer avec le contenu généré |
| `masque_personnage` | MASK | Non | - | Masque définissant les régions du personnage pour un traitement sélectif |
| `poursuite_mouvement` | IMAGE | Non | - | Séquence de mouvement précédente à poursuivre pour la cohérence temporelle |
| `décalage_image_vidéo` | INT | Oui | 0 à MAX_RESOLUTION | Le nombre d'images à décaler dans toutes les vidéos d'entrée. Utilisé pour générer des vidéos plus longues par segments. Connectez-le à la sortie `décalage_image_vidéo` du nœud précédent pour prolonger une vidéo. (par défaut : 0, pas : 1) |

**Contraintes des paramètres :**

- Lorsque `pose_video` est fourni, la longueur de sortie sera ajustée pour correspondre à la durée de la vidéo de pose si la logique `trim_to_pose_video` est active (actuellement définie sur `False` dans le code source)
- `face_video` est automatiquement redimensionné en résolution 512x512 et normalisé dans une plage de -1,0 à 1,0 lors du traitement
- Les images de `continue_motion` sont limitées par le paramètre `continue_motion_max_frames` ; seules les dernières images `continue_motion_max_frames` de l'entrée sont utilisées
- Les vidéos d'entrée (`face_video`, `pose_video`, `background_video`, `character_mask`) sont décalées de `video_frame_offset` avant le traitement ; si le décalage dépasse la longueur de la vidéo, l'entrée est ignorée
- Si `character_mask` ne contient qu'une seule image, elle sera répétée sur toutes les images
- Lorsque `clip_vision_output` est fourni, il est appliqué à la fois au conditionnement positif et négatif
- Si `reference_image` n'est pas fourni, une image noire (tous les zéros) est utilisée comme référence par défaut
- Si `continue_motion` n'est pas fourni, les images initiales sont remplies avec un bruit gris (intensité 0,5)

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `négatif` | CONDITIONING | Conditionnement positif modifié avec contexte vidéo supplémentaire incluant la sortie de vision CLIP, le latent de la vidéo de pose, les pixels de la vidéo faciale, l'image latente concaténée et le masque concaténé |
| `latent` | CONDITIONING | Conditionnement négatif modifié avec contexte vidéo supplémentaire incluant la sortie de vision CLIP, le latent de la vidéo de pose, les pixels de la vidéo faciale (inversés), l'image latente concaténée et le masque concaténé |
| `latent_rogné` | LATENT | Contenu vidéo généré au format d'espace latent avec la forme [batch_size, 16, latent_length + trim_latent, latent_height, latent_width] |
| `image_rognée` | INT | Informations de rognage dans l'espace latent indiquant le nombre d'images latentes à rogner depuis le début (correspond aux images latentes de l'image de référence) |
| `décalage de trame vidéo` | INT | Informations de rognage dans l'espace image pour les images de mouvement de référence, indiquant le nombre d'images à rogner depuis le début |
| `décalage_image_vidéo` | INT | Décalage d'images mis à jour pour poursuivre la génération vidéo par segments, calculé comme le décalage précédent plus la longueur générée |

---
**Source fingerprint (SHA-256):** `c2ca90f4963f629d51cdd7f4bdb67e01c32ce5ca7d916b1f992ccd220f57566c`
