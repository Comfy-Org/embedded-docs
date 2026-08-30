# Meshy : Rig du modèle

Le nœud Meshy: Rig Model prend un modèle 3D d'une tâche Meshy précédente et crée automatiquement une armature pour celui-ci, produisant un personnage avec armature qui peut être posé et animé. Le nœud génère le modèle avec armature dans les formats de fichiers GLB et FBX.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `meshy_task_id` | L'identifiant de tâche unique d'une opération Meshy précédente (par exemple, text-to-3D ou image-to-3D) qui a généré le modèle à doter d'une armature. | STRING | Oui | N/A |
| `hauteur_mètres` | La hauteur approximative du modèle de personnage en mètres. Cela facilite la précision de la mise à l'échelle et de la création d'armature (par défaut : 1.7). | FLOAT | Oui | 0.1 à 15.0 |
| `image_texture` | L'image de texture de couleur de base du modèle, avec UV dépliés. | IMAGE | Non | N/A |

**Remarque :** Le processus de création automatique d'armature n'est actuellement pas adapté aux maillages sans texture, aux ressources non humanoïdes, ni aux ressources humanoïdes dont la structure des membres et du corps n'est pas claire.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_file` | Une sortie héritée pour la rétrocompatibilité, contenant le nom de fichier du modèle GLB. | STRING |
| `rig_task_id` | L'identifiant de tâche unique pour cette opération de création d'armature, qui peut être utilisé pour référencer le résultat. | STRING |
| `GLB` | Le modèle de personnage 3D avec armature enregistré au format de fichier GLB. | FILE3DGLB |
| `FBX` | Le modèle de personnage 3D avec armature enregistré au format de fichier FBX. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRigModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `6ae79359fa54f36dd2491a952fe54fa56866038758e8cd475a2d2f8e9e47e3b3`
