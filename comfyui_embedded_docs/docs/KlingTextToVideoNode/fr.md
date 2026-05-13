> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/fr.md)

Voici la traduction en français de la documentation du nœud Kling Text to Video :

Le nœud Kling Texte vers Vidéo convertit des descriptions textuelles en contenu vidéo. Il prend des invites textuelles et génère des séquences vidéo correspondantes en fonction des paramètres de configuration spécifiés. Le nœud prend en charge différents ratios d'aspect et modes de génération pour produire des vidéos de durées et qualités variées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `prompt` | STRING | Oui | - | Invite textuelle positive |
| `negative_prompt` | STRING | Oui | - | Invite textuelle négative |
| `cfg_scale` | FLOAT | Non | 0.0 à 1.0 | Valeur de l'échelle de configuration (par défaut : 1.0) |
| `aspect_ratio` | COMBO | Non | Options de KlingVideoGenAspectRatio | Réglage du ratio d'aspect de la vidéo (par défaut : "16:9") |
| `mode` | COMBO | Non | Plusieurs options disponibles | Configuration à utiliser pour la génération vidéo suivant le format : mode / durée / nom_du_modèle. (par défaut : modes[8]) |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `video_id` | VIDEO | La sortie vidéo générée |
| `duration` | STRING | Identifiant unique de la vidéo générée |
| `duration` | STRING | Informations sur la durée de la vidéo générée |

---
**Source fingerprint (SHA-256):** `467f89a47890bfbfe6cebac8897fef3bce37d888d3419b248d13be89bed442f3`
