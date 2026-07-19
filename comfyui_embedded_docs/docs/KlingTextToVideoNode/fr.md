# Kling Texte en Vidéo

Voici la traduction en français de la documentation du nœud Kling Text to Video :

Le nœud Kling Texte vers Vidéo convertit des descriptions textuelles en contenu vidéo. Il prend des invites textuelles et génère des séquences vidéo correspondantes en fonction des paramètres de configuration spécifiés. Le nœud prend en charge différents ratios d'aspect et modes de génération pour produire des vidéos de durées et qualités variées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | Invite textuelle positive | STRING | Oui | - |
| `negative_prompt` | Invite textuelle négative | STRING | Oui | - |
| `cfg_scale` | Valeur de l'échelle de configuration (par défaut : 1.0) | FLOAT | Non | 0.0 à 1.0 |
| `aspect_ratio` | Réglage du ratio d'aspect de la vidéo (par défaut : "16:9") | COMBO | Non | Options de KlingVideoGenAspectRatio |
| `mode` | Configuration à utiliser pour la génération vidéo suivant le format : mode / durée / nom_du_modèle. (par défaut : modes[8]) | COMBO | Non | Plusieurs options disponibles |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `video_id` | La sortie vidéo générée | VIDEO |
| `video_id` | Identifiant unique de la vidéo générée | STRING |
| `duration` | Informations sur la durée de la vidéo générée | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `467f89a47890bfbfe6cebac8897fef3bce37d888d3419b248d13be89bed442f3`
