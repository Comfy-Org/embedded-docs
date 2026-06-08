Voici la traduction en français de la documentation du nœud Kling Camera Controls :

Le nœud Kling Camera Controls vous permet de configurer divers paramètres de mouvement et de rotation de caméra pour créer des effets de contrôle de mouvement dans la génération vidéo. Il fournit des contrôles pour le positionnement, la rotation et le zoom de la caméra afin de simuler différents mouvements de caméra.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `camera_control_type` | Spécifie le type de configuration de contrôle de caméra à utiliser | COMBO | Oui | `"simple"`<br>`"advanced"` |
| `horizontal_movement` | Contrôle le mouvement de la caméra le long de l'axe horizontal (axe x). Une valeur négative indique un déplacement vers la gauche, une valeur positive vers la droite (par défaut : 0.0) | FLOAT | Non | -10.0 à 10.0 |
| `vertical_movement` | Contrôle le mouvement de la caméra le long de l'axe vertical (axe y). Une valeur négative indique un déplacement vers le bas, une valeur positive vers le haut (par défaut : 0.0) | FLOAT | Non | -10.0 à 10.0 |
| `pan` | Contrôle la rotation de la caméra dans le plan vertical (axe x). Une valeur négative indique une rotation vers le bas, une valeur positive vers le haut (par défaut : 0.5) | FLOAT | Non | -10.0 à 10.0 |
| `tilt` | Contrôle la rotation de la caméra dans le plan horizontal (axe y). Une valeur négative indique une rotation vers la gauche, une valeur positive vers la droite (par défaut : 0.0) | FLOAT | Non | -10.0 à 10.0 |
| `roll` | Contrôle l'inclinaison latérale de la caméra (axe z). Une valeur négative indique une rotation antihoraire, une valeur positive une rotation horaire (par défaut : 0.0) | FLOAT | Non | -10.0 à 10.0 |
| `zoom` | Contrôle la modification de la distance focale de la caméra. Une valeur négative indique un champ de vision plus étroit, une valeur positive un champ de vision plus large (par défaut : 0.0) | FLOAT | Non | -10.0 à 10.0 |

**Remarque :** Au moins un des paramètres de contrôle de caméra (`horizontal_movement`, `vertical_movement`, `pan`, `tilt`, `roll` ou `zoom`) doit avoir une valeur non nulle pour que la configuration soit valide.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `camera_control` | Renvoie les paramètres de contrôle de caméra configurés pour une utilisation dans la génération vidéo | CAMERA_CONTROL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControls/fr.md)

---
**Source fingerprint (SHA-256):** `4e1d826518ae17afd2c0aa22ebf6cce67b3ef33bb1730f0ce5ead5b9431cd548`
