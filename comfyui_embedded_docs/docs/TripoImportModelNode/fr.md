# Tripo : Importer un modèle

Ce nœud importe un fichier de modèle 3D externe dans le système Tripo afin de pouvoir l'utiliser avec les nœuds de post-traitement Tripo tels que Texture, Rig et Convert. Il télécharge votre modèle et renvoie un identifiant de tâche que les autres nœuds Tripo peuvent utiliser pour référencer le modèle importé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_3d` | Modèle 3D à importer (GLB / FBX / OBJ / STL, jusqu'à 150 Mo). Les fichiers OBJ et STL ne contiennent pas de textures intégrées. | FILE3D | Oui | GLB<br>FBX<br>OBJ<br>STL<br>Tout format 3D |

**Remarque :** Le format GLB est recommandé car les textures sont conservées uniquement lorsqu'elles sont intégrées directement dans le fichier. Les fichiers OBJ et STL ne prennent pas en charge les textures intégrées. Le format GLTF (.gltf) n'est pas pris en charge car il référence des fichiers externes ; utilisez plutôt un fichier GLB unique.

## Sorties

| Nom de la sortie | Description | Type de données |
|------------------|-------------|-----------------|
| `model task_id` | Un identifiant de tâche qui identifie le modèle importé pour une utilisation avec les nœuds de post-traitement Tripo | MODEL_TASK_ID |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImportModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `4fa13a108804f2a52190a85b5b5d58ff18190e9d182b556abada444788012fab`
