# Kling Image to Video

Le nœud Kling Image to Video génère une courte vidéo en utilisant une image de départ comme première image. Il combine l'image avec des invites de texte et des paramètres de génération, puis renvoie la vidéo résultante ainsi que son identifiant et sa durée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `start_frame` | L'image de référence utilisée pour générer la vidéo. L'image doit avoir au moins 300x300 pixels et un rapport hauteur/largeur compris entre 1:2.5 et 2.5:1. | IMAGE | Oui | - |
| `prompt` | Invite de texte positive. Ne doit pas être vide. 500 caractères maximum. | STRING | Oui | - |
| `negative_prompt` | Invite de texte négative. 500 caractères maximum. Laisser vide si non utilisé. | STRING | Oui | - |
| `model_name` | Le modèle utilisé pour la génération de la vidéo (par défaut : `"kling-v2-5-turbo"`). | COMBO | Oui | `"kling-v2-5-turbo"` |
| `cfg_scale` | Contrôle à quel point la vidéo suit l'invite. Des valeurs plus élevées signifient une adhérence plus forte (par défaut : 0.8). | FLOAT | Oui | 0.0 à 1.0 |
| `mode` | Le mode de génération (par défaut : `"pro"`). | COMBO | Oui | `"pro"` |
| `aspect_ratio` | Le rapport hauteur/largeur de la vidéo générée (par défaut : `"16:9"`). | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | La durée de la vidéo générée en secondes (par défaut : `"5"`). | COMBO | Oui | `"5"`<br>`"10"` |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La sortie vidéo générée. | VIDEO |
| `video_id` | Identifiant unique de la vidéo générée. | STRING |
| `duration` | Informations sur la durée de la vidéo générée. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImage2VideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `f4a461819bc05f92d867bddcc78a66ad7beaa10707ef8cae3e7eb9e6f72c890a`
