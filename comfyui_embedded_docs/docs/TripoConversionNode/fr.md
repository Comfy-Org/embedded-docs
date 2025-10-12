> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/fr.md)

Le TripoConversionNode convertit des modèles 3D entre différents formats de fichiers en utilisant l'API Tripo. Il prend un identifiant de tâche d'une opération Tripo précédente et convertit le modèle résultant vers votre format souhaité avec diverses options d'exportation.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `original_model_task_id` | MODEL_TASK_ID,RIG_TASK_ID,RETARGET_TASK_ID | Oui | MODEL_TASK_ID<br>RIG_TASK_ID<br>RETARGET_TASK_ID | L'identifiant de tâche d'une opération Tripo précédente (génération de modèle, rigging ou retargeting) |
| `format` | COMBO | Oui | GLTF<br>USDZ<br>FBX<br>OBJ<br>STL<br>3MF | Le format de fichier cible pour le modèle 3D converti |
| `quad` | BOOLEAN | Non | True/False | Indique s'il faut convertir les triangles en quads (par défaut : False) |
| `face_limit` | INT | Non | -1 à 500000 | Nombre maximum de faces dans le modèle de sortie, utiliser -1 pour aucune limite (par défaut : -1) |
| `texture_size` | INT | Non | 128 à 4096 | Taille des textures de sortie en pixels (par défaut : 4096) |
| `texture_format` | COMBO | Non | BMP<br>DPX<br>HDR<br>JPEG<br>OPEN_EXR<br>PNG<br>TARGA<br>TIFF<br>WEBP | Format des textures exportées (par défaut : JPEG) |

**Note :** Le `original_model_task_id` doit être un identifiant de tâche valide provenant d'une opération Tripo précédente (génération de modèle, rigging ou retargeting).

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| *Aucune sortie nommée* | - | Ce nœud traite la conversion de manière asynchrone et retourne le résultat via le système d'API Tripo |
