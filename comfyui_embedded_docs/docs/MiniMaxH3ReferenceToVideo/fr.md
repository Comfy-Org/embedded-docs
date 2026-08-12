# MiniMax H3 Référence vers Vidéo

MiniMax H3 Reference to Video crée le conditionnement textuel et le latent vidéo vide nécessaires à la génération vidéo de référence vers vidéo de MiniMax H3. Vous fournissez un prompt ainsi que des images, vidéos et clips audio de référence facultatifs, et le nœud encode ces références en jetons que le modèle peut utiliser pendant la génération. Le prompt fait référence aux références avec les balises `<Picture i>`, `<Video k>` et `<Audio j>`.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `clip` | Modèle CLIP utilisé pour tokeniser le prompt et encoder les médias de référence en jetons de conditionnement. | CLIP | Oui | |
| `vae` | VAE utilisé pour encoder les images de référence et les trames de vidéos de référence dans l'espace latent. | VAE | Oui | |
| `audio_vae` | VAE utilisé pour encoder l'audio de référence dans l'espace latent (taux d'échantillonnage audio de 32 kHz). | VAE | Oui | |
| `invite` | Prompt textuel pour la vidéo. Les médias de référence peuvent être désignés avec les balises `<Picture i>`, `<Video k>` et `<Audio j>` (indexés à partir de 1 par type). Prend en charge les prompts multi-lignes et dynamiques. | STRING | Oui | |
| `largeur` | Largeur de la vidéo générée en pixels (défaut : 1344). | INT | Oui | 32 à 16384 (pas de 32) |
| `hauteur` | Hauteur de la vidéo générée en pixels (défaut : 768). | INT | Oui | 32 à 16384 (pas de 32) |
| `longueur` | Nombre de trames à 24 fps ; 124 = ~5 s, plage d'entraînement ~124-362 (défaut : 124). | INT | Oui | 5 à 3600 (pas de 17) |
| `taille_image_référence` | Mode de dimensionnement des images de référence. `match` réduit chaque image de référence uniquement, en conservant le ratio hauteur/largeur, à la surface en pixels de la génération ; `max` utilise le petit côté de 2048 px du pipeline de référence pour une meilleure fidélité d'identité. Les jetons de référence traversent chaque étape d'échantillonnage, donc `max` peut être plusieurs fois plus lent (défaut : `match`). | COMBO | Oui | `"match"`<br>`"max"` |
| `images_de_référence` | Images de référence facultatives. Chaque image est réduite à un petit côté de 2048 px si elle est plus grande et jamais agrandie. Plusieurs images peuvent être fournies. | IMAGE | Non | 0 à 9 |
| `vidéos_de_référence` | Trames de vidéos de référence facultatives à 24 fps (2-15 s). Plusieurs vidéos peuvent être fournies. | IMAGE | Non | 0 à 3 |
| `audios_vidéo_de_référence` | Bandes sonores facultatives associées aux vidéos de référence par index ; `ref_video_audio_N` est la bande sonore de la vidéo `ref_video_N` portant le même numéro. | AUDIO | Non | 0 à 3 |
| `audios_de_référence` | Clips audio de référence autonomes facultatifs. | AUDIO | Non | 0 à 3 |

Remarques :
- Le prompt fait référence aux médias de référence avec des balises indexées à partir de 1 par type : `<Picture i>` pour les images, `<Video k>` pour les vidéos, et `<Audio j>` pour l'audio. Les références sont présentées au modèle dans un ordre fixe : les images, puis les vidéos (avec l'étiquette `<Audio j>` de chaque bande sonore juste avant sa `<Video k>`), puis l'audio autonome.
- Les vidéos de référence doivent contenir au moins 5 trames (~0,2 seconde à 24 fps), sinon le nœud génère une erreur. Les trames vidéo sont également plafonnées à la `length` sélectionnée et réduites à un nombre de trames pris en charge.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positif` | Conditionnement contenant le prompt encodé ainsi que les jetons d'images, de vidéos et d'audio de référence encodés utilisés par le modèle MiniMax H3. | CONDITIONING |
| `latent` | Latent audio-vidéo vide à la `largeur`, `hauteur` et `longueur` (nombre de trames) demandées. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ReferenceToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `529e51c5c9c63a94176a15851f40ac42f7bd93e7d7c6ad334ed22aa29d04dfde`
