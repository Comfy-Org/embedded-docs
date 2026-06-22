# WanMoveVisualizeTracks

Le nœud WanMoveVisualizeTracks superpose les données de suivi de mouvement sur une séquence d'images ou de trames vidéo. Il dessine des représentations visuelles des points suivis, incluant leurs trajectoires et positions actuelles, rendant les données de mouvement visibles et plus faciles à analyser.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `images` | La séquence d'images d'entrée ou de trames vidéo sur laquelle visualiser les pistes. | IMAGE | Oui | - |
| `pistes` | Les données de suivi de mouvement contenant les trajectoires des points et les informations de visibilité. Si non fournies, les images d'entrée sont transmises sans modification. | TRACKS | Non | - |
| `résolution_de_ligne` | Le nombre de trames précédentes à utiliser pour tracer la ligne de trajectoire de chaque piste (par défaut : 24). | INT | Oui | 1 - 1024 |
| `taille_du_cercle` | La taille du cercle dessiné à la position actuelle de chaque piste (par défaut : 12). | INT | Oui | 1 - 128 |
| `opacité` | L'opacité des superpositions de pistes dessinées (par défaut : 0.75). | FLOAT | Oui | 0.0 - 1.0 |
| `largeur_de_ligne` | La largeur des lignes utilisées pour tracer les trajectoires des pistes (par défaut : 16). | INT | Oui | 1 - 128 |

**Remarque :** Si le nombre d'images d'entrée ne correspond pas au nombre de trames dans les données `tracks` fournies, la séquence d'images sera répétée pour correspondre à la longueur des pistes.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `IMAGE` | La séquence d'images avec les données de suivi de mouvement visualisées sous forme de superpositions. Si aucune `pistes` n'a été fournie, les images d'entrée originales sont retournées. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveVisualizeTracks/fr.md)

---
**Source fingerprint (SHA-256):** `b32169a8c9d3a2dd74463c81f6bd7d9a4bc66486af156843f32b0874f0eaeb8f`
