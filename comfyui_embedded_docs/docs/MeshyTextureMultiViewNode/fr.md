# Meshy : Texturer le modèle (multi-vues)

Ce nœud texture un modèle 3D créé précédemment à l’aide de 1 à 4 vues de référence du même objet. Vous fournissez l’ID de tâche du modèle d’origine et les images de référence ; le nœud les envoie au service Meshy, attend la fin du travail, puis renvoie le modèle texturé sous forme de fichiers GLB et FBX.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle IA utilisé pour le travail de texturation. Seul `"meshy-7"` est actuellement disponible. | COMBO | Oui | `"meshy-7"` |
| `meshy_task_id` | L’ID de tâche du modèle 3D créé précédemment à texturer. | MESHY_TASK_ID | Oui | — |
| `multiview_images` | Vues de référence du même objet. La première image est la vue principale (avant) ; l’ordre des vues restantes n’a pas d’importance. Emplacement extensible : connectez 1 à 4 images (`image_1` à `image_4`). | IMAGE | Oui | 1 à 4 images |
| `enable_original_uv` | Utiliser l’UV d’origine du modèle au lieu de générer de nouvelles UV. Lorsque cette option est activée, Meshy préserve les textures existantes du modèle téléchargé. Si le modèle n’a pas d’UV d’origine, la qualité de la sortie pourrait être moins bonne. (par défaut : True) | BOOLEAN | Non | True / False |
| `pbr` | Active la génération de textures PBR (rendu physiquement basé). (par défaut : False) | BOOLEAN | Non | True / False |
| `texture_resolution` | Résolution de la texture de couleur de base. Des résolutions plus élevées capturent plus de détails de surface. | COMBO | Oui | `"2k"`<br>`"4k"`<br>`"8k"` |

**Remarque :** `multiview_images` doit contenir entre 1 et 4 images. Le nœud valide ce point lors de l’exécution et lève une erreur si le nombre est en dehors de cette plage. Si une image connectée contient un lot de plusieurs images, chaque image du lot compte dans la limite. La première image est utilisée comme vue principale (avant) ; l’ordre des images restantes n’a pas d’importance.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_file` | Nom du fichier de modèle. Cette sortie est conservée uniquement pour des raisons de rétrocompatibilité. | STRING |
| `meshy_task_id` | ID de tâche du travail de texturation. | MESHY_TASK_ID |
| `GLB` | Le modèle 3D texturé téléchargé au format GLB. | GLB |
| `FBX` | Le modèle 3D texturé téléchargé au format FBX. | FBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureMultiViewNode/fr.md)

---
**Source fingerprint (SHA-256):** `3a08d003683a182121471a064833c09b932c7c84c20fd5cb5ac0285e135b2b7e`
