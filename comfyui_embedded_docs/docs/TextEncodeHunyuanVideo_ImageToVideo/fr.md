# TextEncodeHunyuanVideo_ImageToVideo

Le nœud `TextEncodeHunyuanVideo_ImageToVideo` crée des données de conditionnement pour la génération image-vers-vidéo en combinant une invite textuelle avec des informations visuelles provenant d'une image de référence. Il utilise un modèle CLIP pour traiter à la fois le texte et les embeddings d'image issus d'une sortie de vision CLIP, puis génère des jetons qui fusionnent ces deux sources selon le paramètre `image_interleave`.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP utilisé pour la tokenisation et l'encodage. | CLIP | Oui | - |
| `sortie_vision_clip` | Les embeddings visuels d'un modèle de vision CLIP qui fournissent le contexte d'image pour l'image de référence. | CLIP_VISION_OUTPUT | Oui | - |
| `invite` | La description textuelle pour guider la génération vidéo. Prend en charge la saisie multiligne et les invites dynamiques. L'invite est formatée à l'aide d'un modèle qui demande au modèle de décrire la vidéo en fonction de l'image de référence, couvrant des aspects comme le contenu principal, les détails des objets, les actions, l'arrière-plan et les angles de caméra. | STRING | Oui | - |
| `entrelacement_image` | Degré d'influence de l'image par rapport à l'invite textuelle. Un nombre plus élevé signifie une plus grande influence de l'invite textuelle. (défaut : 2) | INT | Oui | 1-512 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | Les données de conditionnement qui combinent les informations textuelles et d'image pour la génération vidéo. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeHunyuanVideo_ImageToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `016b87ead6f7a6ca61eff220e57f59252018cc78e80ec8cff5b83223b8f90f73`
