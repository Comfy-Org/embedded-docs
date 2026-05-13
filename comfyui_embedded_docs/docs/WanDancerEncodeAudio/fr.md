> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerEncodeAudio/fr.md)

Voici la traduction en français de la documentation technique du nœud ComfyUI :

## Aperçu

Ce nœud traite une entrée audio pour en extraire des caractéristiques pouvant être utilisées pour guider un modèle de génération vidéo. Il analyse l'audio afin de détecter le tempo, les battements et autres caractéristiques musicales, puis regroupe ces informations dans un format adapté au conditionnement d'un modèle vidéo, permettant ainsi de synchroniser la vidéo générée avec l'audio.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `audio` | AUDIO | Oui | - | L'entrée audio à analyser et encoder. |
| `video_frames` | INT | Oui | Min : 1, Max : 268435456 (MAX_RESOLUTION), Pas : 4 | Le nombre d'images dans la vidéo cible. Utilisé pour calculer la fréquence d'images pour la synchronisation (par défaut : 149). |
| `audio_inject_scale` | FLOAT | Oui | Min : 0.0, Max : 10.0, Pas : 0.01 | L'échelle des caractéristiques audio lors de leur injection dans le modèle vidéo (par défaut : 1.0). |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `fps_string` | AUDIO_ENCODER_OUTPUT | Un dictionnaire contenant les caractéristiques audio traitées, la fréquence d'images calculée (fps) et l'échelle d'injection audio. Cette sortie est utilisée pour conditionner le modèle de génération vidéo. |
| `fps_string` | STRING | Une chaîne de texte décrivant la fréquence d'images calculée (fps) en fonction de la durée audio et du nombre d'images vidéo. Cette chaîne est destinée à être utilisée dans le prompt du modèle vidéo. |

---
**Source fingerprint (SHA-256):** `ef230c92b23a04369708041b2e5d03c1b2928edf746dc43020bae777f9f0b589`
