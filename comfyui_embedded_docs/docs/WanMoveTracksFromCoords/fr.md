# WanMoveTracksFromCoords

Le nœud WanMoveTracksFromCoords crée des pistes de mouvement à partir d'une chaîne de coordonnées au format JSON. Il convertit les données de coordonnées en un format de pistes pouvant être utilisé par d'autres nœuds de traitement vidéo, et peut éventuellement appliquer un masque pour contrôler la visibilité des pistes au fil du temps.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `track_coords` | Une chaîne au format JSON contenant les données de coordonnées pour les pistes. La valeur par défaut est une liste vide (`"[]"`). Cette entrée est une entrée forcée, elle doit donc être connectée dans l'interface utilisateur. | STRING | Non | N/A |
| `track_mask` | Un masque facultatif. Lorsqu'il est fourni, le nœud l'utilise pour déterminer la visibilité des pistes image par image : les pistes sont visibles dans les images où le masque contient au moins un pixel non nul. Lorsqu'il n'est pas fourni, toutes les pistes sont visibles dans toutes les images. | MASK | Non | N/A |

**Remarque :** L'entrée `track_coords` attend une structure JSON spécifique. Elle doit être une liste de pistes, où chaque piste est une liste d'images, et chaque image est un objet avec des coordonnées `x` et `y`. Le nombre d'images doit être cohérent pour toutes les pistes, et au moins une piste doit être fournie.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `tracks` | Les données de pistes générées, contenant les coordonnées de trajectoire et les informations de visibilité pour chaque piste. | TRACKS |
| `track_length` | Le nombre total d'images dans les pistes générées. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTracksFromCoords/fr.md)

---
**Source fingerprint (SHA-256):** `125187c96332fa81f0a30bcc4c927f405b56b578638ea565642a2b88dff808b7`
