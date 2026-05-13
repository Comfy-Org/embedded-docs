> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeAdd/fr.md)

Le nœud CLIPMergeAdd combine deux modèles CLIP en ajoutant des correctifs du second modèle au premier. Il crée une copie du premier modèle CLIP et intègre sélectivement les correctifs clés du second modèle, en excluant les identifiants de position et les paramètres d'échelle logit. Cela permet de fusionner des composants de modèles CLIP tout en préservant la structure du modèle de base.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `clip1` | CLIP | Oui | - | Le modèle CLIP de base qui sera cloné et utilisé comme fondation pour la fusion |
| `clip2` | CLIP | Oui | - | Le modèle CLIP secondaire qui fournit les correctifs clés à ajouter au modèle de base |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `CLIP` | CLIP | Un modèle CLIP fusionné contenant la structure du modèle de base avec les correctifs ajoutés du modèle secondaire |

---
**Source fingerprint (SHA-256):** `f212c2750f317ad51516a10a1a03a838b75bc878333381348d5eb388a2faf516`
