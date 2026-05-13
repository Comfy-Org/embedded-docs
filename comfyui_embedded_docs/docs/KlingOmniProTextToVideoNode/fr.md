> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProTextToVideoNode/fr.md)

Ce nœud utilise le dernier modèle d'IA Kling pour générer une vidéo à partir d'une description textuelle. Il envoie votre prompt à une API distante et retourne la vidéo générée. Le nœud vous permet de contrôler la durée, le format, la qualité de la vidéo, et même de créer des storyboards multi-plans.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model_name` | COMBO | Oui | `"kling-v3-omni"`<br>`"kling-video-o1"` | Le modèle Kling spécifique à utiliser pour la génération vidéo (par défaut : `"kling-v3-omni"`). |
| `prompt` | STRING | Oui | 0 à 2500 caractères | Un prompt textuel décrivant le contenu de la vidéo. Peut inclure des descriptions positives et négatives. Ignoré lorsque les storyboards sont activés. |
| `aspect_ratio` | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"` | Le format ou les dimensions de la vidéo à générer. |
| `duration` | INT | Oui | 3 à 15 secondes | La durée de la vidéo en secondes (par défaut : 5). |
| `resolution` | COMBO | Non | `"4k"`<br>`"1080p"`<br>`"720p"` | La qualité ou la résolution en pixels de la vidéo (par défaut : `"1080p"`). |
| `storyboards` | DYNAMIC_COMBO | Non | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` | Génère une série de segments vidéo avec des prompts et durées individuels. Ignoré pour le modèle o1. |
| `générer l'audio` | BOOLEAN | Non | Vrai / Faux | Indique s'il faut générer l'audio pour la vidéo (par défaut : Faux). |
| `seed` | INT | Non | 0 à 2147483647 | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine (par défaut : 0). |

### Contraintes et limitations des paramètres

- **Limitations spécifiques au modèle :**
  - Le modèle `kling-video-o1` ne prend en charge que des durées de **5 ou 10 secondes**.
  - Le modèle `kling-video-o1` ne prend **pas** en charge la génération audio.
  - Le modèle `kling-video-o1` ne prend **pas** en charge la résolution 4k.
  - Le modèle `kling-video-o1` ne prend **pas** en charge les storyboards.
- **Contraintes des storyboards :**
  - Lorsque les storyboards sont activés, le champ `prompt` est ignoré.
  - Chaque storyboard nécessite son propre prompt (1 à 512 caractères) et sa propre durée.
  - La durée totale de tous les storyboards doit être exactement égale au paramètre global `duration`.
- **Exigences du prompt :**
  - Lorsque les storyboards sont **désactivés**, le champ `prompt` est requis (minimum 1 caractère).
  - Lorsque les storyboards sont **activés**, le champ `prompt` peut être vide (0 caractères).

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `output` | VIDEO | La vidéo générée en fonction du prompt textuel fourni et des paramètres. |

---
**Source fingerprint (SHA-256):** `2f867e0bd2e7b0ec901a9ad8d2adcfe712ed479c1613b80f86af3a20863e9f4c`
