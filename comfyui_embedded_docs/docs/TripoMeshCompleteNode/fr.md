# Tripo : Compléter les parties du maillage

Complète les parties d’un modèle 3D segmenté et répare les régions manquantes ou endommagées du maillage. Il prend l’ID de tâche d’un résultat de segmentation de maillage Tripo, demande la tâche de complétion à Tripo et attend qu’elle se termine. Vous pouvez éventuellement limiter le travail à des noms de parties spécifiques. Le modèle complété est renvoyé sous forme de fichier GLB.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `segment_task_id` | ID de tâche d’une tâche de segmentation de maillage Tripo. Les parties du modèle segmenté issues de cette tâche sont complétées. Connectez la sortie SEGMENT_TASK_ID d’un nœud précédent de segmentation de maillage Tripo. | SEGMENT_TASK_ID | Oui | ID de tâche unique |
| `part_names` | Noms de parties à compléter, séparés par des virgules. Vide complète toutes les parties. Par défaut : chaîne vide. Les espaces supplémentaires autour des noms sont supprimés et les noms en double sont ignorés. | STRING | Non | Texte libre ou vide |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_file` | Nom de fichier du modèle complété. Cette sortie existe uniquement pour la compatibilité ascendante. | STRING |
| `model task_id` | ID de tâche de la tâche de complétion de maillage Tripo complétée. Peut être utilisé comme entrée par d’autres nœuds Tripo qui attendent un ID de tâche de modèle. | MODEL_TASK_ID |
| `GLB` | Le modèle 3D complété avec les parties réparées, téléchargé sous forme de fichier GLB. | GLB |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMeshCompleteNode/fr.md)

---
**Source fingerprint (SHA-256):** `c5709231fa2e33e6f3c9b25669acca1d4ae9adb882b90210d703aeddc0d11ecc`
