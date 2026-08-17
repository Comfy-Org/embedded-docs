# TextEncodeHunyuanVideo_ImageToVideo

Le nœud `TextEncodeHunyuanVideo_ImageToVideo` crée des données de conditionnement pour la génération vidéo en combinant des invites textuelles avec des embeddings d'image. Il utilise un modèle CLIP pour traiter à la fois l'entrée textuelle et les informations visuelles issues d'une sortie CLIP vision, puis génère des tokens qui fusionnent ces deux sources selon le réglage d'interleave d'image spécifié.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP utilisé pour la tokenisation et l'encodage | CLIP | Oui | - |
| `clip_vision_output` | Les embeddings visuels provenant d'un modèle CLIP vision, fournissant le contexte de l'image | CLIP_VISION_OUTPUT | Oui | - |
| `prompt` | La description textuelle qui guide la génération vidéo. Prend en charge la saisie multiligne et les invites dynamiques. L'invite est formatée à l'aide d'un modèle qui demande au modèle de décrire la vidéo à partir de l'image de référence, en couvrant des aspects comme le contenu principal, les détails des objets, les actions, l'arrière-plan et les angles de caméra. | STRING | Oui | - |
| `image_interleave` | Degré d'influence de l'image par rapport à l'invite textuelle. Une valeur plus élevée signifie une plus grande influence de l'invite textuelle. (défaut : 2, paramètre avancé) | INT | Oui | 1-512 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | Les données de conditionnement qui combinent les informations textuelles et visuelles pour la génération vidéo | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeHunyuanVideo_ImageToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `016b87ead6f7a6ca61eff220e57f59252018cc78e80ec8cff5b83223b8f90f73`
