# WanMoveVisualizeTracks

Le nœud WanMoveVisualizeTracks dessine des données de suivi de mouvement sur une séquence d'images ou de trames vidéo. Il place un cercle à la position actuelle de chaque point suivi et trace une ligne de trajectoire en fondu montrant où le point s'est déplacé au cours des trames récentes. Si aucune donnée de suivi n'est fournie, les images d'entrée sont renvoyées inchangées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `images` | La séquence d'images ou de trames vidéo d'entrée sur laquelle les trajectoires seront visualisées. | IMAGE | Oui | - |
| `tracks` | Les données de suivi de mouvement contenant les positions des points et les informations de visibilité. Si non fournies, les images d'entrée sont transmises telles quelles. | TRACKS | Non | - |
| `line_resolution` | Le nombre de trames précédentes à utiliser pour dessiner la ligne de trajectoire de chaque point suivi (défaut : 24). | INT | Oui | 1 - 1024 |
| `circle_size` | La taille du cercle dessiné à la position actuelle de chaque point suivi (défaut : 12). | INT | Oui | 1 - 128 |
| `opacity` | L'opacité des superpositions de trajectoires dessinées (défaut : 0,75). | FLOAT | Oui | 0.0 - 1.0 |
| `line_width` | La largeur des lignes utilisées pour dessiner les trajectoires des points (défaut : 16). | INT | Oui | 1 - 128 |

**Remarque :** Si le nombre d'images d'entrée ne correspond pas au nombre de trames dans les données `tracks` fournies, la séquence d'images d'entrée est répétée pour s'aligner sur les données de suivi.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `IMAGE` | La séquence d'images avec les données de suivi de mouvement dessinées en superposition. Si aucun `tracks` n'a été fourni, les images d'entrée originales sont renvoyées inchangées. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveVisualizeTracks/fr.md)

---
**Source fingerprint (SHA-256):** `d94bfde28dfdad682edcc81b1c63408f1352e0dbc94af4d043d750e8cd4c099b`
