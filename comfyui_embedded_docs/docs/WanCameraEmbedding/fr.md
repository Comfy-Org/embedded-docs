# Intégration de caméra Wan

Le nœud WanCameraEmbedding génère des embeddings de trajectoire de caméra à l'aide d'embeddings de Plücker basés sur les paramètres de mouvement de la caméra. Il crée une séquence de poses de caméra simulant différents mouvements de caméra et les convertit en tenseurs d'embedding adaptés aux pipelines de génération vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `pose de caméra` | Le type de mouvement de caméra à simuler (par défaut : "Static") | COMBO | Oui | "Static"<br>"Pan Up"<br>"Pan Down"<br>"Pan Left"<br>"Pan Right"<br>"Zoom In"<br>"Zoom Out"<br>"Anti Clockwise (ACW)"<br>"ClockWise (CW)" |
| `largeur` | La largeur de la sortie en pixels (par défaut : 832, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | La hauteur de la sortie en pixels (par défaut : 480, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `longueur` | La longueur de la séquence de trajectoire de caméra (par défaut : 81, pas : 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `vitesse` | La vitesse du mouvement de la caméra (par défaut : 1.0, pas : 0.1) | FLOAT | Non | 0.0 à 10.0 |
| `fx` | Le paramètre de distance focale x (par défaut : 0.5, pas : 0.000000001) | FLOAT | Non | 0.0 à 1.0 |
| `fy` | Le paramètre de distance focale y (par défaut : 0.5, pas : 0.000000001) | FLOAT | Non | 0.0 à 1.0 |
| `cx` | La coordonnée x du point principal (par défaut : 0.5, pas : 0.01) | FLOAT | Non | 0.0 à 1.0 |
| `cy` | La coordonnée y du point principal (par défaut : 0.5, pas : 0.01) | FLOAT | Non | 0.0 à 1.0 |

Remarque : `fx`, `fy`, `cx` et `cy` sont des paramètres intrinsèques avancés de la caméra. Le paramètre `speed` met à l'échelle l'angle de rotation et la distance de translation du mouvement de caméra sélectionné.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `intégration de caméra` | Le tenseur d'embedding de caméra généré contenant la séquence de trajectoire | TENSOR |
| `largeur` | La valeur de largeur utilisée pour le traitement | INT |
| `hauteur` | La valeur de hauteur utilisée pour le traitement | INT |
| `longueur` | La valeur de longueur utilisée pour le traitement | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraEmbedding/fr.md)

---
**Source fingerprint (SHA-256):** `1a2f98d83d18033581823dee61b5a3686d560c749c55223f81febca89654a29f`
