> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlI2VNode/fr.md)

Voici la traduction en français de la documentation du nœud ComfyUI **KlingCameraControlI2VNode** :

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlI2VNode/en.md)

Le nœud de contrôle de caméra Kling Image to Video transforme des images fixes en vidéos cinématographiques avec des mouvements de caméra professionnels. Ce nœud spécialisé image-vers-vidéo vous permet de contrôler des actions de caméra virtuelle, notamment le zoom, la rotation, le panoramique, l'inclinaison et la vue à la première personne, tout en conservant l'attention sur votre image d'origine. Le contrôle de la caméra est actuellement uniquement pris en charge en mode pro avec le modèle `kling-v1-5` pour une durée de 5 secondes.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `start_frame` | IMAGE | Oui | - | Image de référence - URL ou chaîne encodée en Base64, ne peut pas dépasser 10 Mo, résolution minimale de 300x300 px, rapport hauteur/largeur compris entre 1:2,5 et 2,5:1. Le Base64 ne doit pas inclure le préfixe `data:image`. |
| `prompt` | STRING | Oui | - | Texte d'incitation positif décrivant le contenu vidéo souhaité |
| `negative_prompt` | STRING | Oui | - | Texte d'incitation négatif décrivant ce qu'il faut éviter dans la vidéo générée |
| `cfg_scale` | FLOAT | Non | 0,0 à 1,0 | Contrôle la force du guidage textuel. Des valeurs plus élevées font que la sortie suit plus fidèlement l'incitation (par défaut : 0,75) |
| `aspect_ratio` | COMBO | Non | `"16:9"`<br>`"9:16"`<br>`"1:1"` | Le rapport hauteur/largeur de la vidéo générée (par défaut : "16:9") |
| `camera_control` | CAMERA_CONTROL | Oui | - | Peut être créé à l'aide du nœud Kling Camera Controls. Contrôle le mouvement et le déplacement de la caméra pendant la génération vidéo. |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `video_id` | VIDEO | La sortie vidéo générée |
| `duration` | STRING | Identifiant unique de la vidéo générée |
| `duration` | STRING | Durée de la vidéo générée |

---
**Source fingerprint (SHA-256):** `a2965975cd484768298f4c7e504423f782ea032dfb5ef304579715be9c27cb79`
