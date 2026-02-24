> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImagesByShorterEdge/fr.md)

Ce nœud redimensionne les images en ajustant leurs dimensions de sorte que la longueur du côté le plus court corresponde à une valeur cible spécifiée. Il calcule les nouvelles dimensions pour conserver le ratio d'aspect original de l'image. L'image redimensionnée est renvoyée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée à redimensionner. |
| `shorter_edge` | INT | Non | 1 à 8192 | Longueur cible pour le côté le plus court. (par défaut : 512) |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | L'image redimensionnée. |
