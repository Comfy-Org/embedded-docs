> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraEmbedding/fr.md)

Le nœud WanCameraEmbedding génère des intégrations de trajectoire de caméra en utilisant des intégrations de Plücker basées sur les paramètres de mouvement de la caméra. Il crée une séquence de poses de caméra qui simulent différents mouvements et les convertit en tenseurs d'intégration adaptés aux pipelines de génération vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `pose de caméra` | COMBO | Oui | "Statique"<br>"Panoramique vers le haut"<br>"Panoramique vers le bas"<br>"Panoramique vers la gauche"<br>"Panoramique vers la droite"<br>"Zoom avant"<br>"Zoom arrière"<br>"Rotation antihoraire (ACW)"<br>"Rotation horaire (CW)" | Le type de mouvement de caméra à simuler (par défaut : "Statique") |
| `largeur` | INT | Oui | 16 à RÉSOLUTION_MAX | La largeur de la sortie en pixels (par défaut : 832, pas : 16) |
| `hauteur` | INT | Oui | 16 à RÉSOLUTION_MAX | La hauteur de la sortie en pixels (par défaut : 480, pas : 16) |
| `longueur` | INT | Oui | 1 à RÉSOLUTION_MAX | La longueur de la séquence de trajectoire de la caméra (par défaut : 81, pas : 4) |
| `vitesse` | FLOAT | Non | 0,0 à 10,0 | La vitesse du mouvement de la caméra (par défaut : 1,0, pas : 0,1) |
| `fx` | FLOAT | Non | 0,0 à 1,0 | Le paramètre de distance focale x (par défaut : 0,5, pas : 0,000000001) |
| `fy` | FLOAT | Non | 0,0 à 1,0 | Le paramètre de distance focale y (par défaut : 0,5, pas : 0,000000001) |
| `cx` | FLOAT | Non | 0,0 à 1,0 | La coordonnée x du point principal (par défaut : 0,5, pas : 0,01) |
| `cy` | FLOAT | Non | 0,0 à 1,0 | La coordonnée y du point principal (par défaut : 0,5, pas : 0,01) |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `largeur` | TENSOR | Le tenseur d'intégration de caméra généré contenant la séquence de trajectoire |
| `hauteur` | INT | La valeur de largeur utilisée pour le traitement |
| `longueur` | INT | La valeur de hauteur utilisée pour le traitement |
| `longueur` | INT | La valeur de longueur utilisée pour le traitement |

---
**Source fingerprint (SHA-256):** `422c4a1fdfb6fd403afac26a609f80cbdbaa87f2c115068de9d7a33c756e71fd`
