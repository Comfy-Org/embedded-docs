> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddTextPrefix/fr.md)

Le nœud Add Text Prefix modifie du texte en ajoutant une chaîne spécifiée au début de chaque texte d'entrée. Il prend le texte et un préfixe en entrée, puis renvoie le résultat combiné.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `text` | STRING | Oui | | Le texte auquel le préfixe sera ajouté. |
| `prefix` | STRING | Non | | La chaîne de caractères à ajouter au début du texte (par défaut : ""). |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `text` | STRING | Le texte résultant avec le préfixe ajouté au début. |
