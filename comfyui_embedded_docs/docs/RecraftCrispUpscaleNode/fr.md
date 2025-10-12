> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftCrispUpscaleNode/fr.md)

Redimensionnement d'image synchrone. Améliore une image raster donnée en utilisant l'outil 'crisp upscale', augmentant la résolution de l'image et la rendant plus nette et plus propre.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée à redimensionner |
| `auth_token` | STRING | Non | - | Jeton d'authentification pour l'API Recraft |
| `comfy_api_key` | STRING | Non | - | Clé API pour les services Comfy.org |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | L'image redimensionnée avec une résolution et une clarté améliorées |