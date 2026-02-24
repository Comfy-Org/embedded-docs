> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImagesByLongerEdge/fr.md)

Le nœud Redimensionner les Images par le Bord le Plus Long redimensionne une ou plusieurs images de sorte que leur côté le plus long corresponde à une longueur cible spécifiée. Il détermine automatiquement si la largeur ou la hauteur est la plus longue et met à l'échelle l'autre dimension proportionnellement pour préserver le ratio d'aspect original. Cela est utile pour standardiser la taille des images en fonction de leur plus grande dimension.

## Entrées

| Paramètre | Type de Données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée ou le lot d'images à redimensionner. |
| `longer_edge` | INT | Non | 1 - 8192 | Longueur cible pour le bord le plus long. Le bord le plus court sera mis à l'échelle proportionnellement. (par défaut : 1024) |

## Sorties

| Nom de Sortie | Type de Données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | L'image ou le lot d'images redimensionné(s). La sortie contiendra le même nombre d'images que l'entrée, le bord le plus long de chacune correspondant à la longueur `longer_edge` spécifiée. |
