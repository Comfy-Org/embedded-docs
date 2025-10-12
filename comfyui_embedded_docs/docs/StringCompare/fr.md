> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringCompare/fr.md)

Le nœud StringCompare compare deux chaînes de texte en utilisant différentes méthodes de comparaison. Il peut vérifier si une chaîne commence par une autre, se termine par une autre, ou si les deux chaînes sont exactement égales. La comparaison peut être effectuée en tenant compte ou non des différences de casse.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `string_a` | STRING | Oui | - | La première chaîne à comparer |
| `string_b` | STRING | Oui | - | La deuxième chaîne à comparer |
| `mode` | COMBO | Oui | "Starts With"<br>"Ends With"<br>"Equal" | La méthode de comparaison à utiliser |
| `case_sensitive` | BOOLEAN | Non | - | Indique si la casse doit être prise en compte lors de la comparaison (par défaut : true) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | BOOLEAN | Retourne true si la condition de comparaison est satisfaite, false sinon |