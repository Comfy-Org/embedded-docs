# Kling Image to Video

Le nœud Kling Image to Video génère une vidéo à partir d'une image de référence initiale en utilisant des invites textuelles. Il utilise l'image comme première image et crée une séquence vidéo basée sur des descriptions textuelles positives et négatives, avec des options configurables pour le modèle, la durée, le mode de génération et le rapport hauteur/largeur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `start_frame` | L'image de référence utilisée pour générer la vidéo. Elle doit faire au moins 300x300 pixels avec un rapport hauteur/largeur compris entre 1:2.5 et 2.5:1. | IMAGE | Oui | - |
| `prompt` | Invite de texte positive. Maximum 500 caractères. | STRING | Oui | - |
| `negative_prompt` | Invite de texte négative. Maximum 500 caractères. Peut être laissée vide. | STRING | Oui | - |
| `model_name` | Le modèle utilisé pour la génération de la vidéo (par défaut : `"kling-v2-5-turbo"`). | COMBO | Oui | `"kling-v2-5-turbo"` |
| `cfg_scale` | Contrôle à quel point la vidéo respecte l'invite. Des valeurs plus élevées indiquent un respect plus fort (par défaut : 0.8). | FLOAT | Oui | 0.0 à 1.0 |
| `mode` | Le mode de génération (par défaut : `"pro"`). | COMBO | Oui | `"pro"` |
| `aspect_ratio` | Le rapport hauteur/largeur de la vidéo générée (par défaut : `"16:9"`). | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | La durée de la vidéo générée en secondes (par défaut : `"5"`). | COMBO | Oui | `"5"`<br>`"10"` |

Remarque : L'invite positive ne doit pas être vide. Les invites positive et négative sont limitées à 500 caractères. L'image d'entrée doit faire au moins 300x300 pixels et avoir un rapport hauteur/largeur compris entre 1:2.5 et 2.5:1.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La vidéo générée. | VIDEO |
| `video_id` | Identifiant unique de la vidéo générée. | STRING |
| `duration` | Durée de la vidéo générée. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImage2VideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `f4a461819bc05f92d867bddcc78a66ad7beaa10707ef8cae3e7eb9e6f72c890a`
