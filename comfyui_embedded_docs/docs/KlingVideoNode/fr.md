# Kling 3.0 Vidéo

Ce nœud génère des vidéos avec le modèle Kling V3. Il prend en charge le texte-vers-vidéo, où une vidéo est créée à partir d'une description textuelle, et l'image-vers-vidéo, où une image existante est animée. Il peut également créer des vidéos multi-segments à l'aide d'invites de storyboard et générer facultativement de l'audio.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `multi_shot` | Générer une série de segments vidéo avec des invites et des durées individuelles. Lorsqu'il est défini sur une option de storyboard, des entrées supplémentaires pour l'invite et la durée de chaque storyboard apparaissent. | DYNAMIC_COMBO | Oui | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `generate_audio` | Lorsqu'activé, le nœud génère de l'audio pour la vidéo. Remarque : `"kling-3.0-turbo"` génère toujours de l'audio natif, donc l'option audio est ignorée pour ce modèle. La valeur par défaut est True. | BOOLEAN | Oui | True<br>False |
| `model` | Modèle et paramètres de génération. La sélection d'un modèle révèle ses sous-paramètres de résolution et de rapport d'aspect. | DYNAMIC_COMBO | Oui | `"kling-v3"`<br>`"kling-3.0-turbo"` |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. La valeur par défaut est 0. | INT | Oui | 0 à 2147483647 |
| `start_frame` | Image de début facultative. Lorsqu'elle est connectée, bascule en mode image-vers-vidéo. | IMAGE | Non | - |

### Entrées kling-v3

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model.resolution` | La résolution de la vidéo générée. La valeur par défaut est `"1080p"`. | COMBO | Oui | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `model.aspect_ratio` | Le rapport d'aspect de la vidéo générée. Ignoré en mode image-vers-vidéo. | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"` |

### Entrées kling-3.0-turbo

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model.resolution` | La résolution de la vidéo générée. La valeur par défaut est `"720p"`. | COMBO | Oui | `"1080p"`<br>`"720p"` |
| `model.aspect_ratio` | Le rapport d'aspect de la vidéo générée. Ignoré en mode image-vers-vidéo. | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"` |

### Entrées multi-plans

**Lorsque `multi_shot` est défini sur `"disabled"` :**

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Description textuelle principale de la vidéo. Doit contenir entre 1 et 2500 caractères. | STRING | Oui | 1 à 2500 caractères |
| `negative_prompt` | Texte décrivant ce qui ne doit pas apparaître dans la vidéo. Peut être laissé vide. | STRING | Non | - |
| `duration` | Durée de la vidéo en secondes. La valeur par défaut est 5. | INT | Oui | 3 à 15 |

**Lorsque `multi_shot` est défini sur une option de storyboard (par ex. `"3 storyboards"`) :**

Pour chaque segment de storyboard N (de 1 jusqu'au nombre de storyboards sélectionné), les entrées suivantes apparaissent :

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `storyboard_N_prompt` | Invite pour le segment de storyboard N. 512 caractères max. | STRING | Oui | 1 à 512 caractères |
| `storyboard_N_duration` | Durée du segment de storyboard N en secondes. La valeur par défaut est 4. | INT | Oui | 1 à 15 |

**Contraintes et comportement :**

- Le mode texte-vers-vidéo est utilisé lorsque `start_frame` n'est pas connecté ; le mode image-vers-vidéo est utilisé lorsque `start_frame` est connecté. En mode image-vers-vidéo, `model.aspect_ratio` est ignoré et l'image d'entrée doit mesurer au moins 300x300 pixels avec un rapport d'aspect compris entre 1:2.5 et 2.5:1.
- En mode storyboard, les paramètres `prompt` principal et `negative_prompt` ne sont pas utilisés. La somme totale de toutes les durées de storyboard doit être comprise entre 3 et 15 secondes.
- `negative_prompt` n'est utilisé qu'avec `kling-v3` ; il est ignoré lorsque `kling-3.0-turbo` est sélectionné.
- Pour `kling-v3`, chaque storyboard est envoyé à l'API en tant que segment distinct. Pour `kling-3.0-turbo`, les invites et durées des storyboards sont combinées en une seule invite multi-plans.
- Pour `kling-3.0-turbo`, `generate_audio` est ignoré car ce modèle génère toujours de l'audio natif.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `2863d7a971a1978b6009e5321ed2112a9c04809281acd5f65d85ab72c4b49f08`
