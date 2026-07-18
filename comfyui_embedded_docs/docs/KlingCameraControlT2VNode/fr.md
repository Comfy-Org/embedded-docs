Voici la traduction en français de la documentation du nœud **Kling Text to Video Camera Control** :

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlT2VNode/en.md)

**Nœud de contrôle de caméra Kling Text to Video**  
Transforme du texte en vidéos cinématographiques avec des mouvements de caméra professionnels simulant la cinématographie réelle. Ce nœud permet de contrôler des actions de caméra virtuelle, notamment le zoom, la rotation, le panoramique, l’inclinaison et la vue à la première personne, tout en restant fidèle à votre texte d’origine. La durée, le mode et le nom du modèle sont codés en dur, car le contrôle de la caméra n’est pris en charge qu’en mode pro avec le modèle `kling-v1-5` pour une durée de 5 secondes.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | Texte d’invite positif | STRING | Oui | - |
| `negative_prompt` | Texte d’invite négatif | STRING | Oui | - |
| `cfg_scale` | Contrôle la fidélité de la sortie par rapport à l’invite (par défaut : 0.75) | FLOAT | Non | 0.0-1.0 |
| `aspect_ratio` | Le rapport hauteur/largeur de la vidéo générée (par défaut : "16:9") | COMBO | Non | "16:9"<br>"9:16"<br>"1:1"<br>"21:9"<br>"3:4"<br>"4:3" |
| `camera_control` | Peut être créé à l’aide du nœud Kling Camera Controls. Contrôle le mouvement et le déplacement de la caméra pendant la génération de la vidéo. | CAMERA_CONTROL | Non | - |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `video_id` | La vidéo générée avec les effets de contrôle de caméra | VIDEO |
| `video_id` | L’identifiant unique de la vidéo générée | STRING |
| `duration` | La durée de la vidéo générée | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlT2VNode/fr.md)

---
**Source fingerprint (SHA-256):** `4ebdd6af31f9e5c0816c4bcba886179b3f7d2b5030ff4fa3ddad6df25c528af7`
