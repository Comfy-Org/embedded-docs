> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImage2VideoNode/fr.md)

Le nœud Kling Image to Video génère du contenu vidéo à partir d'une image de départ en utilisant des invites textuelles. Il prend une image de référence et crée une séquence vidéo basée sur les descriptions textuelles positives et négatives fournies, avec diverses options de configuration pour la sélection du modèle, la durée et le format d'image.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `start_frame` | IMAGE | Oui | - | L'image de référence utilisée pour générer la vidéo. |
| `prompt` | STRING | Oui | - | L'invite textuelle positive. |
| `negative_prompt` | STRING | Oui | - | L'invite textuelle négative. |
| `model_name` | COMBO | Oui | Plusieurs options disponibles | Sélection du modèle pour la génération de vidéo (par défaut : "kling-v2-master"). |
| `cfg_scale` | FLOAT | Oui | 0.0-1.0 | Paramètre d'échelle de configuration (par défaut : 0.8). |
| `mode` | COMBO | Oui | Plusieurs options disponibles | Sélection du mode de génération de vidéo (par défaut : std). |
| `aspect_ratio` | COMBO | Oui | Plusieurs options disponibles | Format d'image pour la vidéo générée (par défaut : field_16_9). |
| `duration` | COMBO | Oui | Plusieurs options disponibles | Durée de la vidéo générée (par défaut : field_5). |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `video_id` | VIDEO | La sortie vidéo générée. |
| `duration` | STRING | Identifiant unique pour la vidéo générée. |
| `duration` | STRING | Informations sur la durée de la vidéo générée. |