# MiniMax H3 Référence vers Vidéo

MiniMax H3 Reference to Video crée le conditionnement textuel et le latent audio-vidéo vide nécessaires à la génération référence-vers-vidéo de MiniMax H3. Vous fournissez un prompt ainsi que des images, vidéos et clips audio de référence facultatifs, et le nœud encode ces références en un conditionnement que le modèle peut utiliser pendant la génération. Le prompt fait référence aux médias de référence avec les balises `<Picture i>`, `<Video k>` et `<Audio j>`.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `clip` | Modèle CLIP utilisé pour tokeniser le prompt et encoder les médias de référence en tokens de conditionnement. | CLIP | Oui | |
| `vae` | VAE vidéo. Sans lui, les images/vidéos de référence ne conditionnent que l'encodeur de texte. | VAE | Non | |
| `audio_vae` | VAE audio. Sans lui, l'audio de référence ne conditionne que l'encodeur de texte. | VAE | Non | |
| `prompt` | Prompt textuel pour la vidéo. Les médias de référence peuvent être adressés avec les balises `<Picture i>`, `<Video k>` et `<Audio j>` (indexées à partir de 1 par type). Prend en charge les prompts multilignes et dynamiques. | STRING | Oui | |
| `width` | Largeur de la vidéo générée en pixels (par défaut : 1344). | INT | Oui | 32 à 16384 (pas 32) |
| `height` | Hauteur de la vidéo générée en pixels (par défaut : 768). | INT | Oui | 32 à 16384 (pas 32) |
| `length` | Nombre d'images à 24 fps, (124 = ~5 s, plage d'entraînement ~124-362) (par défaut : 124). | INT | Oui | 5 à 3600 (pas 17) |
| `ref_image_size` | Dimensionnement des images de référence. `match` met à l'échelle chaque réf (uniquement vers le bas, en conservant les proportions) vers la zone en pixels de la génération ; `max` utilise le petit côté de 2048 px du pipeline de référence pour une meilleure fidélité d'identité. Les tokens de référence traversent chaque étape d'échantillonnage, donc `max` peut être plusieurs fois plus lent (par défaut : `match`). | COMBO | Oui | `"match"`<br>`"max"` |
| `ref_images` | Emplacement extensible : connectez jusqu'à 9 images de référence (`ref_image_1` ... `ref_image_9`). Image de référence (réduite à un petit côté de 2048 px si plus grande, jamais agrandie). | IMAGE | Non | 0 à 9 |
| `ref_videos` | Emplacement extensible : connectez jusqu'à 3 vidéos de référence (`ref_video_1` ... `ref_video_3`). Images de vidéo de référence à 24 fps (2-15 s). | IMAGE | Non | 0 à 3 |
| `ref_video_audios` | Emplacement extensible : connectez jusqu'à 3 pistes audio (`ref_video_audio_1` ... `ref_video_audio_3`). Piste audio de la vidéo de référence portant le même numéro. | AUDIO | Non | 0 à 3 |
| `ref_audios` | Emplacement extensible : connectez jusqu'à 3 clips audio de référence autonomes (`ref_audio_1` ... `ref_audio_3`). Audio de référence autonome. | AUDIO | Non | 0 à 3 |

Remarques :

- Le prompt fait référence aux médias de référence avec des balises indexées à partir de 1 par type : `<Picture i>` pour les images, `<Video k>` pour les vidéos et `<Audio j>` pour l'audio. Les références sont présentées au modèle dans un ordre fixe : les images, puis les vidéos (avec l'étiquette `<Audio j>` de chaque piste audio juste avant sa `<Video k>`), puis l'audio autonome.
- Une piste audio connectée à `ref_video_audio_N` est utilisée avec la vidéo de référence connectée à `ref_video_N`.
- Les vidéos de référence doivent contenir au moins 5 images (~0,2 seconde à 24 fps), sinon le nœud lève une erreur. Les images au-delà de la `length` demandée sont coupées, et le nombre d'images restant est ajusté à une valeur prise en charge par le modèle.
- La `length` demandée est alignée sur un nombre d'images pris en charge avant la création du latent.
- Sans `vae`, les images et vidéos de référence ne conditionnent que l'encodeur de texte (aucun latent de référence n'est produit). Sans `audio_vae`, l'audio de référence ne conditionne que l'encodeur de texte.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positive` | Conditionnement contenant le prompt encodé. Lorsque des médias de référence et les VAE appropriés sont fournis, il contient également le contenu encodé des images, vidéos et audio de référence utilisé par le modèle MiniMax H3. | CONDITIONING |
| `latent` | Latent audio-vidéo vide aux `width`, `height` et `length` (nombre d'images) demandés, incluant le latent vidéo aligné et le latent audio. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ReferenceToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `47df0d6d13cb02aa4f69b50a7f8d0f6c1639c1fb5e0f69bf8fc57dd4cb752db8`
