# Meshy : Animer le modèle

Ce nœud applique une action d'animation spécifique à un personnage 3D préalablement riggé à l'aide du service Meshy. Il prend un ID de tâche issu d'une opération de rigging antérieure et un ID d'action pour sélectionner l'animation souhaitée dans la bibliothèque, puis renvoie le modèle animé aux formats de fichier GLB et FBX.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `rig_task_id` | L'ID de tâche unique d'une opération de rigging de personnage Meshy précédemment terminée. | STRING | Oui | N/A |
| `action_id` | Le numéro d'ID de l'action d'animation à appliquer. Consultez https://docs.meshy.ai/en/api/animation-library pour une liste des valeurs disponibles. (défaut : 0) | INT | Oui | 0 à 696 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_file` | Un identifiant de chaîne pour le modèle animé. Cette sortie est fournie uniquement pour la rétrocompatibilité. | STRING |
| `GLB` | Le fichier du modèle 3D animé au format GLB. | FILE3DGLB |
| `FBX` | Le fichier du modèle 3D animé au format FBX. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyAnimateModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `760e94d3a92910051d9b473545191842dc9672e6c4a59c3d1cd9cfdc5eb2589d`
