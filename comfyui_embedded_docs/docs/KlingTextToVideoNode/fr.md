> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/fr.md)

Le nœud Kling Text to Video convertit des descriptions textuelles en contenu vidéo. Il prend des invites textuelles et génère des séquences vidéo correspondantes basées sur les paramètres de configuration spécifiés. Le nœud prend en charge différents ratios d'aspect et modes de génération pour produire des vidéos de durées et qualités variables.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | - | Invite textuelle positive (par défaut : aucune) |
| `negative_prompt` | STRING | Oui | - | Invite textuelle négative (par défaut : aucune) |
| `cfg_scale` | FLOAT | Non | 0.0-1.0 | Valeur d'échelle de configuration (par défaut : 1.0) |
| `aspect_ratio` | COMBO | Non | Options de KlingVideoGenAspectRatio | Paramètre du ratio d'aspect de la vidéo (par défaut : "16:9") |
| `mode` | COMBO | Non | Plusieurs options disponibles | La configuration à utiliser pour la génération de vidéo suivant le format : mode / durée / nom_du_modèle. (par défaut : modes[4]) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | La vidéo générée en sortie |
| `video_id` | STRING | Identifiant unique pour la vidéo générée |
| `duration` | STRING | Information de durée pour la vidéo générée |