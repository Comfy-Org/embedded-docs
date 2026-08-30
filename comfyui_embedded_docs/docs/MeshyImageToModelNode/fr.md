# Meshy : Image vers modèle

Le nœud Meshy: Image to Model utilise l'API Meshy pour générer un modèle 3D à partir d'une image d'entrée unique. Il télécharge votre image, soumet une tâche de traitement, puis renvoie les fichiers du modèle 3D généré (GLB et FBX) ainsi que l'identifiant de la tâche pour référence.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Spécifie la version du modèle d'IA à utiliser pour la génération. | COMBO | Oui | `"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `image` | L'image d'entrée à convertir en modèle 3D. | IMAGE | Oui | - |
| `should_remesh` | Lorsque défini sur `"false"`, renvoie un maillage triangulaire non traité. | DYNAMIC_COMBO | Oui | `"true"`<br>`"false"` |
| `topology` | La topologie polygonale cible pour le modèle remaillé. Cette entrée n'est disponible que lorsque `should_remesh` est défini sur `"true"`. | COMBO | Non* | `"triangle"`<br>`"quad"` |
| `target_polycount` | Le nombre cible de polygones pour le modèle remaillé. Cette entrée n'est disponible que lorsque `should_remesh` est défini sur `"true"`. Défaut : 300000. | INT | Non* | 100 - 300000 |
| `symmetry_mode` | Contrôle la symétrie appliquée au modèle 3D généré. | COMBO | Oui | `"auto"`<br>`"on"`<br>`"off"` |
| `should_texture` | Détermine si des textures sont générées. Le définir sur `"false"` ignore la phase de texturation et renvoie un maillage sans texture. | DYNAMIC_COMBO | Oui | `"true"`<br>`"false"` |
| `enable_pbr` | Génère des cartes PBR (métallique, rugosité, normale) en plus de la couleur de base. Cette entrée n'est disponible que lorsque `should_texture` est défini sur `"true"`. Défaut : `False`. | BOOLEAN | Non* | - |
| `texture_prompt` | Fournit une invite textuelle pour guider le processus de texturation. Maximum 600 caractères. Ne peut pas être utilisé en même temps que `texture_image`. Cette entrée n'est disponible que lorsque `should_texture` est défini sur `"true"`. Défaut : chaîne vide. | STRING | Non* | - |
| `texture_image` | Une seule des entrées `texture_image` ou `texture_prompt` peut être utilisée à la fois. Cette entrée n'est disponible que lorsque `should_texture` est défini sur `"true"`. | IMAGE | Non* | - |
| `texture_resolution` | Résolution de la texture de couleur de base. Les résolutions plus élevées capturent plus de détails de surface. Cette entrée n'est disponible que lorsque `should_texture` est défini sur `"true"`. | COMBO | Non* | `"2k"`<br>`"4k"`<br>`"8k"` |
| `pose_mode` | Spécifie le mode de pose du modèle généré. Il s'agit d'un paramètre avancé. | COMBO | Oui | `""` (vide)<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | La graine détermine si le nœud doit être réexécuté ; les résultats ne sont pas déterministes quelle que soit la graine. Défaut : 0. | INT | Oui | 0 - 2147483647 |
| `ultra_mode` | Exécute une passe de raffinement supplémentaire pour une géométrie plus fidèle avec des détails de surface plus fins. Défaut : `False`. | BOOLEAN | Oui | - |

**Remarque concernant les contraintes des paramètres :**

* Les entrées `topology` et `target_polycount` ne sont disponibles que lorsque `should_remesh` est défini sur `"true"`.
* Les entrées `enable_pbr`, `texture_prompt`, `texture_image` et `texture_resolution` ne sont disponibles que lorsque `should_texture` est défini sur `"true"`.
* Lorsque `should_texture` est défini sur `"true"`, `texture_prompt` et `texture_image` ne peuvent pas être utilisés en même temps. Si les deux sont fournis, le nœud génère une erreur.
* `texture_prompt` a une longueur maximale de 600 caractères.
* `ultra_mode` nécessite le modèle `"meshy-7"` ou `"latest"`. Si `ultra_mode` est activé avec le modèle `"meshy-6"`, le nœud génère une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model_file` | Le nom du fichier du modèle GLB généré. Conservé uniquement pour la compatibilité ascendante. | STRING |
| `meshy_task_id` | L'identifiant unique de la tâche API Meshy, qui peut être utilisé pour référence ou pour le dépannage. | MESHY_TASK_ID |
| `GLB` | Le modèle 3D généré au format de fichier GLB. | FILE3DGLB |
| `FBX` | Le modèle 3D généré au format de fichier FBX. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `689828ad52de4493e1039aecc408e18af4122d2c0e2511fd254ba0f1d56bad14`
