# TripoMeshCompleteNode

Complète les parties manquantes ou incomplètes d'un modèle 3D déjà segmenté et répare les zones endommagées du maillage. Il prend l'ID de tâche d'un résultat de segmentation de maillage Tripo et demande à Tripo de compléter le modèle, puis attend la fin du travail. Les parties complétées sont renvoyées sous forme de fichier GLB, et vous pouvez éventuellement limiter le travail à des noms de parties spécifiques.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `segment_task_id` | ID de tâche d'une tâche de segmentation de maillage Tripo. Les parties du modèle segmenté issues de cette tâche sont complétées. Connectez la sortie SEGMENT_TASK_ID d'un nœud précédent de segmentation de maillage Tripo. | SEGMENT_TASK_ID | Oui | ID de tâche unique |
| `part_names` | Noms de parties séparés par des virgules à compléter. Vide complète chaque partie. Par défaut : chaîne vide. Les espaces supplémentaires autour des noms sont supprimés et les noms en double sont ignorés. | STRING | Non | Texte libre ou vide |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_file` | Nom du fichier du modèle complété. Cette sortie n'existe que pour des raisons de rétrocompatibilité. | STRING |
| `task_id du modèle` | ID de tâche de la tâche de complétion de maillage Tripo terminée. Peut être utilisé comme entrée par d'autres nœuds Tripo qui attendent un ID de tâche de modèle. | MODEL_TASK_ID |
| `GLB` | Le modèle 3D complété avec ses parties réparées, téléchargé sous forme de fichier GLB. | GLB |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMeshCompleteNode/fr.md)

---
**Source fingerprint (SHA-256):** `aa7173f25f54d9fca9605e246a93fe319cf46c07d8d3aacc214a24a60c92e611`
