# Tripo : Modèle squeletté redirigé

Voici la traduction en français de la documentation du nœud TripoRetargetNode :

Le TripoRetargetNode applique des animations prédéfinies à des modèles de personnages 3D en réaffectant les données de mouvement. Il prend un modèle 3D préalablement riggé et applique l'une des plusieurs animations prédéfinies, générant un fichier de modèle 3D animé en sortie. Le nœud communique avec l'API Tripo pour traiter l'opération de réaffectation d'animation.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `ID_tâche_modèle_original` | L'ID de tâche du modèle 3D riggé précédemment traité auquel appliquer l'animation | RIG_TASK_ID | Oui | - |
| `animation` | L'animation prédéfinie à appliquer au modèle 3D. Les options incluent les animations humanoïdes (idle, walk, run, dive, climb, jump, slash, shoot, hurt, fall, turn) et les animations de créatures (quadruped walk, hexapod walk, octopod walk, serpentine march, aquatic march). | STRING | Oui | "preset:idle"<br>"preset:walk"<br>"preset:run"<br>"preset:dive"<br>"preset:climb"<br>"preset:jump"<br>"preset:slash"<br>"preset:shoot"<br>"preset:hurt"<br>"preset:fall"<br>"preset:turn"<br>"preset:quadruped:walk"<br>"preset:hexapod:walk"<br>"preset:octopod:walk"<br>"preset:serpentine:march"<br>"preset:aquatic:march" |
| `auth_token_comfy_org` | Jeton d'authentification pour l'accès à l'API Comfy.org (paramètre caché) | AUTH_TOKEN_COMFY_ORG | Non | - |
| `api_key_comfy_org` | Clé API pour l'accès au service Comfy.org (paramètre caché) | API_KEY_COMFY_ORG | Non | - |
| `unique_id` | Identifiant unique pour le suivi de l'opération (paramètre caché) | UNIQUE_ID | Non | - |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `retarget task_id` | Le fichier de modèle 3D animé généré (uniquement pour la rétrocompatibilité) | STRING |
| `GLB` | L'ID de tâche pour le suivi de l'opération de réaffectation | RETARGET_TASK_ID |
| `GLB` | Le modèle 3D animé au format GLB | FILE3DGLB |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/fr.md)

---
**Source fingerprint (SHA-256):** `304326afdc1fa3e8c3593f151f771f93520e061802c831838c58ebc401b9e9e2`
