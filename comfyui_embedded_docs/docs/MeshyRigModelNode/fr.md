> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRigModelNode/fr.md)

Le nœud Meshy : Rig Model prend un modèle 3D issu d'une tâche Meshy précédente et crée automatiquement un squelette pour celui-ci, produisant un personnage armaturé pouvant être posé et animé. Le nœud génère le modèle armaturé aux formats de fichier GLB et FBX.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `meshy_task_id` | STRING | Oui | N/A | L'identifiant unique de tâche d'une opération Meshy antérieure (ex. texte-vers-3D ou image-vers-3D) ayant généré le modèle à armaturer. |
| `hauteur_mètres` | FLOAT | Oui | 0,1 à 15,0 | La hauteur approximative du modèle de personnage en mètres. Cela facilite la mise à l'échelle et la précision de l'armature (valeur par défaut : 1,7). |
| `image_texture` | IMAGE | Non | N/A | L'image de texture de couleur de base du modèle, dépliée en UV. |

**Remarque :** Le processus d'armature automatique n'est actuellement pas adapté aux maillages non texturés, aux éléments non humanoïdes, ni aux éléments humanoïdes dont la structure des membres et du corps est peu claire.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `rig_task_id` | STRING | Une sortie héritée pour la rétrocompatibilité, contenant le nom du fichier du modèle GLB. |
| `GLB` | STRING | L'identifiant unique de tâche pour cette opération d'armature, pouvant être utilisé pour référencer le résultat. |
| `FBX` | FILE3DGLB | Le modèle de personnage 3D armaturé enregistré au format de fichier GLB. |
| `FBX` | FILE3DFBX | Le modèle de personnage 3D armaturé enregistré au format de fichier FBX. |

---
**Source fingerprint (SHA-256):** `91e06e3465d3d309d2267ae307ec5a704af3903b7a6d7fb6011217dd58a63973`
