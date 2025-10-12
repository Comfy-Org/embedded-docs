> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimateToVideo/fr.md)

Le nœud WanAnimateToVideo génère du contenu vidéo en combinant plusieurs entrées de conditionnement incluant des références de pose, des expressions faciales et des éléments d'arrière-plan. Il traite diverses entrées vidéo pour créer des séquences animées cohérentes tout en maintenant une consistance temporelle entre les images. Le nœud gère les opérations dans l'espace latent et peut étendre des vidéos existantes en poursuivant les motifs de mouvement.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Oui | - | Conditionnement positif pour guider la génération vers le contenu souhaité |
| `negative` | CONDITIONING | Oui | - | Conditionnement négatif pour éloigner la génération du contenu indésirable |
| `vae` | VAE | Oui | - | Modèle VAE utilisé pour l'encodage et le décodage des données d'image |
| `width` | INT | Non | 16 à MAX_RESOLUTION | Largeur de la vidéo de sortie en pixels (par défaut : 832, pas : 16) |
| `height` | INT | Non | 16 à MAX_RESOLUTION | Hauteur de la vidéo de sortie en pixels (par défaut : 480, pas : 16) |
| `length` | INT | Non | 1 à MAX_RESOLUTION | Nombre d'images à générer (par défaut : 77, pas : 4) |
| `batch_size` | INT | Non | 1 à 4096 | Nombre de vidéos à générer simultanément (par défaut : 1) |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Non | - | Sortie optionnelle du modèle de vision CLIP pour un conditionnement supplémentaire |
| `reference_image` | IMAGE | Non | - | Image de référence utilisée comme point de départ pour la génération |
| `face_video` | IMAGE | Non | - | Entrée vidéo fournissant un guidage des expressions faciales |
| `pose_video` | IMAGE | Non | - | Entrée vidéo fournissant un guidage de la pose et du mouvement |
| `continue_motion_max_frames` | INT | Non | 1 à MAX_RESOLUTION | Nombre maximum d'images à continuer à partir du mouvement précédent (par défaut : 5, pas : 4) |
| `background_video` | IMAGE | Non | - | Vidéo d'arrière-plan à composer avec le contenu généré |
| `character_mask` | MASK | Non | - | Masque définissant les régions des personnages pour un traitement sélectif |
| `continue_motion` | IMAGE | Non | - | Séquence de mouvement précédente à partir de laquelle continuer pour la consistance temporelle |
| `video_frame_offset` | INT | Non | 0 à MAX_RESOLUTION | Le nombre d'images à avancer dans toutes les vidéos d'entrée. Utilisé pour générer des vidéos plus longues par segments. Connectez à la sortie video_frame_offset du nœud précédent pour étendre une vidéo. (par défaut : 0, pas : 1) |

**Contraintes des paramètres :**

- Lorsque `pose_video` est fourni et que la logique `trim_to_pose_video` est active, la longueur de sortie sera ajustée pour correspondre à la durée de la vidéo de pose
- `face_video` est automatiquement redimensionné à une résolution de 512x512 lors du traitement
- Les images de `continue_motion` sont limitées par le paramètre `continue_motion_max_frames`
- Les vidéos d'entrée (`face_video`, `pose_video`, `background_video`, `character_mask`) sont décalées par `video_frame_offset` avant traitement
- Si `character_mask` ne contient qu'une seule image, elle sera répétée sur toutes les images
- Lorsque `clip_vision_output` est fourni, il est appliqué à la fois au conditionnement positif et négatif

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Conditionnement positif modifié avec un contexte vidéo supplémentaire |
| `negative` | CONDITIONING | Conditionnement négatif modifié avec un contexte vidéo supplémentaire |
| `latent` | LATENT | Contenu vidéo généré au format de l'espace latent |
| `trim_latent` | INT | Informations de rognage de l'espace latent pour le traitement en aval |
| `trim_image` | INT | Informations de rognage de l'espace image pour les images de mouvement de référence |
| `video_frame_offset` | INT | Décalage d'image mis à jour pour continuer la génération vidéo par segments |
