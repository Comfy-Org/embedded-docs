> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNode/fr.md)

Ce nœud permet aux utilisateurs d'interagir avec les modèles d'IA Gemini de Google pour générer des réponses textuelles. Vous pouvez fournir plusieurs types d'entrées, notamment du texte, des images, de l'audio, de la vidéo et des fichiers, comme contexte pour que le modèle génère des réponses plus pertinentes et significatives. Le nœud gère automatiquement toute la communication avec l'API et l'analyse des réponses.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `prompt` | STRING | Oui | - | Entrées textuelles pour le modèle, utilisées pour générer une réponse. Vous pouvez inclure des instructions détaillées, des questions ou un contexte pour le modèle. Valeur par défaut : chaîne vide. |
| `modèle` | COMBO | Oui | `gemini-2.5-pro-preview-05-06`<br>`gemini-2.5-flash-preview-04-17`<br>`gemini-2.5-pro`<br>`gemini-2.5-flash`<br>`gemini-3-pro-preview`<br>`gemini-3-1-pro`<br>`gemini-3-1-flash-lite` | Le modèle Gemini à utiliser pour générer des réponses. Valeur par défaut : gemini-3-1-pro. |
| `graine` | INT | Oui | 0 à 18446744073709551615 | Lorsque la graine est fixée à une valeur spécifique, le modèle fait de son mieux pour fournir la même réponse pour des requêtes répétées. La sortie déterministe n'est pas garantie. De plus, la modification du modèle ou des paramètres, comme la température, peut entraîner des variations dans la réponse, même en utilisant la même valeur de graine. Par défaut, une valeur de graine aléatoire est utilisée. Valeur par défaut : 42. |
| `images` | IMAGE | Non | - | Image(s) facultative(s) à utiliser comme contexte pour le modèle. Pour inclure plusieurs images, vous pouvez utiliser le nœud Batch Images. Valeur par défaut : Aucune. |
| `audio` | AUDIO | Non | - | Audio facultatif à utiliser comme contexte pour le modèle. Valeur par défaut : Aucun. |
| `vidéo` | VIDEO | Non | - | Vidéo facultative à utiliser comme contexte pour le modèle. Valeur par défaut : Aucune. |
| `fichiers` | GEMINI_INPUT_FILES | Non | - | Fichier(s) facultatif(s) à utiliser comme contexte pour le modèle. Accepte les entrées du nœud Gemini Generate Content Input Files. Valeur par défaut : Aucun. |
| `system_prompt` | STRING | Non | - | Instructions fondamentales qui dictent le comportement d'une IA. Valeur par défaut : chaîne vide. Il s'agit d'un paramètre avancé. |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `STRING` | STRING | La réponse textuelle générée par le modèle Gemini. |

---
**Source fingerprint (SHA-256):** `6addc7c0bc0c5889ddd6dbcb72b0b608ab738189990c591eb7160f849f6b5374`
