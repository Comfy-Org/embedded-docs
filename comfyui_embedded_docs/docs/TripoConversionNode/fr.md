# Tripo : Convertir le modèle

Ce nœud convertit un modèle Tripo 3D existant vers un autre format de fichier 3D. Il prend l’ID de tâche d’un modèle précédemment créé ou traité par une opération Tripo (telle que la génération de modèle, le rigging, le retargeting ou la segmentation), soumet une tâche de conversion à l’API Tripo, attend la fin de cette tâche, puis renvoie le fichier de modèle converti.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `id_tâche_modèle_original` | ID de tâche du modèle Tripo à convertir. Il doit provenir d’une tâche antérieure de génération de modèle, de rigging, de retargeting ou de segmentation Tripo. Si l’ID est manquant ou vide, le nœud déclenche une erreur. | STRING | Oui | MODEL_TASK_ID<br>RIG_TASK_ID<br>RETARGET_TASK_ID<br>SEGMENT_TASK_ID |
| `format` | Format de fichier cible pour le modèle 3D converti. | COMBO | Oui | GLTF<br>USDZ<br>FBX<br>OBJ<br>STL<br>3MF |
| `quad` | Convertir les triangles en quads lorsqu’activé (par défaut : False). | BOOLEAN | Non | True or False |
| `limite_faces` | Nombre maximal de faces dans le modèle converti. Définir sur -1 pour aucune limite (par défaut : -1). | INT | Non | -1 à 2000000 |
| `taille_texture` | Résolution des textures de sortie en pixels (par défaut : 4096). | INT | Non | 128 à 8192 |
| `format_texture` | Format de fichier utilisé pour les textures exportées (par défaut : JPEG). | COMBO | Non | BMP<br>DPX<br>HDR<br>JPEG<br>OPEN_EXR<br>PNG<br>TARGA<br>TIFF<br>WEBP |
| `force_symmetry` | Forcer le modèle à être symétrique lorsqu’activé (par défaut : False). | BOOLEAN | Non | True or False |
| `flatten_bottom` | Aplatir le bas du modèle lorsqu’activé (par défaut : False). | BOOLEAN | Non | True or False |
| `flatten_bottom_threshold` | Profondeur d’aplatissement utilisée avec `flatten_bottom` (par défaut : 0.01). Cette valeur n’est appliquée que lorsque `flatten_bottom` est activé. | FLOAT | Non | 0.01 à 1.0 |
| `pivot_to_center_bottom` | Déplacer le point pivot vers le centre inférieur du modèle lorsqu’activé (par défaut : False). | BOOLEAN | Non | True or False |
| `scale_factor` | Facteur d’échelle appliqué au modèle converti (par défaut : 1.0). | FLOAT | Non | 0.01 et plus |
| `with_animation` | Conserver le squelette et l’animation des modèles riggés ou retargetés (par défaut : True). | BOOLEAN | Non | True or False |
| `pack_uv` | Réempaqueter les coordonnées UV lorsqu’activé (par défaut : False). | BOOLEAN | Non | True or False |
| `bake` | Baker les matériaux avancés dans les textures de base pour une meilleure compatibilité (par défaut : True). | BOOLEAN | Non | True or False |
| `part_names` | Liste de noms de parties du modèle séparés par des virgules à envoyer à la conversion. Les entrées vides sont ignorées et les noms en double sont supprimés. Laisser vide pour omettre cette option (par défaut : vide). | STRING | Non | Liste de noms de parties séparés par des virgules |
| `fbx_preset` | Préréglage de compatibilité FBX. bake_scale intègre la transformation d’échelle dans la géométrie (par défaut : blender). | COMBO | Non | blender<br>mixamo<br>3dsmax<br>bake_scale |
| `export_vertex_colors` | Exporter les couleurs de sommets lorsqu’activé (par défaut : False). | BOOLEAN | Non | True or False |
| `export_orientation` | Axe avant du modèle exporté. default conserve le +x de Tripo (par défaut : default). | COMBO | Non | default<br>+x<br>-x<br>+y<br>-y |
| `animate_in_place` | Animer le modèle sur place lorsqu’activé (par défaut : False). | BOOLEAN | Non | True or False |

**Remarque :** À l’exception de `original_model_task_id` et `format`, toutes les entrées sont des paramètres avancés facultatifs. La plupart des paramètres laissés à leurs valeurs par défaut sont omis de la requête de conversion afin que l’API Tripo puisse utiliser son comportement standard. Les options `with_animation` et `bake` sont toujours envoyées. `flatten_bottom_threshold` n’est appliqué que lorsque `flatten_bottom` est activé.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_3d` | Modèle converti dans le format demandé. OBJ est fourni par Tripo sous forme d’archive ZIP (maillage, matériau et textures). | FILE_3D |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/fr.md)

---
**Source fingerprint (SHA-256):** `b6be09bf6b1c5ccd6de5ae56ed28bfe1f0b81c1ca8ff61623e3094917c98d68a`
