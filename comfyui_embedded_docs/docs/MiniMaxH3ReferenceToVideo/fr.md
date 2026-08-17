# MiniMax H3 Référence vers Vidéo

``markdown
MiniMax H3 Reference to Video crée le conditionnement textuel et le latent audio-vidéo vide nécessaires à la génération référence-vers-vidéo de MiniMax H3. Vous fournissez un prompt ainsi que des images, des vidéos et des clips audio de référence optionnels, et le nœud encode ces références en jetons que le modèle peut utiliser lors de la génération. Le prompt fait référence aux références avec les balises `<Picture i>`, `<Video k>` et `<Audio j>`.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `clip` | Modèle CLIP utilisé pour tokeniser le prompt et encoder les médias de référence en jetons de conditionnement. | CLIP | Oui | |
| `vae` | VAE utilisé pour encoder les images de référence et les images vidéo de référence dans l'espace latent. | VAE | Oui | |
| `audio_vae` | VAE utilisé pour encoder l'audio de référence dans l'espace latent (taux d'échantillonnage audio de 32 kHz). | VAE | Oui | |
| `prompt` | Prompt textuel pour la vidéo. Les médias de référence peuvent être désignés avec les balises `<Picture i>`, `<Video k>` et `<Audio j>` (indexés à partir de 1 pour chaque type). Prend en charge les prompts multilignes et dynamiques. | STRING | Oui | |
| `width` | Largeur de la vidéo générée en pixels (défaut : 1344). | INT | Oui | 32 to 16384 (step 32) |
| `height` | Hauteur de la vidéo générée en pixels (défaut : 768). | INT | Oui | 32 to 16384 (step 32) |
| `length` | Nombre d'images à 24 fps ; 124 = ~5 s, plage d'entraînement ~124-362 (défaut : 124). | INT | Oui | 5 to 3600 (step 17) |
| `ref_image_size` | Mode de dimensionnement des images de référence. `match` réduit chaque image de référence uniquement, en conservant le rapport hauteur/largeur, à la surface de pixels de la génération ; `max` utilise le petit côté de 2048 px du pipeline de référence pour une meilleure fidélité d'identité. Les jetons de référence traversent chaque étape d'échantillonnage, donc `max` peut être plusieurs fois plus lent (défaut : `match`). | COMBO | Oui | `"match"`<br>`"max"` |
| `ref_images` | Images de référence optionnelles. Chaque image est réduite à un petit côté de 2048 px si elle est plus grande, et jamais agrandie. Plusieurs images peuvent être fournies. | IMAGE | Non | 0 to 9 |
| `ref_videos` | Images vidéo de référence optionnelles à 24 fps (2-15 s). Plusieurs vidéos peuvent être fournies. | IMAGE | Non | 0 to 3 |
| `ref_video_audios` | Bandes sonores optionnelles associées aux vidéos de référence par index ; `ref_video_audio_N` est la bande sonore de `ref_video_N` du même numéro. | AUDIO | Non | 0 to 3 |
| `ref_audios` | Clips audio de référence autonomes optionnels. | AUDIO | Non | 0 to 3 |

Remarques :
- Le prompt fait référence aux médias de référence avec des balises indexées à partir de 1 pour chaque type : `<Picture i>` pour les images, `<Video k>` pour les vidéos et `<Audio j>` pour l'audio. Les références sont présentées au modèle dans un ordre fixe : images, puis vidéos (avec l'étiquette `<Audio j>` de chaque bande sonore juste avant son `<Video k>`), puis audio autonome.
- Les vidéos de référence doivent contenir au moins 5 images (~0,2 seconde à 24 fps), sinon le nœud génère une erreur. Les images vidéo sont plafonnées à la `length` sélectionnée et réduites à un nombre d'images pris en charge.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positive` | Conditionnement contenant le prompt encodé ainsi que les jetons de référence encodés pour les images, vidéos et audio, utilisés par le modèle MiniMax H3. | CONDITIONING |
| `latent` | Latent audio-vidéo vide aux dimensions `width`, `height` et `length` (nombre d'images) demandées. | LATENT |
```

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ReferenceToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `d9a444e712cdc255d7c56a3ab38d0523659f198b3228b9283a7028cfd0e4f3f9`
