# MiniMax H3 Référence vers Vidéo

Ce nœud génère une vidéo à l'aide des modèles MiniMax H3, conditionnée par des images, des vidéos et de l'audio de référence. Les références sont désignées dans le prompt par leur ordre de connexion : « Image 1 », « Image 2 », « Video 1 », « Audio 1 », etc. Deux modèles sont disponibles : « MiniMax H3 » et « MiniMax H3 Max ».

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Modèle à utiliser pour la génération vidéo (par défaut : « MiniMax H3 »). Sélectionner « MiniMax H3 » fournit les entrées de génération et de référence MiniMax H3 ci-dessous. Sélectionner « MiniMax H3 Max » fournit les entrées de génération et de référence MiniMax H3 Max ci-dessous. | DYNAMIC_COMBO | Oui | "MiniMax H3"<br>"MiniMax H3 Max" |
| `graine` | Graine aléatoire. La même requête avec la même graine donne des résultats similaires, mais non garantis identiques (par défaut : 42). | INT | Oui | 0 à 4294967295 |
| `filigrane` | Indique s'il faut ajouter un filigrane AIGC à la vidéo (par défaut : false). Pris en charge uniquement par le modèle MiniMax H3. | BOOLEAN | Non | true<br>false |

### Entrées MiniMax H3

Ces entrées sont disponibles lorsque « MiniMax H3 » est sélectionné comme modèle.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt textuel pour la génération vidéo. Les médias de référence peuvent être désignés par leur ordre, par exemple « Image 1 », « Image 2 », « Video 1 » ou « Audio 1 ». | STRING | Oui | Minimum 1 caractère |
| `resolution` | Résolution de la vidéo de sortie (par défaut : « 768P »). | COMBO | Oui | "768P"<br>"2K" |
| `ratio` | Rapport d'aspect de la vidéo de sortie (par défaut : « adaptive »). | COMBO | Oui | "adaptive"<br>"16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Durée de la vidéo de sortie en secondes (par défaut : 5). | INT | Oui | 4 à 15 |

### Entrées MiniMax H3 Max

Ces entrées sont disponibles lorsque « MiniMax H3 Max » est sélectionné comme modèle.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt textuel pour la génération vidéo. Les médias de référence peuvent être désignés par leur ordre, par exemple « Image 1 », « Image 2 », « Video 1 » ou « Audio 1 ». | STRING | Oui | 1 à 50000 caractères |
| `resolution` | Résolution de la vidéo de sortie (par défaut : « 768P »). | COMBO | Oui | "480P"<br>"768P" |
| `ratio` | Rapport d'aspect de la vidéo de sortie (par défaut : « adaptive »). | COMBO | Oui | "adaptive"<br>"16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Durée de la vidéo de sortie en secondes (par défaut : 5). | INT | Oui | 5 à 15 |
| `prompt_expansion_mode` | Niveau d'effort consacré à la réécriture du prompt avant la génération (par défaut : « balanced »). | COMBO | Oui | "balanced"<br>"quality" |
| `reference_detail` | Niveau de détail auquel les images de référence sont envoyées. « high » les envoie à la plus grande taille utilisée par le modèle (jusqu'à un petit côté de 2048 pixels) ; « standard » les réduit à au plus 2048x1024 afin de réduire le coût de référence (par défaut : « standard »). | COMBO | Oui | "high"<br>"standard" |

### Entrées de référence

Ces entrées de référence sont partagées par les deux modèles. Chacune est un emplacement extensible.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `reference_images` | Emplacement extensible : connectez jusqu'à 9 éléments (`image_1`...`image_9`). Images de référence de sujet ou de style, désignées dans le prompt par « Image 1 »..« Image 9 » dans l'ordre de connexion. Jusqu'à 9 images. | IMAGE | Non | 0 à 9 images |
| `reference_videos` | Emplacement extensible : connectez jusqu'à 3 éléments (`video_1`...`video_3`). Vidéos de référence de mouvement ou de scène, désignées dans le prompt par « Video 1 »..« Video 3 » dans l'ordre de connexion. Jusqu'à 3 vidéos, 2 à 15 secondes chacune, 15 secondes au total. | VIDEO | Non | 0 à 3 vidéos |
| `reference_audios` | Emplacement extensible : connectez jusqu'à 3 éléments (`audio_1`...`audio_3`). Références audio, désignées dans le prompt par « Audio 1 »..« Audio 3 » dans l'ordre de connexion. Jusqu'à 3 clips, 2 à 15 secondes chacun, 15 secondes au total. Ne peuvent pas être utilisées sans une image ou une vidéo de référence. | AUDIO | Non | 0 à 3 clips |

### Contraintes des paramètres

- Au moins une image de référence ou une vidéo de référence est requise. Une référence audio seule n'est pas acceptée.
- Chaque image de référence doit avoir un rapport d'aspect compris entre environ 0,4 et 2,5 (2:5 à 5:2) et une largeur et une hauteur minimales de 256 pixels.
- Chaque vidéo de référence doit durer entre 2 et 15 secondes avec une fréquence d'images comprise entre 23,976 et 60 FPS. La durée totale de toutes les vidéos de référence ne peut pas dépasser 15 secondes.
- Chaque clip audio de référence doit durer entre 2 et 15 secondes. La durée totale de tous les clips audio de référence ne peut pas dépasser 15 secondes.
- Lorsque « MiniMax H3 Max » est sélectionné, le paramètre `watermark` doit être désactivé.
- Lorsque « MiniMax H3 Max » est sélectionné, le nombre total de fichiers de référence (images, vidéos et audio combinés) ne peut pas dépasser 12.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo générée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03ReferenceNode/fr.md)

---
**Source fingerprint (SHA-256):** `b77eedb1f7757e60518c04484f1cc24c27cf6886b3ae31c15207ea49fd436a73`
