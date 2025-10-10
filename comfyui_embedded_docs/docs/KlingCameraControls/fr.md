> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControls/fr.md)

Le nœud Kling Camera Controls vous permet de configurer divers paramètres de mouvement et de rotation de caméra pour créer des effets de motion control dans la génération vidéo. Il fournit des contrôles pour le positionnement, la rotation et le zoom de la caméra afin de simuler différents mouvements de caméra.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `camera_control_type` | COMBO | Oui | Plusieurs options disponibles | Spécifie le type de configuration de contrôle de caméra à utiliser |
| `horizontal_movement` | FLOAT | Non | -10.0 à 10.0 | Contrôle le mouvement de la caméra le long de l'axe horizontal (axe x). Négatif indique vers la gauche, positif indique vers la droite (par défaut : 0.0) |
| `vertical_movement` | FLOAT | Non | -10.0 à 10.0 | Contrôle le mouvement de la caméra le long de l'axe vertical (axe y). Négatif indique vers le bas, positif indique vers le haut (par défaut : 0.0) |
| `pan` | FLOAT | Non | -10.0 à 10.0 | Contrôle la rotation de la caméra dans le plan vertical (axe x). Négatif indique une rotation vers le bas, positif indique une rotation vers le haut (par défaut : 0.5) |
| `tilt` | FLOAT | Non | -10.0 à 10.0 | Contrôle la rotation de la caméra dans le plan horizontal (axe y). Négatif indique une rotation vers la gauche, positif indique une rotation vers la droite (par défaut : 0.0) |
| `roll` | FLOAT | Non | -10.0 à 10.0 | Contrôle la quantité de roulis de la caméra (axe z). Négatif indique un mouvement antihoraire, positif indique un mouvement horaire (par défaut : 0.0) |
| `zoom` | FLOAT | Non | -10.0 à 10.0 | Contrôle le changement de distance focale de la caméra. Négatif indique un champ de vision plus étroit, positif indique un champ de vision plus large (par défaut : 0.0) |

**Note :** Au moins l'un des paramètres de contrôle de caméra (`horizontal_movement`, `vertical_movement`, `pan`, `tilt`, `roll` ou `zoom`) doit avoir une valeur non nulle pour que la configuration soit valide.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `camera_control` | CAMERA_CONTROL | Retourne les paramètres de contrôle de caméra configurés pour utilisation dans la génération vidéo |