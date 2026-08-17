# Google Gemini

Ce nœud permet aux utilisateurs d'interagir avec les modèles d'IA Gemini de Google pour générer des réponses textuelles. Vous pouvez fournir plusieurs types d'entrées, notamment du texte, des images, de l'audio, des vidéos et des fichiers comme contexte pour que le modèle génère des réponses plus pertinentes et significatives. Le nœud gère automatiquement toute la communication avec l'API et l'analyse des réponses.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Entrées textuelles pour le modèle, utilisées pour générer une réponse. Vous pouvez inclure des instructions détaillées, des questions ou un contexte pour le modèle. Par défaut : chaîne vide. | STRING | Oui | - |
| `model` | Le modèle Gemini à utiliser pour générer les réponses. Par défaut : gemini-3-1-pro. | COMBO | Oui | "gemini-2.5-pro"<br>"gemini-2.5-flash"<br>"gemini-3-pro-preview"<br>"gemini-3-1-pro"<br>"gemini-3-1-flash-lite" |
| `seed` | Lorsque `seed` est fixée à une valeur spécifique, le modèle fait de son mieux pour fournir la même réponse pour des demandes répétées. La sortie déterministe n'est pas garantie. De plus, la modification du modèle ou des paramètres, tels que la température, peut entraîner des variations dans la réponse même si vous utilisez la même valeur de graine. Par défaut, une valeur de graine aléatoire est utilisée. Par défaut : 42. | INT | Oui | 0 à 18446744073709551615 |
| `images` | Image(s) facultative(s) à utiliser comme contexte pour le modèle. Pour inclure plusieurs images, vous pouvez utiliser le nœud Batch Images. Par défaut : Aucun. | IMAGE | Non | - |
| `audio` | Audio facultatif à utiliser comme contexte pour le modèle. Par défaut : Aucun. | AUDIO | Non | - |
| `video` | Vidéo facultative à utiliser comme contexte pour le modèle. Par défaut : Aucun. | VIDEO | Non | - |
| `files` | Fichier(s) facultatif(s) à utiliser comme contexte pour le modèle. Accepte les entrées du nœud Gemini Generate Content Input Files. Par défaut : Aucun. | GEMINI_INPUT_FILES | Non | - |
| `system_prompt` | Instructions fondamentales qui dictent le comportement d'une IA. Par défaut : chaîne vide. Ceci est un paramètre avancé. | STRING | Non | - |

Note : Ce nœud est marqué comme obsolète.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `STRING` | La réponse textuelle générée par le modèle Gemini. Si le modèle ne renvoie aucun texte, le nœud génère « Empty response from Gemini model... ». | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNode/fr.md)

---
**Source fingerprint (SHA-256):** `d1c53a5d80182085a36302867c8875df696adec6aaea9a9519a21bd6b9543d8f`
