# CLIPTextEncodeKandinsky5

Le nœud CLIP Text Encode (Kandinsky 5) prépare les invites textuelles destinées à être utilisées avec le modèle Kandinsky 5. Il prend deux entrées textuelles distinctes, les tokenise à l'aide d'un modèle CLIP fourni, et les combine en une seule sortie de conditionnement qui guide le processus de génération d'image.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP utilisé pour tokeniser et encoder les invites textuelles. | CLIP | Oui |  |
| `clip_l` | L'invite textuelle principale. Cette entrée prend en charge le texte multiligne et les invites dynamiques. | STRING | Oui |  |
| `qwen25_7b` | L'invite textuelle secondaire. Cette entrée prend en charge le texte multiligne et les invites dynamiques. | STRING | Oui |  |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | Les données de conditionnement combinées générées à partir des deux invites textuelles, prêtes à être transmises à un modèle Kandinsky 5 pour la génération d'image. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeKandinsky5/fr.md)

---
**Source fingerprint (SHA-256):** `d988c47ab9a5f01549a3ae01b365d39e9fa2464bb69ea018ec20151939dcfc56`
