# CLIPMergeAdd

Le nœud CLIPMergeAdd combine deux modèles CLIP en ajoutant des correctifs (patches) du deuxième modèle au premier. Il crée une copie du premier modèle CLIP et incorpore sélectivement les correctifs clés du deuxième modèle, en excluant les identifiants de position et les paramètres d'échelle logit. Cela vous permet de fusionner des composants de modèle CLIP tout en préservant la structure du modèle de base.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip1` | Le modèle CLIP de base qui sera cloné et utilisé comme fondation pour la fusion | CLIP | Oui | - |
| `clip2` | Le modèle CLIP secondaire qui fournit les correctifs clés à ajouter au modèle de base | CLIP | Oui | - |

Remarque : Les correctifs clés de `clip2` sont ajoutés avec une force de 1,0. Les clés se terminant par `.position_ids` ou `.logit_scale` sont exclues de la fusion.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `CLIP` | Un modèle CLIP fusionné contenant la structure du modèle de base avec les correctifs ajoutés provenant du modèle secondaire | CLIP |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeAdd/fr.md)

---
**Source fingerprint (SHA-256):** `e6271ea9139598eb580f79ce63ff5d92307d7ed93f57cdc666c5e022b671a0dd`
