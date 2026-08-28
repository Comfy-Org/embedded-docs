# Kling 3.0 Vidéo

Ce nœud génère des vidéos à l'aide du modèle Kling V3. Il prend en charge le mode texte-vers-vidéo, où une vidéo est créée à partir d'une description textuelle, et le mode image-vers-vidéo, où une image existante est animée. Il offre également des fonctionnalités avancées telles que la création de vidéos multi-segments avec des prompts individuels pour chaque partie (storyboards) et la génération facultative d'un audio d'accompagnement.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `multi_shot` | Génère une série de segments vidéo avec des prompts et des durées individuels. Lorsqu'elle est définie sur une option de storyboard, des entrées supplémentaires apparaissent pour le prompt et la durée de chaque storyboard. | DYNAMIC_COMBO | Oui | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `modèle` | Modèle et paramètres de génération. La sélection d'un modèle révèle ses sous-paramètres de résolution et de rapport hauteur/largeur. | DYNAMIC_COMBO | Oui | `"kling-v3"`<br>`"kling-3.0-turbo"` |
| `générer audio` | Lorsqu'il est activé, le nœud génère un audio pour la vidéo. Remarque : `"kling-3.0-turbo"` génère toujours un audio natif, donc ce paramètre est ignoré pour ce modèle. Par défaut : True. | BOOLEAN | Oui | True<br>False |
| `seed` | La graine (seed) contrôle si le nœud doit s'exécuter à nouveau ; les résultats sont non déterministes quelle que soit la graine. Par défaut : 0. | INT | Oui | 0 à 2147483647 |
| `image de départ` | Image facultative pour la première image. Lorsqu'elle est connectée, le nœud passe en mode image-vers-vidéo. | IMAGE | Non | - |

### Entrées kling-v3

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `résolution` | La résolution de la vidéo générée. Par défaut : `"1080p"`. | COMBO | Oui | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `ratio d’aspect` | Le rapport hauteur/largeur de la vidéo générée. Ignoré en mode image-vers-vidéo. | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"` |

### Entrées kling-3.0-turbo

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `résolution` | La résolution de la vidéo générée. Par défaut : `"720p"`. | COMBO | Oui | `"1080p"`<br>`"720p"` |
| `ratio d’aspect` | Le rapport hauteur/largeur de la vidéo générée. Ignoré en mode image-vers-vidéo. | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"` |

### Entrées multi-shot

**Lorsque `multi_shot` est défini sur `"disabled"` :**

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `prompt` | La description textuelle principale de la vidéo. Doit contenir entre 1 et 2500 caractères. | STRING | Oui | 1 à 2500 caractères |
| `negative_prompt` | Texte décrivant ce qui ne doit pas apparaître dans la vidéo. Peut être laissé vide. | STRING | Non | - |
| `duration` | La durée de la vidéo en secondes. Par défaut : 5. | INT | Oui | 3 à 15 |

**Lorsque `multi_shot` est défini sur une option de storyboard (par ex. `"3 storyboards"`) :**

Pour chaque segment de storyboard N (de 1 jusqu'au nombre de storyboards sélectionné), les entrées suivantes apparaissent :

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `storyboard_N_prompt` | Prompt pour le segment de storyboard N. 512 caractères maximum. | STRING | Oui | 1 à 512 caractères |
| `storyboard_N_duration` | Durée du segment de storyboard N en secondes. Par défaut : 4. | INT | Oui | 1 à 15 |

**Contraintes et comportement :**

- Le mode texte-vers-vidéo est utilisé lorsque `start_frame` n'est pas connecté ; le mode image-vers-vidéo est utilisé lorsque `start_frame` est connecté. En mode image-vers-vidéo, `model.aspect_ratio` est ignoré et l'image d'entrée doit faire au moins 300x300 pixels avec un rapport hauteur/largeur compris entre 1:2,5 et 2,5:1.
- En mode storyboard, le `prompt` principal et le `negative_prompt` ne sont pas utilisés. La somme totale de toutes les durées des storyboards doit être comprise entre 3 et 15 secondes.
- `negative_prompt` est uniquement utilisé avec `kling-v3` ; il est ignoré lorsque `kling-3.0-turbo` est sélectionné.
- Pour `kling-v3`, chaque storyboard est envoyé à l'API comme un segment distinct. Pour `kling-3.0-turbo`, les prompts et les durées des storyboards sont combinés en un seul prompt multi-shot.
- Pour `kling-3.0-turbo`, `generate_audio` est ignoré car ce modèle génère toujours un audio natif.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `2863d7a971a1978b6009e5321ed2112a9c04809281acd5f65d85ab72c4b49f08`
