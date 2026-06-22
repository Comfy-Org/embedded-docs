# SDPoseDrawKeypoints

Le nœud SDPoseDrawKeypoints prend des données d'estimation de pose (points clés) et les dessine sous forme de squelette visuel sur une toile vierge. Il permet de sélectionner différentes parties de la pose à dessiner, comme le corps, les mains, le visage et les pieds, avec des largeurs de ligne et des tailles de points personnalisables. L'image résultante peut être utilisée pour la visualisation ou comme entrée pour d'autres nœuds nécessitant une image de pose.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `keypoints` | Les données de points clés de pose à dessiner. Ces données proviennent généralement d'un nœud de détection de pose. | POSE_KEYPOINT | Oui | - |
| `draw_body` | Contrôle si le squelette principal du corps est dessiné (par défaut : Vrai). | BOOLEAN | Non | - |
| `draw_hands` | Contrôle si les points clés des mains sont dessinés (par défaut : Vrai). | BOOLEAN | Non | - |
| `draw_face` | Contrôle si les points clés du visage sont dessinés (par défaut : Vrai). | BOOLEAN | Non | - |
| `draw_feet` | Contrôle si les points clés des pieds sont dessinés (par défaut : Faux). | BOOLEAN | Non | - |
| `stick_width` | La largeur des lignes utilisées pour dessiner le squelette du corps (par défaut : 4). | INT | Non | 1 à 10 |
| `face_point_size` | La taille des points utilisés pour dessiner les points clés du visage (par défaut : 3). | INT | Non | 1 à 10 |
| `score_threshold` | Le score de confiance minimum qu'un point clé doit avoir pour être dessiné. Les points clés avec un score inférieur à cette valeur sont ignorés (par défaut : 0,3). | FLOAT | Non | 0,0 à 1,0 |

**Remarque :** Si l'entrée `keypoints` est vide ou `None`, le nœud produira une image vierge de 64x64 pixels.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Une image avec les points clés de pose dessinés. Les dimensions de l'image correspondent à la `canvas_height` et `canvas_width` spécifiées dans les données de points clés d'entrée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseDrawKeypoints/fr.md)

---
**Source fingerprint (SHA-256):** `c01397ed3608b65b737b60c2ae50919e0217cfe63b3695b68f176c2d69faa9c1`
