> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/fr.md)

Le TripoRetargetNode applique des animations prédéfinies à des modèles de personnages 3D en retargetant des données de mouvement. Il prend un modèle 3D précédemment traité et applique l'une des plusieurs animations prédéfinies, générant un fichier de modèle 3D animé en sortie. Le nœud communique avec l'API Tripo pour traiter l'opération de retargeting d'animation.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `original_model_task_id` | RIG_TASK_ID | Oui | - | L'identifiant de tâche du modèle 3D précédemment traité auquel appliquer l'animation |
| `animation` | STRING | Oui | "preset:idle"<br>"preset:walk"<br>"preset:climb"<br>"preset:jump"<br>"preset:slash"<br>"preset:shoot"<br>"preset:hurt"<br>"preset:fall"<br>"preset:turn" | L'animation prédéfinie à appliquer au modèle 3D |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | Non | - | Jeton d'authentification pour l'accès à l'API Comfy.org |
| `comfy_api_key` | API_KEY_COMFY_ORG | Non | - | Clé API pour l'accès au service Comfy.org |
| `unique_id` | UNIQUE_ID | Non | - | Identifiant unique pour le suivi de l'opération |

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model_file` | STRING | Le fichier de modèle 3D animé généré |
| `retarget task_id` | RETARGET_TASK_ID | L'identifiant de tâche pour le suivi de l'opération de retargeting |
