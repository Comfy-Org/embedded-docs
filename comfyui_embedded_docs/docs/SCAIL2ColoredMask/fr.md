# SCAIL2ColoredMask

Ce nœud génère des masques colorés à partir des données de suivi SAM3, qui sont ensuite utilisés par le nœud WanSCAILToVideo. Il traite les données de suivi provenant d'une vidéo de pose dynamique et éventuellement d'une image de référence, en attribuant des couleurs cohérentes à chaque personne suivie dans les deux sorties.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `données_de_suivi_conduite` | Suivi SAM3 de la vidéo de pose dynamique. Sera rendu dans la sortie pose_video_mask. | SAM3_TRACK_DATA | Oui | - |
| `données_de_suivi_référence` | Suivi SAM3 de l'image de référence. | SAM3_TRACK_DATA | Non | - |
| `indices_objets` | Liste d'indices de personnes séparés par des virgules à inclure (ex. '0,2,3'). Appliqué aux masques de référence et de vidéo de pose. Vide = tous. | STRING | Oui | - |
| `trier_par` | Ordre d'attribution des couleurs de la palette aux objets suivis (appliqué à la fois à la référence et à la vidéo de pose pour que chaque identité conserve la même couleur). left_to_right = l'objet le plus à gauche (par centroïde de la première image) reçoit la première couleur ; area = l'objet le plus grand (par surface du masque de la première image) reçoit la première couleur ; none = conserve l'ordre de SAM3. (par défaut : "left_to_right") | COMBO | Oui | `"none"`<br>`"left_to_right"`<br>`"area"` |
| `mode_remplacement` | False = Mode Animation (pose_video_mask a un fond noir, reference_image_mask a un fond blanc). True = Mode Remplacement (pose_video_mask a un fond blanc, reference_image_mask a un fond noir). (par défaut : False) | BOOLEAN | Oui | False<br>True |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `reference_image_mask` | Masque coloré généré à partir des données de suivi de la vidéo de pose dynamique. La couleur d'arrière-plan suit le paramètre replacement_mode. | IMAGE |
| `reference_image_mask` | Masque coloré généré à partir des données de suivi de l'image de référence. Toujours rendu avec un fond noir conformément à la convention du modèle. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SCAIL2ColoredMask/fr.md)

---
**Source fingerprint (SHA-256):** `c9f6d87410b8bd4082ffb06ef1cf973829566ed222be643db3528cbc241d3c14`
