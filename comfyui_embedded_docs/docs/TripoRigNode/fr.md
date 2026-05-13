> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/fr.md)

Le nœud TripoRigNode génère un modèle 3D riggé à partir de l'ID de tâche d'un modèle original. Il envoie une requête à l'API Tripo pour créer un rig animé au format GLB selon les spécifications Tripo, puis interroge l'API jusqu'à ce que la tâche de génération du rig soit terminée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `ID_tâche_modèle_original` | MODEL_TASK_ID | Oui | - | ID de tâche du modèle 3D original à rigger |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | Non | - | Jeton d'authentification pour l'accès à l'API Comfy.org |
| `comfy_api_key` | API_KEY_COMFY_ORG | Non | - | Clé API pour l'authentification au service Comfy.org |
| `unique_id` | UNIQUE_ID | Non | - | Identifiant unique pour le suivi de l'opération |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `rig task_id` | STRING | Fichier du modèle 3D riggé généré (conservé pour la rétrocompatibilité) |
| `GLB` | RIG_TASK_ID | ID de tâche pour le suivi du processus de génération du rig |
| `GLB` | FILE3DGLB | Modèle 3D riggé généré au format GLB |

---
**Source fingerprint (SHA-256):** `621a4d08f3b8a349c3afff3dbf888b20d524eb3337685769b7a7badcb28986e4`
