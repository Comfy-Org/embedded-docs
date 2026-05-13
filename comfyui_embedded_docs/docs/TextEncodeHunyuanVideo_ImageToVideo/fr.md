> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeHunyuanVideo_ImageToVideo/fr.md)

Voici la traduction en français de la documentation du nœud ComfyUI `TextEncodeHunyuanVideo_ImageToVideo`, en respectant vos règles.

---

Le nœud `TextEncodeHunyuanVideo_ImageToVideo` crée des données de conditionnement pour la génération vidéo en combinant des invites textuelles avec des embeddings d'images. Il utilise un modèle CLIP pour traiter à la fois l'entrée textuelle et les informations visuelles provenant d'une sortie de vision CLIP, puis génère des jetons qui fusionnent ces deux sources selon le réglage d'entrelacement d'image spécifié.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `clip` | CLIP | Oui | - | Le modèle CLIP utilisé pour la tokenisation et l'encodage |
| `sortie_vision_clip` | CLIP_VISION_OUTPUT | Oui | - | Les embeddings visuels provenant d'un modèle de vision CLIP qui fournissent le contexte de l'image |
| `invite` | STRING | Oui | - | La description textuelle pour guider la génération vidéo, prend en charge les entrées multilignes et les invites dynamiques |
| `entrelacement_image` | INT | Oui | 1-512 | Dans quelle mesure l'image influence les résultats par rapport à l'invite textuelle. Un nombre plus élevé signifie une plus grande influence de l'invite textuelle. (valeur par défaut : 2) |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `CONDITIONING` | CONDITIONING | Les données de conditionnement qui combinent les informations textuelles et visuelles pour la génération vidéo |

---
**Source fingerprint (SHA-256):** `ee748bd1fb1733593eb4cb1187c5cc279171163cfbc389f039378d0e366fc231`
