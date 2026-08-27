# ByteDance2ReferenceNodeV2

ByteDance Seedance 2.5 Reference to Video génère, édite ou étend des vidéos à l’aide des modèles ByteDance Seedance (Seedance 2.5, 2.0, 2.0 Fast et 2.0 Mini) guidé par une invite textuelle et des images, vidéos, audios ou ressources de bibliothèque téléversés précédemment en option. Il téléverse les références, soumet une tâche de génération, attend son achèvement et renvoie le fichier vidéo final.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Sélecteur de modèle. Seedance 2.5 pour le modèle le plus récent, des vidéos jusqu’à 30 secondes et une sortie mp4/mov ; Seedance 2.0 pour une qualité maximale et la 4K ; Fast pour l’optimisation de la vitesse ; Mini pour la génération la plus rapide et la moins coûteuse. La sélection d’un modèle modifie les widgets d’entrée affichés ci-dessous. | DYNAMIC_COMBO | Oui | "Seedance 2.5"<br>"Seedance 2.0"<br>"Seedance 2.0 Fast"<br>"Seedance 2.0 Mini" |
| `seed` | Le seed contrôle si le nœud doit s’exécuter à nouveau ; les résultats sont non déterministes quel que soit le seed. Par défaut : 0. | INT | Oui | 0 à 2147483647 |
| `watermark` | Indique s’il faut ajouter un filigrane à la vidéo. Par défaut : False. Paramètre avancé. | BOOLEAN | Oui | true<br>false |

### Entrées Seedance 2.5

Ces entrées apparaissent lorsque `model` est défini sur « Seedance 2.5 ».

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite textuelle pour la génération de vidéos. Mettez les répliques entre guillemets pour orienter le dialogue généré. Par défaut : chaîne vide. | STRING | Oui | Texte multiligne |
| `resolution` | Résolution de la vidéo de sortie. Par défaut : 720p. | COMBO | Oui | "480p"<br>"720p"<br>"1080p" |
| `ratio` | Rapport d’aspect de la vidéo de sortie. Par défaut : 16:9. | COMBO | Oui | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | Durée de la vidéo de sortie en secondes (4-30). Par défaut : 5. | INT | Oui | 4 à 30 |
| `generate_audio` | Active la génération audio pour la vidéo de sortie. Par défaut : True. | BOOLEAN | Oui | true<br>false |
| `task_type` | Détermine quoi faire avec les médias de référence. Chaque valeur sauf auto est validée lors de la soumission de la tâche, de sorte que les paramètres incompatibles échouent avant le début de la génération.<br>auto : le modèle déduit la tâche à partir du prompt et des entrées, et les paramètres qui contredisent son interprétation n’échouent qu’après le début de la génération.<br>reference : générer une nouvelle vidéo guidée par les images, vidéos et audios de référence.<br>edit : modifier une vidéo de référence connectée (ajouter, supprimer, remplacer) ; la sortie conserve la durée et le format de la source, et les widgets duration et ratio sont ignorés.<br>extend : continuer une vidéo de référence connectée vers l’avant ou vers l’arrière ; le prompt doit contenir « extend forward », « extend backward » ou « continue », le format suit la source, et la sortie ne contient que le segment nouvellement généré de la durée définie, pas la source. Par défaut : auto. | COMBO | Oui | "auto"<br>"reference"<br>"edit"<br>"extend" |
| `output_format` | Format de conteneur de la vidéo de sortie. Par défaut : mp4. | COMBO | Oui | "mp4" |

### Entrées Seedance 2.0

Ces entrées apparaissent lorsque `model` est défini sur « Seedance 2.0 ».

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite textuelle pour la génération de vidéos. Par défaut : chaîne vide. | STRING | Oui | Texte multiligne |
| `resolution` | Résolution de la vidéo de sortie. | COMBO | Oui | "480p"<br>"720p"<br>"1080p"<br>"4k" |
| `ratio` | Rapport d’aspect de la vidéo de sortie. Par défaut : adaptive. | COMBO | Oui | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | Durée de la vidéo de sortie en secondes (4-15). Par défaut : 7. | INT | Oui | 4 à 15 |
| `generate_audio` | Active la génération audio pour la vidéo de sortie. Par défaut : True. | BOOLEAN | Oui | true<br>false |

### Entrées Seedance 2.0 Fast et Seedance 2.0 Mini

Ces entrées apparaissent lorsque `model` est défini sur « Seedance 2.0 Fast » ou « Seedance 2.0 Mini ». Les deux modèles partagent le même ensemble d’entrées.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite textuelle pour la génération de vidéos. Par défaut : chaîne vide. | STRING | Oui | Texte multiligne |
| `resolution` | Résolution de la vidéo de sortie. | COMBO | Oui | "480p"<br>"720p" |
| `ratio` | Rapport d’aspect de la vidéo de sortie. Par défaut : adaptive. | COMBO | Oui | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | Durée de la vidéo de sortie en secondes (4-15). Par défaut : 7. | INT | Oui | 4 à 15 |
| `generate_audio` | Active la génération audio pour la vidéo de sortie. Par défaut : True. | BOOLEAN | Oui | true<br>false |

### Entrées de référence

Ces emplacements de référence extensibles sont disponibles pour tous les modèles. Le nombre maximal d’emplacements diffère selon le modèle : Seedance 2.5 prend en charge jusqu’à 30 images, 10 vidéos, 10 audios et 30 ressources ; Seedance 2.0, 2.0 Fast et 2.0 Mini prennent en charge jusqu’à 9 images, 3 vidéos, 3 audios et 9 ressources.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `reference_images` | Emplacement extensible : connectez 1 à N images de référence qui guident la sortie. La limite de nombre dépend du modèle (voir les sections sur les modèles). Les images sont validées pour leur rapport d’aspect (0,4 à 2,5) et automatiquement réduites à un côté maximal de 6000 pixels. | IMAGE | Non | 1..9 emplacements (famille Seedance 2.0)<br>1..30 emplacements (Seedance 2.5) |
| `reference_videos` | Emplacement extensible : connectez 1 à N vidéos de référence. La limite de nombre dépend du modèle (voir les sections sur les modèles). Chaque vidéo doit durer au moins 1,8 seconde et respecter les limites de pixels du modèle et de la résolution sélectionnés. | VIDEO | Non | 1..3 emplacements (famille Seedance 2.0)<br>1..10 emplacements (Seedance 2.5) |
| `reference_audios` | Emplacement extensible : connectez 1 à N pistes audio de référence. La limite de nombre dépend du modèle (voir les sections sur les modèles). Chaque audio doit durer au moins 1,8 seconde. | AUDIO | Non | 1..3 emplacements (famille Seedance 2.0)<br>1..10 emplacements (Seedance 2.5) |
| `reference_assets` | Emplacement extensible : connectez 1 à N chaînes d’identifiant de ressource pour des médias déjà téléversés dans la bibliothèque virtuelle Seedance. Chaque ressource doit être Active. Vous pouvez faire référence à une ressource dans le prompt avec des jetons tels que `asset1` ou `asset 1` ; le nœud les remplace par l’étiquette positionnelle de la ressource (par exemple « Image 2 » ou « Vidéo 1 »). | STRING | Non | 1..9 emplacements (famille Seedance 2.0)<br>1..30 emplacements (Seedance 2.5) |
| `auto_downscale` | Réduit automatiquement les vidéos de référence qui dépassent le budget de pixels du modèle pour la résolution sélectionnée. Le rapport d’aspect est préservé ; les vidéos déjà dans les limites ne sont pas modifiées. Par défaut : True. | BOOLEAN | Non | true<br>false |
| `auto_upscale` | Augmente automatiquement la résolution des vidéos de référence qui sont en dessous du nombre minimal de pixels du modèle pour la résolution sélectionnée. Le rapport d’aspect est préservé ; les vidéos qui respectent déjà le minimum ne sont pas modifiées. Remarque : augmenter la résolution d’une source en basse résolution n’ajoute pas de vrai détail et peut produire des générations de qualité inférieure. Par défaut : False. Paramètre avancé. | BOOLEAN | Non | true<br>false |

**Remarque :** Au moins une image, une vidéo ou une ressource de référence est requise pour exécuter le nœud (Seedance 2.5 accepte également les références audio uniquement). Les vidéos et audios de référence doivent durer chacun au moins 1,8 seconde, et la durée combinée de toutes les vidéos de référence (et séparément, celle de tous les audios de référence) ne doit pas dépasser le nombre total maximal de secondes du modèle sélectionné. Les images de référence doivent avoir un rapport d’aspect compris entre environ 2:5 et 5:2 (0,4 à 2,5), faire au moins 300x300 pixels, et sont automatiquement réduites à un côté maximal de 6000 pixels. Les options « edit » et « extend » de `task_type` ne sont disponibles qu’avec Seedance 2.5 et nécessitent toutes deux au moins une vidéo de référence ; lorsque « edit » est utilisé, la sortie conserve la durée et le format de la source, et les widgets `duration` et `ratio` sont ignorés ; lorsque « extend » est utilisé, la sortie ne contient que le segment nouvellement généré à la durée définie. Les ressources référencées doivent être au statut Active, sinon la tâche échoue.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo générée, téléchargée depuis le fournisseur une fois la tâche de génération terminée. Contient de l’audio lorsque la génération audio est activée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNodeV2/fr.md)

---
**Source fingerprint (SHA-256):** `3a6bba12e719204ba5dba9d7d5f2b4c5285ed68974ee015b6e4a7892a1cf0933`
