> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImageNode/fr.md)

Voici la traduction en français de la documentation du nœud GeminiImage :

Le nœud GeminiImage génère des réponses textuelles et imagées à partir des modèles d'IA Gemini de Google. Il permet de fournir des entrées multimodales, notamment des invites textuelles, des images et des fichiers, pour créer des sorties textuelles et imagées cohérentes. Le nœud gère toutes les communications avec l'API et l'analyse des réponses des derniers modèles Gemini.

## Entrées

| Paramètre | Type de données | Type d'entrée | Valeur par défaut | Plage | Description |
|-----------|-----------------|---------------|-------------------|-------|-------------|
| `prompt` | STRING | requis | "" | - | Invite textuelle pour la génération |
| `model` | COMBO | requis | gemini_2_5_flash_image_preview | Modèles Gemini disponibles<br>Options extraites de l'énumération GeminiImageModel | Le modèle Gemini à utiliser pour générer les réponses |
| `seed` | INT | requis | 42 | 0 à 18446744073709551615 | Lorsque la graine est fixée à une valeur spécifique, le modèle fait de son mieux pour fournir la même réponse pour des requêtes répétées. La sortie déterministe n'est pas garantie. De plus, modifier le modèle ou les paramètres, comme la température, peut entraîner des variations dans la réponse, même en utilisant la même valeur de graine. Par défaut, une valeur de graine aléatoire est utilisée |
| `images` | IMAGE | optionnel | Aucun | - | Image(s) optionnelle(s) à utiliser comme contexte pour le modèle. Pour inclure plusieurs images, vous pouvez utiliser le nœud Batch Images |
| `files` | GEMINI_INPUT_FILES | optionnel | Aucun | - | Fichier(s) optionnel(s) à utiliser comme contexte pour le modèle. Accepte les entrées du nœud Gemini Generate Content Input Files |

*Remarque : Le nœud inclut des paramètres cachés (`auth_token`, `comfy_api_key`, `unique_id`) qui sont automatiquement gérés par le système et ne nécessitent pas de saisie de la part de l'utilisateur.*

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `IMAGE` | IMAGE | La réponse imagée générée par le modèle Gemini |
| `STRING` | STRING | La réponse textuelle générée par le modèle Gemini |