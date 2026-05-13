> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToModelNode/fr.md)

Le nœud Meshy : Image vers modèle utilise l'API Meshy pour générer un modèle 3D à partir d'une seule image d'entrée. Il télécharge votre image, soumet une tâche de traitement et retourne les fichiers du modèle 3D généré (GLB et FBX) ainsi que l'identifiant de la tâche pour référence.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | COMBO | Oui | `"latest"` | Spécifie la version du modèle d'IA à utiliser pour la génération. |
| `image` | IMAGE | Oui | - | L'image d'entrée à convertir en modèle 3D. |
| `should_remesh` | COMBO DYNAMIQUE | Oui | `"true"`<br>`"false"` | Détermine si le maillage généré doit être traité. Lorsqu'il est défini sur `"false"`, le nœud retourne un maillage triangulaire non traité. |
| `topology` | COMBO | Non* | `"triangle"`<br>`"quad"` | La topologie polygonale cible pour le modèle remaillé. Cette entrée n'est disponible que lorsque `should_remesh` est défini sur `"true"`. |
| `target_polycount` | INT | Non* | 100 - 300000 | Le nombre cible de polygones pour le modèle remaillé. Cette entrée n'est disponible que lorsque `should_remesh` est défini sur `"true"`. La valeur par défaut est 300000. |
| `symmetry_mode` | COMBO | Oui | `"auto"`<br>`"on"`<br>`"off"` | Contrôle la symétrie appliquée au modèle 3D généré. |
| `should_texture` | COMBO DYNAMIQUE | Oui | `"true"`<br>`"false"` | Détermine si des textures sont générées pour le modèle. Le définir sur `"false"` ignore la phase de texturation et retourne un maillage sans textures. |
| `enable_pbr` | BOOLÉEN | Non* | - | Lorsque `should_texture` est `"true"`, cette option génère des cartes PBR (métallique, rugosité, normale) en plus de la couleur de base. La valeur par défaut est `False`. |
| `texture_prompt` | CHAÎNE | Non* | - | Une invite textuelle pour guider le processus de texturation (600 caractères maximum). Cette entrée n'est disponible que lorsque `should_texture` est défini sur `"true"`. Elle ne peut pas être utilisée en même temps que `texture_image`. |
| `texture_image` | IMAGE | Non* | - | Une image pour guider le processus de texturation. Cette entrée n'est disponible que lorsque `should_texture` est défini sur `"true"`. Elle ne peut pas être utilisée en même temps que `texture_prompt`. |
| `pose_mode` | COMBO | Oui | `""` (vide)<br>`"A-pose"`<br>`"T-pose"` | Spécifie le mode de pose pour le modèle généré. Il s'agit d'un paramètre avancé. |
| `seed` | INT | Oui | 0 - 2147483647 | Une valeur de graine pour le processus de génération. Les résultats ne sont pas déterministes quelle que soit la valeur de la graine. La valeur par défaut est 0. |

**Note sur les contraintes des paramètres :**

* Les entrées `topology` et `target_polycount` ne sont disponibles que lorsque `should_remesh` est défini sur `"true"`.
* Les entrées `enable_pbr`, `texture_prompt` et `texture_image` ne sont disponibles que lorsque `should_texture` est défini sur `"true"`.
* Vous ne pouvez pas utiliser `texture_prompt` et `texture_image` en même temps. Si les deux sont fournis lorsque `should_texture` est `"true"`, le nœud générera une erreur.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `meshy_task_id` | CHAÎNE | Le nom du fichier du modèle GLB généré. (Maintenu pour la rétrocompatibilité). |
| `GLB` | MESHY_TASK_ID | L'identifiant unique de la tâche de l'API Meshy, qui peut être utilisé pour référence ou dépannage. |
| `FBX` | FILE3DGLB | Le modèle 3D généré au format de fichier GLB. |
| `FBX` | FILE3DFBX | Le modèle 3D généré au format de fichier FBX. |

---
**Source fingerprint (SHA-256):** `134d9250d8b447bbbd2905f827e81b67f491ba355ebb93d4d256324b644100a2`
