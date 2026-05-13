> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIInputFiles/fr.md)

Charge et formate les fichiers d'entrée pour l'API OpenAI. Ce nœud prépare les fichiers texte (.txt) et PDF (.pdf) à inclure comme contextes d'entrée pour le nœud OpenAI Chat. Les fichiers seront lus par le modèle OpenAI lors de la génération d'une réponse. Plusieurs nœuds OpenAI Input Files peuvent être chaînés ensemble pour inclure plusieurs fichiers dans un seul message.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `file` | COMBO | Oui | Plusieurs options disponibles (tous les fichiers .txt et .pdf dans le répertoire d'entrée de moins de 32 Mo) | Fichiers d'entrée à inclure comme contexte pour le modèle. Accepte uniquement les fichiers texte (.txt) et PDF (.pdf) pour le moment. Les fichiers doivent être inférieurs à 32 Mo. |
| `OPENAI_INPUT_FILES` | OPENAI_INPUT_FILES | Non | N/D | Un ou plusieurs fichiers supplémentaires facultatifs à regrouper avec le fichier chargé depuis ce nœud. Permet le chaînage de fichiers d'entrée afin qu'un seul message puisse inclure plusieurs fichiers d'entrée. |

**Contraintes des fichiers :**

- Seuls les fichiers .txt et .pdf sont pris en charge
- Taille maximale du fichier : 32 Mo
- Les fichiers sont chargés depuis le répertoire d'entrée de ComfyUI

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `OPENAI_INPUT_FILES` | OPENAI_INPUT_FILES | Fichiers d'entrée formatés, prêts à être utilisés comme contexte pour les appels API OpenAI. |

---
**Source fingerprint (SHA-256):** `e5e92f6628072da9af787867e38c89dde3db853b7289ef6c607a066cd04c1cc9`
