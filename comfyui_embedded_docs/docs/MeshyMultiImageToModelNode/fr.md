# Meshy : Multi-image vers modèle

Ce nœud utilise l’API Meshy pour générer un modèle 3D à partir de plusieurs images d’entrée. Il téléverse les images fournies, soumet une tâche de traitement et renvoie les fichiers du modèle 3D résultant (GLB et FBX) ainsi que l’identifiant de tâche pour référence.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Spécifie la version du modèle d’IA à utiliser. | COMBO | Oui | `"latest"` |
| `should_remesh` | Détermine si le maillage généré doit être traité. Lorsque la valeur est `"false"`, le nœud renvoie un maillage triangulaire non traité. Lorsque la valeur est `"true"`, les paramètres de remaillage ci-dessous sont affichés. | DYNAMIC_COMBO | Oui | `"true"`<br>`"false"` |
| `symmetry_mode` | Contrôle l’application de la symétrie au modèle généré. | COMBO | Oui | `"auto"`<br>`"on"`<br>`"off"` |
| `should_texture` | Détermine si des textures sont générées. La définir sur `"false"` ignore la phase de texturation et renvoie un maillage sans texture. Lorsque la valeur est `"true"`, les paramètres de texture ci-dessous sont affichés. | DYNAMIC_COMBO | Oui | `"true"`<br>`"false"` |
| `pose_mode` | Définit le mode de pose du modèle généré. | COMBO | Oui | `""` (vide)<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | Le paramètre `seed` contrôle si le nœud doit se relancer ; les résultats ne sont pas déterministes quelle que soit la valeur de `seed`. (défaut : 0) | INT | Oui | 0 à 2147483647 |

### Paramètres de remaillage (visibles lorsque `should_remesh` est défini sur `"true"`)

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `topology` | Le type de polygone cible pour la sortie remaillée. | COMBO | Non | `"triangle"`<br>`"quad"` |
| `target_polycount` | Le nombre de polygones cible pour le modèle remaillé (défaut : 300000). | INT | Non | 100 à 300000 |

### Paramètres de texture (visibles lorsque `should_texture` est défini sur `"true"`)

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `enable_pbr` | Génère des cartes PBR (métallique, rugosité, normale) en plus de la couleur de base. (défaut : False) | BOOLEAN | Non | True / False |
| `texture_prompt` | Fournissez une invite textuelle pour guider le processus de texturation. 600 caractères maximum. Ce paramètre ne peut pas être utilisé en même temps que `texture_image`. (défaut : vide) | STRING | Non | - |
| `texture_image` | Un seul des paramètres `texture_image` ou `texture_prompt` peut être utilisé à la fois. | IMAGE | Non | - |

### Entrées d’image

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `images` | Emplacement extensible : connectez 2 à 4 images d’entrée (`image_1`, `image_2`, `image_3`, `image_4`). Ces images servent à générer le modèle 3D. | IMAGE | Oui | 2 à 4 images |

**Remarques**

* Vous devez fournir entre 2 et 4 images pour l’entrée `images`.
* Les paramètres `topology` et `target_polycount` ne sont actifs que lorsque `should_remesh` est défini sur `"true"`.
* Les paramètres `enable_pbr`, `texture_prompt` et `texture_image` ne sont actifs que lorsque `should_texture` est défini sur `"true"`.
* `texture_prompt` et `texture_image` sont mutuellement exclusifs ; vous ne pouvez pas utiliser les deux à la fois. `texture_prompt` est limité à 600 caractères.
* La valeur `seed` ne rend pas les résultats déterministes ; la modifier ne fait que relancer la tâche de génération.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model_file` | Le nom de fichier du modèle GLB généré. Cette sortie n’est fournie que pour la rétrocompatibilité. | STRING |
| `meshy_task_id` | L’identifiant unique de la tâche de l’API Meshy. | MESHY_TASK_ID |
| `GLB` | Le modèle 3D généré au format GLB. | FILE3DGLB |
| `FBX` | Le modèle 3D généré au format FBX. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyMultiImageToModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `c2282cad611bbbc8c0a618df6a68fcd9f6e3c29c6d08b2c96a117c29765d8a7a`
