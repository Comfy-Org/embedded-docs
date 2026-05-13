> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRefineNode/fr.md)

Le nœud **Meshy : Affiner le modèle provisoire** prend un modèle 3D provisoire généré précédemment et améliore sa qualité, en ajoutant éventuellement des textures. Il soumet une tâche d'affinement à l'API Meshy et renvoie les fichiers du modèle 3D final une fois le traitement terminé.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | COMBO | Oui | `"latest"` | Spécifie le modèle d'IA à utiliser pour l'affinement. Actuellement, seul le modèle "latest" est disponible. |
| `meshy_task_id` | MESHY_TASK_ID | Oui | - | L'identifiant unique de la tâche du modèle provisoire que vous souhaitez affiner. |
| `enable_pbr` | BOOLEAN | Non | - | Génère des cartes PBR (métallique, rugosité, normale) en plus de la couleur de base. Remarque : doit être défini sur false lors de l'utilisation du style Sculpture, car ce dernier génère son propre ensemble de cartes PBR. (par défaut : `False`) |
| `texture_prompt` | STRING | Non | - | Fournit une invite textuelle pour guider le processus de texturation. Maximum 600 caractères. Ne peut pas être utilisé en même temps que `texture_image`. (par défaut : chaîne vide) |
| `texture_image` | IMAGE | Non | - | Un seul des deux paramètres `texture_image` ou `texture_prompt` peut être utilisé à la fois. |

**Remarque :** Les entrées `texture_prompt` et `texture_image` s'excluent mutuellement. Vous ne pouvez pas fournir à la fois une invite textuelle et une image pour la texturation dans la même opération.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `model_file` | STRING | Le nom du fichier du modèle GLB généré. (Uniquement pour la rétrocompatibilité) |
| `meshy_task_id` | MESHY_TASK_ID | L'identifiant unique de la tâche pour le travail d'affinement soumis. |
| `GLB` | FILE3DGLB | Le modèle 3D final affiné au format GLB. |
| `FBX` | FILE3DFBX | Le modèle 3D final affiné au format FBX. |

---
**Source fingerprint (SHA-256):** `cdf620ead0a4504cbb5d5554e0fe40e4cadd08884726f147cd486e63ab37f278`
