> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GenerateTracks/fr.md)

## Vue d'ensemble

Le nœud `GenerateTracks` crée plusieurs trajectoires de mouvement parallèles pour la génération vidéo. Il définit un chemin principal d'un point de départ à un point d'arrivée, puis génère un ensemble de pistes qui s'exécutent parallèlement à ce chemin, espacées de manière uniforme. Vous pouvez contrôler la forme du chemin (ligne droite ou courbe de Bézier), la vitesse du mouvement le long de celui-ci, et les images dans lesquelles les pistes sont visibles.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | Oui | 16 - 4096 | La largeur de l'image vidéo en pixels. La valeur par défaut est 832. |
| `height` | INT | Oui | 16 - 4096 | La hauteur de l'image vidéo en pixels. La valeur par défaut est 480. |
| `start_x` | FLOAT | Oui | 0.0 - 1.0 | Coordonnée X normalisée (0-1) pour la position de départ. La valeur par défaut est 0.0. |
| `start_y` | FLOAT | Oui | 0.0 - 1.0 | Coordonnée Y normalisée (0-1) pour la position de départ. La valeur par défaut est 0.0. |
| `end_x` | FLOAT | Oui | 0.0 - 1.0 | Coordonnée X normalisée (0-1) pour la position d'arrivée. La valeur par défaut est 1.0. |
| `end_y` | FLOAT | Oui | 0.0 - 1.0 | Coordonnée Y normalisée (0-1) pour la position d'arrivée. La valeur par défaut est 1.0. |
| `num_frames` | INT | Oui | 1 - 1024 | Le nombre total d'images pour lesquelles générer les positions des pistes. La valeur par défaut est 81. |
| `num_tracks` | INT | Oui | 1 - 100 | Le nombre de pistes parallèles à générer. La valeur par défaut est 5. |
| `track_spread` | FLOAT | Oui | 0.0 - 1.0 | Distance normalisée entre les pistes. Les pistes sont réparties perpendiculairement à la direction du mouvement. La valeur par défaut est 0.025. |
| `bezier` | BOOLEAN | Oui | True / False | Active un chemin en courbe de Bézier utilisant le point milieu comme point de contrôle. La valeur par défaut est False. |
| `mid_x` | FLOAT | Oui | 0.0 - 1.0 | Coordonnée X normalisée du point de contrôle pour la courbe de Bézier. Utilisé uniquement lorsque 'bezier' est activé. La valeur par défaut est 0.5. |
| `mid_y` | FLOAT | Oui | 0.0 - 1.0 | Coordonnée Y normalisée du point de contrôle pour la courbe de Bézier. Utilisé uniquement lorsque 'bezier' est activé. La valeur par défaut est 0.5. |
| `interpolation` | COMBO | Oui | `"linear"`<br>`"ease_in"`<br>`"ease_out"`<br>`"ease_in_out"`<br>`"constant"` | Contrôle la temporisation/la vitesse du mouvement le long du chemin. La valeur par défaut est "linear". |
| `track_mask` | MASK | Non | - | Masque optionnel pour indiquer les images visibles. |

**Note :** Les paramètres `mid_x` et `mid_y` ne sont utilisés que lorsque le paramètre `bezier` est défini sur `True`. Lorsque `bezier` est `False`, le chemin est une ligne droite du point de départ au point d'arrivée.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `TRACKS` | TRACKS | Un objet tracks contenant les coordonnées du chemin généré et les informations de visibilité pour toutes les pistes sur toutes les images. |
| `track_length` | INT | Le nombre d'images pour lesquelles les pistes ont été générées, correspondant à l'entrée `num_frames`. |
