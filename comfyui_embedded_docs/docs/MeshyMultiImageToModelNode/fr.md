> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyMultiImageToModelNode/fr.md)

Ce nœud utilise l'API Meshy pour générer un modèle 3D à partir de plusieurs images d'entrée. Il télécharge les images fournies, soumet une tâche de traitement et renvoie les fichiers du modèle 3D résultant (GLB et FBX) ainsi que l'identifiant de la tâche pour référence.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
| :--- | :--- | :--- | :--- | :--- |
| `model` | COMBO | Oui | `"latest"` | Spécifie la version du modèle d'IA à utiliser. |
| `images` | IMAGE | Oui | 2 à 4 images | Un ensemble d'images utilisé pour générer le modèle 3D. Vous devez fournir entre 2 et 4 images. |
| `should_remesh` | COMBO | Oui | `"true"`<br>`"false"` | Détermine si le maillage généré doit être traité. Lorsqu'il est défini sur `"false"`, le nœud renvoie un maillage triangulaire non traité. |
| `topology` | COMBO | Non | `"triangle"`<br>`"quad"` | Le type de polygone cible pour la sortie remaillée. Ce paramètre est uniquement disponible et requis lorsque `should_remesh` est défini sur `"true"`. |
| `target_polycount` | INT | Non | 100 à 300000 | Le nombre cible de polygones pour le modèle remaillé (par défaut : 300000). Ce paramètre est uniquement disponible lorsque `should_remesh` est défini sur `"true"`. |
| `symmetry_mode` | COMBO | Oui | `"auto"`<br>`"on"`<br>`"off"` | Contrôle si la symétrie est appliquée au modèle généré. |
| `should_texture` | COMBO | Oui | `"true"`<br>`"false"` | Détermine si des textures sont générées. Le définir sur `"false"` ignore la phase de texturation et renvoie un maillage sans textures. |
| `enable_pbr` | BOOLEAN | Non | Vrai / Faux | Lorsque `should_texture` est `"true"`, cette option génère des cartes PBR (métallique, rugosité, normale) en plus de la couleur de base (par défaut : Faux). |
| `texture_prompt` | STRING | Non | - | Une invite textuelle pour guider le processus de texturation (600 caractères maximum). Ne peut pas être utilisé en même temps que `texture_image`. Ce paramètre est uniquement disponible lorsque `should_texture` est défini sur `"true"`. |
| `texture_image` | IMAGE | Non | - | Une image pour guider le processus de texturation. Un seul des deux paramètres `texture_image` ou `texture_prompt` peut être utilisé à la fois. Ce paramètre est uniquement disponible lorsque `should_texture` est défini sur `"true"`. |
| `pose_mode` | COMBO | Oui | `""` (vide)<br>`"A-pose"`<br>`"T-pose"` | Spécifie le mode de pose pour le modèle généré. |
| `seed` | INT | Oui | 0 à 2147483647 | Une valeur de graine pour le processus de génération (par défaut : 0). Les résultats ne sont pas déterministes quelle que soit la graine, mais changer la graine peut déclencher une nouvelle exécution du nœud. |

**Contraintes des paramètres :**

* Vous devez fournir entre 2 et 4 images pour l'entrée `images`.
* Les paramètres `topology` et `target_polycount` sont uniquement actifs lorsque `should_remesh` est défini sur `"true"`.
* Les paramètres `enable_pbr`, `texture_prompt` et `texture_image` sont uniquement actifs lorsque `should_texture` est défini sur `"true"`.
* Vous ne pouvez pas utiliser `texture_prompt` et `texture_image` en même temps ; ils sont mutuellement exclusifs.

## Sorties

| Nom de la sortie | Type de données | Description |
| :--- | :--- | :--- |
| `model_file` | STRING | Le nom du fichier du modèle GLB généré. Cette sortie est fournie pour la rétrocompatibilité. |
| `meshy_task_id` | MESHY_TASK_ID | L'identifiant unique de la tâche API Meshy. |
| `GLB` | FILE3DGLB | Le modèle 3D généré au format GLB. |
| `FBX` | FILE3DFBX | Le modèle 3D généré au format FBX. |

---
**Source fingerprint (SHA-256):** `e6f75f50645c8b2cf5ebbe037edb077ef1eb0ea1baf67c581d60ac0033686d00`
