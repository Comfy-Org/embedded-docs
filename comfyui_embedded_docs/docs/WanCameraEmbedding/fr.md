> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraEmbedding/fr.md)

Le nœud WanCameraEmbedding génère des embeddings de trajectoire de caméra en utilisant des embeddings de Plücker basés sur les paramètres de mouvement de la caméra. Il crée une séquence de poses de caméra qui simulent différents mouvements de caméra et les convertit en tenseurs d'embedding adaptés aux pipelines de génération vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `camera_pose` | COMBO | Oui | "Static"<br>"Pan Up"<br>"Pan Down"<br>"Pan Left"<br>"Pan Right"<br>"Zoom In"<br>"Zoom Out"<br>"Anti Clockwise (ACW)"<br>"ClockWise (CW)" | Le type de mouvement de caméra à simuler (par défaut : "Static") |
| `width` | INT | Oui | 16 à MAX_RESOLUTION | La largeur de la sortie en pixels (par défaut : 832, pas : 16) |
| `height` | INT | Oui | 16 à MAX_RESOLUTION | La hauteur de la sortie en pixels (par défaut : 480, pas : 16) |
| `length` | INT | Oui | 1 à MAX_RESOLUTION | La longueur de la séquence de trajectoire de caméra (par défaut : 81, pas : 4) |
| `speed` | FLOAT | Non | 0.0 à 10.0 | La vitesse du mouvement de la caméra (par défaut : 1.0, pas : 0.1) |
| `fx` | FLOAT | Non | 0.0 à 1.0 | Le paramètre de distance focale x (par défaut : 0.5, pas : 0.000000001) |
| `fy` | FLOAT | Non | 0.0 à 1.0 | Le paramètre de distance focale y (par défaut : 0.5, pas : 0.000000001) |
| `cx` | FLOAT | Non | 0.0 à 1.0 | La coordonnée x du point principal (par défaut : 0.5, pas : 0.01) |
| `cy` | FLOAT | Non | 0.0 à 1.0 | La coordonnée y du point principal (par défaut : 0.5, pas : 0.01) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `camera_embedding` | TENSOR | Le tenseur d'embedding de caméra généré contenant la séquence de trajectoire |
| `width` | INT | La valeur de largeur qui a été utilisée pour le traitement |
| `height` | INT | La valeur de hauteur qui a été utilisée pour le traitement |
| `length` | INT | La valeur de longueur qui a été utilisée pour le traitement |