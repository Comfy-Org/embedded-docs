# WanMoveTracksFromCoords

Le nœud WanMoveTracksFromCoords crée des trajectoires de mouvement à partir d'une chaîne de coordonnées au format JSON. Il convertit les données de coordonnées en un format tensoriel utilisable par d'autres nœuds de traitement vidéo, et peut éventuellement appliquer un masque pour contrôler la visibilité des trajectoires dans le temps.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `coordonnées_piste` | Une chaîne au format JSON contenant les données de coordonnées pour les trajectoires. La valeur par défaut est une liste vide (`"[]"`). | STRING | Non | N/A |
| `masque_piste` | Un masque optionnel. Lorsqu'il est fourni, le nœud l'utilise pour déterminer la visibilité de chaque trajectoire par image. | MASK | Non | N/A |

**Remarque :** L'entrée `track_coords` attend une structure JSON spécifique. Il doit s'agir d'une liste de trajectoires, où chaque trajectoire est une liste d'images, et chaque image est un objet avec des coordonnées `x` et `y`. Le nombre d'images doit être cohérent pour toutes les trajectoires.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `longueur_piste` | Les données de trajectoire générées, contenant les coordonnées du chemin et les informations de visibilité pour chaque trajectoire. | TRACKS |
| `longueur_piste` | Le nombre total d'images dans les trajectoires générées. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTracksFromCoords/fr.md)

---
**Source fingerprint (SHA-256):** `106b05b3bdb5ede6e31216b9f3c14160630df0eee1f4e8a645c2b6cf9fbecf8c`
