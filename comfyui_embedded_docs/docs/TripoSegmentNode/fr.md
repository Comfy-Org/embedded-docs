# Tripo : Segmenter le modèle

Ce nœud divise un modèle 3D en parties individuelles. Il envoie le modèle au service de segmentation Tripo, attend la fin de la tâche, puis renvoie le modèle segmenté au format GLB ainsi qu'une liste de noms de parties séparés par des virgules. Ces noms de parties alimentent les étapes en aval telles que Tripo: Complete Mesh Parts, Tripo: Retopology et Tripo: Convert model.

<Note>
Tripo conserve les enregistrements de tâches sur ses serveurs pendant 7 jours (à compter du 1er décembre 2026). Un ID de tâche plus ancien ne peut plus être résolu, donc relancer un workflow enregistré après ce délai échoue sur ce nœud. Pour continuer, relancez le nœud Tripo précédent pour créer un nouvel ID de tâche, ou réimportez le modèle que vous avez déjà téléchargé avec **Tripo : Importer un modèle**.
</Note>

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `model_task_id` | L'ID de tâche du modèle 3D à segmenter en parties. | MODEL_TASK_ID | Oui | N/A |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_file` | Nom du fichier de sortie du modèle GLB segmenté, sous la forme `<task_id>.glb`. Conservé uniquement pour la compatibilité ascendante. | STRING |
| `segment task_id` | L'ID de tâche de la segmentation qui a produit le résultat. | SEGMENT_TASK_ID |
| `GLB` | Le modèle 3D segmenté, sous forme de fichier GLB. | GLB |
| `part_names` | Noms des parties séparés par des virgules. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSegmentNode/fr.md)

---
**Source fingerprint (SHA-256):** `3218f87bfdc347d58b639cbe57b01cf7625c95c753bf381e35b4a28376eeb0e8`
