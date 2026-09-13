# ByteDance Seedance 2.5 Référence vers vidéo

Le nœud ByteDance Seedance 2.5 Reference to Video génère, modifie ou étend des vidéos à l’aide des modèles ByteDance Seedance (Seedance 2.5, 2.0, 2.0 Fast et 2.0 Mini), guidé par un prompt texte et éventuellement des images, vidéos, audios de référence ou des ressources de bibliothèque précédemment téléversées. Il téléverse les références, soumet une tâche de génération, attend la fin de celle-ci et renvoie le fichier vidéo final.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Sélecteur de modèle. Seedance 2.5 pour le modèle le plus récent, des vidéos jusqu’à 30 secondes et une sortie mp4/mov ; Seedance 2.0 pour une qualité maximale et la 4k ; Fast pour l’optimisation de la vitesse ; Mini pour la génération la plus rapide et la moins coûteuse. La sélection d’un modèle modifie les widgets d’entrée affichés ci-dessous. | DYNAMIC_COMBO | Oui | "Seedance 2.5"<br>"Seedance 2.0"<br>"Seedance 2.0 Fast"<br>"Seedance 2.0 Mini" |
| `seed` | Le seed contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la valeur du seed. Par défaut : 0. | INT | Oui | 0 à 2147483647 |
| `watermark` | Indique s’il faut ajouter un filigrane à la vidéo. Par défaut : False. Réglage avancé. | BOOLEAN | Oui | true<br>false |

### Entrées Seedance 2.5

Ces entrées apparaissent lorsque `model` est défini sur « Seedance 2.5 ».

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt textuel pour la génération de vidéo. Placez les répliques parlées entre guillemets doubles pour orienter le dialogue généré. Par défaut : chaîne vide. | STRING | Oui | Texte multiligne |
| `resolution` | Résolution de la vidéo de sortie. Par défaut : 720p. | COMBO | Oui | "480p"<br>"720p"<br>"1080p" |
| `ratio` | Format d’image de la vidéo de sortie. Par défaut : 16:9. | COMBO | Oui | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | Durée de la vidéo de sortie en secondes (4-30). Par défaut : 5. | INT | Oui | 4 à 30 |
| `generate_audio` | Active la génération audio pour la vidéo de sortie. Par défaut : True. | BOOLEAN | Oui | true<br>false |
| `task_type` | Action à effectuer avec le média de référence. Toutes les valeurs sauf auto sont validées au moment de la soumission de la tâche, de sorte que les réglages incohérents échouent avant le début de la génération.<br>auto : le modèle déduit la tâche à partir du prompt et des entrées, et les réglages qui entrent en conflit avec son interprétation échouent seulement après le début de la génération.<br>reference : génère une nouvelle vidéo guidée par les images, vidéos et audios de référence.<br>edit : modifie une vidéo de référence connectée (ajouter, supprimer, remplacer) ; la sortie conserve la longueur et le format d’image propres au clip source, et les widgets `duration` et `ratio` sont ignorés.<br>extend : prolonge une vidéo de référence connectée vers l’avant ou vers l’arrière ; le prompt doit indiquer « extend forward », « extend backward » ou « continue », le format d’image suit le clip source, et la sortie contient uniquement le segment nouvellement généré correspondant à la durée que vous avez définie, et non le clip source. Par défaut : auto. | COMBO | Oui | "auto"<br>"reference"<br>"edit"<br>"extend" |
| `output_format` | Format de conteneur de la vidéo de sortie. Par défaut : mp4. | COMBO | Oui | "mp4" |

### Entrées Seedance 2.0

Ces entrées apparaissent lorsque `model` est défini sur « Seedance 2.0 ».

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt textuel pour la génération de vidéo. Par défaut : chaîne vide. | STRING | Oui | Texte multiligne |
| `resolution` | Résolution de la vidéo de sortie. | COMBO | Oui | "480p"<br>"720p"<br>"1080p"<br>"4k" |
| `ratio` | Format d’image de la vidéo de sortie. Par défaut : adaptive. | COMBO | Oui | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | Durée de la vidéo de sortie en secondes (4-15). Par défaut : 7. | INT | Oui | 4 à 15 |
| `generate_audio` | Active la génération audio pour la vidéo de sortie. Par défaut : True. | BOOLEAN | Oui | true<br>false |

### Entrées Seedance 2.0 Fast et Seedance 2.0 Mini

Ces entrées apparaissent lorsque `model` est défini sur « Seedance 2.0 Fast » ou « Seedance 2.0 Mini ». Les deux modèles partagent le même ensemble d’entrées.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt textuel pour la génération de vidéo. Par défaut : chaîne vide. | STRING | Oui | Texte multiligne |
| `resolution` | Résolution de la vidéo de sortie. | COMBO | Oui | "480p"<br>"720p" |
| `ratio` | Format d’image de la vidéo de sortie. Par défaut : adaptive. | COMBO | Oui | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | Durée de la vidéo de sortie en secondes (4-15). Par défaut : 7. | INT | Oui | 4 à 15 |
| `generate_audio` | Active la génération audio pour la vidéo de sortie. Par défaut : True. | BOOLEAN | Oui | true<br>false |

### Entrées de référence

Ces emplacements de référence extensibles sont disponibles pour tous les modèles. Le nombre maximal d’emplacements diffère selon le modèle : Seedance 2.5 prend en charge jusqu’à 30 images, 10 vidéos, 10 audios et 30 ressources ; Seedance 2.0, 2.0 Fast et 2.0 Mini prennent en charge jusqu’à 9 images, 3 vidéos, 3 audios et 9 ressources.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `reference_images` | Emplacement extensible : connectez 1..N images de référence qui guident la sortie. La limite de nombre dépend du modèle (voir les sections des modèles). Les images sont validées selon leur format d’image (0,4 à 2,5) et automatiquement réduites à une dimension maximale de 6000 pixels. | IMAGE | Non | 1..9 emplacements (famille Seedance 2.0)<br>1..30 emplacements (Seedance 2.5) |
| `reference_videos` | Emplacement extensible : connectez 1..N vidéos de référence. La limite de nombre dépend du modèle (voir les sections des modèles). Chaque vidéo doit durer au moins 1,8 seconde et doit respecter les limites de pixels pour le modèle et la résolution sélectionnés. | VIDEO | Non | 1..3 emplacements (famille Seedance 2.0)<br>1..10 emplacements (Seedance 2.5) |
| `reference_audios` | Emplacement extensible : connectez 1..N pistes audio de référence. La limite de nombre dépend du modèle (voir les sections des modèles). Chaque audio doit durer au moins 1,8 seconde. | AUDIO | Non | 1..3 emplacements (famille Seedance 2.0)<br>1..10 emplacements (Seedance 2.5) |
| `reference_assets` | Emplacement extensible : connectez 1..N chaînes d’ID de ressource pour des médias déjà téléversés dans la bibliothèque virtuelle Seedance. Chaque ressource doit être Active. Vous pouvez faire référence à une ressource dans le prompt avec des jetons tels que `asset1` ou `asset 1` ; le nœud les remplace par le libellé positionnel de la ressource (par exemple « Image 2 » ou « Video 1 »). | STRING | Non | 1..9 emplacements (famille Seedance 2.0)<br>1..30 emplacements (Seedance 2.5) |
| `auto_downscale` | Réduit automatiquement l’échelle des vidéos de référence qui dépassent le budget de pixels du modèle pour la résolution sélectionnée. Le format d’image est conservé ; les vidéos déjà dans les limites ne sont pas modifiées. Par défaut : True. | BOOLEAN | Non | true<br>false |
| `auto_upscale` | Augmente automatiquement l’échelle des vidéos de référence qui sont en dessous du nombre minimal de pixels du modèle pour la résolution sélectionnée. Le format d’image est conservé ; les vidéos respectant déjà le minimum ne sont pas modifiées. Remarque : l’augmentation d’échelle d’une source basse résolution n’ajoute pas de détail réel et peut produire des générations de moindre qualité. Par défaut : False. Réglage avancé. | BOOLEAN | Non | true<br>false |

**Note :** Au moins une image, une vidéo ou une ressource de référence est nécessaire pour exécuter le nœud (Seedance 2.5 accepte également les références audio seules). Les vidéos et audios de référence doivent chacun durer au moins 1,8 seconde, et la durée combinée de toutes les vidéos de référence (et séparément, de tous les audios de référence) ne doit pas dépasser la durée totale maximale en secondes du modèle sélectionné. Les images de référence doivent avoir un format d’image compris entre environ 2:5 et 5:2 (0,4 à 2,5), mesurer au moins 300x300 pixels, et sont automatiquement réduites à une dimension maximale de 6000 pixels. Les options `task_type` « edit » et « extend » ne sont disponibles qu’avec Seedance 2.5 et nécessitent toutes deux au moins une vidéo de référence ; lorsque « edit » est utilisé, la sortie conserve la longueur et le format d’image propres au clip source et les widgets `duration` et `ratio` sont ignorés ; lorsque « extend » est utilisé, la sortie contient uniquement le segment nouvellement généré à la durée que vous avez définie. Les ressources référencées doivent être au statut Active, sinon la tâche échoue.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo générée, téléchargée depuis le fournisseur une fois la tâche de génération terminée. Contient l’audio lorsque la génération audio est activée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNodeV2/fr.md)

---
**Source fingerprint (SHA-256):** `3a6bba12e719204ba5dba9d7d5f2b4c5285ed68974ee015b6e4a7892a1cf0933`
