> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringContains/fr.md)

Le nœud StringContains vérifie si une chaîne de caractères donnée contient une sous-chaîne spécifiée. Il peut effectuer cette vérification avec une correspondance sensible ou insensible à la casse, renvoyant un résultat booléen indiquant si la sous-chaîne a été trouvée dans la chaîne principale.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Oui | - | La chaîne de texte principale dans laquelle effectuer la recherche |
| `substring` | STRING | Oui | - | Le texte à rechercher dans la chaîne principale |
| `case_sensitive` | BOOLEAN | Non | - | Détermine si la recherche doit être sensible à la casse (par défaut : true) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `contains` | BOOLEAN | Renvoie true si la sous-chaîne est trouvée dans la chaîne, false sinon |