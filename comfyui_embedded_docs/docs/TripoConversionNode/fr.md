> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/fr.md)

Voici la traduction en français de la documentation du nœud TripoConversionNode :

Le TripoConversionNode convertit des modèles 3D entre différents formats de fichiers à l'aide de l'API Tripo. Il prend un ID de tâche provenant d'une opération Tripo précédente (génération de modèle, rigging ou retargeting) et convertit le modèle résultant dans le format souhaité avec diverses options d'exportation.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `original_model_task_id` | MODEL_TASK_ID,RIG_TASK_ID,RETARGET_TASK_ID | Oui | MODEL_TASK_ID<br>RIG_TASK_ID<br>RETARGET_TASK_ID | L'ID de tâche d'une opération Tripo précédente (génération de modèle, rigging ou retargeting) |
| `format` | COMBO | Oui | GLTF<br>USDZ<br>FBX<br>OBJ<br>STL<br>3MF | Le format de fichier cible pour le modèle 3D converti |
| `quad` | BOOLEAN | Non | Vrai/Faux | Convertir les triangles en quads (par défaut : Faux) |
| `face_limit` | INT | Non | -1 à 2000000 | Nombre maximal de faces dans le modèle de sortie, utiliser -1 pour aucune limite (par défaut : -1) |
| `texture_size` | INT | Non | 128 à 4096 | Taille des textures de sortie en pixels (par défaut : 4096) |
| `texture_format` | COMBO | Non | BMP<br>DPX<br>HDR<br>JPEG<br>OPEN_EXR<br>PNG<br>TARGA<br>TIFF<br>WEBP | Format des textures exportées (par défaut : JPEG) |
| `force_symmetry` | BOOLEAN | Non | Vrai/Faux | Forcer la symétrie sur le modèle (par défaut : Faux) |
| `flatten_bottom` | BOOLEAN | Non | Vrai/Faux | Aplatir le bas du modèle (par défaut : Faux) |
| `flatten_bottom_threshold` | FLOAT | Non | 0.0 à 1.0 | Seuil pour l'aplatissement du bas (par défaut : 0.0) |
| `pivot_to_center_bottom` | BOOLEAN | Non | Vrai/Faux | Déplacer le point de pivot au centre bas du modèle (par défaut : Faux) |
| `scale_factor` | FLOAT | Non | 0.0 et plus | Facteur d'échelle à appliquer au modèle (par défaut : 1.0) |
| `with_animation` | BOOLEAN | Non | Vrai/Faux | Inclure les données d'animation dans l'exportation (par défaut : Faux) |
| `pack_uv` | BOOLEAN | Non | Vrai/Faux | Empaqueter les coordonnées UV (par défaut : Faux) |
| `bake` | BOOLEAN | Non | Vrai/Faux | Cuire les textures (par défaut : Faux) |
| `part_names` | STRING | Non | Liste séparée par des virgules | Liste séparée par des virgules des noms de pièces à inclure dans l'exportation (par défaut : "") |
| `fbx_preset` | COMBO | Non | blender<br>mixamo<br>3dsmax | Préréglage d'exportation FBX à utiliser (par défaut : blender) |
| `export_vertex_colors` | BOOLEAN | Non | Vrai/Faux | Exporter les couleurs des sommets (par défaut : Faux) |
| `export_orientation` | COMBO | Non | align_image<br>default | Mode d'orientation d'exportation (par défaut : default) |
| `animate_in_place` | BOOLEAN | Non | Vrai/Faux | Animer le modèle sur place (par défaut : Faux) |

**Remarque :** Le `original_model_task_id` doit être un ID de tâche valide provenant d'une opération Tripo précédente (génération de modèle, rigging ou retargeting). Les paramètres marqués comme "avancés" sont facultatifs et ne nécessitent une configuration que pour des besoins d'exportation spécifiques.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| *Aucune sortie nommée* | - | Ce nœud traite la conversion de manière asynchrone et renvoie le résultat via le système d'API Tripo |

---
**Source fingerprint (SHA-256):** `b11ecab98701b7153a350f5e4980ddc2f446c0a12be3402ca98a5e6de60bd7ce`
