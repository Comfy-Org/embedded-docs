# Créer un masque coloré SCAIL-2

Ce nœud génère des masques colorés à partir des données de suivi SAM3, qui sont utilisés par le nœud WanSCAILToVideo. Il traite les données de suivi d'une vidéo de pose pilote et, en option, d'une image de référence, en attribuant des couleurs cohérentes à chaque personne suivie dans les deux sorties.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `données_de_suivi_conduite` | Suivi SAM3 de la vidéo de pose pilote. Sera rendu dans la sortie pose_video_mask. | SAM3_TRACK_DATA | Oui | - |
| `données_de_suivi_référence` | Suivi SAM3 de la ou des image(s) de référence (une identité par objet, colorées dans l'ordre du lot), ou un MASK simple du sujet de référence (rendu comme une seule identité). | SAM3_TRACK_DATA ou MASK | Non | - |
| `indices_objets` | Liste d'indices de personnes à inclure, séparés par des virgules (par ex. '0,2,3'). Appliquée à la fois aux masques de référence et de vidéo de pose. Vide = tous. (par défaut : "") | STRING | Oui | - |
| `trier_par` | Ordre dans lequel les couleurs de la palette sont attribuées aux objets suivis (appliqué à la fois à la référence et à la vidéo de pose afin que chaque identité conserve la même couleur). Les objets qui apparaissent dans les premières images viennent toujours en premier ; au sein d'une image, left_to_right = l'objet le plus à gauche (par centroïde lors de sa première apparition) reçoit la première couleur, area = le plus grand objet (par aire du masque lors de sa première apparition) reçoit la première couleur ; none = conserve l'ordre de SAM3. (par défaut : "left_to_right") | COMBO | Oui | `"none"`<br>`"left_to_right"`<br>`"area"` |
| `mode_remplacement` | False = Mode Animation (pose_video_mask a un fond noir, reference_image_mask a un fond blanc). True = Mode Remplacement (pose_video_mask a un fond blanc, reference_image_mask a un fond noir). (par défaut : False) | BOOLEAN | Oui | False<br>True |

Remarque : `object_indices` accepte uniquement des chiffres séparés par des virgules ; les entrées non numériques et les indices hors plage sont ignorés. Lorsque `ref_track_data` n'est pas fourni, la sortie `reference_image_mask` est un remplissage uni utilisant la couleur d'arrière-plan de référence (blanc en Mode Animation, noir en Mode Remplacement).

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `pose_video_mask` | Masque coloré rendu à partir des données de suivi de la vidéo de pose pilote. La couleur d'arrière-plan suit le paramètre replacement_mode. | IMAGE |
| `reference_image_mask` | Masque coloré rendu à partir des données de suivi de l'image de référence. L'arrière-plan est noir en Mode Remplacement et blanc en Mode Animation. Si aucune donnée de référence n'est fournie, renvoie un remplissage uni correspondant à la couleur d'arrière-plan de référence. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SCAIL2ColoredMask/fr.md)

---
**Source fingerprint (SHA-256):** `ce0669ad0ed3c76cc18ef0ee7b620f5aa6eaa1e5b96c189941c0a5b744c3351f`
