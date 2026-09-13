# Kling Omni Texte vers Vidéo (Pro)

Ce nœud génère une vidéo à partir d'une description textuelle en utilisant le dernier modèle Kling AI. Il envoie votre prompt à une API distante et renvoie la vidéo générée. Vous pouvez contrôler la longueur, la forme et la qualité de la vidéo, et éventuellement construire des storyboards multi-plans.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_name` | Le modèle Kling spécifique à utiliser pour la génération vidéo (par défaut : `"kling-v3-omni"`). | COMBO | Oui | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | Un prompt textuel décrivant le contenu de la vidéo. Il peut inclure à la fois des descriptions positives et négatives. Ignoré lorsque les storyboards sont activés. | STRING | Oui | 0 à 2500 caractères |
| `aspect_ratio` | La forme ou les dimensions de la vidéo à générer. | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | La longueur de la vidéo en secondes (par défaut : 5). | INT | Oui | 3 à 15 secondes |
| `resolution` | La qualité ou la résolution en pixels de la vidéo (par défaut : `"1080p"`). Correspond en interne à une qualité standard, pro ou 4k. | COMBO | Non | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `storyboards` | Générer une série de segments vidéo avec des prompts et des durées individuels. Ignoré pour le modèle o1. | DYNAMIC_COMBO | Non | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `generate_audio` | Indique s'il faut générer de l'audio pour la vidéo (par défaut : False). | BOOLEAN | Non | True / False |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine (par défaut : 0). | INT | Non | 0 à 2147483647 |

### Sous-entrées de storyboard

Lorsque `storyboards` est défini sur une valeur autre que `"disabled"`, les entrées suivantes apparaissent pour chaque segment de storyboard. Dans les noms de paramètres ci-dessous, `{i}` correspond au numéro du segment, de 1 jusqu'au nombre de storyboards sélectionné.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `storyboard_{i}_prompt` | Prompt pour le segment de storyboard {i}. 512 caractères max. | STRING | Oui | 1 à 512 caractères |
| `storyboard_{i}_duration` | Durée du segment de storyboard {i} en secondes (par défaut : 4). | INT | Oui | 1 à 15 secondes |

### Contraintes et limitations des paramètres

- **Limitations propres au modèle :**
  - Le modèle `kling-video-o1` ne prend en charge que des durées de **5 ou 10 secondes**.
  - Le modèle `kling-video-o1` ne prend **pas** en charge la génération audio.
  - Le modèle `kling-video-o1` ne prend **pas** en charge la résolution 4k.
  - Le modèle `kling-video-o1` ne prend **pas** en charge les storyboards.
- **Contraintes des storyboards :**
  - Lorsque les storyboards sont activés, le champ `prompt` est ignoré.
  - Chaque storyboard nécessite son propre prompt (1 à 512 caractères) et sa propre durée.
  - La durée totale de tous les storyboards doit être exactement égale au paramètre global `duration`.
- **Exigences relatives au prompt :**
  - Lorsque les storyboards sont **désactivés**, le champ `prompt` est requis (minimum 1 caractère).
  - Lorsque les storyboards sont **activés**, le champ `prompt` peut être vide (0 caractère).

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La vidéo générée en fonction du prompt textuel et des paramètres fournis. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProTextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `d2fbbe7c6aae283eb3fa7f73d788b809098a9a4dd6e8ada54697d43fd5bf10f2`
