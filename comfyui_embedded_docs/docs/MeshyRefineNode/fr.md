# Meshy : Affiner le modèle brouillon

Le nœud **Meshy : Affiner le modèle provisoire** prend un modèle 3D provisoire généré précédemment et améliore sa qualité, en ajoutant éventuellement des textures. Il soumet une tâche d'affinement à l'API Meshy et renvoie les fichiers du modèle 3D final une fois le traitement terminé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Spécifie le modèle d'IA à utiliser pour l'affinement. Actuellement, seul le modèle "latest" est disponible. | COMBO | Oui | `"latest"` |
| `meshy_task_id` | L'identifiant unique de la tâche du modèle provisoire que vous souhaitez affiner. | MESHY_TASK_ID | Oui | - |
| `activer_pbr` | Génère des cartes PBR (métallique, rugosité, normale) en plus de la couleur de base. Remarque : doit être défini sur false lors de l'utilisation du style Sculpture, car ce dernier génère son propre ensemble de cartes PBR. (par défaut : `False`) | BOOLEAN | Non | - |
| `invite_texture` | Fournit une invite textuelle pour guider le processus de texturation. Maximum 600 caractères. Ne peut pas être utilisé en même temps que `image_texture`. (par défaut : chaîne vide) | STRING | Non | - |
| `image_texture` | Un seul des deux paramètres `image_texture` ou `invite_texture` peut être utilisé à la fois. | IMAGE | Non | - |

**Remarque :** Les entrées `texture_prompt` et `texture_image` s'excluent mutuellement. Vous ne pouvez pas fournir à la fois une invite textuelle et une image pour la texturation dans la même opération.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `model_file` | Le nom du fichier du modèle GLB généré. (Uniquement pour la rétrocompatibilité) | STRING |
| `meshy_task_id` | L'identifiant unique de la tâche pour le travail d'affinement soumis. | MESHY_TASK_ID |
| `GLB` | Le modèle 3D final affiné au format GLB. | FILE3DGLB |
| `FBX` | Le modèle 3D final affiné au format FBX. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRefineNode/fr.md)

---
**Source fingerprint (SHA-256):** `cdf620ead0a4504cbb5d5554e0fe40e4cadd08884726f147cd486e63ab37f278`
