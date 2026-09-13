# Google Gemini

Ce nœud permet aux utilisateurs d'interagir avec les modèles d'IA Gemini de Google pour générer des réponses textuelles. Vous pouvez fournir plusieurs types d'entrées, notamment du texte, des images, de l'audio, de la vidéo et des fichiers, comme contexte pour permettre au modèle de générer des réponses plus pertinentes et significatives. Le nœud gère automatiquement toute la communication avec l'API et l'analyse des réponses.

**Remarque :** Ce nœud est marqué comme obsolète dans le code source.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Entrées texte pour le modèle, utilisées pour générer une réponse. Vous pouvez inclure des instructions détaillées, des questions ou du contexte pour le modèle. Par défaut : chaîne vide. | STRING | Oui | - |
| `model` | Le modèle Gemini à utiliser pour générer des réponses. Par défaut : gemini-3-1-pro. | COMBO | Oui | "gemini-2.5-pro"<br>"gemini-2.5-flash"<br>"gemini-3-pro-preview"<br>"gemini-3-1-pro"<br>"gemini-3-1-flash-lite" |
| `seed` | Lorsque `seed` est fixé à une valeur spécifique, le modèle fait de son mieux pour fournir la même réponse pour des requêtes répétées. Une sortie déterministe n'est pas garantie. De plus, changer le modèle ou les paramètres, comme la température, peut entraîner des variations dans la réponse même si vous utilisez la même valeur de `seed`. Par défaut, une valeur de `seed` aléatoire est utilisée. Par défaut : 42. | INT | Oui | 0 à 18446744073709551615 |
| `images` | Image(s) facultative(s) à utiliser comme contexte pour le modèle. Pour inclure plusieurs images, vous pouvez utiliser le nœud Batch Images. Par défaut : Aucune. | IMAGE | Non | - |
| `audio` | Audio facultatif à utiliser comme contexte pour le modèle. Par défaut : Aucun. | AUDIO | Non | - |
| `video` | Vidéo facultative à utiliser comme contexte pour le modèle. Par défaut : Aucune. | VIDEO | Non | - |
| `files` | Fichier(s) facultatif(s) à utiliser comme contexte pour le modèle. Accepte les entrées du nœud Gemini Generate Content Input Files. Par défaut : Aucun. | GEMINI_INPUT_FILES | Non | - |
| `system_prompt` | Instructions fondamentales qui dictent le comportement d'une IA. Par défaut : chaîne vide. Il s'agit d'un paramètre avancé. | STRING | Non | - |

Toutes les images connectées sont utilisées comme contexte. Lorsque plus de 10 images sont fournies, les 10 premières sont téléversées comme références de fichiers et les images restantes sont envoyées en inline à l'API.

Le nœud utilise le nom du modèle sélectionné tel qu'indiqué dans la liste ; certaines entrées sont associées en interne à leurs identifiants de modèle API actuels avant l'envoi de la requête.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `STRING` | La réponse textuelle générée par le modèle Gemini. Si le modèle ne produit aucun texte, le nœud renvoie "Empty response from Gemini model...". | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNode/fr.md)

---
**Source fingerprint (SHA-256):** `d1c53a5d80182085a36302867c8875df696adec6aaea9a9519a21bd6b9543d8f`
