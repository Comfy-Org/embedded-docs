> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiInputFiles/fr.md)

Charge et formate les fichiers d'entrée pour une utilisation avec l'API Gemini. Ce nœud permet aux utilisateurs d'inclure des fichiers texte (.txt) et PDF (.pdf) comme contexte d'entrée pour le modèle Gemini. Les fichiers sont convertis au format approprié requis par l'API et peuvent être chaînés pour inclure plusieurs fichiers dans une seule requête.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `file` | COMBO | Oui | Plusieurs options disponibles | Fichiers d'entrée à inclure comme contexte pour le modèle. Accepte uniquement les fichiers texte (.txt) et PDF (.pdf) pour le moment. Les fichiers doivent être plus petits que la limite maximale de taille de fichier d'entrée. |
| `GEMINI_INPUT_FILES` | GEMINI_INPUT_FILES | Non | N/A | Fichier(s) supplémentaire(s) facultatif(s) à regrouper avec le fichier chargé depuis ce nœud. Permet le chaînage des fichiers d'entrée afin qu'un seul message puisse inclure plusieurs fichiers d'entrée. |

**Remarque :** Le paramètre `file` affiche uniquement les fichiers texte (.txt) et PDF (.pdf) dont la taille est inférieure à la limite maximale de taille de fichier d'entrée. Les fichiers sont automatiquement filtrés et triés par nom.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `GEMINI_INPUT_FILES` | GEMINI_INPUT_FILES | Données de fichier formatées, prêtes à être utilisées avec les nœuds Gemini LLM, contenant le contenu du fichier chargé dans le format approprié pour l'API. |

---
**Source fingerprint (SHA-256):** `54da8696d144513efa9660fbc5ddbf5480da12eafe4d2791c8e81cd207ef8a52`
