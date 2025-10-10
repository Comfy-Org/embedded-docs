> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImageNode/fr.md)

Le nœud GeminiImage génère des réponses textuelles et visuelles à partir des modèles d'IA Gemini de Google. Il vous permet de fournir des entrées multimodales incluant des invites textuelles, des images et des fichiers pour créer des sorties cohérentes de texte et d'images. Le nœud gère toute la communication API et l'analyse des réponses avec les derniers modèles Gemini.

## Entrées

| Paramètre | Type de données | Type d'entrée | Par défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `prompt` | STRING | requis | "" | - | Invite textuelle pour la génération |
| `model` | COMBO | requis | gemini_2_5_flash_image_preview | Modèles Gemini disponibles<br>Options extraites de l'énumération GeminiImageModel | Le modèle Gemini à utiliser pour générer les réponses |
| `seed` | INT | requis | 42 | 0 à 18446744073709551615 | Lorsque la graine est fixée à une valeur spécifique, le modèle fait de son mieux pour fournir la même réponse pour des requêtes répétées. Une sortie déterministe n'est pas garantie. De plus, changer le modèle ou les paramètres, comme la température, peut causer des variations dans la réponse même lorsque vous utilisez la même valeur de graine. Par défaut, une valeur de graine aléatoire est utilisée |
| `images` | IMAGE | optionnel | Aucun | - | Image(s) optionnelle(s) à utiliser comme contexte pour le modèle. Pour inclure plusieurs images, vous pouvez utiliser le nœud Batch Images |
| `files` | GEMINI_INPUT_FILES | optionnel | Aucun | - | Fichier(s) optionnel(s) à utiliser comme contexte pour le modèle. Accepte les entrées du nœud Gemini Generate Content Input Files |

*Note : Le nœud inclut des paramètres cachés (`auth_token`, `comfy_api_key`, `unique_id`) qui sont automatiquement gérés par le système et ne nécessitent pas d'intervention de l'utilisateur.*

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | La réponse image générée par le modèle Gemini |
| `STRING` | STRING | La réponse textuelle générée par le modèle Gemini |