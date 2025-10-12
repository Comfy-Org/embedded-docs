> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringSubstring/fr.md)

Le nœud StringSubstring extrait une portion de texte d'une chaîne plus longue. Il prend une position de départ et une position de fin pour définir la section que vous souhaitez extraire, puis retourne le texte situé entre ces deux positions.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Oui | - | La chaîne de texte d'entrée depuis laquelle extraire |
| `start` | INT | Oui | - | L'index de position de départ pour la sous-chaîne |
| `end` | INT | Oui | - | L'index de position de fin pour la sous-chaîne |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | STRING | La sous-chaîne extraite du texte d'entrée |