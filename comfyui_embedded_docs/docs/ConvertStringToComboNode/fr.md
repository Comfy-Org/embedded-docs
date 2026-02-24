> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConvertStringToComboNode/fr.md)

## ## Aperçu général

Le nœud Convert String to Combo prend une chaîne de texte en entrée et la convertit en un type de données COMBO. Cela vous permet d'utiliser une valeur textuelle comme sélection pour d'autres nœuds qui nécessitent une entrée de type COMBO. Il transmet simplement la valeur de la chaîne inchangée, mais modifie son type de données.

## ## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Oui | N/A | La chaîne de texte à convertir en type COMBO. |

## ## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | COMBO | La chaîne d'entrée, désormais formatée en tant que type de données COMBO. |
