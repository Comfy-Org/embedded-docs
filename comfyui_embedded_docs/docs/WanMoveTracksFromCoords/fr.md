# WanMoveTracksFromCoords

Le nœud WanMoveTracksFromCoords crée des pistes de mouvement à partir d'une chaîne de coordonnées au format JSON. Il convertit les données de coordonnées en un format tensoriel utilisable par d'autres nœuds de traitement vidéo, et peut éventuellement appliquer un masque pour contrôler la visibilité des pistes dans le temps.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `track_coords` | Chaîne au format JSON contenant les données de coordonnées des pistes. La valeur par défaut est une liste vide (`"[]"`). | STRING | Non | N/A |
| `track_mask` | Un masque optionnel. Lorsqu'il est fourni, le nœud l'utilise pour déterminer la visibilité de chaque piste par image. Lorsqu'il n'est pas fourni, toutes les pistes sont considérées comme visibles pour chaque image. | MASK | Non | N/A |

**Remarque :** L'entrée `track_coords` attend une structure JSON spécifique. Il doit s'agir d'une liste de pistes, où chaque piste est une liste d'images, et chaque image est un objet avec des coordonnées `x` et `y`. Le nombre d'images doit être cohérent dans toutes les pistes.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `tracks` | Les données de pistes générées, contenant les coordonnées du chemin et les informations de visibilité pour chaque piste. | TRACKS |
| `track_length` | Le nombre total d'images dans les pistes générées. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTracksFromCoords/fr.md)

---
**Source fingerprint (SHA-256):** `125187c96332fa81f0a30bcc4c927f405b56b578638ea565642a2b88dff808b7`
