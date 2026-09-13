# WanMoveVisualizeTracks

Le nœud WanMoveVisualizeTracks superpose les données de suivi de mouvement sur une séquence d'images ou de trames vidéo. Il dessine des représentations visuelles des points suivis, y compris leurs trajectoires de déplacement et leurs positions actuelles, ce qui rend les données de mouvement visibles et plus faciles à analyser.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images` | La séquence d'images d'entrée ou de trames vidéo sur lesquelles visualiser les pistes. | IMAGE | Oui | - |
| `tracks` | Les données de suivi de mouvement contenant les trajectoires de points et les informations de visibilité. Si elles ne sont pas fournies, les images d'entrée sont transmises sans modification. | TRACKS | Non | - |
| `line_resolution` | Le nombre de trames précédentes à utiliser lors du tracé de la ligne de trajectoire pour chaque piste (par défaut : 24). | INT | Oui | 1 - 1024 |
| `circle_size` | La taille du cercle dessiné à la position actuelle de chaque piste (par défaut : 12). Marqué comme paramètre avancé. | INT | Oui | 1 - 128 |
| `opacity` | L'opacité des superpositions de pistes dessinées (par défaut : 0.75). | FLOAT | Oui | 0.0 - 1.0 |
| `line_width` | La largeur des lignes utilisées pour dessiner les trajectoires des pistes (par défaut : 16). Marqué comme paramètre avancé. | INT | Oui | 1 - 128 |

**Remarque :** Si le nombre d'images d'entrée ne correspond pas au nombre de trames dans les données `tracks` fournies, la séquence d'images sera répétée pour correspondre à la longueur des pistes.

**Remarque :** Les points de suivi sont dessinés avec un ensemble limité de couleurs répétées, et un point est ignoré dans une trame lorsque son indicateur de visibilité vaut zéro pour cette trame.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | La séquence d'images avec les données de suivi de mouvement visualisées sous forme de superpositions. Si aucune `tracks` n'a été fournie, les images d'entrée d'origine sont renvoyées. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveVisualizeTracks/fr.md)

---
**Source fingerprint (SHA-256):** `d94bfde28dfdad682edcc81b1c63408f1352e0dbc94af4d043d750e8cd4c099b`
