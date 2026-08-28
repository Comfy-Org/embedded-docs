# MiniMax H3 Référence vers Vidéo

MiniMax H3 Reference to Video crée le conditionnement textuel et le latent audio-vidéo vide nécessaires à la génération de vidéo de référence avec MiniMax H3. Vous fournissez une invite ainsi que des images, des vidéos et des clips audio de référence optionnels, et le nœud encode ces références en tokens que le modèle peut utiliser pendant la génération. L'invite fait référence aux références avec les balises `<Picture i>`, `<Video k>` et `<Audio j>`.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `clip` | Modèle CLIP utilisé pour tokeniser l'invite et encoder les médias de référence en tokens de conditionnement. | CLIP | Oui | |
| `vae` | VAE utilisé pour encoder les images de référence et les trames vidéo de référence dans l'espace latent. | VAE | Oui | |
| `audio_vae` | VAE utilisé pour encoder l'audio de référence dans l'espace latent. L'audio est rééchantillonné au taux d'échantillonnage de l'audio VAE (32 kHz par défaut). | VAE | Oui | |
| `invite` | Invite textuelle pour la vidéo. Les médias de référence peuvent être désignés avec les balises `<Picture i>`, `<Video k>` et `<Audio j>` (indexées à partir de 1 par type). Prend en charge les invites multilignes et dynamiques. | STRING | Oui | |
| `largeur` | Largeur de la vidéo générée en pixels (défaut : 1344). | INT | Oui | 32 à 16384 (pas de 32) |
| `hauteur` | Hauteur de la vidéo générée en pixels (défaut : 768). | INT | Oui | 32 à 16384 (pas de 32) |
| `longueur` | Nombre d'images à 24 fps ; 124 = ~5 s, plage d'entraînement ~124-362 (défaut : 124). | INT | Oui | 5 à 3600 (pas de 17) |
| `taille_image_référence` | Dimensionnement des images de référence. `match` réduit chaque image de référence uniquement en conservant le rapport hauteur/largeur, à la zone de pixels de la génération ; `max` utilise le petit côté de 2048 px du pipeline de référence pour une meilleure fidélité de l'identité. Les tokens de référence traversent chaque étape d'échantillonnage, donc `max` peut être plusieurs fois plus lent (défaut : `match`). | COMBO | Oui | `"match"`<br>`"max"` |
| `images_de_référence` | Emplacement extensible : connectez 1 à 9 images de référence (`ref_image_1` ... `ref_image_9`). Chaque image est réduite à un petit côté de 2048 px si elle est plus grande et jamais agrandie. | IMAGE | Non | 0 à 9 |
| `vidéos_de_référence` | Emplacement extensible : connectez 1 à 3 vidéos de référence (`ref_video_1` ... `ref_video_3`). Images de vidéo de référence à 24 fps (2-15 s). | IMAGE | Non | 0 à 3 |
| `audios_vidéo_de_référence` | Emplacement extensible : connectez 1 à 3 bandes sonores (`ref_video_audio_1` ... `ref_video_audio_3`). Bande sonore de la vidéo de référence portant le même numéro. | AUDIO | Non | 0 à 3 |
| `audios_de_référence` | Emplacement extensible : connectez 1 à 3 clips audio de référence autonomes (`ref_audio_1` ... `ref_audio_3`). | AUDIO | Non | 0 à 3 |

Remarques :

- L'invite fait référence aux médias de référence avec des balises indexées à partir de 1 par type : `<Picture i>` pour les images, `<Video k>` pour les vidéos et `<Audio j>` pour l'audio. Les références sont présentées au modèle dans un ordre fixe : images, puis vidéos (avec l'étiquette `<Audio j>` de chaque bande sonore juste avant son `<Video k>`), puis audio autonome.
- Les vidéos de référence doivent contenir au moins 5 images (~0,2 seconde à 24 fps), sinon le nœud génère une erreur. Les images vidéo sont également limitées à la `length` sélectionnée et réduites à un nombre d'images pris en charge.
- La `length` demandée est alignée sur un nombre d'images pris en charge avant la création du latent.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positif` | Conditionnement contenant l'invite encodée ainsi que les tokens d'image, de vidéo et d'audio de référence encodés utilisés par le modèle MiniMax H3. | CONDITIONING |
| `latent` | Latent audio-vidéo vide à la `width`, `height` et `length` (nombre d'images) demandées. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ReferenceToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `d9a444e712cdc255d7c56a3ab38d0523659f198b3228b9283a7028cfd0e4f3f9`
