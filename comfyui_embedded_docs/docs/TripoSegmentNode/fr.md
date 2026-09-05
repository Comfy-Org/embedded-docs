# TripoSegmentNode

Ce nœud divise un modèle 3D en parties distinctes. Il envoie le modèle au service de segmentation Tripo, attend la fin du travail, puis renvoie le modèle segmenté au format GLB avec une liste de noms de parties séparés par des virgules. Ces noms alimentent les étapes aval telles que Tripo: Complete Mesh Parts, Tripo: Retopology et Tripo: Convert model.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_task_id` | L’identifiant de tâche du modèle 3D à segmenter en parties. | MODEL_TASK_ID | Oui | N/A |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_file` | Nom du fichier de sortie du modèle GLB segmenté. Conservé uniquement pour la rétrocompatibilité. | STRING |
| `segment task_id` | L’identifiant de tâche du travail de segmentation ayant produit le résultat. | SEGMENT_TASK_ID |
| `GLB` | Le modèle 3D segmenté, sous forme de fichier GLB. | GLB |
| `part_names` | Noms des parties, séparés par des virgules. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSegmentNode/fr.md)

---
**Source fingerprint (SHA-256):** `d27580a7f2118e76cecff5e1d682c7605f966bf657d7a02b2d2ddf764d9b72d0`
