> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIInputFiles/fr.md)

Charge et formate les fichiers d'entrée pour l'API OpenAI. Ce nœud prépare les fichiers texte et PDF à inclure comme entrées de contexte pour le nœud OpenAI Chat. Les fichiers seront lus par le modèle OpenAI lors de la génération des réponses. Plusieurs nœuds de fichiers d'entrée peuvent être chaînés pour inclure plusieurs fichiers dans un seul message.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `file` | COMBO | Oui | Plusieurs options disponibles | Fichiers d'entrée à inclure comme contexte pour le modèle. Accepte uniquement les fichiers texte (.txt) et PDF (.pdf) pour le moment. Les fichiers doivent être inférieurs à 32 Mo. |
| `OPENAI_INPUT_FILES` | OPENAI_INPUT_FILES | Non | N/A | Fichier(s) supplémentaire(s) optionnel(s) à regrouper avec le fichier chargé depuis ce nœud. Permet le chaînage des fichiers d'entrée afin qu'un seul message puisse inclure plusieurs fichiers d'entrée. |

**Contraintes des fichiers :**
- Seuls les fichiers .txt et .pdf sont pris en charge
- Taille maximale des fichiers : 32 Mo
- Les fichiers sont chargés depuis le répertoire d'entrée

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `OPENAI_INPUT_FILES` | OPENAI_INPUT_FILES | Fichiers d'entrée formatés prêts à être utilisés comme contexte pour les appels d'API OpenAI. |