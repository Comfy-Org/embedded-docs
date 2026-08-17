# ByteDance Seedance 2.0 Première-Dernière-Image vers Vidéo

Ce nœud génère une vidéo à partir d’une première image obligatoire et d’une dernière image facultative à l’aide des modèles ByteDance Seedance 2.5 ou Seedance 2.0. La première image définit le début du clip, la dernière image (si fournie) définit la fin, et une invite textuelle décrit le mouvement. Le modèle sélectionné contrôle les résolutions, durées et options de format de sortie disponibles.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `model` | Le modèle utilisé pour la génération de vidéos. Seedance 2.5 est le modèle le plus récent, avec des vidéos jusqu’à 30 secondes et une sortie mp4/mov ; Seedance 2.0 offre une qualité maximale et du 1080p/4k ; Fast est optimisé pour la vitesse ; Mini est la génération la plus rapide et la moins coûteuse. La sélection d’un modèle révèle ses entrées spécifiques ci-dessous. | DYNAMIC_COMBO | Oui | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `first_frame` | Première image de la vidéo. L’un de `first_frame` ou `first_frame_asset_id` est requis. | IMAGE | Non | - |
| `last_frame` | Dernière image de la vidéo. | IMAGE | Non | - |
| `first_frame_asset_id` | asset_id Seedance à utiliser comme première image. Mutuellement exclusif avec l’entrée d’image `first_frame`. La valeur par défaut est une chaîne vide. | STRING | Non | - |
| `last_frame_asset_id` | asset_id Seedance à utiliser comme dernière image. Mutuellement exclusif avec l’entrée d’image `last_frame`. La valeur par défaut est une chaîne vide. | STRING | Non | - |
| `seed` | Le seed contrôle si le nœud doit s’exécuter à nouveau ; les résultats sont non déterministes quel que soit le seed. La valeur par défaut est 0. | INT | Non | 0 à 2147483647 |
| `watermark` | Indique s’il faut ajouter un filigrane à la vidéo. La valeur par défaut est False. | BOOLEAN | Non | - |

### Entrées Seedance 2.5

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Invite textuelle pour la génération de la vidéo. Placez les répliques prononcées entre guillemets pour orienter le dialogue généré. La valeur par défaut est une chaîne vide. | STRING | Oui | - |
| `resolution` | Résolution de la vidéo de sortie. La valeur par défaut est « 720p ». | COMBO | Oui | `"480p"`<br>`"720p"` |
| `duration` | Durée de la vidéo de sortie en secondes (4-30). La valeur par défaut est 5. | INT | Oui | 4 à 30 |
| `generate_audio` | Active la génération audio pour la vidéo de sortie. La valeur par défaut est True. | BOOLEAN | Oui | - |
| `output_format` | Format de conteneur de la vidéo de sortie. La valeur par défaut est « mp4 ». | COMBO | Oui | `"mp4"` |

### Entrées Seedance 2.0

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Invite textuelle pour la génération de la vidéo. La valeur par défaut est une chaîne vide. | STRING | Oui | - |
| `resolution` | Résolution de la vidéo de sortie. | COMBO | Oui | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Format d’image de la vidéo de sortie. La valeur par défaut est « adaptive ». | COMBO | Oui | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Durée de la vidéo de sortie en secondes (4-15). La valeur par défaut est 7. | INT | Oui | 4 à 15 |
| `generate_audio` | Active la génération audio pour la vidéo de sortie. La valeur par défaut est True. | BOOLEAN | Oui | - |

### Partagées par Seedance 2.0 Fast et Seedance 2.0 Mini

Ces deux modèles exposent les mêmes entrées que Seedance 2.0, sauf que seules les résolutions 480p et 720p sont disponibles.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Invite textuelle pour la génération de la vidéo. La valeur par défaut est une chaîne vide. | STRING | Oui | - |
| `resolution` | Résolution de la vidéo de sortie. | COMBO | Oui | `"480p"`<br>`"720p"` |
| `ratio` | Format d’image de la vidéo de sortie. La valeur par défaut est « adaptive ». | COMBO | Oui | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Durée de la vidéo de sortie en secondes (4-15). La valeur par défaut est 7. | INT | Oui | 4 à 15 |
| `generate_audio` | Active la génération audio pour la vidéo de sortie. La valeur par défaut est True. | BOOLEAN | Oui | - |

**Contraintes et limitations :**

*   Le `prompt` est requis et doit contenir au moins un caractère non blanc (les espaces de début et de fin sont ignorés).
*   Vous devez fournir exactement une source de première image : soit l’image `first_frame`, soit le `first_frame_asset_id`. Fournir les deux génère une erreur, et n’en fournir aucun génère également une erreur.
*   L’image `last_frame` et le `last_frame_asset_id` sont mutuellement exclusifs. Les deux peuvent être omis.
*   Les asset_id doivent référencer des assets Seedance existants avec un statut Active. Si un asset n’est pas actif ou n’est pas un asset Image, une erreur est générée.
*   Les images locales doivent avoir un format d’image compris entre 0,4 et 2,5 (2:5 à 5:2).
*   Pour les modèles Seedance 2.0, les images locales doivent avoir au moins 300 x 300 pixels. Elles sont automatiquement redimensionnées aux dimensions de sortie exactes prises en charge pour la résolution et le format sélectionnés, et la requête est soumise avec le format « adaptive ». Lorsque `ratio` est « adaptive », le format d’image de sortie est dérivé du format d’image de la première image, arrondi au format pris en charge le plus proche. Lorsque des asset_id sont utilisés au lieu d’images locales, la valeur `ratio` sélectionnée est appliquée directement.
*   Pour Seedance 2.5, et pour tout modèle lorsque des asset_id sont utilisés, les images sont automatiquement réduites à un côté maximal de 6000 pixels et doivent avoir entre 300 et 6000 pixels dans chaque dimension.
*   Seedance 2.5 conserve toujours le format d’image de la première image, donc aucune entrée `ratio` n’est affichée pour ce modèle.
*   Les limites de durée varient selon le modèle : Seedance 2.5 prend en charge de 4 à 30 secondes, tandis que Seedance 2.0, 2.0 Fast et 2.0 Mini prennent en charge de 4 à 15 secondes.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `output` | La vidéo générée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/fr.md)

---
**Source fingerprint (SHA-256):** `d87265eb75d67f7d80f76474fc699f7ca87b6edbddda36733d5e440708b074a2`
