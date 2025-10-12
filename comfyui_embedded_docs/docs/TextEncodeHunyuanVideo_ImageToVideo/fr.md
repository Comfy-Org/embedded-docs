> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeHunyuanVideo_ImageToVideo/fr.md)

Le nœud TextEncodeHunyuanVideo_ImageToVideo crée des données de conditionnement pour la génération vidéo en combinant des invites textuelles avec des embeddings d'image. Il utilise un modèle CLIP pour traiter à la fois l'entrée textuelle et les informations visuelles provenant d'une sortie vision CLIP, puis génère des tokens qui fusionnent ces deux sources selon le paramètre d'entrelacement d'image spécifié.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Oui | - | Le modèle CLIP utilisé pour la tokenisation et l'encodage |
| `sortie_vision_clip` | CLIP_VISION_OUTPUT | Oui | - | Les embeddings visuels d'un modèle vision CLIP qui fournissent le contexte de l'image |
| `invite` | STRING | Oui | - | La description textuelle pour guider la génération vidéo, prend en charge l'entrée multiligne et les invites dynamiques |
| `entrelacement_image` | INT | Oui | 1-512 | Détermine l'influence de l'image par rapport à l'invite textuelle. Un nombre plus élevé signifie plus d'influence de l'invite textuelle. (par défaut : 2) |

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Les données de conditionnement qui combinent les informations textuelles et visuelles pour la génération vidéo |