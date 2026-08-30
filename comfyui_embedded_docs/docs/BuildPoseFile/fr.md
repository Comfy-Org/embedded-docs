# Créer un fichier d’animation 3D

Ce nœud génère un fichier d’animation 3D prêt à enregistrer à partir de données de pose. Vous pouvez exporter un GLB animé selon plusieurs styles visuels — un maillage corporel complet, un aperçu articulations uniquement, un squelette OpenPose ou un rig à capsules SCAIL — ou enregistrer à la place un clip de capture de mouvement BVH. La sortie se connecte à un nœud d’enregistrement de fichier tel que Save 3D Model pour écrire le fichier sur le disque.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `pose_data` | Données de pose 3D. Accepte les données de pose MHR (paramètres de modèle/forme/expression, points clés MHR70, couleurs canoniques, masque de vertex des mains) ou les données de pose Kimodo (rig externe en Y-up avec vertex prédits par frame et caméra). | MHR_POSE_DATA / KIMODO_POSE_DATA | Oui | — |
| `format` | Format de sortie, également transmis à Save 3D Model pour l’écriture sur disque. ‘glb’ = GLB animé (mesh / bones / openpose / scail). ‘bvh’ = clip de capture de mouvement BVH (un seul squelette ; nécessite le modèle). (défaut : glb) | DYNAMIC_COMBO | Oui | "glb"<br>"bvh" |
| `sam3d_body_model` | Modèle corporel SAM3D facultatif. Requis pour les formats ‘bvh’, ‘body_mesh’ et ‘bones_only’ sauf si les données de pose contiennent un remplacement de squelette. | SAM3D_BODY_MODEL | Non | — |
| `fps` | Cadence d’animation. (défaut : 24.0) | FLOAT | Oui | 1.0-240.0 |
| `camera_translation` | Intégrer pred_cam_t dans la translation de la racine : ‘off’ = position de liaison ; ‘centered’ = delta par rapport à la frame 0 ; ‘absolute’ = brut (Z est la profondeur caméra — généralement en mètres). (défaut : off) | COMBO | Oui | "off"<br>"centered"<br>"absolute" |
| `track_index` | Sélection de piste : -1 = toutes les pistes ; ≥0 = piste unique. (défaut : -1) | INT | Oui | -1 à 15 |

### Entrées GLB

Ces entrées apparaissent lorsque `format` est défini sur « glb ».

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `mesh_style` | Style visuel du GLB : ‘body_mesh’ = véritable armature (127 os, skinning, keyframes TRS, 72 morphs faciaux ; nécessite le modèle). ‘bones_only’ = primitives en forme d’os à chaque articulation (armature d’aperçu). ‘openpose’ = squelette 3D OpenPose-18 à partir des points clés. ‘scail’ = rig à capsules 3D SCAIL (cylindres ouverts fermés à fleur par des sphères articulaires). (défaut : body_mesh) | DYNAMIC_COMBO | Oui | "body_mesh"<br>"bones_only"<br>"openpose"<br>"scail" |
| `bone_smooth_window` | Fenêtre de lissage gaussien sur les keyframes de rotation par os / pistes de points clés. 0 = désactivé. 7-15 calme les rotations brusques/instabilités lorsque le lissage en amont manque des pics. (défaut : 0) | INT | Oui | 0-51, step 2 |

#### Entrées Body Mesh

Apparaissent lorsque `mesh_style` est « body_mesh ».

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `bone_vis` | Forme de visualisation des os, skinning rigide sur chaque articulation. ‘off’ = aucune visualisation des os ; ‘octahedrons’ = os directionnels de style Blender. (défaut : off) | DYNAMIC_COMBO | Oui | "off"<br>"octahedrons" |
| `bone_vis_radius_m` | Apparaît lorsque `bone_vis` = « octahedrons ». Rayon en m (rayon de la sphère / demi-largeur de l’octaèdre). (défaut : 0.02) | FLOAT | Oui | 0.005-0.5 |
| `bone_vis_color` | Apparaît lorsque `bone_vis` = « octahedrons ». Couleurs de vertex par os (matériau non éclairé). ‘white’ = aucune, ‘rainbow_y’ = dégradé arc-en-ciel de la tête aux pieds. (défaut : rainbow_y) | COMBO | Oui | "white"<br>"rainbow_y" |
| `shader` | Intégrer des couleurs par vertex correspondant aux shaders du nœud Render (COLOR_0 + KHR_materials_unlit). ‘default’ = aucune couleur. (défaut : default) | DYNAMIC_COMBO | Oui | "default"<br>"rainbow"<br>"rainbow_face_normal"<br>"rainbow_face_semantic" |
| `rainbow_tilt_z` | Apparaît lorsque `shader` est une variante arc-en-ciel. Fait pivoter l’axe du dégradé arc-en-ciel autour de Z (avant). Différencie gauche/droite. (défaut : -35.0) | FLOAT | Oui | -90.0 à 90.0 |
| `rainbow_tilt_x` | Apparaît lorsque `shader` est une variante arc-en-ciel. Fait pivoter l’axe du dégradé arc-en-ciel autour de X (droite). Différencie avant/arrière. (défaut : 0.0) | FLOAT | Oui | -90.0 à 90.0 |
| `person_palette_falloff` | Apparaît lorsque `shader` est une variante arc-en-ciel. Désaturation par personne : chaque piste reçoit un mélange pastel (1 - falloff^k). (défaut : 0.6) | FLOAT | Oui | 0.1-1.0 |

#### Entrées Bones Only

Apparaissent lorsque `mesh_style` est « bones_only ».

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `bone_vis` | Forme de visualisation des os, skinning rigide sur chaque articulation. ‘octahedrons’ = os directionnels de style Blender (articulation → enfant principal). | DYNAMIC_COMBO | Oui | "octahedrons" |
| `bone_vis_radius_m` | Rayon en m (rayon de la sphère / demi-largeur de l’octaèdre). (défaut : 0.02) | FLOAT | Oui | 0.005-0.5 |
| `bone_vis_color` | Couleurs de vertex par os (matériau non éclairé). ‘white’ = aucune, ‘rainbow_y’ = dégradé arc-en-ciel de la tête aux pieds. (défaut : rainbow_y) | COMBO | Oui | "white"<br>"rainbow_y" |

#### Entrées OpenPose

Apparaissent lorsque `mesh_style` est « openpose ».

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `marker_radius_m` | Rayon de la sphère en m. (défaut : 0.010) | FLOAT | Oui | 0.005-0.1 |
| `stick_radius_m` | Demi-largeur du membre en m. Borné automatiquement à longueur de l’os x 0.1. (défaut : 0.008) | FLOAT | Oui | 0.002-0.05 |
| `include_hands` | Ajouter les mains OpenPose 21+21 (poignet + 5 doigts x 4 articulations, base→extrémité) provenant de pred_keypoints_3d. (défaut : False) | BOOLEAN | Oui | True / False |
| `hand_marker_radius_m` | Rayon de la sphère de la main en m. (défaut : 0.005) | FLOAT | Oui | 0.001-0.1 |
| `hand_stick_radius_m` | Demi-largeur du membre de la main en m. (défaut : 0.003) | FLOAT | Oui | 0.001-0.05 |
| `face_style` | Points de repère du contour du visage échantillonnés à partir de pred_vertices à des IDs de vertex fixes du maillage de tête (nécessite canonical_colors sur pose_data). ‘full’ = tous les ~30 points ; ‘eyes_mouth’ = yeux + lèvres externes uniquement. (défaut : disabled) | COMBO | Oui | "disabled"<br>"full"<br>"eyes_mouth" |
| `face_marker_radius_m` | Rayon des points du visage. 0 = auto = 0.3 x marker_radius_m. (défaut : 0.0) | FLOAT | Oui | 0.0-0.05 |

#### Entrées SCAIL

Apparaissent lorsque `mesh_style` est « scail ».

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `stick_radius_m` | Rayon du cylindre en m. Les os sont des cylindres ouverts à rayon constant ; les sphères articulaires (dimensionnées automatiquement pour correspondre) ferment les extrémités ouvertes. Référence SCAIL = 0.0215 m. (défaut : 0.022) | FLOAT | Oui | 0.002-0.1 |
| `marker_radius_m` | Rayon de la sphère articulaire. 0 = auto = stick_radius_m (fermeture affleurante). (défaut : 0.0) | FLOAT | Oui | 0.0-0.1 |
| `material_roughness` | Rugosité PBR. Réf. SCAIL = 0.3. 1 = mat ; 0 = chrome. (défaut : 0.3) | FLOAT | Oui | 0.0-1.0 |
| `include_hands` | Ajouter les points clés de main 21+21 et les bâtonnets à capsule par piste. (défaut : False) | BOOLEAN | Oui | True / False |
| `hand_marker_radius_m` | Rayon de la sphère de la main en m. (défaut : 0.005) | FLOAT | Oui | 0.001-0.05 |
| `hand_stick_radius_m` | Rayon du cylindre de la main en m. (défaut : 0.003) | FLOAT | Oui | 0.001-0.05 |
| `face_style` | Points de repère du contour du visage échantillonnés à partir de pred_vertices (nécessite canonical_colors sur pose_data). ‘full’ = tous les ~30 points ; ‘eyes_mouth’ = yeux + lèvres externes uniquement. (défaut : disabled) | COMBO | Oui | "disabled"<br>"full"<br>"eyes_mouth" |

### Entrées BVH

Apparaissent lorsque `format` est défini sur « bvh ».

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `units` | Unités OFFSET/position BVH. ‘cm’ est la norme mocap. (défaut : cm) | COMBO | Oui | "cm"<br>"m" |

**Remarques :**

- Le format `bvh` et les styles de maillage `body_mesh` et `bones_only` nécessitent l’entrée `sam3d_body_model`, sauf si `pose_data` contient lui-même un remplacement de squelette (un dict `_skeleton_override`, par exemple provenant d’un nœud KimodoSample). Le nœud génère une erreur si aucun des deux n’est disponible. Les styles `openpose` et `scail` sont indépendants du rig et fonctionnent directement à partir des points clés sans le modèle corporel.
- Dans le format `bvh`, la sortie contient un seul squelette. Lorsque `track_index` est -1 (toutes les pistes), la première piste est utilisée.
- Les options `full` et `eyes_mouth` de `face_style` nécessitent `canonical_colors` sur les données de pose, lesquelles sont présentes lorsque les données de pose proviennent du pipeline MHR avec le modèle corporel.
- `bone_smooth_window` progresse par pas de 2 entre 0 et 51.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_3d` | Le fichier d’animation généré : un GLB animé ou un clip de capture de mouvement BVH, prêt à être enregistré sur disque avec un nœud tel que Save 3D Model. | 3D_FILE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BuildPoseFile/fr.md)

---
**Source fingerprint (SHA-256):** `f3672f0749c4f9affcc92da98198c5b142f6fcd9f5e317ab43dd7e53533c0fa3`
