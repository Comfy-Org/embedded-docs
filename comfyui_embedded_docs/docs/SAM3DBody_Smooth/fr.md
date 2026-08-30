# Lisser les données de pose corporelle SAM3D

Smooth SAM3D Body Pose Data réduit la gigue d'une image à l'autre dans les séquences de pose corporelle 3D en moyennant le mouvement dans le temps. Il applique un lissage complet aux données de caméra et d'apparence, tout en réduisant le lissage de la géométrie du maillage lorsque le sujet tourne rapidement, afin que les rotations rapides ne soient pas aplaties.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `mhr_pose_data` | La séquence de données de pose MHR à lisser, contenant les paramètres de modèle, les paramètres de forme, les paramètres d'expression, la disposition des points clés MHR70 et les données de maillage associées. | MHR_POSE_DATA | Oui | — |
| `intensité` | Force de lissage. 0 = brut, 1 = lissé. (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas de 0.05) |
| `méthode` | gaussian : moyenne pondérée symétrique, meilleur lissage généraliste.<br>savgol : ajustement polynomial glissant, préserve les pics nets. (défaut : « savgol ») | COMBO | Oui | « gaussian »<br>« savgol » |
| `fenêtre` | Fenêtre temporelle en images (valeurs impaires). (défaut : 7) | INT | Oui | 1 à 51 (valeurs impaires, pas de 2) |
| `rotation_threshold_degrees` | Désactive le lissage pour ce taux de rotation de la racine (degré/image) afin de préserver les rotations rapides. 30° convient à la plupart des contenus ; des valeurs faibles peuvent désactiver le lissage sur la gigue ordinaire et affecter silencieusement la qualité. 0 = désactiver. (défaut : 30.0) | FLOAT | Oui | 0.0 à 90.0 (pas de 1.0) |

Remarque : lorsque `strength` est à 0.0 ou moins, ou que `window` est à 1 ou moins, le nœud renvoie les données d'entrée inchangées. L'entrée doit contenir au moins 2 images et des données de points clés ; sinon, le nœud renvoie les données d'entrée inchangées. Lorsque `rotation_threshold_degrees` est à 0.0, l'atténuation du lissage basée sur la rotation est désactivée.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `mhr_pose_data` | La séquence de données de pose MHR lissée, avec une gigue d'image à image réduite. | MHR_POSE_DATA |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Smooth/fr.md)

---
**Source fingerprint (SHA-256):** `a80a1c121f1d2bc49e9112576775588d5deab4690c4cd6ec9c1f98de78457b30`
