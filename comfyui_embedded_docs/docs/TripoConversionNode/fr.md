Voici la traduction en français de la documentation du nœud TripoConversionNode :

Le TripoConversionNode convertit des modèles 3D entre différents formats de fichiers à l'aide de l'API Tripo. Il prend un ID de tâche provenant d'une opération Tripo précédente (génération de modèle, rigging ou retargeting) et convertit le modèle résultant dans le format souhaité avec diverses options d'exportation.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `id_tâche_modèle_original` | L'ID de tâche d'une opération Tripo précédente (génération de modèle, rigging ou retargeting) | MODEL_TASK_ID,RIG_TASK_ID,RETARGET_TASK_ID | Oui | MODEL_TASK_ID<br>RIG_TASK_ID<br>RETARGET_TASK_ID |
| `format` | Le format de fichier cible pour le modèle 3D converti | COMBO | Oui | GLTF<br>USDZ<br>FBX<br>OBJ<br>STL<br>3MF |
| `quad` | Convertir les triangles en quads (par défaut : Faux) | BOOLEAN | Non | Vrai/Faux |
| `limite_faces` | Nombre maximal de faces dans le modèle de sortie, utiliser -1 pour aucune limite (par défaut : -1) | INT | Non | -1 à 2000000 |
| `taille_texture` | Taille des textures de sortie en pixels (par défaut : 4096) | INT | Non | 128 à 4096 |
| `format_texture` | Format des textures exportées (par défaut : JPEG) | COMBO | Non | BMP<br>DPX<br>HDR<br>JPEG<br>OPEN_EXR<br>PNG<br>TARGA<br>TIFF<br>WEBP |
| `force_symmetry` | Forcer la symétrie sur le modèle (par défaut : Faux) | BOOLEAN | Non | Vrai/Faux |
| `flatten_bottom` | Aplatir le bas du modèle (par défaut : Faux) | BOOLEAN | Non | Vrai/Faux |
| `flatten_bottom_threshold` | Seuil pour l'aplatissement du bas (par défaut : 0.0) | FLOAT | Non | 0.0 à 1.0 |
| `pivot_to_center_bottom` | Déplacer le point de pivot au centre bas du modèle (par défaut : Faux) | BOOLEAN | Non | Vrai/Faux |
| `scale_factor` | Facteur d'échelle à appliquer au modèle (par défaut : 1.0) | FLOAT | Non | 0.0 et plus |
| `with_animation` | Inclure les données d'animation dans l'exportation (par défaut : Faux) | BOOLEAN | Non | Vrai/Faux |
| `pack_uv` | Empaqueter les coordonnées UV (par défaut : Faux) | BOOLEAN | Non | Vrai/Faux |
| `bake` | Cuire les textures (par défaut : Faux) | BOOLEAN | Non | Vrai/Faux |
| `part_names` | Liste séparée par des virgules des noms de pièces à inclure dans l'exportation (par défaut : "") | STRING | Non | Liste séparée par des virgules |
| `fbx_preset` | Préréglage d'exportation FBX à utiliser (par défaut : blender) | COMBO | Non | blender<br>mixamo<br>3dsmax |
| `export_vertex_colors` | Exporter les couleurs des sommets (par défaut : Faux) | BOOLEAN | Non | Vrai/Faux |
| `export_orientation` | Mode d'orientation d'exportation (par défaut : default) | COMBO | Non | align_image<br>default |
| `animate_in_place` | Animer le modèle sur place (par défaut : Faux) | BOOLEAN | Non | Vrai/Faux |

**Remarque :** Le `original_model_task_id` doit être un ID de tâche valide provenant d'une opération Tripo précédente (génération de modèle, rigging ou retargeting). Les paramètres marqués comme "avancés" sont facultatifs et ne nécessitent une configuration que pour des besoins d'exportation spécifiques.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| *Aucune sortie nommée* | Ce nœud traite la conversion de manière asynchrone et renvoie le résultat via le système d'API Tripo | - |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/fr.md)

---
**Source fingerprint (SHA-256):** `b11ecab98701b7153a350f5e4980ddc2f446c0a12be3402ca98a5e6de60bd7ce`
