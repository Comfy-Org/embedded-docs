# Rendu de la pose corporelle 3D

Rend les données de pose corporelle 3D en une image à l'aide d'un style sélectionnable. Le nœud accepte les données de pose du suivi de corps SAM3D (MHR) ou d'un rig externe en Y-up tel que Kimodo, et peut composer le résultat sur une image d'arrière-plan facultative (ou une toile noire lorsqu'aucune n'est fournie). Les styles de rendu disponibles incluent un maillage 3D ombré, une silhouette binaire, des squelettes de style OpenPose en 2D et 3D, et des capsules corporelles de style SCAIL.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `render_style` | Mode de rendu. 'mesh' = maillage 3D MHR rastérisé à travers la caméra. 'silhouette' = masque binaire du maillage. 'openpose_2d' = squelette 2D plat. 'openpose_3d' = squelette OpenPose en modèle 3D à ombrage plat. 'scail' = capsules 3D SCAIL. (défaut : "mesh") | DYNAMIC_COMBO | Oui | "mesh"<br>"silhouette"<br>"openpose_2d"<br>"openpose_3d"<br>"scail" |
| `pose_data` | Données de pose MHR, ou données de pose d'un rig externe en Y-up (KimodoSample). Tous les styles de rendu fonctionnent pour les rigs externes qui portent des cartes d'articulations OpenPose dans leur `_skeleton_override` (c'est le cas de KimodoSample). | MHR_POSE_DATA ou KIMODO_POSE_DATA | Oui | — |
| `arrière-plan` | Arrière-plan par image. Omis = toile noire. | IMAGE | Non | — |
| `largeur` | Largeur de sortie en pixels. 0 = utiliser la taille d'image native des données de pose. Si une seule des valeurs width/height est définie, l'autre est dérivée en préservant le rapport d'aspect d'origine. (défaut : 0) | INT | Non | 0 à 16384, step 8 |
| `hauteur` | Hauteur de sortie en pixels. 0 = utiliser la taille d'image native des données de pose. Si une seule des valeurs width/height est définie, l'autre est dérivée en préservant le rapport d'aspect d'origine. (défaut : 0) | INT | Non | 0 à 16384, step 8 |
| `camera_info` | Remplacement de caméra 6DOF libre. Lorsqu'elle est connectée, la pose est reprojetée à travers cette caméra (position/cible/zoom/rotation/FoV) au lieu de celle prédite. | LOAD_3D_CAMERA | Non | — |

### Entrées de maillage

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `shader` | Shader prédéfini. 'normals' = normale de surface courante dans l'espace caméra (convention de normal-map OpenGL Y+ : +X→R, +Y→G, +Z→B). 'rainbow' = dégradé jet selon l'axe Y du corps, style RealisDance ; les variantes 'rainbow_face_*' remplacent les sommets du visage par des couleurs normales/par région ; 'depth' = gris linéaire. (défaut : "default") | DYNAMIC_COMBO | Non | "default"<br>"normals"<br>"rainbow"<br>"rainbow_face_normal"<br>"rainbow_face_semantic"<br>"depth" |
| `rainbow_tilt_z` | Fait pivoter l'axe du dégradé jet autour de Z (avant). Différencie gauche/droite. Disponible uniquement lorsque `shader` est "rainbow", "rainbow_face_normal" ou "rainbow_face_semantic". (défaut : -35.0) | FLOAT | Non | -90.0 à 90.0, step 0.5 |
| `rainbow_tilt_x` | Fait pivoter l'axe du dégradé jet autour de X (droite). Différencie avant/arrière. Disponible uniquement lorsque `shader` est "rainbow", "rainbow_face_normal" ou "rainbow_face_semantic". (défaut : 0.0) | FLOAT | Non | -90.0 à 90.0, step 0.5 |
| `opacity` | Alpha du maillage sur l'image d'arrière-plan, ou sur le noir lorsqu'aucune n'est connectée. (défaut : 1.0) | FLOAT | Non | 0.0 à 1.0, step 0.01 |
| `person_palette_falloff` | Désaturation par personne vers le blanc : la piste k reçoit un mélange pastel (1 - falloff^k) (SCAIL « seconde personne plus douce »). 1.0 = désactivé. (défaut : 0.6) | FLOAT | Non | 0.1 à 1.0, step 0.05 |
| `region` | 'hands_only' filtre les faces via le `hand_vert_mask` précalculé (poids LBS par rapport aux points clés de main canoniques) — isole le maillage de la main pour le débogage. Revient au maillage complet si le masque est manquant. (défaut : "full_body") | COMBO | Non | "full_body"<br>"hands_only" |

### Entrées de silhouette

Lorsque `render_style` est "silhouette", le nœud rend un masque binaire du maillage 3D. Ce mode n'a aucun paramètre supplémentaire.

### Entrées OpenPose 2D

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `marker_radius_px` | Rayon des points clés du corps (px). (défaut : 4) | INT | Non | 1 à 32, step 1 |
| `stick_width_px` | Demi-largeur de l'ellipse des membres du corps (px). Le défaut DWPose = 4. (défaut : 4) | INT | Non | 1 à 32, step 1 |
| `limb_alpha` | Alpha par membre. Défaut DWPose = 0,6. (défaut : 0,6) | FLOAT | Non | 0.0 à 1.0, step 0.05 |
| `face_style` | 'full' = tous les points de repère du visage (sapiens-238 si présent, sinon repli rig ~30). 'eyes_mouth' = sous-ensemble de repli rig (~12 points : yeux + lèvres externes uniquement). 'disabled' = aucun point du visage. (défaut : "disabled") | COMBO | Non | "disabled"<br>"full"<br>"eyes_mouth" |
| `hand_style` | Dessine les points clés des mains 21+21 + les traits. 'disabled' = pas de mains. 'dwpose' = points bleu uni ; 'openpose' = points arc-en-ciel. (défaut : "disabled") | COMBO | Non | "disabled"<br>"dwpose"<br>"openpose" |
| `person_palette_falloff` | Désaturation par personne : la piste k se mélange vers le blanc par 1 - falloff^k. La piste 0 reste vive ; 1,0 désactive la désaturation. (défaut : 0,6) | FLOAT | Non | 0.1 à 1.0, step 0.05 |

### Entrées OpenPose 3D

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `radius_m` | Rayon des capsules des membres en mètres (fin = en forme de bâton). (défaut : 0,015) | FLOAT | Non | 0.004 à 0.1, step 0.001 |
| `include_hands` | Dessine les points clés des mains 21+21 sous forme de capsules 3D. (défaut : True) | BOOLEAN | Non | True or False |
| `person_palette_falloff` | Désaturation par personne : la piste k se mélange vers le blanc par 1 - falloff^k. La piste 0 reste vive ; 1,0 désactive la désaturation. (défaut : 0,6) | FLOAT | Non | 0.1 à 1.0, step 0.05 |

### Entrées SCAIL

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `radius_m` | Rayon des capsules en mètres (référence SCAIL : ~0,022 m). (défaut : 0,022) | FLOAT | Non | 0.005 à 0.2, step 0.001 |
| `hand_style` | Compose des mains OpenPose 2D par-dessus le corps en capsules 3D (correspond à SCAIL — pas de capsules de mains 3D). 'disabled' = pas de mains. 'dwpose' = points de mains bleu uni ; 'openpose' = points arc-en-ciel. Les traits restent arc-en-ciel par doigt dans les deux cas. (défaut : "dwpose") | COMBO | Non | "disabled"<br>"dwpose"<br>"openpose" |
| `face_style` | 'full' = tous les points de repère du visage (sapiens-238 si présent, sinon repli rig ~30). 'eyes_mouth' = sous-ensemble de repli rig (~12 points : yeux + lèvres externes uniquement). 'disabled' = aucun point du visage. (défaut : "disabled") | COMBO | Non | "disabled"<br>"full"<br>"eyes_mouth" |
| `person_palette_falloff` | Désaturation par personne : la piste k se mélange vers le blanc par 1 - falloff^k. La piste 0 reste vive ; 1,0 désactive la désaturation. (défaut : 0,6) | FLOAT | Non | 0.1 à 1.0, step 0.05 |

### Remarques

- Si `width` et `height` sont tous deux à 0, la sortie utilise la taille d'image native des données de pose. Si une seule d'entre elles est définie, l'autre est dérivée en préservant le rapport d'aspect d'origine. Un `background` connecté est redimensionné pour correspondre à la résolution de rendu.
- Lorsque `camera_info` est connectée, la pose est reprojetée à travers cette caméra au lieu de celle prédite.
- En mode maillage, `rainbow_tilt_z` et `rainbow_tilt_x` ne sont disponibles que lorsque `shader` est défini sur "rainbow", "rainbow_face_normal" ou "rainbow_face_semantic".
- En mode maillage, lorsque `region` est "hands_only", le filtre de région des mains nécessite que les données de pose contiennent un masque de sommets des mains ; si le masque est manquant, le maillage complet est rendu à la place.
- En mode scail, les mains sont toujours dessinées en superposition 2D ; il n'y a pas de capsules de mains 3D.
- Lorsque la résolution de sortie diffère de la résolution native des données de pose, les tailles des marqueurs et des traits openpose_2d sont mises à l'échelle proportionnellement.
- Si l'arrière-plan a moins d'images que les données de pose, la dernière image d'arrière-plan est réutilisée pour les images restantes.
- La sortie contient une image par image de pose en entrée. Si les données de pose ne contiennent aucune image, une seule image noire est renvoyée.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | Les images rendues : les données de pose dessinées dans le style de rendu sélectionné, composées sur l'arrière-plan lorsqu'il est connecté, ou sur le noir sinon. Une image par image de pose en entrée, renvoyée comme une seule image groupée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Render/fr.md)

---
**Source fingerprint (SHA-256):** `96556283cf07727e6b4bb3549537bf925ed771bab8607f65c93ab54a5f0e9ba5`
