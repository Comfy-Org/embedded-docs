> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRefineNode/fr.md)

Le TripoRefineNode affine les modèles 3D préliminaires créés spécifiquement par les modèles Tripo v1.4. Il prend un identifiant de tâche de modèle et le traite via l'API Tripo pour générer une version améliorée du modèle. Ce nœud est conçu pour fonctionner exclusivement avec les modèles préliminaires produits par les modèles Tripo v1.4.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model_task_id` | MODEL_TASK_ID | Oui | - | Doit être un modèle Tripo v1.4 |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | Non | - | Jeton d'authentification pour l'API Comfy.org |
| `comfy_api_key` | API_KEY_COMFY_ORG | Non | - | Clé API pour les services Comfy.org |
| `unique_id` | UNIQUE_ID | Non | - | Identifiant unique pour l'opération |

**Note :** Ce nœud n'accepte que les modèles préliminaires créés par les modèles Tripo v1.4. L'utilisation de modèles d'autres versions peut entraîner des erreurs.

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model_file` | STRING | Le chemin du fichier ou la référence vers le modèle raffiné |
| `model task_id` | MODEL_TASK_ID | L'identifiant de tâche pour l'opération de raffinement du modèle |