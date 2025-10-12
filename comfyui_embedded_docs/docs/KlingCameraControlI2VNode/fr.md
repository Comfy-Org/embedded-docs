> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlI2VNode/fr.md)

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `start_frame` | IMAGE | Oui | - | Image de référence - URL ou chaîne encodée en Base64, ne peut pas dépasser 10 Mo, résolution non inférieure à 300*300 px, ratio d'aspect entre 1:2,5 ~ 2,5:1. Base64 ne doit pas inclure le préfixe data:image. |
| `prompt` | STRING | Oui | - | Prompt texte positif |
| `negative_prompt` | STRING | Oui | - | Prompt texte négatif |
| `cfg_scale` | FLOAT | Non | 0,0-1,0 | Contrôle l'intensité du guidage par le texte (par défaut : 0,75) |
| `aspect_ratio` | COMBO | Non | Plusieurs options disponibles | Sélection du ratio d'aspect de la vidéo (par défaut : 16:9) |
| `camera_control` | CAMERA_CONTROL | Oui | - | Peut être créé en utilisant le nœud Kling Camera Controls. Contrôle le mouvement et l'animation de la caméra pendant la génération de la vidéo. |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `video_id` | VIDEO | La vidéo générée en sortie |
| `duration` | STRING | Identifiant unique pour la vidéo générée |
| `duration` | STRING | Durée de la vidéo générée |