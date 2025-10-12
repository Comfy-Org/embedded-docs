> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftRemoveBackgroundNode/fr.md)

Ce nœud supprime l'arrière-plan des images en utilisant le service API Recraft. Il traite chaque image du lot d'entrée et renvoie à la fois les images traitées avec des arrière-plans transparents et les masques alpha correspondants qui indiquent les zones d'arrière-plan supprimées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image ou les images d'entrée à traiter pour la suppression de l'arrière-plan |
| `auth_token` | STRING | Non | - | Jeton d'authentification pour l'accès à l'API Recraft |
| `comfy_api_key` | STRING | Non | - | Clé API pour l'intégration du service Comfy.org |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | Images traitées avec des arrière-plans transparents |
| `mask` | MASK | Masques de canal alpha indiquant les zones d'arrière-plan supprimées |
