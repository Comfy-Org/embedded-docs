> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringReplace/fr.md)

Le nœud StringReplace effectue des opérations de remplacement de texte sur des chaînes d'entrée. Il recherche une sous-chaîne spécifiée dans le texte d'entrée et remplace toutes ses occurrences par une sous-chaîne différente. Ce nœud retourne la chaîne modifiée avec tous les remplacements appliqués.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Oui | - | La chaîne de texte d'entrée où les remplacements seront effectués |
| `find` | STRING | Oui | - | La sous-chaîne à rechercher dans le texte d'entrée |
| `replace` | STRING | Oui | - | Le texte de remplacement qui substituera toutes les occurrences trouvées |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | STRING | La chaîne modifiée avec toutes les occurrences du texte à trouver remplacées par le texte de remplacement |
