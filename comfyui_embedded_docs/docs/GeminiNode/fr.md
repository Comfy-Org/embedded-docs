> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNode/fr.md)

Ce nœud permet aux utilisateurs d'interagir avec les modèles d'IA Gemini de Google pour générer des réponses textuelles. Vous pouvez fournir plusieurs types d'entrées, y compris du texte, des images, de l'audio, de la vidéo et des fichiers, comme contexte pour que le modèle génère des réponses plus pertinentes et significatives. Le nœud gère automatiquement toute la communication API et l'analyse des réponses.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | - | Entrées textuelles pour le modèle, utilisées pour générer une réponse. Vous pouvez inclure des instructions détaillées, des questions ou un contexte pour le modèle. Par défaut : chaîne vide. |
| `model` | COMBO | Oui | `gemini-2.0-flash-exp`<br>`gemini-2.0-flash-thinking-exp`<br>`gemini-2.5-pro-exp`<br>`gemini-2.0-flash`<br>`gemini-2.0-flash-thinking`<br>`gemini-2.5-pro`<br>`gemini-2.0-flash-lite`<br>`gemini-1.5-flash`<br>`gemini-1.5-flash-8b`<br>`gemini-1.5-pro`<br>`gemini-1.0-pro` | Le modèle Gemini à utiliser pour générer les réponses. Par défaut : gemini-2.5-pro. |
| `seed` | INT | Oui | 0 à 18446744073709551615 | Lorsque la graine est fixée à une valeur spécifique, le modèle fait de son mieux pour fournir la même réponse pour des requêtes répétées. Une sortie déterministe n'est pas garantie. De plus, changer le modèle ou les paramètres, tels que la température, peut entraîner des variations dans la réponse même en utilisant la même valeur de graine. Par défaut, une valeur de graine aléatoire est utilisée. Par défaut : 42. |
| `images` | IMAGE | Non | - | Image(s) optionnelle(s) à utiliser comme contexte pour le modèle. Pour inclure plusieurs images, vous pouvez utiliser le nœud Batch Images. Par défaut : Aucune. |
| `audio` | AUDIO | Non | - | Audio optionnel à utiliser comme contexte pour le modèle. Par défaut : Aucun. |
| `video` | VIDEO | Non | - | Vidéo optionnelle à utiliser comme contexte pour le modèle. Par défaut : Aucune. |
| `files` | GEMINI_INPUT_FILES | Non | - | Fichier(s) optionnel(s) à utiliser comme contexte pour le modèle. Accepte les entrées du nœud Gemini Generate Content Input Files. Par défaut : Aucun. |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `STRING` | STRING | La réponse textuelle générée par le modèle Gemini. |