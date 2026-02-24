> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddTextSuffix/fr.md)

Ce nœud ajoute un suffixe spécifié à la fin d'une chaîne de texte d'entrée. Il prend le texte original et le suffixe en entrées, puis renvoie le résultat combiné.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `text` | STRING | Oui | | Le texte original auquel le suffixe sera ajouté. |
| `suffix` | STRING | Non | | Le suffixe à ajouter au texte (par défaut : ""). |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `text` | STRING | Le texte résultant après l'ajout du suffixe. |
