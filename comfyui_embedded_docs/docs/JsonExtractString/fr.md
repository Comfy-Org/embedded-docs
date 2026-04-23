> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JsonExtractString/fr.md)

Le nœud JsonExtractString lit une chaîne de texte contenant des données JSON et extrait la valeur associée à une clé spécifique. Il convertit la valeur extraite en chaîne de caractères. Si le JSON est invalide, si la clé n'est pas trouvée ou si la valeur est nulle, le nœud renvoie une chaîne vide.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `json_string` | STRING | Oui | N/A | Le texte contenant les données JSON à analyser. |
| `key` | STRING | Oui | N/A | La clé spécifique dont vous souhaitez extraire la valeur (sous forme de chaîne) de l'objet JSON. |

**Note :** Le nœud n'extrait des valeurs que depuis des objets JSON (dictionnaires). Si le JSON analysé n'est pas un objet ou si la clé spécifiée n'existe pas à l'intérieur, la sortie sera une chaîne vide.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | STRING | La valeur extraite du JSON pour la clé spécifiée, sous forme de chaîne de caractères, ou une chaîne vide si l'extraction échoue. |