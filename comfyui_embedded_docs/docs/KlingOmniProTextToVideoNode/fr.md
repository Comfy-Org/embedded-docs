# Kling Omni Texte vers Vidéo (Pro)

Ce nœud utilise le dernier modèle Kling AI pour générer une vidéo à partir d'une description textuelle. Il envoie votre invite à une API distante et renvoie la vidéo générée. Le nœud vous permet de contrôler la longueur, la forme, la qualité de la vidéo, et même de créer des storyboards multi-plans.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_name` | Le modèle Kling spécifique à utiliser pour la génération de vidéos (par défaut : `"kling-v3-omni"`). | COMBO | Oui | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | Une invite textuelle décrivant le contenu de la vidéo. Elle peut inclure des descriptions à la fois positives et négatives. Ignorée lorsque les storyboards sont activés. | STRING | Oui | 0 à 2500 caractères |
| `aspect_ratio` | La forme ou les dimensions de la vidéo à générer. | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | La durée de la vidéo en secondes (par défaut : 5). | INT | Oui | 3 à 15 secondes |
| `resolution` | La qualité ou la résolution en pixels de la vidéo (par défaut : `"1080p"`). | COMBO | Non | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `storyboards` | Génère une série de segments vidéo avec des invites et des durées individuelles. Ignoré pour le modèle o1. | DYNAMIC_COMBO | Non | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `générer l'audio` | Indique s'il faut générer de l'audio pour la vidéo (par défaut : False). | BOOLEAN | Non | True / False |
| `seed` | Le seed contrôle si le nœud doit s'exécuter à nouveau ; les résultats sont non déterministes quel que soit le seed (par défaut : 0). | INT | Non | 0 à 2147483647 |

### Sous-entrées du storyboard

Lorsque `storyboards` est défini sur une valeur autre que `"disabled"`, les entrées suivantes apparaissent pour chaque segment de storyboard. Dans les noms de paramètres ci-dessous, `{i}` est le numéro du segment, de 1 jusqu'au nombre de storyboards sélectionné.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `storyboard_{i}_prompt` | Invite pour le segment de storyboard {i}. Maximum 512 caractères. | STRING | Oui | 1 à 512 caractères |
| `storyboard_{i}_duration` | Durée du segment de storyboard {i} en secondes (par défaut : 4). | INT | Oui | 1 à 15 secondes |

### Contraintes et limites des paramètres

- **Limites spécifiques au modèle :**
  - Le modèle `kling-video-o1` ne prend en charge que des durées de **5 ou 10 secondes**.
  - Le modèle `kling-video-o1` ne prend **pas** en charge la génération audio.
  - Le modèle `kling-video-o1` ne prend **pas** en charge la résolution 4k.
  - Le modèle `kling-video-o1` ne prend **pas** en charge les storyboards.
- **Contraintes des storyboards :**
  - Lorsque les storyboards sont activés, le champ `prompt` est ignoré.
  - Chaque storyboard nécessite sa propre invite (1 à 512 caractères) et sa propre durée.
  - La durée totale de tous les storyboards doit être exactement égale au paramètre global `duration`.
- **Exigences relatives à l'invite :**
  - Lorsque les storyboards sont **désactivés**, le champ `prompt` est obligatoire (minimum 1 caractère).
  - Lorsque les storyboards sont **activés**, le champ `prompt` peut être vide (0 caractère).

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La vidéo générée à partir de l'invite textuelle et des paramètres fournis. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProTextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `d2fbbe7c6aae283eb3fa7f73d788b809098a9a4dd6e8ada54697d43fd5bf10f2`
