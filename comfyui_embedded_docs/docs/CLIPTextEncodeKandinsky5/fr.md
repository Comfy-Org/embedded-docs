> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeKandinsky5/fr.md)

Le nœud CLIPTextEncodeKandinsky5 prépare les invites textuelles pour une utilisation avec le modèle Kandinsky 5. Il prend deux entrées textuelles distinctes, les tokenise à l'aide d'un modèle CLIP fourni, et les combine en une seule sortie de conditionnement. Cette sortie est utilisée pour guider le processus de génération d'image.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Oui | | Le modèle CLIP utilisé pour tokeniser et encoder les invites textuelles. |
| `clip_l` | STRING | Oui | | L'invite textuelle principale. Cette entrée prend en charge le texte multiligne et les invites dynamiques. |
| `qwen25_7b` | STRING | Oui | | Une invite textuelle secondaire. Cette entrée prend en charge le texte multiligne et les invites dynamiques. |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Les données de conditionnement combinées générées à partir des deux invites textuelles, prêtes à être utilisées par un modèle Kandinsky 5 pour la génération d'image. |
