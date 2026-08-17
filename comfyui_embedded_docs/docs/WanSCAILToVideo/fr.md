# WanSCAILToVideo

Le nœud WanSCAILToVideo prépare le conditionnement et un espace latent vide pour la génération vidéo. Il traite des entrées optionnelles comme les images de référence, les vidéos de pose, les sorties CLIP vision et les segments de frames précédentes, en les intégrant dans le conditionnement positif et négatif d'un modèle vidéo. Le nœud renvoie le conditionnement modifié et un tenseur latent vide aux dimensions vidéo spécifiées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `positive` | L'entrée de conditionnement positive. | CONDITIONING | Oui | - |
| `negative` | L'entrée de conditionnement négative. | CONDITIONING | Oui | - |
| `vae` | Le modèle VAE utilisé pour encoder les images et les frames vidéo. | VAE | Oui | - |
| `width` | La largeur de la vidéo de sortie en pixels (défaut : 512). Ajustable par pas de 32. | INT | Oui | 32 à MAX_RESOLUTION |
| `height` | La hauteur de la vidéo de sortie en pixels (défaut : 896). Ajustable par pas de 32. | INT | Oui | 32 à MAX_RESOLUTION |
| `length` | Le nombre de frames dans la vidéo (défaut : 81). Ajustable par pas de 4 à partir de 1. | INT | Oui | 1 à MAX_RESOLUTION |
| `batch_size` | Le nombre de vidéos à générer dans un lot (défaut : 1). | INT | Oui | 1 à 4096 |
| `pose_strength` | Force du latent de pose (défaut : 1.0). | FLOAT | Oui | 0.0 à 10.0 |
| `pose_start` | Étape de début du conditionnement de pose (défaut : 0.0). | FLOAT | Oui | 0.0 à 1.0 |
| `pose_end` | Étape de fin du conditionnement de pose (défaut : 1.0). | FLOAT | Oui | 0.0 à 1.0 |
| `video_frame_offset` | Frame de sortie cumulée à laquelle ce segment commence. Connectez depuis la sortie `video_frame_offset` du segment précédent (défaut : 0). | INT | Oui | 0 à MAX_RESOLUTION |
| `previous_frame_count` | Frames de fin de `previous_frames` à utiliser comme ancrage. SCAIL-2 entraîné à 5 (segments de 81 frames, pas de 76 frames) (défaut : 5). | INT | Oui | 1 à MAX_RESOLUTION |
| `pose_video` | Vidéo utilisée pour le conditionnement de pose. Elle sera réduite à la moitié de la résolution de la vidéo principale. | IMAGE | Non | - |
| `pose_video_mask` | Réservé à SCAIL-2. Vidéo de masque SAM3 colorée par identité, à la même résolution que `pose_video`. | IMAGE | Non | - |
| `replacement_mode` | Réservé à SCAIL-2. False = Mode Animation (`pose_video_mask` doit avoir un fond noir). True = Mode Remplacement (`pose_video_mask` doit avoir un fond blanc). Défaut : False. | BOOLEAN | Non | - |
| `reference_image` | Image de référence. La première image est la référence principale (composez toutes les identités dessus). SCAIL-2 : les images supplémentaires du lot sont utilisées comme vues additionnelles (vue arrière, gros plan, arrière-plan masqué), chacune nécessitant un `reference_image_mask` correspondant dans la couleur de cette identité. | IMAGE | Non | - |
| `reference_image_mask` | Réservé à SCAIL-2. Masque de référence coloré, correspondant par lot à `reference_image` (le premier = masque de référence principal, les autres = masques d'identité pour les `reference_image` supplémentaires). | IMAGE | Non | - |
| `clip_vision_output` | Caractéristiques CLIP vision pour le conditionnement. Le modèle est entraîné avec un redimensionnement par étirement au ratio d'aspect. | CLIP_VISION_OUTPUT | Non | - |
| `previous_frames` | Réservé à SCAIL-2. Sortie décodée complète du segment précédent. Seules les dernières `previous_frame_count` sont utilisées comme ancrage d'extension. | IMAGE | Non | - |

**Remarque :**

- Les entrées `pose_video` et `pose_video_mask` sont découpées à partir de `video_frame_offset` ; si la vidéo n'a pas de frames au-delà de ce décalage, elle est ignorée. Elles sont ensuite tronquées ensemble à la plus courte des deux et plafonnées à `length` frames. Le `pose_video` est réduit à la moitié de la résolution de la vidéo principale avant l'encodage.
- L'entrée `reference_image_mask` ne s'applique que lorsque `reference_image` est également fournie. Chaque image du lot `reference_image` est encodée individuellement comme référence latente sur une frame unique. En Mode Remplacement (`replacement_mode=True`), les images de référence sont composées sur un fond noir en utilisant le masque d'image de référence comme alpha matte.
- Lorsque `clip_vision_output` est fourni, il est appliqué à la fois au conditionnement positif et négatif.
- Lorsque `previous_frames` est fourni, seules les dernières `previous_frame_count` frames sont utilisées comme ancrage d'extension. Le latent de sortie est partiellement rempli avec l'encodage de ces frames, un masque de bruit est inclus dans la sortie latente, et `video_frame_offset` est ajusté en soustrayant le nombre de frames conservées (jamais en dessous de 0).

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positive` | Le conditionnement positif modifié, contenant potentiellement des latents d'image de référence intégrés, la sortie CLIP vision, des latents de vidéo de pose, des masques de conduite, des masques de référence ou des latents de frames précédentes. | CONDITIONING |
| `negative` | Le conditionnement négatif modifié, contenant potentiellement des latents d'image de référence intégrés, la sortie CLIP vision, des latents de vidéo de pose, des masques de conduite, des masques de référence ou des latents de frames précédentes. | CONDITIONING |
| `latent` | Un tenseur latent vide de forme `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]`. Lorsque `previous_frames` est fourni, le latent est partiellement rempli avec les frames précédentes encodées et un masque de bruit est inclus. | LATENT |
| `video_frame_offset` | Décalage ajusté + longueur. Connectez au segment suivant pour la génération vidéo séquentielle. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSCAILToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `4a1a2201dfa94bd2f1330db02ec18a5e0a6aae9e9ac5ae97d456b7af1aa84b7b`
