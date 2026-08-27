# SDPoseDrawKeypoints

Le nœud SDPoseDrawKeypoints prend des données d'estimation de pose (keypoints) et les dessine sous forme de squelette visuel sur un canevas vierge. Il permet de dessiner sélectivement différentes parties de la pose, telles que le corps, la tête, les mains, le visage et les pieds, avec des largeurs de ligne et des tailles de points personnalisables. L'image résultante peut être utilisée pour la visualisation ou comme entrée pour d'autres nœuds nécessitant une image de pose.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `keypoints` | Les données de keypoints de pose à dessiner. Ces données proviennent généralement d'un nœud de détection de pose et peuvent contenir une ou plusieurs images. | POSE_KEYPOINT | Oui | - |
| `draw_body` | Contrôle si le squelette principal du corps est dessiné (par défaut : True). | BOOLEAN | Non | - |
| `draw_hands` | Contrôle si les keypoints des mains sont dessinés (par défaut : True). | BOOLEAN | Non | - |
| `draw_face` | Contrôle si les keypoints du visage sont dessinés (par défaut : True). | BOOLEAN | Non | - |
| `draw_feet` | Contrôle si les keypoints des pieds sont dessinés (par défaut : False). | BOOLEAN | Non | - |
| `stick_width` | La largeur des lignes utilisées pour dessiner le squelette du corps et de la tête (par défaut : 4). | INT | Non | 1 à 10 |
| `face_point_size` | La taille des points utilisés pour dessiner les keypoints du visage (par défaut : 3). | INT | Non | 1 à 10 |
| `score_threshold` | Le score de confiance minimal qu'un keypoint doit avoir pour être dessiné. Les keypoints dont les scores sont inférieurs à cette valeur sont ignorés (par défaut : 0.3). | FLOAT | Non | 0.0 à 1.0 |
| `dessiner_tête` | Contrôle si les keypoints de la tête (nez, yeux, oreilles) sont dessinés (par défaut : True). | BOOLEAN | Non | - |

**Remarque :** Si l'entrée `keypoints` est vide ou `None`, le nœud produira une image vide de 64x64.

**Remarque :** `draw_body` et `draw_head` fonctionnent indépendamment. Lorsque `draw_head` est désactivé, les keypoints de la tête ne sont pas dessinés même si `draw_body` est activé. Lorsque `draw_body` est désactivé mais que `draw_head` est activé, seuls les keypoints de la tête et le point du cou sont dessinés. Si les deux sont désactivés, aucun keypoint du corps ou de la tête n'est dessiné.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Une image avec les keypoints de pose dessinés. Les dimensions de l'image correspondent à `canvas_height` et `canvas_width` spécifiés dans les données de keypoints d'entrée. Lorsque l'entrée contient plusieurs images, un lot d'images est renvoyé. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseDrawKeypoints/fr.md)

---
**Source fingerprint (SHA-256):** `2b2b9530b55c56e278666bd5d139bb6a1bb503b75b948a89266b9982b5a295e4`
