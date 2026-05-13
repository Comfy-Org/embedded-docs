> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImage2VideoNode/fr.md)

Voici la traduction en français de la documentation du nœud ComfyUI Kling Image to Video :

Le nœud Kling Image to Video génère une vidéo à partir d'une image de référence initiale en utilisant des invites textuelles. Il prend une image comme première image et crée une séquence vidéo basée sur des descriptions textuelles positives et négatives, avec des options configurables pour le modèle, la durée, le rapport hauteur/largeur et le mode de génération.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `start_frame` | IMAGE | Oui | - | L'image de référence utilisée pour générer la vidéo. |
| `prompt` | STRING | Oui | - | Invite textuelle positive. |
| `negative_prompt` | STRING | Oui | - | Invite textuelle négative. |
| `model_name` | COMBO | Oui | `"kling-v2-master"`<br>`"kling-v2-1-master"`<br>`"kling-v2-5-turbo"`<br>`"kling-v2-1"`<br>`"kling-v1-6"`<br>`"kling-v1-5"`<br>`"kling-v1-4"`<br>`"kling-v1-0"` | Le modèle utilisé pour la génération vidéo (par défaut : `"kling-v2-master"`). |
| `cfg_scale` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la fidélité de la vidéo à l'invite. Des valeurs plus élevées signifient une adhérence plus forte (par défaut : 0.8). |
| `mode` | COMBO | Oui | `"std"`<br>`"pro"` | Le mode de génération. `"std"` correspond à une qualité standard, `"pro"` à une qualité supérieure (par défaut : `"std"`). |
| `aspect_ratio` | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"` | Le rapport hauteur/largeur de la vidéo générée (par défaut : `"16:9"`). |
| `duration` | COMBO | Oui | `"5"`<br>`"10"` | La durée de la vidéo générée en secondes (par défaut : `"5"`). |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `video_id` | VIDEO | La sortie vidéo générée. |
| `duration` | STRING | Identifiant unique pour la vidéo générée. |
| `duration` | STRING | Informations sur la durée de la vidéo générée. |

---
**Source fingerprint (SHA-256):** `2f82997307265dba6714733523e265d1e0a25fd7491b043f05d7d000b7b9b2f3`
