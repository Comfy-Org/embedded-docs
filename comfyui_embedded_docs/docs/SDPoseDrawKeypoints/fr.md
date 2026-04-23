> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseDrawKeypoints/fr.md)

Le nœud SDPoseDrawKeypoints prend des données d'estimation de pose (points clés) et les dessine sous forme de squelette visuel sur un canevas vierge. Il permet de dessiner sélectivement différentes parties de la pose, comme le corps, les mains, le visage et les pieds, avec des largeurs de ligne et des tailles de point personnalisables. L'image résultante peut être utilisée pour la visualisation ou comme entrée pour d'autres nœuds nécessitant une image de pose.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `keypoints` | POSE_KEYPOINT | Oui | - | Les données de points clés de pose à dessiner. Ces données proviennent généralement d'un nœud de détection de pose. |
| `draw_body` | BOOLEAN | Non | - | Contrôle si le squelette principal du corps est dessiné (par défaut : True). |
| `draw_hands` | BOOLEAN | Non | - | Contrôle si les points clés des mains sont dessinés (par défaut : True). |
| `draw_face` | BOOLEAN | Non | - | Contrôle si les points clés du visage sont dessinés (par défaut : True). |
| `draw_feet` | BOOLEAN | Non | - | Contrôle si les points clés des pieds sont dessinés (par défaut : False). |
| `stick_width` | INT | Non | 1 à 10 | La largeur des lignes utilisées pour dessiner le squelette du corps (par défaut : 4). |
| `face_point_size` | INT | Non | 1 à 10 | La taille des points utilisés pour dessiner les points clés du visage (par défaut : 3). |
| `score_threshold` | FLOAT | Non | 0.0 à 1.0 | Le score de confiance minimum qu'un point clé doit avoir pour être dessiné. Les points clés avec des scores inférieurs à cette valeur sont ignorés (par défaut : 0.3). |

**Note :** Si l'entrée `keypoints` est vide ou `None`, le nœud produira une image vierge de 64x64 pixels.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | IMAGE | Une image avec les points clés de pose dessinés. Les dimensions de l'image correspondent aux `canvas_height` et `canvas_width` spécifiés dans les données de points clés d'entrée. |