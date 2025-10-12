> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/fr.md)

Le TripoRigNode génère un modèle 3D articulé à partir d'un ID de tâche de modèle original. Il envoie une requête à l'API Tripo pour créer une armature animée au format GLB en utilisant la spécification Tripo, puis interroge l'API jusqu'à ce que la tâche de génération de l'armature soit terminée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `original_model_task_id` | MODEL_TASK_ID | Oui | - | L'ID de tâche du modèle 3D original à articuler |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | Non | - | Jeton d'authentification pour l'accès à l'API Comfy.org |
| `comfy_api_key` | API_KEY_COMFY_ORG | Non | - | Clé API pour l'authentification au service Comfy.org |
| `unique_id` | UNIQUE_ID | Non | - | Identifiant unique pour le suivi de l'opération |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model_file` | STRING | Le fichier du modèle 3D articulé généré |
| `rig task_id` | RIG_TASK_ID | L'ID de tâche pour le suivi du processus de génération de l'armature |
