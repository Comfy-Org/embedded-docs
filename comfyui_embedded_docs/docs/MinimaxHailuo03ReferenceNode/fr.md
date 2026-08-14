# MiniMax H3 Référence vers Vidéo

Ce nœud génère une vidéo en utilisant le modèle MiniMax H3, en s'appuyant sur des images de référence, des vidéos et des audios pour conditionner le résultat. Les références sont désignées dans le prompt selon leur ordre de connexion : « Image 1 », « Image 2 », « Vidéo 1 », « Audio 1 », etc.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `model` | Modèle à utiliser pour la génération de vidéos (par défaut : "MiniMax H3"). La sélection de "MiniMax H3" fournit les paramètres `prompt`, `resolution`, `ratio`, `duration`, `reference_images`, `reference_videos` et `reference_audios` ci-dessous. | STRING | Oui | "MiniMax H3" |
| `seed` | Graine aléatoire. La même demande avec la même graine donne des résultats similaires, mais pas garantis identiques (par défaut : 42). | INT | Oui | 0 à 4294967295 |
| `watermark` | Indique si un filigrane AIGC doit être ajouté à la vidéo (par défaut : false). | BOOLEAN | Non | true<br>false |

### Entrées MiniMax H3

Ces entrées apparaissent lorsque "MiniMax H3" est sélectionné comme modèle.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt textuel pour la génération de vidéos. Les médias de référence peuvent être désignés par leur ordre, par exemple "Image 1", "Image 2", "Vidéo 1" ou "Audio 1". | STRING | Oui | Longueur minimale : 1 caractère |
| `resolution` | Résolution de la vidéo de sortie (par défaut : "768P"). | STRING | Oui | "768P"<br>"2K" |
| `ratio` | Rapport d'aspect de la vidéo de sortie (par défaut : "adaptive"). | STRING | Oui | "adaptive"<br>"16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Durée de la vidéo de sortie en secondes (par défaut : 5). | INT | Oui | 4 à 15 |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Emplacement extensible : connectez 1 à 9 éléments (`image_1`...`image_9`). Images de référence de sujet ou de style, désignées dans le prompt comme "Image 1"..."Image 9" dans l'ordre de connexion. Jusqu'à 9 images. | IMAGE | Non | 0 à 9 images |
| `reference_videos` | Emplacement extensible : connectez 1 à 3 éléments (`video_1`...`video_3`). Vidéos de référence de mouvement ou de scène, désignées dans le prompt comme "Vidéo 1"..."Vidéo 3" dans l'ordre de connexion. Jusqu'à 3 vidéos, chacune de 2 à 15 secondes, pour un total de 15 secondes. | VIDEO | Non | 0 à 3 vidéos |
| `reference_audios` | Emplacement extensible : connectez 1 à 3 éléments (`audio_1`...`audio_3`). Références audio, désignées dans le prompt comme "Audio 1"..."Audio 3" dans l'ordre de connexion. Jusqu'à 3 clips, chacun de 2 à 15 secondes, pour un total de 15 secondes. Ne peut pas être utilisé sans une image ou une vidéo de référence. | AUDIO | Non | 0 à 3 clips |

### Contraintes des paramètres

- Au moins une image de référence ou une vidéo de référence est requise. Une référence audio seule n'est pas acceptée.
- Chaque image de référence doit avoir un rapport d'aspect compris entre environ 0,4 et 2,5 (2:5 à 5:2) et une largeur et une hauteur minimales de 256 pixels.
- Chaque vidéo de référence doit durer entre 2 et 15 secondes avec une cadence d'images comprise entre 23,976 et 60 FPS. La durée totale de toutes les vidéos de référence ne peut pas dépasser 15 secondes.
- Chaque clip audio de référence doit durer entre 2 et 15 secondes. La durée totale de tous les clips audio de référence ne peut pas dépasser 15 secondes.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `video` | La vidéo générée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03ReferenceNode/fr.md)

---
**Source fingerprint (SHA-256):** `f7e9c68addda6b48a2366139ecfa28ee57e6cda4aa5cd775c2d769517366573f`
