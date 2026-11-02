# Tripo : Importer un modèle

Ce nœud importe un modèle 3D externe dans Tripo afin que les nœuds de post-traitement Tripo, tels que Texture, Rig et Convert, puissent l’utiliser. Le nœud téléverse le fichier vers Tripo et renvoie un ID de tâche qui identifie le modèle importé pour utilisation par ces nœuds. GLB est recommandé car les textures ne sont préservées que lorsqu’elles sont intégrées dans le fichier, et la texturation d’un modèle importé nécessite un prompt de texture. L’utilisation de ce nœud est gratuite.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_3d` | Modèle 3D à importer (GLB / FBX / OBJ / STL, jusqu’à 150 Mo). Les fichiers OBJ et STL ne contiennent pas de textures intégrées. | FILE3D | Oui | GLB<br>FBX<br>OBJ<br>STL<br>Tout format 3D |

**Remarque :** Seuls les formats GLB, FBX, OBJ et STL sont pris en charge. GLTF (.gltf) ne peut pas être importé car il référence des fichiers externes ; exportez plutôt un GLB à fichier unique. Le fichier de modèle doit faire 150 Mo ou moins. GLB est recommandé car les textures ne survivent à l’importation que lorsqu’elles sont intégrées dans le fichier. Les fichiers OBJ et STL ne comportent pas de textures intégrées. La texturation d’un modèle importé nécessite un prompt de texture.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model task_id` | Un ID de tâche qui identifie le modèle importé, à utiliser avec les nœuds de post-traitement Tripo | MODEL_TASK_ID |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImportModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `bf91e964c5705f7377868dd06bbf5d57b41cc3607fc377cd45886d3d6c5ceddc`
