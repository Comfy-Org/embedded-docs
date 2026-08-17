# SDPoseDrawKeypoints

Le nœud SDPoseDrawKeypoints prend des données d'estimation de pose (points clés) et les dessine sous forme de squelette visuel sur un canevas vierge. Il vous permet de dessiner sélectivement différentes parties de la pose, telles que le corps, la tête, les mains, le visage et les pieds, avec des largeurs de ligne et des tailles de points personnalisables. L'image résultante peut être utilisée pour la visualisation ou comme entrée pour d'autres nœuds nécessitant une image de pose.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `keypoints` | Les données de points clés de pose à dessiner. Ces données proviennent généralement d'un nœud de détection de pose. | POSE_KEYPOINT | Oui | - |
| `draw_body` | Contrôle si le squelette principal du corps est dessiné (par défaut : True). | BOOLEAN | Non | - |
| `draw_hands` | Contrôle si les points clés des mains sont dessinés (par défaut : True). | BOOLEAN | Non | - |
| `draw_face` | Contrôle si les points clés du visage sont dessinés (par défaut : True). | BOOLEAN | Non | - |
| `draw_feet` | Contrôle si les points clés des pieds sont dessinés (par défaut : False). | BOOLEAN | Non | - |
| `stick_width` | La largeur des lignes utilisées pour dessiner le squelette du corps (par défaut : 4). | INT | Non | 1 à 10 |
| `face_point_size` | La taille des points utilisés pour dessiner les points clés du visage (par défaut : 3). | INT | Non | 1 à 10 |
| `score_threshold` | Le score de confiance minimal qu'un point clé doit avoir pour être dessiné. Les points clés avec des scores inférieurs à cette valeur sont ignorés (par défaut : 0.3). | FLOAT | Non | 0.0 à 1.0 |
| `draw_head` | Contrôle si les points clés de la tête (nez, yeux, oreilles) et les connexions de la tête sont dessinés (par défaut : True). | BOOLEAN | Non | - |

**Remarque :** Si l'entrée `keypoints` est vide ou `None`, le nœud produira une image vide de 64x64.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Une image avec les points clés de pose dessinés. Les dimensions de l'image correspondent à `canvas_height` et `canvas_width` spécifiés dans les données de points clés d'entrée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseDrawKeypoints/fr.md)

---
**Source fingerprint (SHA-256):** `2b2b9530b55c56e278666bd5d139bb6a1bb503b75b948a89266b9982b5a295e4`
