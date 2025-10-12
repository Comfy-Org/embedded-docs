> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringLength/fr.md)

Le nœud StringLength calcule le nombre de caractères dans une chaîne de texte. Il prend n'importe quelle entrée texte et retourne le nombre total de caractères, incluant les espaces et la ponctuation. Ceci est utile pour mesurer la longueur du texte ou valider les exigences de taille de chaîne.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Oui | N/A | La chaîne de texte dont il faut mesurer la longueur. Prend en charge la saisie multiligne. |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `length` | INT | Le nombre total de caractères dans la chaîne d'entrée, incluant les espaces et les caractères spéciaux. |
