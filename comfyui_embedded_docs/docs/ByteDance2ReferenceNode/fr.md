# ByteDance Seedance 2.0 Référence vers Vidéo

Ce nœud génère, édite ou étend des vidéos à l'aide des modèles d'IA Seedance 2.5 ou 2.0 de ByteDance. Vous décrivez la vidéo dans une invite textuelle et pouvez ajouter des images, des vidéos et de l'audio de référence pour guider le résultat. Il prend en charge les entrées de référence multimodales, l'édition vidéo et l'extension vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `model` | Le modèle d'IA utilisé pour générer la vidéo. Seedance 2.5 est le modèle le plus récent, avec des vidéos jusqu'à 30 secondes et une sortie mp4/mov ; Seedance 2.0 est conçu pour une qualité maximale et 1080p/4k ; Fast est pour l'optimisation de la vitesse ; Mini est pour la génération la plus rapide et la moins coûteuse. La sélection d'un modèle révèle les entrées spécifiques au modèle listées ci-dessous. | COMBO | Oui | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | Le seed contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quel que soit le seed (par défaut : 0). | INT | Oui | 0 à 2147483647 |
| `watermark` | Indique s'il faut ajouter un filigrane à la vidéo (par défaut : False). | BOOLEAN | Oui | `True`<br>`False` |
| `prompt` | Invite textuelle pour la génération de vidéo. Pour Seedance 2.5, placez les répliques entre guillemets pour orienter le dialogue généré. Doit contenir au moins un caractère non blanc. | STRING | Oui | Any text |
| `resolution` | Résolution de la vidéo de sortie. Seedance 2.5, 2.0 Fast et 2.0 Mini offrent 480p et 720p ; Seedance 2.0 offre également 1080p et 4k (par défaut pour Seedance 2.5 : 720p). | COMBO | Oui | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Ratio d'aspect de la vidéo de sortie (par défaut pour Seedance 2.5 : `"16:9"` ; par défaut pour les modèles Seedance 2.0 : `"adaptive"`). | COMBO | Oui | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Durée de la vidéo de sortie en secondes (Seedance 2.5 : 4-30, par défaut 5 ; modèles Seedance 2.0 : 4-15, par défaut 7). | INT | Oui | 4 à 30 (Seedance 2.5)<br>4 à 15 (Seedance 2.0)<br>Step: 1 |
| `generate_audio` | Active la génération audio pour la vidéo de sortie (par défaut : True). | BOOLEAN | Oui | `True`<br>`False` |
| `video_editing` | Réservé à Seedance 2.5. À activer lorsque l'invite modifie une vidéo de référence connectée, par exemple pour remplacer un objet dans celle-ci. La sortie conserve alors la longueur et le ratio d'aspect de la source, et les widgets de durée et de ratio sont ignorés. Laissez désactivé pour générer une nouvelle vidéo, ou pour étendre une vidéo jusqu'à la durée définie (par défaut : False). | BOOLEAN | Oui | `True`<br>`False` |
| `output_format` | Réservé à Seedance 2.5. Format de conteneur de la vidéo de sortie (par défaut : `"mp4"`). | COMBO | Oui | `"mp4"` |
| `reference_images` | Images de référence qui guident la génération de la vidéo. Les images sont automatiquement réduites à un côté maximum de 6000 pixels et doivent faire au moins 300x300 pixels avec un ratio d'aspect compris entre 0,4 et 2,5. | IMAGE | Non | Up à 30 (Seedance 2.5)<br>Up à 9 (Seedance 2.0) |
| `reference_videos` | Vidéos de référence qui guident la génération de la vidéo ; utilisées pour l'édition et l'extension vidéo. | VIDEO | Non | Up à 10 (Seedance 2.5)<br>Up à 3 (Seedance 2.0) |
| `reference_audios` | Fichiers audio de référence qui guident la génération de la vidéo. | AUDIO | Non | Up à 10 (Seedance 2.5)<br>Up à 3 (Seedance 2.0) |
| `auto_downscale` | Réduit automatiquement les vidéos de référence qui dépassent le budget de pixels du modèle pour la résolution sélectionnée. Le ratio d'aspect est préservé ; les vidéos déjà dans les limites ne sont pas modifiées (par défaut : True). | BOOLEAN | Non | `True`<br>`False` |
| `auto_upscale` | Agrandit automatiquement les vidéos de référence qui sont en dessous du nombre minimal de pixels du modèle pour la résolution sélectionnée. Le ratio d'aspect est préservé ; les vidéos atteignant déjà le minimum ne sont pas modifiées. Remarque : l'agrandissement d'une source en basse résolution n'ajoute pas de détails réels et peut produire des générations de qualité inférieure (par défaut : False). | BOOLEAN | Non | `True`<br>`False` |
| `reference_assets` | Identifiants de ressources de la bibliothèque virtuelle Seedance préalablement créées (image, vidéo ou audio) à utiliser comme références. Chaque ressource doit exister et avoir un statut Actif. Dans l'invite, les ressources peuvent être désignées comme asset1, asset 2, etc. ; le nœud remplace ces jetons par des étiquettes telles que Image 2. | STRING | Non | Up à 30 (Seedance 2.5)<br>Up à 9 (Seedance 2.0) |

**Contraintes importantes :**

* Au moins une référence est requise. Pour Seedance 2.0, 2.0 Fast et 2.0 Mini, vous devez fournir au moins une référence image ou vidéo (via `reference_images`, `reference_videos`, ou une entrée `reference_assets` de type image/vidéo). Seedance 2.5 accepte en plus les références audio uniquement.
* Les nombres de références dépendent du modèle : Seedance 2.5 permet jusqu'à 30 `reference_images`, 10 `reference_videos`, 10 `reference_audios` et 30 `reference_assets` ; les modèles Seedance 2.0 permettent jusqu'à 9 images, 3 vidéos, 3 clips audio et 9 ressources. Les totaux sont comptés en combinant les entrées directes et les références de ressources, et sont validés avant la génération.
* Chaque vidéo de référence doit durer au moins 1,8 seconde, et chaque clip audio de référence doit durer au moins 1,8 seconde. La durée totale de toutes les vidéos de référence et de tous les clips audio de référence doit rester dans la limite du modèle sélectionné (15,1 secondes pour les modèles Seedance 2.0).
* Les vidéos de référence doivent également respecter les limites de nombre de pixels du modèle pour la résolution sélectionnée. Avec `auto_downscale` activé (par défaut), les vidéos trop grandes sont automatiquement redimensionnées ; avec `auto_upscale` activé, les vidéos trop petites sont agrandies. Si l'une de ces adaptations automatiques est désactivée, les vidéos hors limite correspondante génèrent une erreur.
* Lorsque `video_editing` est activé sur Seedance 2.5, les entrées `duration` et `ratio` sont ignorées ; la sortie correspond à la longueur et au ratio d'aspect de la vidéo de référence.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `video` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/fr.md)

---
**Source fingerprint (SHA-256):** `4429306ac40b0f04ce7176cd805b34164de5e4e2b7204b008ea076b57663c200`
