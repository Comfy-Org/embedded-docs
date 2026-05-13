> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyAnimateModelNode/fr.md)

Ce nœud applique une animation spécifique à un modèle de personnage 3D déjà riggé via le service Meshy. Il utilise un identifiant de tâche provenant d'une opération de rigging antérieure et un identifiant d'action pour sélectionner l'animation souhaitée dans la bibliothèque. Le nœud traite ensuite la requête et retourne le modèle animé aux formats de fichier GLB et FBX.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `rig_task_id` | STRING | Oui | N/A | L'identifiant unique de tâche d'une opération de rigging de personnage Meshy précédemment réalisée. |
| `action_id` | INT | Oui | 0 à 696 | Le numéro d'identifiant de l'action d'animation à appliquer. Consultez <https://docs.meshy.ai/en/api/animation-library> pour obtenir la liste des valeurs disponibles. (valeur par défaut : 0) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `GLB` | STRING | Un identifiant textuel pour le modèle animé. Cette sortie est fournie uniquement pour des raisons de compatibilité ascendante. |
| `FBX` | FILE3DGLB | Le fichier du modèle 3D animé au format GLB. |
| `FBX` | FILE3DFBX | Le fichier du modèle 3D animé au format FBX. |

---
**Source fingerprint (SHA-256):** `3b7610b5f6f763dde86a52f9212b3fc98f41e54bda30097fcb8f5f0bd020899e`
