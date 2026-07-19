# Meshy : Multi-image vers modèle

Ce nœud utilise l'API Meshy pour générer un modèle 3D à partir de plusieurs images d'entrée. Il télécharge les images fournies, soumet une tâche de traitement et renvoie les fichiers du modèle 3D résultant (GLB et FBX) ainsi que l'identifiant de la tâche pour référence.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Spécifie la version du modèle d'IA à utiliser. | COMBO | Oui | `"latest"` |
| `images` | Un ensemble d'images utilisé pour générer le modèle 3D. Vous devez fournir entre 2 et 4 images. | IMAGE | Oui | 2 à 4 images |
| `should_remesh` | Détermine si le maillage généré doit être traité. Lorsqu'il est défini sur `"false"`, le nœud renvoie un maillage triangulaire non traité. | COMBO | Oui | `"true"`<br>`"false"` |
| `topology` | Le type de polygone cible pour la sortie remaillée. Ce paramètre est uniquement disponible et requis lorsque `should_remesh` est défini sur `"true"`. | COMBO | Non | `"triangle"`<br>`"quad"` |
| `target_polycount` | Le nombre cible de polygones pour le modèle remaillé (par défaut : 300000). Ce paramètre est uniquement disponible lorsque `should_remesh` est défini sur `"true"`. | INT | Non | 100 à 300000 |
| `symmetry_mode` | Contrôle si la symétrie est appliquée au modèle généré. | COMBO | Oui | `"auto"`<br>`"on"`<br>`"off"` |
| `should_texture` | Détermine si des textures sont générées. Le définir sur `"false"` ignore la phase de texturation et renvoie un maillage sans textures. | COMBO | Oui | `"true"`<br>`"false"` |
| `enable_pbr` | Lorsque `should_texture` est `"true"`, cette option génère des cartes PBR (métallique, rugosité, normale) en plus de la couleur de base (par défaut : Faux). | BOOLEAN | Non | Vrai / Faux |
| `texture_prompt` | Une invite textuelle pour guider le processus de texturation (600 caractères maximum). Ne peut pas être utilisé en même temps que `texture_image`. Ce paramètre est uniquement disponible lorsque `should_texture` est défini sur `"true"`. | STRING | Non | - |
| `texture_image` | Une image pour guider le processus de texturation. Un seul des deux paramètres `texture_image` ou `texture_prompt` peut être utilisé à la fois. Ce paramètre est uniquement disponible lorsque `should_texture` est défini sur `"true"`. | IMAGE | Non | - |
| `pose_mode` | Spécifie le mode de pose pour le modèle généré. | COMBO | Oui | `""` (vide)<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | Une valeur de graine pour le processus de génération (par défaut : 0). Les résultats ne sont pas déterministes quelle que soit la graine, mais changer la graine peut déclencher une nouvelle exécution du nœud. | INT | Oui | 0 à 2147483647 |

**Contraintes des paramètres :**

* Vous devez fournir entre 2 et 4 images pour l'entrée `images`.
* Les paramètres `topology` et `target_polycount` sont uniquement actifs lorsque `should_remesh` est défini sur `"true"`.
* Les paramètres `enable_pbr`, `texture_prompt` et `texture_image` sont uniquement actifs lorsque `should_texture` est défini sur `"true"`.
* Vous ne pouvez pas utiliser `texture_prompt` et `texture_image` en même temps ; ils sont mutuellement exclusifs.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `model_file` | Le nom du fichier du modèle GLB généré. Cette sortie est fournie pour la rétrocompatibilité. | STRING |
| `meshy_task_id` | L'identifiant unique de la tâche API Meshy. | MESHY_TASK_ID |
| `GLB` | Le modèle 3D généré au format GLB. | FILE3DGLB |
| `FBX` | Le modèle 3D généré au format FBX. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyMultiImageToModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `e6f75f50645c8b2cf5ebbe037edb077ef1eb0ea1baf67c581d60ac0033686d00`
