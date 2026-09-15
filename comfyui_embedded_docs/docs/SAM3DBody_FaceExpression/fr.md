# Expression faciale vers corps SAM3D

Ce nœud ajoute des expressions faciales à un corps SAM3D en détectant les visages dans une image avec le MediaPipe Face Landmarker, en associant chaque visage détecté à une personne suivie, et en mappant les 52 blendshapes ARKit sur les paramètres d’expression à 72 axes de MHR. Il relance ensuite le modèle de corps afin que les sommets du maillage de sortie et les points clés reflètent la nouvelle expression.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `sam3d_body_model` | Le modèle de corps SAM3D contenant le détecteur de repères faciaux utilisé pour détecter les visages et régénérer le maillage du corps. | SAM3D_BODY_MODEL | Oui | - |
| `mhr_pose_data` | Données de pose contenant, pour chaque image, les personnes suivies avec leurs boîtes englobantes, points clés et paramètres d’expression. Le nœud associe chaque visage détecté à une personne et écrit les paramètres d’expression mis à jour dans ces données. | MHR_POSE_DATA | Oui | - |
| `image` | Images utilisées pour détecter les visages. Si le lot d’images contient moins d’images que les données de pose, la dernière image est réutilisée pour les images restantes. | IMAGE | Oui | - |
| `strength` | Multiplicateur global appliqué à tous les blendshapes. >1 exagère. Défaut : 1.0. | FLOAT | Non | 0.0 à 4.0 (pas 0.05, défaut 1.0) |
| `mouth_strength` | Multiplicateur appliqué aux formes de bouche/mâchoire. La valeur jawOpen de MediaPipe sature près de 1.0. Défaut : 1.0. | FLOAT | Non | 0.0 à 4.0 (pas 0.05, défaut 1.0) |
| `eye_strength` | Multiplicateur appliqué aux formes des yeux. MediaPipe dépasse rarement 0.5 ; un facteur 2-3x est souvent nécessaire. Défaut : 2.0. | FLOAT | Non | 0.0 à 4.0 (pas 0.05, défaut 2.0) |
| `brow_strength` | Multiplicateur appliqué aux formes de sourcils/joues/rictus. Les sorties MediaPipe sont ~0.1-0.3 ; un facteur 2-3x. Défaut : 2.0. | FLOAT | Non | 0.0 à 4.0 (pas 0.05, défaut 2.0) |
| `input_threshold` | Zone morte sur la sortie brute de MediaPipe (en dessous = zéro, au-dessus = remappage linéaire). Défaut : 0.02. | FLOAT | Non | 0.0 à 0.5 (pas 0.01, défaut 0.02) |
| `blendshape_smooth_window` | Fenêtre gaussienne appliquée au signal par image de MediaPipe avant le mappage MHR. La sortie brute de MediaPipe oscille de 30 à 70 % d’une image à l’autre sur des visages statiques. 1 = désactivé. Utiliser des valeurs impaires. Défaut : 7. | INT | Non | 1 à 31 (pas 2, défaut 7) |

Remarque : une soustraction de ligne de base par clip est appliquée uniquement lorsqu’au moins 30 images du clip contiennent des personnes détectées. Les lacunes de détection allant jusqu’à 12 images par personne sont comblées par interpolation.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `mhr_pose_data` | Les données de pose mises à jour. Les paramètres d’expression de chaque personne suivie sont remplacés par l’expression faciale mappée, et les sommets du maillage ainsi que les points clés sont régénérés pour correspondre. | MHR_POSE_DATA |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_FaceExpression/fr.md)

---
**Source fingerprint (SHA-256):** `b2299e51be3556e639d5b04fcbee541ecf41e0d84c2c8a0fd4e211b2f6caba0b`
