> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlT2VNode/fr.md)

## Entrées

| Paramètre | Type de données | Obligatoire | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | - | Prompt texte positif |
| `negative_prompt` | STRING | Oui | - | Prompt texte négatif |
| `cfg_scale` | FLOAT | Non | 0.0-1.0 | Contrôle à quel point la sortie suit fidèlement le prompt (par défaut : 0.75) |
| `aspect_ratio` | COMBO | Non | "16:9"<br>"9:16"<br>"1:1"<br>"21:9"<br>"3:4"<br>"4:3" | Le ratio d'aspect pour la vidéo générée (par défaut : "16:9") |
| `camera_control` | CAMERA_CONTROL | Non | - | Peut être créé en utilisant le nœud Kling Camera Controls. Contrôle le mouvement et la trajectoire de la caméra pendant la génération de la vidéo. |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | La vidéo générée avec les effets de contrôle de caméra |
| `video_id` | STRING | L'identifiant unique de la vidéo générée |
| `duration` | STRING | La durée de la vidéo générée |

Le nœud Kling Text to Video Camera Control transforme du texte en vidéos cinématographiques avec des mouvements de caméra professionnels qui simulent une cinématographie réelle. Ce nœud permet de contrôler les actions de caméra virtuelle incluant le zoom, la rotation, le panoramique, l'inclinaison et la vue à la première personne, tout en maintenant la focalisation sur votre texte original. La durée, le mode et le nom du modèle sont codés en dur car le contrôle de caméra n'est pris en charge qu'en mode pro avec le modèle kling-v1-5 pour une durée de 5 secondes.