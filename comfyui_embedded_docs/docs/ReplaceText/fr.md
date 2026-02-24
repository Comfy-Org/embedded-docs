> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceText/fr.md)

Le nœud Replace Text effectue une substitution de texte simple. Il recherche un morceau de texte spécifié dans l'entrée et remplace chaque occurrence par un nouveau morceau de texte. L'opération est appliquée à toutes les entrées de texte fournies au nœud.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `text` | STRING | Oui | - | Le texte à traiter. |
| `find` | STRING | Non | - | Le texte à trouver et remplacer (par défaut : chaîne vide). |
| `replace` | STRING | Non | - | Le texte par lequel remplacer le texte trouvé (par défaut : chaîne vide). |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `text` | STRING | Le texte traité, avec toutes les occurrences du texte `find` remplacées par le texte `replace`. |
