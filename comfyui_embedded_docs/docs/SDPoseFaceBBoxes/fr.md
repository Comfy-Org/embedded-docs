> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseFaceBBoxes/fr.md)

## Vue d'ensemble

Le nœud SDPoseFaceBBoxes traite les données de points clés de pose pour détecter et générer des boîtes englobantes autour des visages humains. Il analyse les points clés 2D du visage pour chaque personne dans une image, calcule une boîte englobante basée sur ces points, et peut ajuster la taille et la forme de la boîte. Les boîtes englobantes résultantes sont formatées pour être compatibles avec d'autres nœuds du flux de travail SDPose, tels que le SDPoseKeypointExtractor.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `keypoints` | POSE_KEYPOINT | Oui | - | Les données de points clés de pose contenant des informations sur les personnes détectées et leurs repères corporels/visuels par image. |
| `scale` | FLOAT | Non | 1.0 - 10.0 | Multiplicateur pour la zone de la boîte englobante autour de chaque visage détecté. Une valeur plus grande crée une boîte plus grande. (par défaut : 1.5) |
| `force_square` | BOOLEAN | Non | - | Étend l'axe le plus court de la boîte englobante pour que la zone de recadrage soit toujours carrée. (par défaut : True) |

**Note :** L'entrée `keypoints` doit être dans le format spécifique produit par des nœuds comme SDPoseKeypointExtractor, contenant les données `canvas_height`, `canvas_width` et `people` avec `face_keypoints_2d` pour chaque personne.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `bboxes` | BOUNDINGBOX | Une liste de boîtes englobantes de visages pour chaque image. Chaque boîte englobante est définie par ses coordonnées du coin supérieur gauche (`x`, `y`), `width` (largeur) et `height` (hauteur). Cette sortie est compatible avec l'entrée `bboxes` du nœud SDPoseKeypointExtractor. |