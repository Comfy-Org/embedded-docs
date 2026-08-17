# WanDancerEncodeAudio

Ce nœud traite une entrée audio pour extraire des caractéristiques pouvant être utilisées pour guider un modèle de génération vidéo. Il analyse l’audio afin de détecter le tempo, les battements et d’autres caractéristiques musicales, puis regroupe ces informations dans un format adapté au conditionnement d’un modèle vidéo, permettant ainsi de synchroniser la vidéo générée avec l’audio.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `audio` | L’entrée audio à analyser et à encoder. | AUDIO | Oui | - |
| `video_frames` | Le nombre d’images de la vidéo cible. Utilisé pour calculer la fréquence d’images (fps) pour la synchronisation (défaut : 149). | INT | Oui | Min : 1, Max : 268435456 (MAX_RESOLUTION), Step : 4 |
| `audio_inject_scale` | L’échelle des caractéristiques audio lors de leur injection dans le modèle vidéo (défaut : 1.0). | FLOAT | Oui | Min : 0.0, Max : 10.0, Step : 0.01 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `audio_encoder_output` | Un dictionnaire contenant les caractéristiques audio traitées, la fréquence d’images calculée (fps) et l’échelle d’injection audio. Cette sortie est utilisée pour conditionner le modèle de génération vidéo. | AUDIO_ENCODER_OUTPUT |
| `fps_string` | Une chaîne de caractères décrivant la fréquence d’images calculée (fps) en fonction de la durée de l’audio et du nombre d’images de la vidéo. Cette chaîne est destinée à être utilisée dans le prompt du modèle vidéo. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerEncodeAudio/fr.md)

---
**Source fingerprint (SHA-256):** `ce27a3bdea2d9e3cf8875c24236a2a0a1429e9bc13a58581e372fb669d2c0018`
