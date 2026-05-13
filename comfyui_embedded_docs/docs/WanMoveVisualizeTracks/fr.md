> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveVisualizeTracks/fr.md)

Le nœud WanMoveVisualizeTracks superpose les données de suivi de mouvement sur une séquence d'images ou de trames vidéo. Il dessine des représentations visuelles des points suivis, incluant leurs trajectoires et positions actuelles, rendant les données de mouvement visibles et plus faciles à analyser.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `images` | IMAGE | Oui | - | La séquence d'images d'entrée ou de trames vidéo sur laquelle visualiser les pistes. |
| `tracks` | TRACKS | Non | - | Les données de suivi de mouvement contenant les trajectoires des points et les informations de visibilité. Si non fournies, les images d'entrée sont transmises sans modification. |
| `line_resolution` | INT | Oui | 1 - 1024 | Le nombre de trames précédentes à utiliser pour tracer la ligne de trajectoire de chaque piste (par défaut : 24). |
| `circle_size` | INT | Oui | 1 - 128 | La taille du cercle dessiné à la position actuelle de chaque piste (par défaut : 12). |
| `opacity` | FLOAT | Oui | 0.0 - 1.0 | L'opacité des superpositions de pistes dessinées (par défaut : 0.75). |
| `line_width` | INT | Oui | 1 - 128 | La largeur des lignes utilisées pour tracer les trajectoires des pistes (par défaut : 16). |

**Remarque :** Si le nombre d'images d'entrée ne correspond pas au nombre de trames dans les données `tracks` fournies, la séquence d'images sera répétée pour correspondre à la longueur des pistes.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `IMAGE` | IMAGE | La séquence d'images avec les données de suivi de mouvement visualisées sous forme de superpositions. Si aucune `tracks` n'a été fournie, les images d'entrée originales sont retournées. |

---
**Source fingerprint (SHA-256):** `b32169a8c9d3a2dd74463c81f6bd7d9a4bc66486af156843f32b0874f0eaeb8f`
