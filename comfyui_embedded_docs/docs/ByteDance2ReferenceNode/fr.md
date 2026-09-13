# ByteDance Seedance 2.5 Référence vers vidéo (hérité)

Ce nœud génère, modifie ou étend des vidéos à l'aide des modèles IA Seedance 2.5 ou Seedance 2.0 de ByteDance. Vous décrivez la vidéo dans une invite textuelle et pouvez joindre des images, vidéos et audio de référence pour guider le résultat, avec prise en charge des références multimodales, de l'édition vidéo et de l'extension vidéo. Il s'agit de la version héritée et obsolète du nœud Seedance de référence vers vidéo.

## Entrées

La sélection d'un `model` détermine lesquels des paramètres ci-dessous sont disponibles. `video_editing` et `output_format` n'apparaissent que lorsque Seedance 2.5 est sélectionné. Les emplacements de référence extensibles et les options de redimensionnement automatique des vidéos de référence sont partagés par tous les modèles et sont décrits dans la section Entrées de référence.

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle d'IA utilisé pour générer la vidéo. Seedance 2.5 pour le modèle le plus récent, des vidéos jusqu'à 30 secondes et une sortie mp4/mov ; Seedance 2.0 pour une qualité maximale et la 4k ; Fast pour l'optimisation de la vitesse ; Mini pour la génération la plus rapide et la moins coûteuse. La sélection d'un modèle révèle les entrées spécifiques au modèle listées ci-dessous. | DYNAMIC_COMBO | Oui | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine (par défaut : 0). | INT | Oui | 0 à 2147483647<br>Pas : 1 |
| `watermark` | Indique s'il faut ajouter un filigrane à la vidéo (par défaut : False). Paramètre avancé. | BOOLEAN | Oui | `True`<br>`False` |

### Entrées Seedance 2.5

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite textuelle pour la génération de la vidéo. Placez les répliques parlées entre guillemets doubles pour orienter le dialogue généré. Doit contenir au moins un caractère non blanc (par défaut : vide). | STRING | Oui | Texte quelconque |
| `resolution` | Résolution de la vidéo de sortie (par défaut : `"720p"`). | COMBO | Oui | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `ratio` | Rapport d'aspect de la vidéo de sortie (par défaut : `"16:9"`). | COMBO | Oui | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Durée de la vidéo de sortie en secondes (par défaut : 5). | INT | Oui | 4 à 30<br>Pas : 1 |
| `generate_audio` | Activer la génération audio pour la vidéo de sortie (par défaut : True). | BOOLEAN | Oui | `True`<br>`False` |
| `video_editing` | Activez lorsque l'invite modifie une vidéo de référence connectée, par exemple en remplaçant un objet qu'elle contient. La sortie conserve alors la longueur et le rapport d'aspect du clip source, et les widgets `duration` et `ratio` sont ignorés. Laissez désactivé pour générer une nouvelle vidéo, ou pour en étendre une jusqu'à la durée que vous définissez (par défaut : False). | BOOLEAN | Oui | `True`<br>`False` |
| `output_format` | Format de conteneur de la vidéo de sortie (par défaut : `"mp4"`). | COMBO | Oui | `"mp4"` |

### Entrées Seedance 2.0

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite textuelle pour la génération de la vidéo. Doit contenir au moins un caractère non blanc (par défaut : vide). | STRING | Oui | Texte quelconque |
| `resolution` | Résolution de la vidéo de sortie. | COMBO | Oui | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Rapport d'aspect de la vidéo de sortie (par défaut : `"adaptive"`). | COMBO | Oui | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Durée de la vidéo de sortie en secondes (par défaut : 7). | INT | Oui | 4 à 15<br>Pas : 1 |
| `generate_audio` | Activer la génération audio pour la vidéo de sortie (par défaut : True). | BOOLEAN | Oui | `True`<br>`False` |

### Entrées Seedance 2.0 Fast et Seedance 2.0 Mini

Partagées par Seedance 2.0 Fast et Seedance 2.0 Mini. Ces deux modèles exposent le même ensemble d'entrées que Seedance 2.0, sauf que `resolution` est limitée à 480p et 720p.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite textuelle pour la génération de la vidéo. Doit contenir au moins un caractère non blanc (par défaut : vide). | STRING | Oui | Texte quelconque |
| `resolution` | Résolution de la vidéo de sortie. | COMBO | Oui | `"480p"`<br>`"720p"` |
| `ratio` | Rapport d'aspect de la vidéo de sortie (par défaut : `"adaptive"`). | COMBO | Oui | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Durée de la vidéo de sortie en secondes (par défaut : 7). | INT | Oui | 4 à 15<br>Pas : 1 |
| `generate_audio` | Activer la génération audio pour la vidéo de sortie (par défaut : True). | BOOLEAN | Oui | `True`<br>`False` |

### Entrées de référence

Disponibles pour tous les modèles. Le nombre maximal d'emplacements dépend du modèle sélectionné : Seedance 2.5 prend en charge plus de références que les modèles Seedance 2.0.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `reference_images` | Emplacement extensible : connectez une ou plusieurs images de référence (`image_1`, `image_2`, ...) qui guident la génération de la vidéo. Les images sont automatiquement réduites à une dimension maximale de 6000 pixels et doivent faire au moins 300x300 pixels avec un rapport d'aspect compris entre 0,4 et 2,5. | IMAGE | Non | Jusqu'à 30 (Seedance 2.5)<br>Jusqu'à 9 (modèles Seedance 2.0) |
| `reference_videos` | Emplacement extensible : connectez une ou plusieurs vidéos de référence (`video_1`, `video_2`, ...) qui guident la génération de la vidéo ; utilisées pour l'édition et l'extension vidéo. | VIDEO | Non | Jusqu'à 10 (Seedance 2.5)<br>Jusqu'à 3 (modèles Seedance 2.0) |
| `reference_audios` | Emplacement extensible : connectez un ou plusieurs clips audio de référence (`audio_1`, `audio_2`, ...) qui guident la génération de la vidéo. | AUDIO | Non | Jusqu'à 10 (Seedance 2.5)<br>Jusqu'à 3 (modèles Seedance 2.0) |
| `auto_downscale` | Réduit automatiquement l'échelle des vidéos de référence qui dépassent le budget de pixels du modèle pour la résolution sélectionnée. Le rapport d'aspect est préservé ; les vidéos déjà dans les limites ne sont pas modifiées (par défaut : True). | BOOLEAN | Non | `True`<br>`False` |
| `auto_upscale` | Paramètre avancé. Agrandit automatiquement l'échelle des vidéos de référence qui sont en dessous du nombre minimal de pixels du modèle pour la résolution sélectionnée. Le rapport d'aspect est préservé ; les vidéos respectant déjà le minimum ne sont pas modifiées. Remarque : l'agrandissement d'une source à basse résolution n'ajoute pas de détail réel et peut produire des générations de moindre qualité (par défaut : False). | BOOLEAN | Non | `True`<br>`False` |
| `reference_assets` | Emplacement extensible : ID d'assets de la bibliothèque virtuelle Seedance précédemment créés (Image, Video ou Audio) à utiliser comme références (`asset_1`, `asset_2`, ...). Chaque asset doit exister et avoir un statut Active. Dans l'invite, les assets peuvent être référencés par `asset1`, `asset 1`, etc. ; le nœud remplace ces jetons par des libellés tels que « Image 2 ». | STRING | Non | Jusqu'à 30 (Seedance 2.5)<br>Jusqu'à 9 (modèles Seedance 2.0) |

**Contraintes importantes :**

* Au moins une référence est requise. Pour Seedance 2.0, 2.0 Fast et 2.0 Mini, vous devez fournir au moins une référence image ou vidéo (via `reference_images`, `reference_videos`, ou une entrée image ou vidéo dans `reference_assets`). Seedance 2.5 accepte en plus les références audio uniquement (via `reference_audios` ou une entrée audio dans `reference_assets`).
* Les nombres de références dépendent du modèle et sont validés en combinant les entrées directes et les références d'assets : Seedance 2.5 autorise jusqu'à 30 `reference_images`, 10 `reference_videos`, 10 `reference_audios` et 30 `reference_assets` ; les modèles Seedance 2.0 autorisent jusqu'à 9 images, 3 vidéos, 3 clips audio et 9 assets.
* Chaque vidéo de référence doit durer au moins 1,8 seconde, et chaque clip audio de référence doit durer au moins 1,8 seconde. La durée totale de toutes les vidéos de référence et de tous les audios de référence doit rester dans la limite du modèle sélectionné (15,1 secondes pour les modèles Seedance 2.0).
* Les vidéos de référence doivent également respecter les limites de nombre de pixels du modèle pour la résolution sélectionnée. Avec `auto_downscale` activé (par défaut), les vidéos surdimensionnées sont automatiquement redimensionnées ; avec `auto_upscale` activé, les vidéos sous-dimensionnées sont agrandies. Si l'un ou l'autre des ajustements automatiques est désactivé, les vidéos en dehors de la limite correspondante génèrent une erreur.
* Lorsque `video_editing` est activé sur Seedance 2.5, les entrées `duration` et `ratio` sont ignorées ; la sortie correspond à la longueur et au rapport d'aspect propres à la vidéo de référence. Si le fournisseur interprète l'invite comme une édition d'une vidéo de référence, la génération échoue, sauf si `video_editing` est activé ou si l'invite est reformulée pour décrire une nouvelle vidéo.
* Si le fournisseur rejette la piste audio générée pour la vidéo (par exemple, une correspondance possible avec des droits d'auteur), la tâche échoue ; désactiver `generate_audio` produit une vidéo silencieuse.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/fr.md)

---
**Source fingerprint (SHA-256):** `4a1b62f65ff3515cdb749c9b3916e631e53523fe144e8cdf71ca020825196ae6`
