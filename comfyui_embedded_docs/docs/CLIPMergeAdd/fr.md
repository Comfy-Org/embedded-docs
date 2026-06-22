# CLIPMergeAdd

Le nœud CLIPMergeAdd combine deux modèles CLIP en ajoutant des correctifs du second modèle au premier. Il crée une copie du premier modèle CLIP et intègre sélectivement les correctifs clés du second modèle, en excluant les identifiants de position et les paramètres d'échelle logit. Cela permet de fusionner des composants de modèles CLIP tout en préservant la structure du modèle de base.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip1` | Le modèle CLIP de base qui sera cloné et utilisé comme fondation pour la fusion | CLIP | Oui | - |
| `clip2` | Le modèle CLIP secondaire qui fournit les correctifs clés à ajouter au modèle de base | CLIP | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `CLIP` | Un modèle CLIP fusionné contenant la structure du modèle de base avec les correctifs ajoutés du modèle secondaire | CLIP |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeAdd/fr.md)

---
**Source fingerprint (SHA-256):** `f212c2750f317ad51516a10a1a03a838b75bc878333381348d5eb388a2faf516`
