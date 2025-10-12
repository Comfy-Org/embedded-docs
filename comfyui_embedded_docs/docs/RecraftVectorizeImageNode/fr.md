> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftVectorizeImageNode/fr.md)

Génère un SVG de manière synchrone à partir d'une image d'entrée. Ce nœud convertit les images matricielles en format graphique vectoriel en traitant chaque image du lot d'entrée et en combinant les résultats en une seule sortie SVG.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée à convertir au format SVG |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | Non | - | Jeton d'authentification pour l'accès à l'API |
| `comfy_api_key` | API_KEY_COMFY_ORG | Non | - | Clé API pour les services Comfy.org |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `SVG` | SVG | La sortie graphique vectorielle générée combinant toutes les images traitées |
