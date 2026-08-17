# Intégration de caméra Wan

Le nœud WanCameraEmbedding génère des plongements de trajectoire de caméra à l'aide de plongements de Plücker basés sur les paramètres de mouvement de la caméra. Il crée une séquence de poses de caméra qui simulent différents mouvements de caméra et les convertit en tenseurs de plongement adaptés aux pipelines de génération vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `camera_pose` | Le type de mouvement de caméra à simuler (par défaut : « Static ») | COMBO | Oui | « Static »<br>« Pan Up »<br>« Pan Down »<br>« Pan Left »<br>« Pan Right »<br>« Zoom In »<br>« Zoom Out »<br>« Anti Clockwise (ACW) »<br>« ClockWise (CW) » |
| `width` | La largeur de la sortie en pixels (par défaut : 832, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `height` | La hauteur de la sortie en pixels (par défaut : 480, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `length` | La longueur de la séquence de trajectoire de caméra (par défaut : 81, pas : 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `speed` | La vitesse du mouvement de caméra (par défaut : 1.0, pas : 0.1) | FLOAT | Non | 0.0 à 10.0 |
| `fx` | Le paramètre de distance focale x (par défaut : 0.5, pas : 0.000000001) | FLOAT | Non | 0.0 à 1.0 |
| `fy` | Le paramètre de distance focale y (par défaut : 0.5, pas : 0.000000001) | FLOAT | Non | 0.0 à 1.0 |
| `cx` | La coordonnée x du point principal (par défaut : 0.5, pas : 0.01) | FLOAT | Non | 0.0 à 1.0 |
| `cy` | La coordonnée y du point principal (par défaut : 0.5, pas : 0.01) | FLOAT | Non | 0.0 à 1.0 |

Remarque : `fx`, `fy`, `cx` et `cy` sont des paramètres avancés. Le paramètre `length` utilise un pas de 4 car la première image de la caméra est répétée en interne, de sorte que la longueur effective de la séquence traitée devient `length + 3`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `camera_embedding` | Le tenseur de plongement de caméra généré contenant la séquence de trajectoire | TENSOR |
| `width` | La valeur de largeur utilisée pour le traitement | INT |
| `height` | La valeur de hauteur utilisée pour le traitement | INT |
| `length` | La valeur de longueur utilisée pour le traitement | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraEmbedding/fr.md)

---
**Source fingerprint (SHA-256):** `1a2f98d83d18033581823dee61b5a3686d560c749c55223f81febca89654a29f`
