# WanDancerEncodeAudio

Ce nœud analyse un clip audio et le transforme en un ensemble de caractéristiques pouvant guider un modèle de génération vidéo. Il estime le tempo et les battements, extrait le mel-spectrogramme, les MFCC, la chroma et les caractéristiques d'onset, puis les regroupe avec une fréquence d'images calculée pour la synchronisation.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `audio` | L'entrée audio à analyser et encoder. Si l'audio comporte plusieurs canaux, les canaux sont moyennés en mono avant l'extraction des caractéristiques. | AUDIO | Oui | - |
| `video_frames` | Le nombre d'images dans la vidéo cible. Utilisé pour calculer la fréquence d'images pour la synchronisation (par défaut : 149). | INT | Oui | Min : 1, Max : 16384 (MAX_RESOLUTION), Pas : 4 |
| `audio_inject_scale` | L'échelle des caractéristiques audio lorsqu'elles sont injectées dans le modèle vidéo (par défaut : 1.0). | FLOAT | Oui | Min : 0.0, Max : 10.0, Pas : 0.01 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `audio_encoder_output` | Un dictionnaire contenant les caractéristiques audio traitées, la fréquence d'images calculée (fps) et l'échelle d'injection audio. Cette sortie est utilisée pour conditionner le modèle de génération vidéo. | AUDIO_ENCODER_OUTPUT |
| `fps_string` | Une chaîne de texte décrivant la fréquence d'images calculée (fps) en fonction de la longueur de l'audio et du nombre d'images vidéo. Cette chaîne est destinée à être utilisée dans le prompt du modèle vidéo. Elle est formatée en chinois pour correspondre au pipeline de référence. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerEncodeAudio/fr.md)

---
**Source fingerprint (SHA-256):** `ce27a3bdea2d9e3cf8875c24236a2a0a1429e9bc13a58581e372fb669d2c0018`
