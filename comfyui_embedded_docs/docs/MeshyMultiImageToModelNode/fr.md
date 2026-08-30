# Meshy : Multi-image vers modèle

Ce nœud utilise l'API Meshy pour générer un modèle 3D à partir de plusieurs images d'entrée. Il télécharge les images fournies, soumet une tâche de traitement et renvoie les fichiers du modèle 3D résultant (GLB et FBX) ainsi que l'identifiant de la tâche pour référence.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Spécifie la version du modèle IA à utiliser. | COMBO | Oui | `"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `should_remesh` | Détermine si le maillage généré est traité. Lorsqu'il est défini sur `"false"`, le nœud renvoie un maillage triangulaire non traité. Lorsqu'il est défini sur `"true"`, les paramètres de remaillage ci-dessous sont affichés. | DYNAMIC_COMBO | Oui | `"true"`<br>`"false"` |
| `symmetry_mode` | Contrôle si une symétrie est appliquée au modèle généré. | COMBO | Oui | `"auto"`<br>`"on"`<br>`"off"` |
| `should_texture` | Détermine si les textures sont générées. Le définir sur `"false"` ignore la phase de texturation et renvoie un maillage sans textures. Lorsqu'il est défini sur `"true"`, les paramètres de texture ci-dessous sont affichés. | DYNAMIC_COMBO | Oui | `"true"`<br>`"false"` |
| `pose_mode` | Spécifie le mode de pose pour le modèle généré. | COMBO | Oui | `""` (vide)<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | Le seed contrôle si le nœud doit se relancer ; les résultats sont non déterministes quel que soit le seed. (défaut : 0) | INT | Oui | 0 à 2147483647 |

### Paramètres de remaillage (visibles lorsque `should_remesh` est `"true"`)

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `topology` | Le type de polygone cible pour la sortie remaillée. | COMBO | Non | `"triangle"`<br>`"quad"` |
| `target_polycount` | Le nombre cible de polygones pour le modèle remaillé (défaut : 300000). | INT | Non | 100 à 300000 |

### Paramètres de texture (visibles lorsque `should_texture` est `"true"`)

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `enable_pbr` | Génère des cartes PBR (métallique, rugosité, normale) en plus de la couleur de base. (défaut : False) | BOOLEAN | Non | True / False |
| `texture_prompt` | Fournissez une invite textuelle pour guider le processus de texturation. 600 caractères maximum. Ne peut pas être utilisé en même temps que `texture_image`. (défaut : vide) | STRING | Non | Jusqu'à 600 caractères |
| `texture_image` | Un seul de `texture_image` ou `texture_prompt` peut être utilisé en même temps. | IMAGE | Non | - |
| `texture_resolution` | Résolution de la texture de couleur de base. Les résolutions plus élevées capturent davantage de détails de surface. | COMBO | Non | `"2k"`<br>`"4k"`<br>`"8k"` |

### Entrées d'images

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `images` | Emplacement extensible : connectez 2 à 4 images d'entrée (`image_1`, `image_2`, `image_3`, `image_4`). Ces images sont utilisées pour générer le modèle 3D. | IMAGE | Oui | 2 à 4 images |

**Remarques**

* Vous devez fournir entre 2 et 4 images pour l'entrée `images`.
* Les paramètres `topology` et `target_polycount` ne sont actifs que lorsque `should_remesh` est défini sur `"true"`.
* Les paramètres `enable_pbr`, `texture_prompt`, `texture_image` et `texture_resolution` ne sont actifs que lorsque `should_texture` est défini sur `"true"`.
* `texture_prompt` et `texture_image` sont mutuellement exclusifs ; vous ne pouvez pas utiliser les deux en même temps. `texture_prompt` est limité à 600 caractères.
* La valeur `seed` ne rend pas les résultats déterministes ; la modifier fait simplement que le nœud relance la tâche de génération.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model_file` | Le nom de fichier du modèle GLB généré. Cette sortie n'est fournie que pour la rétrocompatibilité. | STRING |
| `meshy_task_id` | L'identifiant unique pour la tâche de l'API Meshy. | MESHY_TASK_ID |
| `GLB` | Le modèle 3D généré au format GLB. | FILE3DGLB |
| `FBX` | Le modèle 3D généré au format FBX. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyMultiImageToModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `a8b2fc23ef8a8a4af097489c15beb3e0ed205dfdc8309afc95207d7a5616d37a`
