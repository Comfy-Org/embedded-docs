# Tripo: Smart UV

Tripo: Smart UV redéplie les UV d’un modèle et remappe ses textures, son rig et son animation sur la nouvelle disposition. Utilisez-le lorsque la disposition UV d’origine d’un modèle est inutilisable, par exemple après une retopologie ou lorsque les coutures de texture doivent être refaites. Le modèle d’entrée ne doit pas dépasser 80 000 triangles (un quad compte pour deux), donc réduisez d’abord les modèles plus volumineux avec Tripo: Retopology ou une `face_limit`.

> **Remarque :** Tripo conserve les enregistrements de tâches sur ses serveurs pendant 7 jours (à compter du 1er décembre 2026). Un ID de tâche plus ancien ne peut plus être résolu ; l’exécution d’un workflow enregistré après ce délai échoue donc au niveau de ce nœud. Réexécutez le nœud Tripo précédent pour créer un nouvel ID de tâche, ou réimportez le modèle téléchargé avec **Tripo: Import Model**.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_task_id` | ID de tâche du modèle à redéplier. Accepte un ID de tâche de modèle provenant d’un nœud de génération Tripo, ou un ID de tâche de rig, de retarget ou de segmentation. | MODEL_TASK_ID | Oui | ID de tâche Tripo |
| `bake` | Cuire les textures existantes sur la nouvelle disposition UV. Désactivé, la cuisson est ignorée et le modèle est renvoyé sans ses textures de couleur (par défaut : True). | BOOLEAN | Oui | `True`<br>`False` |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model task_id` | ID de tâche de la tâche UV terminée. Peut être transmis à d’autres nœuds Tripo, par exemple Tripo: Texture. | MODEL_TASK_ID |
| `GLB` | Le modèle redéplié au format GLB. Vide lorsque le modèle source est FBX. | GLB FILE |
| `FBX` | Le modèle redéplié au format FBX. Rempli uniquement lorsque le modèle source est FBX, par exemple un maillage quad. | FBX FILE |
| `UV atlas` | La disposition UV rendue du modèle sous forme d’image. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSmartUVNode/fr.md)

---
**Source fingerprint (SHA-256):** `55c9352c7c8129fa7a4f99f803bdc6db112830454e7d9566fa734063cb283532`
