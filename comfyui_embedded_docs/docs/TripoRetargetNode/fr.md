> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/fr.md)

Voici la traduction en français de la documentation du nœud TripoRetargetNode :

Le TripoRetargetNode applique des animations prédéfinies à des modèles de personnages 3D en réaffectant les données de mouvement. Il prend un modèle 3D préalablement riggé et applique l'une des plusieurs animations prédéfinies, générant un fichier de modèle 3D animé en sortie. Le nœud communique avec l'API Tripo pour traiter l'opération de réaffectation d'animation.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `original_model_task_id` | RIG_TASK_ID | Oui | - | L'ID de tâche du modèle 3D riggé précédemment traité auquel appliquer l'animation |
| `animation` | STRING | Oui | "preset:idle"<br>"preset:walk"<br>"preset:run"<br>"preset:dive"<br>"preset:climb"<br>"preset:jump"<br>"preset:slash"<br>"preset:shoot"<br>"preset:hurt"<br>"preset:fall"<br>"preset:turn"<br>"preset:quadruped:walk"<br>"preset:hexapod:walk"<br>"preset:octopod:walk"<br>"preset:serpentine:march"<br>"preset:aquatic:march" | L'animation prédéfinie à appliquer au modèle 3D. Les options incluent les animations humanoïdes (idle, walk, run, dive, climb, jump, slash, shoot, hurt, fall, turn) et les animations de créatures (quadruped walk, hexapod walk, octopod walk, serpentine march, aquatic march). |
| `auth_token_comfy_org` | AUTH_TOKEN_COMFY_ORG | Non | - | Jeton d'authentification pour l'accès à l'API Comfy.org (paramètre caché) |
| `api_key_comfy_org` | API_KEY_COMFY_ORG | Non | - | Clé API pour l'accès au service Comfy.org (paramètre caché) |
| `unique_id` | UNIQUE_ID | Non | - | Identifiant unique pour le suivi de l'opération (paramètre caché) |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `model_file` | STRING | Le fichier de modèle 3D animé généré (uniquement pour la rétrocompatibilité) |
| `retarget task_id` | RETARGET_TASK_ID | L'ID de tâche pour le suivi de l'opération de réaffectation |
| `GLB` | FILE3DGLB | Le modèle 3D animé au format GLB |

---
**Source fingerprint (SHA-256):** `304326afdc1fa3e8c3593f151f771f93520e061802c831838c58ebc401b9e9e2`
