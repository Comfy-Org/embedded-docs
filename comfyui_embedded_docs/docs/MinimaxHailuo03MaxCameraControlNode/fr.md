# MiniMax H3 Max Camera Control

Ce nœud génère une vidéo qui part d'une image fixe et déplace la caméra vers un nouvel angle et une nouvelle distance autour du sujet. L'azimut, l'élévation et la distance décrivent la position finale de la caméra ; la première image reste exactement telle que fournie. Lorsqu'aucun prompt n'est fourni, la scène reste figée et seule la caméra se déplace.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Modèle à utiliser pour la génération vidéo. | DYNAMIC_COMBO | Oui | "MiniMax H3 Max" |

### Entrées MiniMax H3 Max

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | Première image de la vidéo, au moins 256x256 pixels. Le rapport d'aspect doit être compris entre 0,4 et 2,5. | IMAGE | Oui | Image unique |
| `camera_info` | Caméra de fin facultative, par exemple issue de Create Camera Info ou Compose Camera Angle Prompt, avec l'image comme vue de face. Lorsqu'elle est connectée, elle définit l'azimut et l'élévation. | LOAD3D_CAMERA | Non | Informations de caméra |
| `prompt` | Facultatif. Lorsqu'il est vide, la scène reste figée et seule la caméra se déplace. | STRING | Oui | 0 à 50000 caractères |
| `azimuth` | Orbite horizontale autour du sujet à la fin de la vidéo, en degrés par rapport à l'image (par défaut : 90). Les valeurs positives déplacent la caméra vers la droite, de sorte que le sujet tourne vers la gauche du cadre. Il s'agit d'une cible : une orbite de 90 degrés aboutit souvent entre 30 et 90 degrés. Ignoré lorsque `camera_info` est connecté. | INT | Oui | -360 à 360 |
| `elevation` | Angle vertical de la caméra à la fin de la vidéo, en degrés (par défaut : 0). Les valeurs positives regardent vers le bas depuis le dessus, les valeurs négatives regardent vers le haut depuis le dessous. Ignoré lorsque `camera_info` est connecté. | INT | Oui | -90 à 90 |
| `distance` | Distance de la caméra à la fin de la vidéo par rapport à l'image : 1 la conserve, une valeur inférieure à 1 rapproche, une valeur supérieure à 1 éloigne (par défaut : 1.0). | FLOAT | Oui | 0.1 à 10.0 |
| `duration` | Durée de la vidéo de sortie en secondes (par défaut : 5). | INT | Oui | 1 à 15 |
| `resolution` | Résolution de la vidéo de sortie (par défaut : "768P"). | COMBO | Oui | "480P"<br>"768P"<br>"1080P" |
| `prompt_expansion_mode` | Niveau d'effort consacré à la réécriture du prompt avant la génération (par défaut : "balanced"). | COMBO | Oui | "disabled"<br>"balanced"<br>"quality" |
| `seed` | Graine aléatoire. La même requête avec la même graine donne des résultats similaires, mais pas nécessairement identiques (par défaut : 42). | INT | Oui | 0 à 4294967295 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `video` | La vidéo générée avec le mouvement de caméra appliqué. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxCameraControlNode/fr.md)

---
**Source fingerprint (SHA-256):** `d9eed1a3ae91891b974bea39ea00101c0577cf5b204d4c701b13b232e0604153`
