> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexMatch/fr.md)

Le nœud RegexMatch vérifie si une chaîne de texte correspond à un motif d'expression régulière spécifié. Il recherche dans la chaîne d'entrée toute occurrence du motif regex et retourne si une correspondance a été trouvée. Vous pouvez configurer divers indicateurs regex comme la sensibilité à la casse, le mode multiligne et le mode dotall pour contrôler le comportement de la correspondance de motif.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Oui | - | La chaîne de texte dans laquelle rechercher des correspondances |
| `regex_pattern` | STRING | Oui | - | Le motif d'expression régulière à comparer avec la chaîne |
| `case_insensitive` | BOOLEAN | Non | - | Indique s'il faut ignorer la casse lors de la correspondance (par défaut : True) |
| `multiline` | BOOLEAN | Non | - | Indique s'il faut activer le mode multiligne pour la correspondance regex (par défaut : False) |
| `dotall` | BOOLEAN | Non | - | Indique s'il faut activer le mode dotall pour la correspondance regex (par défaut : False) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `matches` | BOOLEAN | Retourne True si le motif regex correspond à une partie de la chaîne d'entrée, False sinon |