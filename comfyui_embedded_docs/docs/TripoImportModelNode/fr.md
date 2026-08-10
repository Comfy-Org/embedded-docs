# Tripo : Importer un modèle

Ce nœud importe un modèle 3D externe dans Tripo afin que d'autres nœuds de post-traitement Tripo, tels que Texture, Rig et Convert, puissent l'utiliser. Le nœud téléverse le modèle et renvoie un ID de tâche qui identifie le modèle importé. GLB est recommandé car les textures ne sont conservées que lorsqu'elles sont intégrées dans le fichier, et texturer un modèle importé nécessite une invite de texture.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_3d` | Modèle 3D à importer (GLB / FBX / OBJ / STL, jusqu'à 150 Mo). Les fichiers OBJ et STL ne contiennent pas de textures intégrées. | FILE3D | Oui | GLB<br>FBX<br>OBJ<br>STL<br>Tout format 3D |

**Remarque :** Seuls les formats GLB, FBX, OBJ et STL sont pris en charge. GLTF (.gltf) ne peut pas être importé car il fait référence à des fichiers externes ; utilisez plutôt un GLB à fichier unique. Le fichier de modèle doit faire 150 Mo ou moins. GLB est recommandé car les textures ne survivent à l'importation que lorsqu'elles sont intégrées dans le fichier. Les fichiers OBJ et STL ne contiennent pas de textures intégrées. Texturer un modèle importé nécessite une invite de texture.

## Sorties

| Nom de la sortie | Description | Type de données |
|------------------|-------------|-----------------|
| `model task_id` | Un identifiant de tâche qui identifie le modèle importé pour une utilisation avec les nœuds de post-traitement Tripo | MODEL_TASK_ID |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImportModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `4fa13a108804f2a52190a85b5b5d58ff18190e9d182b556abada444788012fab`
