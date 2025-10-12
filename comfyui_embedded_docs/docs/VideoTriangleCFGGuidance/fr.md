> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTriangleCFGGuidance/fr.md)

Le nœud VideoTriangleCFGGuidance applique un motif d'échelle triangulaire d'orientation sans classifieur aux modèles vidéo. Il modifie l'échelle de conditionnement au fil du temps en utilisant une fonction d'onde triangulaire qui oscille entre la valeur CFG minimale et l'échelle de conditionnement d'origine. Cela crée un motif d'orientation dynamique qui peut aider à améliorer la cohérence et la qualité de la génération vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle vidéo auquel appliquer l'orientation CFG triangulaire |
| `min_cfg` | FLOAT | Oui | 0.0 - 100.0 | La valeur d'échelle CFG minimale pour le motif triangulaire (par défaut : 1.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle modifié avec l'orientation CFG triangulaire appliquée |