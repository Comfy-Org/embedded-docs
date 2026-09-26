# ByteDance Seedance 2.5 Référence vers vidéo

ByteDance Seedance 2.5 Reference to Video génère, modifie ou étend des vidéos à l'aide des modèles ByteDance Seedance (Seedance 2.5, 2.5 Draft, 2.0, 2.0 Fast et 2.0 Mini), guidé par un prompt texte et éventuellement des images, vidéos, audios de référence ou des assets de bibliothèque précédemment téléversés. Il téléverse les références, soumet une tâche de génération, attend la fin de l'exécution et renvoie le fichier vidéo final. Sélectionner `Seedance 2.5 Draft` produit à la place un aperçu rapide en 480p ; connectez le `draft_task_id` obtenu au nœud ByteDance Seedance 2.5 Draft to Final Video pour générer la version finale en 1080p.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `model` | Sélecteur de modèle. Seedance 2.5 pour le modèle le plus récent, des vidéos allant jusqu'à 30 secondes et une sortie mp4 ; Seedance 2.5 Draft pour un aperçu rapide en 480p dont la sortie `draft_task_id` génère la version finale en 1080p dans le nœud ByteDance Seedance 2.5 Draft to Final Video ; Seedance 2.0 pour une qualité maximale et la 4k ; Fast pour l'optimisation de la vitesse ; Mini pour la génération la plus rapide et la moins coûteuse. La sélection d'un modèle modifie les widgets d'entrée affichés ci-dessous. | DYNAMIC_COMBO | Oui | "Seedance 2.5"<br>"Seedance 2.5 Draft"<br>"Seedance 2.0"<br>"Seedance 2.0 Fast"<br>"Seedance 2.0 Mini" |
| `seed` | `seed` contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. Par défaut : 0. | INT | Oui | 0 à 2147483647 |
| `watermark` | Indique s'il faut ajouter un filigrane à la vidéo. Par défaut : False. Réglage avancé. | BOOLEAN | Oui | true<br>false |

### Entrées Seedance 2.5

Ces entrées apparaissent lorsque `model` est défini sur "Seedance 2.5".

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `prompt` | Prompt texte pour la génération vidéo. Placez les répliques parlées entre guillemets doubles pour orienter le dialogue généré. Par défaut : chaîne vide. | STRING | Oui | Texte multiligne |
| `resolution` | Résolution de la vidéo de sortie. Par défaut : 720p. | COMBO | Oui | "480p"<br>"720p"<br>"1080p" |
| `ratio` | Rapport d'aspect de la vidéo de sortie. Par défaut : 16:9. | COMBO | Oui | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | Durée de la vidéo de sortie en secondes (4-30). Par défaut : 5. | INT | Oui | 4 à 30 |
| `generate_audio` | Active la génération audio pour la vidéo de sortie. Par défaut : True. | BOOLEAN | Oui | true<br>false |
| `task_type` | Ce qu'il faut faire avec les médias de référence. Toutes les valeurs sauf auto sont validées lors de la soumission de la tâche ; les réglages incompatibles échouent donc avant le début de la génération.<br>auto : le modèle déduit la tâche à partir du prompt et des entrées, et les réglages qui entrent en conflit avec son interprétation échouent seulement après le début de la génération.<br>reference : génère une nouvelle vidéo guidée par les images, vidéos et audios de référence.<br>edit : modifie une vidéo de référence connectée (ajouter, supprimer, remplacer) ; la sortie conserve la longueur et le rapport d'aspect du clip source, et les widgets `duration` et `ratio` sont ignorés.<br>extend : prolonge une vidéo de référence connectée vers l'avant ou vers l'arrière ; le prompt doit indiquer "extend forward", "extend backward" ou "continue", le rapport d'aspect suit le clip source, et la sortie contient uniquement le segment nouvellement généré correspondant à la durée que vous définissez, et non le clip source. Par défaut : auto. | COMBO | Oui | "auto"<br>"reference"<br>"edit"<br>"extend" |
| `output_format` | Format de conteneur de la vidéo de sortie. Par défaut : mp4. | COMBO | Oui | "mp4" |

### Entrées Seedance 2.5 Draft

Ces entrées apparaissent lorsque `model` est défini sur "Seedance 2.5 Draft". L'ensemble des paramètres correspond à Seedance 2.5 ci-dessus, sauf que `resolution` ne propose que `"480p"` (par défaut `"480p"`).

### Entrées Seedance 2.0

Ces entrées apparaissent lorsque `model` est défini sur "Seedance 2.0".

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `prompt` | Prompt texte pour la génération vidéo. Par défaut : chaîne vide. | STRING | Oui | Texte multiligne |
| `resolution` | Résolution de la vidéo de sortie. | COMBO | Oui | "480p"<br>"720p"<br>"1080p"<br>"4k" |
| `ratio` | Rapport d'aspect de la vidéo de sortie. Par défaut : adaptive. | COMBO | Oui | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | Durée de la vidéo de sortie en secondes (4-15). Par défaut : 7. | INT | Oui | 4 à 15 |
| `generate_audio` | Active la génération audio pour la vidéo de sortie. Par défaut : True. | BOOLEAN | Oui | true<br>false |

### Entrées Seedance 2.0 Fast et Seedance 2.0 Mini

Ces entrées apparaissent lorsque `model` est défini sur "Seedance 2.0 Fast" ou "Seedance 2.0 Mini". Les deux modèles partagent le même ensemble d'entrées.

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `prompt` | Prompt texte pour la génération vidéo. Par défaut : chaîne vide. | STRING | Oui | Texte multiligne |
| `resolution` | Résolution de la vidéo de sortie. | COMBO | Oui | "480p"<br>"720p" |
| `ratio` | Rapport d'aspect de la vidéo de sortie. Par défaut : adaptive. | COMBO | Oui | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | Durée de la vidéo de sortie en secondes (4-15). Par défaut : 7. | INT | Oui | 4 à 15 |
| `generate_audio` | Active la génération audio pour la vidéo de sortie. Par défaut : True. | BOOLEAN | Oui | true<br>false |

### Entrées de référence

Ces emplacements de référence extensibles sont disponibles pour tous les modèles. Le nombre maximal d'emplacements diffère selon le modèle : Seedance 2.5 prend en charge jusqu'à 30 images, 10 vidéos, 10 audios et 30 assets ; Seedance 2.0, 2.0 Fast et 2.0 Mini prennent en charge jusqu'à 9 images, 3 vidéos, 3 audios et 9 assets.

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `reference_images` | Emplacement extensible : connectez 1..N images de référence qui guident la sortie. La limite du nombre dépend du modèle (voir les sections des modèles). Les images sont validées selon leur rapport d'aspect (0,4 à 2,5) et automatiquement réduites à un côté maximal de 6000 pixels. | IMAGE | Non | 1..9 emplacements (famille Seedance 2.0)<br>1..30 emplacements (Seedance 2.5) |
| `reference_videos` | Emplacement extensible : connectez 1..N vidéos de référence. La limite du nombre dépend du modèle (voir les sections des modèles). Chaque vidéo doit durer au moins 1,8 seconde et respecter les limites de pixels du modèle et de la résolution sélectionnés. | VIDEO | Non | 1..3 emplacements (famille Seedance 2.0)<br>1..10 emplacements (Seedance 2.5) |
| `reference_audios` | Emplacement extensible : connectez 1..N pistes audio de référence. La limite du nombre dépend du modèle (voir les sections des modèles). Chaque audio doit durer au moins 1,8 seconde. | AUDIO | Non | 1..3 emplacements (famille Seedance 2.0)<br>1..10 emplacements (Seedance 2.5) |
| `reference_assets` | Emplacement extensible : connectez 1..N chaînes d'ID d'asset pour des médias déjà téléversés dans la bibliothèque virtuelle Seedance. Chaque asset doit être Active. Vous pouvez référencer un asset dans le prompt avec des jetons tels que `asset1` ou `asset 1` ; le nœud les remplace par le libellé positionnel de l'asset (par exemple "Image 2" ou "Video 1"). | STRING | Non | 1..9 emplacements (famille Seedance 2.0)<br>1..30 emplacements (Seedance 2.5) |
| `auto_downscale` | Réduit automatiquement l'échelle des vidéos de référence qui dépassent le budget de pixels du modèle pour la résolution sélectionnée. Le rapport d'aspect est préservé ; les vidéos déjà dans les limites ne sont pas modifiées. Par défaut : True. | BOOLEAN | Non | true<br>false |
| `auto_upscale` | Augmente automatiquement l'échelle des vidéos de référence qui sont en dessous du nombre minimal de pixels du modèle pour la résolution sélectionnée. Le rapport d'aspect est préservé ; les vidéos respectant déjà le minimum ne sont pas modifiées. Remarque : augmenter l'échelle d'une source à basse résolution n'ajoute pas de détail réel et peut produire des générations de moindre qualité. Par défaut : False. Réglage avancé. | BOOLEAN | Non | true<br>false |

**Remarque :** Au moins une image, une vidéo ou un asset de référence est requis pour exécuter le nœud (Seedance 2.5 accepte également les références audio seules). Les vidéos et audios de référence doivent chacun durer au moins 1,8 seconde, et la durée combinée de toutes les vidéos de référence (et séparément, de tous les audios de référence) ne doit pas dépasser le nombre maximal total de secondes du modèle sélectionné. Les images de référence doivent avoir un rapport d'aspect compris entre environ 2:5 et 5:2 (0,4 à 2,5), mesurer au moins 300x300 pixels, et sont automatiquement réduites à un côté maximal de 6000 pixels. Les options `task_type` "edit" et "extend" ne sont disponibles qu'avec Seedance 2.5 et nécessitent toutes deux au moins une vidéo de référence ; lorsque "edit" est utilisé, la sortie conserve la longueur et le rapport d'aspect du clip source et les widgets `duration` et `ratio` sont ignorés, et lorsque "extend" est utilisé, la sortie contient uniquement le segment nouvellement généré à la durée que vous définissez. Les assets référencés doivent être au statut Active, sinon la tâche échoue. Chaque exécution renvoie son ID de tâche en tant que `draft_task_id`, mais seul l'ID d'une exécution `Seedance 2.5 Draft` peut être généré par le nœud ByteDance Seedance 2.5 Draft to Final Video ; avec tout autre modèle, la sortie doit donc rester non connectée, sinon l'exécution échoue.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo générée, téléchargée depuis le fournisseur une fois la tâche de génération terminée. Contient de l'audio lorsque la génération audio est activée. | VIDEO |
| `draft_task_id` | ID de tâche renvoyé par l'exécution. Seule une exécution `Seedance 2.5 Draft` produit un draft que le nœud ByteDance Seedance 2.5 Draft to Final Video peut générer ; avec tout autre modèle, la sortie doit rester non connectée, sinon l'exécution échoue. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNodeV2/fr.md)

---
**Source fingerprint (SHA-256):** `12fee29b280ff71e29f268f52131d1c15cf3066e0804356b735b61d97c80a6a9`
