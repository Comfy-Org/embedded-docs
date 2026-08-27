# ByteDance Seedance 2.0 Référence vers Vidéo

Ce nœud génère, édite ou étend des vidéos à l’aide des modèles d’IA Seedance 2.5 ou 2.0 de ByteDance. Vous décrivez la vidéo dans une invite texte et pouvez ajouter des images, des vidéos et des fichiers audio de référence pour guider le résultat. Il prend en charge les entrées de référence multimodales, l’édition vidéo et l’extension vidéo. Il s’agit de la version héritée et dépréciée du nœud Seedance de référence vers vidéo.

## Entrées

La sélection d’un `model` détermine lesquels des paramètres ci-dessous sont disponibles. `video_editing` et `output_format` n’apparaissent que lorsque Seedance 2.5 est sélectionné. Les emplacements de référence extensibles et les options de redimensionnement automatique des vidéos de référence sont communs à tous les modèles et sont décrits sous Entrées de référence.

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle d’IA utilisé pour générer la vidéo. Seedance 2.5 pour le modèle le plus récent, vidéos jusqu’à 30 secondes et sortie mp4/mov ; Seedance 2.0 pour une qualité maximale et la 4k ; Fast pour l’optimisation de la vitesse ; Mini pour la génération la plus rapide et la moins coûteuse. La sélection d’un modèle révèle les entrées spécifiques au modèle listées ci-dessous. | DYNAMIC_COMBO | Oui | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | `seed` contrôle si le nœud doit s’exécuter à nouveau ; les résultats sont non déterministes quel que soit le seed (par défaut : 0). | INT | Oui | 0 à 2147483647<br>Pas : 1 |
| `filigrane` | Indique s’il faut ajouter un filigrane à la vidéo (par défaut : False). Réglage avancé. | BOOLEAN | Oui | `True`<br>`False` |

### Entrées Seedance 2.5

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite texte pour la génération de vidéo. Placez les répliques parlées entre guillemets pour orienter le dialogue généré. Doit contenir au moins un caractère non blanc (par défaut : vide). | STRING | Oui | Texte quelconque |
| `resolution` | Résolution de la vidéo de sortie (par défaut : `"720p"`). | COMBO | Oui | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `ratio` | Ratio d’aspect de la vidéo de sortie (par défaut : `"16:9"`). | COMBO | Oui | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Durée de la vidéo de sortie en secondes (par défaut : 5). | INT | Oui | 4 à 30<br>Pas : 1 |
| `generate_audio` | Activer la génération audio pour la vidéo de sortie (par défaut : True). | BOOLEAN | Oui | `True`<br>`False` |
| `video_editing` | Activer lorsque l’invite modifie une vidéo de référence connectée, par exemple en remplaçant un objet dans celle-ci. La sortie conserve alors la durée et le ratio d’aspect propres au clip source, et les widgets durée et ratio sont ignorés. Laissez désactivé pour générer une nouvelle vidéo ou pour en étendre une jusqu’à la durée définie (par défaut : False). | BOOLEAN | Oui | `True`<br>`False` |
| `output_format` | Format conteneur de la vidéo de sortie (par défaut : `"mp4"`). | COMBO | Oui | `"mp4"` |

### Entrées Seedance 2.0

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite texte pour la génération de vidéo. Doit contenir au moins un caractère non blanc (par défaut : vide). | STRING | Oui | Texte quelconque |
| `resolution` | Résolution de la vidéo de sortie. | COMBO | Oui | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Ratio d’aspect de la vidéo de sortie (par défaut : `"adaptive"`). | COMBO | Oui | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Durée de la vidéo de sortie en secondes (par défaut : 7). | INT | Oui | 4 à 15<br>Pas : 1 |
| `generate_audio` | Activer la génération audio pour la vidéo de sortie (par défaut : True). | BOOLEAN | Oui | `True`<br>`False` |

### Entrées Seedance 2.0 Fast et Seedance 2.0 Mini

Partagées par Seedance 2.0 Fast et Seedance 2.0 Mini. Ces deux modèles exposent le même ensemble d’entrées que Seedance 2.0, sauf que `resolution` est limitée à 480p et 720p.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite texte pour la génération de vidéo. Doit contenir au moins un caractère non blanc (par défaut : vide). | STRING | Oui | Texte quelconque |
| `resolution` | Résolution de la vidéo de sortie. | COMBO | Oui | `"480p"`<br>`"720p"` |
| `ratio` | Ratio d’aspect de la vidéo de sortie (par défaut : `"adaptive"`). | COMBO | Oui | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Durée de la vidéo de sortie en secondes (par défaut : 7). | INT | Oui | 4 à 15<br>Pas : 1 |
| `generate_audio` | Activer la génération audio pour la vidéo de sortie (par défaut : True). | BOOLEAN | Oui | `True`<br>`False` |

### Entrées de référence

Disponibles pour tous les modèles. Le nombre maximal d’emplacements dépend du modèle sélectionné : Seedance 2.5 prend en charge plus de références que les modèles Seedance 2.0.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `reference_images` | Emplacement extensible : connectez une ou plusieurs images de référence (`image_1`, `image_2`, ...) qui guident la génération de la vidéo. Les images sont automatiquement réduites à une dimension maximale de 6000 pixels et doivent faire au moins 300x300 pixels avec un ratio d’aspect entre 0,4 et 2,5. | IMAGE | Non | Jusqu’à 30 (Seedance 2.5)<br>Jusqu’à 9 (modèles Seedance 2.0) |
| `reference_videos` | Emplacement extensible : connectez une ou plusieurs vidéos de référence (`video_1`, `video_2`, ...) qui guident la génération de la vidéo ; utilisées pour l’édition et l’extension vidéo. | VIDEO | Non | Jusqu’à 10 (Seedance 2.5)<br>Jusqu’à 3 (modèles Seedance 2.0) |
| `reference_audios` | Emplacement extensible : connectez un ou plusieurs clips audio de référence (`audio_1`, `audio_2`, ...) qui guident la génération de la vidéo. | AUDIO | Non | Jusqu’à 10 (Seedance 2.5)<br>Jusqu’à 3 (modèles Seedance 2.0) |
| `auto_downscale` | Réduit automatiquement les vidéos de référence qui dépassent le budget de pixels du modèle pour la résolution sélectionnée. Le ratio d’aspect est préservé ; les vidéos déjà dans les limites ne sont pas modifiées (par défaut : True). | BOOLEAN | Non | `True`<br>`False` |
| `auto_upscale` | Réglage avancé. Agrandit automatiquement les vidéos de référence qui sont sous le nombre minimal de pixels du modèle pour la résolution sélectionnée. Le ratio d’aspect est préservé ; les vidéos qui respectent déjà le minimum ne sont pas modifiées. Remarque : agrandir une source basse résolution n’ajoute pas de véritable détail et peut produire des générations de qualité inférieure (par défaut : False). | BOOLEAN | Non | `True`<br>`False` |
| `reference_assets` | Emplacement extensible : identifiants d’actifs Seedance de bibliothèque virtuelle précédemment créés (Image, Video ou Audio) à utiliser comme références (`asset_1`, `asset_2`, ...). Chaque actif doit exister et avoir un statut Actif. Dans l’invite, les actifs peuvent être référencés comme `asset1`, `asset 1`, etc. ; le nœud remplace ces jetons par des libellés tels que « Image 2 ». | STRING | Non | Jusqu’à 30 (Seedance 2.5)<br>Jusqu’à 9 (modèles Seedance 2.0) |

**Contraintes importantes :**

* Au moins une référence est requise. Pour Seedance 2.0, 2.0 Fast et 2.0 Mini, vous devez fournir au moins une référence image ou vidéo (via `reference_images`, `reference_videos`, ou une entrée image ou vidéo dans `reference_assets`). Seedance 2.5 accepte en outre les références audio uniquement (via `reference_audios` ou une entrée audio dans `reference_assets`).
* Les nombres de références dépendent du modèle et sont validés en combinant les entrées directes et les références d’actifs : Seedance 2.5 permet jusqu’à 30 `reference_images`, 10 `reference_videos`, 10 `reference_audios` et 30 `reference_assets` ; les modèles Seedance 2.0 permettent jusqu’à 9 images, 3 vidéos, 3 clips audio et 9 actifs.
* Chaque vidéo de référence doit durer au moins 1,8 seconde, et chaque clip audio de référence doit durer au moins 1,8 seconde. La durée totale de toutes les vidéos de référence et de tous les audio de référence doit rester dans la limite du modèle sélectionné (15,1 secondes pour les modèles Seedance 2.0).
* Les vidéos de référence doivent également respecter les limites de pixels du modèle pour la résolution sélectionnée. Avec `auto_downscale` activé (par défaut), les vidéos trop grandes sont automatiquement redimensionnées ; avec `auto_upscale` activé, les vidéos trop petites sont agrandies. Si l’un des ajustements automatiques est désactivé, les vidéos hors limite correspondante génèrent une erreur.
* Lorsque `video_editing` est activé sur Seedance 2.5, les entrées `duration` et `ratio` sont ignorées ; la sortie correspond à la durée et au ratio d’aspect propres à la vidéo de référence. Si le fournisseur interprète l’invite comme une édition d’une vidéo de référence, la génération échoue à moins que `video_editing` soit activé ou que l’invite soit reformulée pour décrire une nouvelle vidéo.
* Si le fournisseur rejette la piste audio générée pour la vidéo (par exemple, une correspondance de droits d’auteur possible), la tâche échoue ; désactiver `generate_audio` produit une vidéo silencieuse.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/fr.md)

---
**Source fingerprint (SHA-256):** `4a1b62f65ff3515cdb749c9b3916e631e53523fe144e8cdf71ca020825196ae6`
