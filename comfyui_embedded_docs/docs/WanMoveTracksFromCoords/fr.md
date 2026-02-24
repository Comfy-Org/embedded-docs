> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTracksFromCoords/fr.md)

## Vue d'ensemble

Le nœud WanMoveTracksFromCoords génère un ensemble de pistes de mouvement à partir d'une liste de points de coordonnées. Il convertit une chaîne de caractères au format JSON contenant des coordonnées en un format tensoriel utilisable par d'autres nœuds de traitement vidéo, et peut optionnellement appliquer un masque pour contrôler la visibilité des pistes au fil du temps.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `track_coords` | STRING | Oui | N/A | Une chaîne de caractères au format JSON contenant les données de coordonnées pour les pistes. La valeur par défaut est une liste vide (`"[]"`). |
| `track_mask` | MASK | Non | N/A | Un masque optionnel. Lorsqu'il est fourni, le nœud l'utilise pour déterminer la visibilité de chaque piste par image. |

**Note :** L'entrée `track_coords` attend une structure JSON spécifique. Il doit s'agir d'une liste de pistes, où chaque piste est une liste d'images, et chaque image est un objet avec des coordonnées `x` et `y`. Le nombre d'images doit être cohérent pour toutes les pistes.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `tracks` | TRACKS | Les données de piste générées, contenant les coordonnées du chemin et les informations de visibilité pour chaque piste. |
| `track_length` | INT | Le nombre total d'images dans les pistes générées. |
