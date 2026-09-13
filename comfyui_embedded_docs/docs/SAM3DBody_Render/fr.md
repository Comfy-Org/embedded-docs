# Rendu de la pose corporelle 3D

Rend les données de pose corporelle 3D dans une image à l'aide d'un style sélectionnable. Le nœud accepte les données de pose du traqueur corporel SAM3D (MHR) ou d'un rig externe orienté Y-up tel que Kimodo, et peut composer le résultat sur une image d'arrière-plan facultative (ou sur un canevas noir lorsqu'aucune n'est fournie). Les styles de rendu disponibles incluent un maillage 3D ombré, une silhouette binaire, des squelettes de style OpenPose 2D et 3D, ainsi que des capsules corporelles de style SCAIL.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `render_style` | Mode de rendu. 'mesh' = maillage MHR 3D rastérisé via la caméra. 'silhouette' = masque binaire du maillage. 'openpose_2d' = squelette 2D plat. 'openpose_3d' = squelette OpenPose sous forme de modèle 3D à ombrage plat. 'scail' = capsules 3D SCAIL. (défaut : "mesh") | DYNAMIC_COMBO | Oui | "mesh"<br>"silhouette"<br>"openpose_2d"<br>"openpose_3d"<br>"scail" |
| `pose_data` | Données de pose MHR, ou données de pose d'un rig externe orienté Y-up (KimodoSample). Tous les styles de rendu fonctionnent pour les rigs externes qui contiennent des cartes d'articulations OpenPose dans leur `_skeleton_override` (KimodoSample le fait). | MHR_POSE_DATA ou KIMODO_POSE_DATA | Oui | — |
| `background` | Arrière-plan par image. Omis = canevas noir. | IMAGE | Non | — |
| `width` | Largeur de sortie en pixels. 0 = utiliser la taille d'image native (`image_size`) des données de pose. Si une seule des valeurs `width`/`height` est définie, l'autre est dérivée en préservant le rapport d'aspect d'origine. (défaut : 0) | INT | Non | 0 à 16384, pas 8 |
| `height` | Hauteur de sortie en pixels. 0 = utiliser la taille d'image native (`image_size`) des données de pose. Si une seule des valeurs `width`/`height` est définie, l'autre est dérivée en préservant le rapport d'aspect d'origine. (défaut : 0) | INT | Non | 0 à 16384, pas 8 |
| `camera_info` | Remplacement libre de caméra 6DOF. Lorsqu'elle est connectée, la pose est reprojetée via cette caméra (position/cible/zoom/rotation/FoV) au lieu de celle prédite. | LOAD_3D_CAMERA | Non | — |

### Entrées Mesh

Ces paramètres apparaissent lorsque `render_style` vaut "mesh".

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `shader` | Shader prédéfini. 'normals' = normale de surface actuelle dans l'espace caméra (convention de normal-map OpenGL Y+ : +X→R, +Y→G, +Z→B). 'rainbow' = jet Y corporel de style RealisDance ; les variantes 'rainbow_face_*' remplacent les sommets du visage par des couleurs de normale/par région ; 'depth' = gris linéaire. (défaut : "default") | DYNAMIC_COMBO | Non | "default"<br>"normals"<br>"rainbow"<br>"rainbow_face_normal"<br>"rainbow_face_semantic"<br>"depth" |
| `rainbow_tilt_z` | Fait tourner l'axe du jet rainbow autour de Z (avant). Différencie gauche/droite. Disponible uniquement lorsque `shader` vaut "rainbow", "rainbow_face_normal" ou "rainbow_face_semantic". (défaut : -35.0) | FLOAT | Non | -90.0 à 90.0, pas 0.5 |
| `rainbow_tilt_x` | Fait tourner l'axe du jet rainbow autour de X (droite). Différencie avant/arrière. Disponible uniquement lorsque `shader` vaut "rainbow", "rainbow_face_normal" ou "rainbow_face_semantic". (défaut : 0.0) | FLOAT | Non | -90.0 à 90.0, pas 0.5 |
| `opacity` | Alpha du maillage sur l'image d'arrière-plan, ou sur noir lorsqu'aucune n'est connectée. (défaut : 1.0) | FLOAT | Non | 0.0 à 1.0, pas 0.01 |
| `person_palette_falloff` | Désaturation par personne vers le blanc : la piste k reçoit un mélange pastel (1 - falloff^k) (le « softer second person » de SCAIL). 1.0 = désactivé. (défaut : 0.6) | FLOAT | Non | 0.1 à 1.0, pas 0.05 |
| `region` | 'hands_only' filtre les faces via le `hand_vert_mask` précalculé (poids LBS par rapport aux KPs canoniques de la main) — isole le maillage de la main pour le débogage. Revient au maillage complet si le masque est absent. (défaut : "full_body") | COMBO | Non | "full_body"<br>"hands_only" |

### Entrées Silhouette

Lorsque `render_style` vaut "silhouette", le nœud rend un masque binaire du maillage 3D. Ce mode n'a aucun paramètre supplémentaire.

### Entrées OpenPose 2D

Ces paramètres apparaissent lorsque `render_style` vaut "openpose_2d".

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `marker_radius_px` | Rayon des points des keypoints corporels (px). (défaut : 4) | INT | Non | 1 à 32, pas 1 |
| `stick_width_px` | Demi-largeur de l'ellipse des membres corporels (px). Défaut DWPose = 4. (défaut : 4) | INT | Non | 1 à 32, pas 1 |
| `limb_alpha` | Alpha par membre. Défaut DWPose = 0.6. (défaut : 0.6) | FLOAT | Non | 0.0 à 1.0, pas 0.05 |
| `face_style` | 'full' = tous les points de repère du visage (sapiens-238 si présent, sinon repli de rig ~30). 'eyes_mouth' = sous-ensemble de repli de rig (~12 points : yeux + lèvres externes uniquement). 'disabled' = aucun point de visage. (défaut : "disabled") | COMBO | Non | "disabled"<br>"full"<br>"eyes_mouth" |
| `hand_style` | Dessine les keypoints de main 21+21 + bâtonnets. 'disabled' = aucune main. 'dwpose' = points bleu uni ; 'openpose' = points arc-en-ciel. (défaut : "disabled") | COMBO | Non | "disabled"<br>"dwpose"<br>"openpose" |
| `person_palette_falloff` | Désaturation par personne : la piste k se mélange vers le blanc selon 1 - falloff^k. La piste 0 reste vive ; 1.0 désactive le falloff. (défaut : 0.6) | FLOAT | Non | 0.1 à 1.0, pas 0.05 |

### Entrées OpenPose 3D

Ces paramètres apparaissent lorsque `render_style` vaut "openpose_3d".

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `radius_m` | Rayon des capsules de membres en mètres (fin = aspect bâton). (défaut : 0.015) | FLOAT | Non | 0.004 à 0.1, pas 0.001 |
| `include_hands` | Dessine les keypoints de main 21+21 sous forme de capsules 3D. (défaut : True) | BOOLEAN | Non | True ou False |
| `person_palette_falloff` | Désaturation par personne : la piste k se mélange vers le blanc selon 1 - falloff^k. La piste 0 reste vive ; 1.0 désactive le falloff. (défaut : 0.6) | FLOAT | Non | 0.1 à 1.0, pas 0.05 |

### Entrées SCAIL

Ces paramètres apparaissent lorsque `render_style` vaut "scail".

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `radius_m` | Rayon des capsules en mètres (référence SCAIL : ~0.022 m). (défaut : 0.022) | FLOAT | Non | 0.005 à 0.2, pas 0.001 |
| `hand_style` | Compose des mains OpenPose 2D par-dessus le corps en capsules 3D (correspond à SCAIL — pas de capsules de main 3D). 'disabled' = aucune main. 'dwpose' = points de main bleu uni ; 'openpose' = points arc-en-ciel. Les bâtonnets restent arc-en-ciel par doigt dans les deux cas. (défaut : "dwpose") | COMBO | Non | "disabled"<br>"dwpose"<br>"openpose" |
| `face_style` | 'full' = tous les points de repère du visage (sapiens-238 si présent, sinon repli de rig ~30). 'eyes_mouth' = sous-ensemble de repli de rig (~12 points : yeux + lèvres externes uniquement). 'disabled' = aucun point de visage. (défaut : "disabled") | COMBO | Non | "disabled"<br>"full"<br>"eyes_mouth" |
| `person_palette_falloff` | Désaturation par personne : la piste k se mélange vers le blanc selon 1 - falloff^k. La piste 0 reste vive ; 1.0 désactive le falloff. (défaut : 0.6) | FLOAT | Non | 0.1 à 1.0, pas 0.05 |

### Remarques

- Si `width` et `height` valent tous les deux 0, la sortie utilise la taille d'image native des données de pose. Si une seule des deux est définie, l'autre est dérivée en préservant le rapport d'aspect d'origine. Un `background` connecté est redimensionné pour correspondre à la résolution de rendu.
- Lorsque `camera_info` est connecté, la pose est reprojetée via cette caméra au lieu de celle prédite.
- En mode mesh, `rainbow_tilt_z` et `rainbow_tilt_x` ne sont disponibles que lorsque `shader` est défini sur "rainbow", "rainbow_face_normal" ou "rainbow_face_semantic".
- En mode mesh, lorsque `region` vaut "hands_only", le filtre de région de main exige que les données de pose contiennent un masque de sommets de main ; si le masque est absent, le maillage complet est rendu à la place.
- En mode scail, les mains sont dessinées comme des superpositions OpenPose 2D par-dessus le corps en capsules 3D plutôt que comme des capsules 3D ; définir `hand_style` sur "disabled" les supprime entièrement.
- Lorsque la résolution de sortie diffère de la résolution native des données de pose, les tailles de marqueur et de bâtonnet de openpose_2d sont mises à l'échelle proportionnellement.
- Si l'arrière-plan contient moins d'images que les données de pose, la dernière image d'arrière-plan est réutilisée pour les images restantes.
- La sortie contient une image par image de pose en entrée. Si les données de pose ne contiennent aucune image, une seule image noire est renvoyée.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | Les images rendues : les données de pose dessinées dans le style de rendu sélectionné, composées sur l'arrière-plan lorsqu'il est connecté, ou sur noir sinon. Une image par image de pose en entrée, renvoyée sous forme d'un seul lot d'images. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Render/fr.md)

---
**Source fingerprint (SHA-256):** `96556283cf07727e6b4bb3549537bf925ed771bab8607f65c93ab54a5f0e9ba5`
