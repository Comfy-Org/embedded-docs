# GenerateTracks

Le nœud `GenerateTracks` crée plusieurs trajectoires de mouvement parallèles pour la génération vidéo. Il définit un chemin principal d'un point de départ à un point d'arrivée, puis génère un ensemble de pistes parallèles à ce chemin, espacées uniformément. Vous pouvez contrôler la forme du chemin (ligne droite ou courbe de Bézier), la vitesse de déplacement le long de celui-ci, et les images dans lesquelles les pistes sont visibles.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `width` | La largeur de l'image vidéo en pixels. La valeur par défaut est 832. | INT | Oui | 16 - 4096 |
| `height` | La hauteur de l'image vidéo en pixels. La valeur par défaut est 480. | INT | Oui | 16 - 4096 |
| `start_x` | Coordonnée X normalisée (0-1) pour la position de départ. La valeur par défaut est 0.0. | FLOAT | Oui | 0.0 - 1.0 |
| `start_y` | Coordonnée Y normalisée (0-1) pour la position de départ. La valeur par défaut est 0.0. | FLOAT | Oui | 0.0 - 1.0 |
| `end_x` | Coordonnée X normalisée (0-1) pour la position d'arrivée. La valeur par défaut est 1.0. | FLOAT | Oui | 0.0 - 1.0 |
| `end_y` | Coordonnée Y normalisée (0-1) pour la position d'arrivée. La valeur par défaut est 1.0. | FLOAT | Oui | 0.0 - 1.0 |
| `num_frames` | Le nombre total d'images pour lequel générer les positions des pistes. La valeur par défaut est 81. | INT | Oui | 1 - 1024 |
| `num_tracks` | Le nombre de pistes parallèles à générer. La valeur par défaut est 5. | INT | Oui | 1 - 100 |
| `track_spread` | Distance normalisée entre les pistes. Les pistes sont réparties perpendiculairement à la direction du mouvement. La valeur par défaut est 0.025. | FLOAT | Oui | 0.0 - 1.0 |
| `bezier` | Active le chemin en courbe de Bézier en utilisant le point médian comme point de contrôle. La valeur par défaut est False. | BOOLEAN | Oui | True / False |
| `mid_x` | Point de contrôle X normalisé pour la courbe de Bézier. Utilisé uniquement lorsque `bezier` est activé. La valeur par défaut est 0.5. | FLOAT | Oui | 0.0 - 1.0 |
| `mid_y` | Point de contrôle Y normalisé pour la courbe de Bézier. Utilisé uniquement lorsque `bezier` est activé. La valeur par défaut est 0.5. | FLOAT | Oui | 0.0 - 1.0 |
| `interpolation` | Contrôle le timing/vitesse du mouvement le long du chemin. La valeur par défaut est "linear". Avec "constant", tous les points restent à la position de départ. | COMBO | Oui | `"linear"`<br>`"ease_in"`<br>`"ease_out"`<br>`"ease_in_out"`<br>`"constant"` |
| `track_mask` | Masque optionnel pour indiquer les images visibles. | MASK | Non | - |

**Remarque :** Les paramètres `mid_x` et `mid_y` ne sont utilisés que lorsque le paramètre `bezier` est défini sur `True`. Lorsque `bezier` est `False`, le chemin est une ligne droite allant du point de départ au point d'arrivée.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `TRACKS` | Un objet de pistes contenant les coordonnées de chemin générées et les informations de visibilité pour toutes les pistes sur toutes les images. | TRACKS |
| `track_length` | Le nombre d'images pour lequel les pistes ont été générées, correspondant à l'entrée `num_frames`. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GenerateTracks/fr.md)

---
**Source fingerprint (SHA-256):** `4bd4d03a84f4b7ea260555b43f217af0b90dd4ca5196aca94e8f3886875ab912`
