# Tripo : Modèle squeletté

Le nœud TripoRigNode génère un modèle 3D riggé à partir de l'ID de tâche d'un modèle original. Il envoie une requête à l'API Tripo pour créer un rig animé au format GLB selon les spécifications Tripo, puis interroge l'API jusqu'à ce que la tâche de génération du rig soit terminée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `ID_tâche_modèle_original` | ID de tâche du modèle 3D original à rigger | MODEL_TASK_ID | Oui | - |
| `auth_token` | Jeton d'authentification pour l'accès à l'API Comfy.org | AUTH_TOKEN_COMFY_ORG | Non | - |
| `comfy_api_key` | Clé API pour l'authentification au service Comfy.org | API_KEY_COMFY_ORG | Non | - |
| `unique_id` | Identifiant unique pour le suivi de l'opération | UNIQUE_ID | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `rig task_id` | Fichier du modèle 3D riggé généré (conservé pour la rétrocompatibilité) | STRING |
| `GLB` | ID de tâche pour le suivi du processus de génération du rig | RIG_TASK_ID |
| `GLB` | Modèle 3D riggé généré au format GLB | FILE3DGLB |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/fr.md)

---
**Source fingerprint (SHA-256):** `621a4d08f3b8a349c3afff3dbf888b20d524eb3337685769b7a7badcb28986e4`
