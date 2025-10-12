> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPAdd/fr.md)

Le nœud CLIPAdd combine deux modèles CLIP en fusionnant leurs patches clés. Il crée une copie du premier modèle CLIP puis ajoute la plupart des patches clés du second modèle, à l'exclusion des identifiants de position et des paramètres d'échelle logit. Cela permet de mélanger les caractéristiques de différents modèles CLIP tout en préservant la structure du premier modèle.

## Entrées

| Paramètre | Type de données | Type d'entrée | Par défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `clip1` | CLIP | Requis | - | - | Le modèle CLIP principal qui servira de base pour la fusion |
| `clip2` | CLIP | Requis | - | - | Le modèle CLIP secondaire qui fournit les patches supplémentaires à ajouter |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `CLIP` | CLIP | Retourne un modèle CLIP fusionné combinant les caractéristiques des deux modèles d'entrée |
