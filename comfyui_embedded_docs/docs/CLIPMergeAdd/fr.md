> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeAdd/fr.md)

Le nœud CLIPMergeAdd combine deux modèles CLIP en ajoutant des patches du second modèle au premier modèle. Il crée une copie du premier modèle CLIP et incorpore sélectivement les patches clés du second modèle, en excluant les identifiants de position et les paramètres d'échelle logit. Cela vous permet de fusionner des composants de modèles CLIP tout en préservant la structure du modèle de base.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `clip1` | CLIP | Oui | - | Le modèle CLIP de base qui sera cloné et utilisé comme fondation pour la fusion |
| `clip2` | CLIP | Oui | - | Le modèle CLIP secondaire qui fournit les patches clés à ajouter au modèle de base |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `CLIP` | CLIP | Un modèle CLIP fusionné contenant la structure du modèle de base avec des patches ajoutés du modèle secondaire |