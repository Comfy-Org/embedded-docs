# SDPoseFaceBBoxes

Le nœud SDPoseFaceBBoxes traite les données de points clés de pose pour détecter et générer des boîtes englobantes autour des visages humains. Il analyse les points clés 2D du visage pour chaque personne dans une image, calcule une boîte englobante basée sur ces points et peut ajuster la taille et la forme de la boîte. Les boîtes englobantes résultantes sont formatées pour être compatibles avec d'autres nœuds du workflow SDPose, tels que le SDPoseKeypointExtractor.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `keypoints` | Données de points clés de pose contenant des informations sur les personnes détectées et leurs repères corporels/du visage par image. | POSE_KEYPOINT | Oui | - |
| `scale` | Multiplicateur pour la zone de la boîte englobante autour de chaque visage détecté. Une valeur plus grande crée une boîte plus grande. (par défaut : 1.5) | FLOAT | Non | 1.0 - 10.0 |
| `force_square` | Étend l'axe le plus court de la boîte englobante pour que la zone de recadrage soit toujours carrée. (par défaut : True) | BOOLEAN | Non | - |

**Remarque :** L'entrée `keypoints` doit être au format spécifique produit par des nœuds comme SDPoseKeypointExtractor, contenant `canvas_height`, `canvas_width` et des données `people` avec `face_keypoints_2d` pour chaque personne.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `bboxes` | Une liste de boîtes englobantes de visages pour chaque image. Chaque boîte englobante est définie par ses coordonnées du coin supérieur gauche (`x`, `y`), sa `largeur` et sa `hauteur`. Cette sortie est compatible avec l'entrée `bboxes` du nœud SDPoseKeypointExtractor. | BOUNDINGBOX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseFaceBBoxes/fr.md)

---
**Source fingerprint (SHA-256):** `bffbcddb882f6743a6cace6a4884fa5a257b746897c79ba9260c15260fab874e`
