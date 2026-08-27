# Meshy : Image vers modèle

Le nœud Meshy: Image to Model utilise l'API Meshy pour générer un modèle 3D à partir d'une seule image d'entrée. Il téléverse votre image, soumet une tâche de traitement et renvoie les fichiers du modèle 3D généré (GLB et FBX) ainsi que l'identifiant de tâche pour référence.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Spécifie la version du modèle d'IA à utiliser pour la génération. | COMBO | Oui | `"latest"` |
| `image` | L'image d'entrée à convertir en modèle 3D. | IMAGE | Oui | - |
| `should_remesh` | Lorsqu'elle est définie sur `"false"`, renvoie un maillage triangulaire non traité. | DYNAMIC_COMBO | Oui | `"true"`<br>`"false"` |
| `topology` | La topologie de polygones cible pour le modèle remaillé. Cette entrée n'est disponible que lorsque `should_remesh` est défini sur `"true"`. | COMBO | Non* | `"triangle"`<br>`"quad"` |
| `target_polycount` | Le nombre cible de polygones pour le modèle remaillé. Cette entrée n'est disponible que lorsque `should_remesh` est défini sur `"true"`. Par défaut : 300000. | INT | Non* | 100 - 300000 |
| `symmetry_mode` | Contrôle la symétrie appliquée au modèle 3D généré. | COMBO | Oui | `"auto"`<br>`"on"`<br>`"off"` |
| `should_texture` | Détermine si des textures sont générées. La définir sur `"false"` ignore la phase de texturation et renvoie un maillage sans textures. | DYNAMIC_COMBO | Oui | `"true"`<br>`"false"` |
| `enable_pbr` | Génère des cartes PBR (métallique, rugosité, normale) en plus de la couleur de base. Cette entrée n'est disponible que lorsque `should_texture` est défini sur `"true"`. Par défaut : `False`. | BOOLEAN | Non* | - |
| `texture_prompt` | Fournissez une invite textuelle pour guider le processus de texturation. 600 caractères maximum. Ne peut pas être utilisée en même temps que `texture_image`. Cette entrée n'est disponible que lorsque `should_texture` est défini sur `"true"`. Par défaut : chaîne vide. | STRING | Non* | - |
| `texture_image` | Un seul de `texture_image` ou `texture_prompt` peut être utilisé en même temps. Cette entrée n'est disponible que lorsque `should_texture` est défini sur `"true"`. | IMAGE | Non* | - |
| `pose_mode` | Spécifiez le mode de pose pour le modèle généré. Il s'agit d'un paramètre avancé. | COMBO | Oui | `""` (vide)<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | La graine contrôle si le nœud doit s'exécuter à nouveau ; les résultats sont non déterministes quelle que soit la graine. Par défaut : 0. | INT | Oui | 0 - 2147483647 |

**Note sur les contraintes des paramètres :**

* Les entrées `topology` et `target_polycount` ne sont disponibles que lorsque `should_remesh` est défini sur `"true"`.
* Les entrées `enable_pbr`, `texture_prompt` et `texture_image` ne sont disponibles que lorsque `should_texture` est défini sur `"true"`.
* Lorsque `should_texture` est défini sur `"true"`, `texture_prompt` et `texture_image` ne peuvent pas être utilisés en même temps. Si les deux sont fournis, le nœud génère une erreur.
* `texture_prompt` a une longueur maximale de 600 caractères.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model_file` | Le nom de fichier du modèle GLB généré. Conservé uniquement pour la rétrocompatibilité. | STRING |
| `meshy_task_id` | L'identifiant unique de la tâche Meshy API, qui peut être utilisé pour référence ou pour le dépannage. | MESHY_TASK_ID |
| `GLB` | Le modèle 3D généré au format de fichier GLB. | FILE3DGLB |
| `FBX` | Le modèle 3D généré au format de fichier FBX. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `9f7abcb0db3c78715e4ba7370efe294caf186590f7ab62da8568778848fc838c`
