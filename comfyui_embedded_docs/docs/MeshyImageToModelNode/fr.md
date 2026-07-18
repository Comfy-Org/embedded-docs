Le nœud Meshy : Image vers modèle utilise l'API Meshy pour générer un modèle 3D à partir d'une seule image d'entrée. Il télécharge votre image, soumet une tâche de traitement et retourne les fichiers du modèle 3D généré (GLB et FBX) ainsi que l'identifiant de la tâche pour référence.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Spécifie la version du modèle d'IA à utiliser pour la génération. | COMBO | Oui | `"latest"` |
| `image` | L'image d'entrée à convertir en modèle 3D. | IMAGE | Oui | - |
| `should_remesh` | Détermine si le maillage généré doit être traité. Lorsqu'il est défini sur `"false"`, le nœud retourne un maillage triangulaire non traité. | COMBO DYNAMIQUE | Oui | `"true"`<br>`"false"` |
| `topology` | La topologie polygonale cible pour le modèle remaillé. Cette entrée n'est disponible que lorsque `should_remesh` est défini sur `"true"`. | COMBO | Non* | `"triangle"`<br>`"quad"` |
| `target_polycount` | Le nombre cible de polygones pour le modèle remaillé. Cette entrée n'est disponible que lorsque `should_remesh` est défini sur `"true"`. La valeur par défaut est 300000. | INT | Non* | 100 - 300000 |
| `symmetry_mode` | Contrôle la symétrie appliquée au modèle 3D généré. | COMBO | Oui | `"auto"`<br>`"on"`<br>`"off"` |
| `should_texture` | Détermine si des textures sont générées pour le modèle. Le définir sur `"false"` ignore la phase de texturation et retourne un maillage sans textures. | COMBO DYNAMIQUE | Oui | `"true"`<br>`"false"` |
| `enable_pbr` | Lorsque `should_texture` est `"true"`, cette option génère des cartes PBR (métallique, rugosité, normale) en plus de la couleur de base. La valeur par défaut est `False`. | BOOLÉEN | Non* | - |
| `texture_prompt` | Une invite textuelle pour guider le processus de texturation (600 caractères maximum). Cette entrée n'est disponible que lorsque `should_texture` est défini sur `"true"`. Elle ne peut pas être utilisée en même temps que `texture_image`. | CHAÎNE | Non* | - |
| `texture_image` | Une image pour guider le processus de texturation. Cette entrée n'est disponible que lorsque `should_texture` est défini sur `"true"`. Elle ne peut pas être utilisée en même temps que `texture_prompt`. | IMAGE | Non* | - |
| `pose_mode` | Spécifie le mode de pose pour le modèle généré. Il s'agit d'un paramètre avancé. | COMBO | Oui | `""` (vide)<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | Une valeur de graine pour le processus de génération. Les résultats ne sont pas déterministes quelle que soit la valeur de la graine. La valeur par défaut est 0. | INT | Oui | 0 - 2147483647 |

**Note sur les contraintes des paramètres :**

* Les entrées `topology` et `target_polycount` ne sont disponibles que lorsque `should_remesh` est défini sur `"true"`.
* Les entrées `enable_pbr`, `texture_prompt` et `texture_image` ne sont disponibles que lorsque `should_texture` est défini sur `"true"`.
* Vous ne pouvez pas utiliser `texture_prompt` et `texture_image` en même temps. Si les deux sont fournis lorsque `should_texture` est `"true"`, le nœud générera une erreur.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `model_file` | Le nom du fichier du modèle GLB généré. (Maintenu pour la rétrocompatibilité). | CHAÎNE |
| `meshy_task_id` | L'identifiant unique de la tâche de l'API Meshy, qui peut être utilisé pour référence ou dépannage. | MESHY_TASK_ID |
| `GLB` | Le modèle 3D généré au format de fichier GLB. | FILE3DGLB |
| `FBX` | Le modèle 3D généré au format de fichier FBX. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `134d9250d8b447bbbd2905f827e81b67f491ba355ebb93d4d256324b644100a2`
