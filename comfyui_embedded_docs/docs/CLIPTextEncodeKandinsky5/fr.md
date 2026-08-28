# CLIPTextEncodeKandinsky5

Le nœud **CLIP Text Encode (Kandinsky 5)** prépare les prompts texte pour une utilisation avec le modèle Kandinsky 5. Il prend deux entrées texte distinctes, les tokenise à l'aide d'un modèle CLIP fourni, et les combine en une seule sortie de conditionnement. Cette sortie est utilisée pour guider le processus de génération d'images.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP utilisé pour tokeniser et encoder les prompts texte. | CLIP | Oui |  |
| `clip_l` | Le prompt texte principal. Cette entrée prend en charge le texte multiligne et les prompts dynamiques. | STRING | Oui |  |
| `qwen25_7b` | Le prompt texte secondaire. Cette entrée prend en charge le texte multiligne et les prompts dynamiques. | STRING | Oui |  |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | Les données de conditionnement combinées générées à partir des deux prompts texte, prêtes à être introduites dans un modèle Kandinsky 5 pour la génération d'images. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeKandinsky5/fr.md)

---
**Source fingerprint (SHA-256):** `d988c47ab9a5f01549a3ae01b365d39e9fa2464bb69ea018ec20151939dcfc56`
