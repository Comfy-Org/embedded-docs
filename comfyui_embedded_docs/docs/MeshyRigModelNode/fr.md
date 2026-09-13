# Meshy : Rig du modèle

Le nœud Meshy: Rig Model prend un modèle 3D issu d’une tâche Meshy précédente et crée automatiquement un squelette pour celui-ci, produisant un personnage riggé qui peut être mis en pose et animé. Le nœud produit le modèle riggé aux formats de fichier GLB et FBX.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `meshy_task_id` | L’ID de tâche unique provenant d’une opération Meshy précédente (par ex., text-to-3D ou image-to-3D) ayant généré le modèle à rigger. | MESHY_TASK_ID | Oui | N/A |
| `hauteur_mètres` | La hauteur approximative du modèle de personnage en mètres. Cela contribue à la précision de la mise à l’échelle et du rigging (valeur par défaut : 1.7). | FLOAT | Oui | 0.1 à 15.0 |
| `image_texture` | L’image de texture de couleur de base du modèle, dépliée en UV. | IMAGE | Non | N/A |

**Remarque :** Le processus de rigging automatique n’est actuellement pas adapté aux maillages non texturés, aux ressources non humanoïdes, ni aux ressources humanoïdes dont la structure des membres et du corps n’est pas claire.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_file` | Une sortie héritée conservée uniquement pour la rétrocompatibilité, contenant le nom de fichier du modèle GLB. | STRING |
| `rig_task_id` | L’ID de tâche unique pour cette opération de rigging, qui peut être utilisé pour référencer le résultat dans les nœuds Meshy ultérieurs. | MESHY_RIGGED_TASK_ID |
| `GLB` | Le modèle de personnage 3D riggé enregistré au format de fichier GLB. | FILE3DGLB |
| `FBX` | Le modèle de personnage 3D riggé enregistré au format de fichier FBX. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRigModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `6ae79359fa54f36dd2491a952fe54fa56866038758e8cd475a2d2f8e9e47e3b3`
