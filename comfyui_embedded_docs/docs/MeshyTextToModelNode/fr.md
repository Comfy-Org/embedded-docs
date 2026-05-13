> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextToModelNode/fr.md)

Voici la traduction en français de la documentation du nœud MeshyTextToModelNode :

Le nœud Meshy : Texte vers modèle utilise l'API Meshy pour générer un modèle 3D à partir d'une description textuelle. Il envoie une requête à l'API avec votre invite et vos paramètres, puis attend la fin de la génération et télécharge les fichiers du modèle résultant.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `modèle` | COMBO | Oui | `"latest"` | Spécifie la version du modèle d'IA à utiliser. Actuellement, seule la version "latest" est disponible. |
| `invite` | STRING | Oui | - | La description textuelle du modèle 3D que vous souhaitez générer. Doit contenir entre 1 et 600 caractères. |
| `style` | COMBO | Oui | `"realistic"`<br>`"sculpture"` | Le style artistique pour le modèle 3D généré. |
| `doit_remesher` | DYNAMIC COMBO | Oui | `"true"`<br>`"false"` | Contrôle si le maillage généré est traité. Lorsqu'il est défini sur "false", le nœud renvoie un maillage triangulaire non traité. La sélection de "true" révèle des paramètres supplémentaires pour la topologie et le nombre de polygones. |
| `topology` | COMBO | Non* | `"triangle"`<br>`"quad"` | Le type de polygone cible pour le modèle remaillé. Ce paramètre n'est disponible et requis que lorsque `doit_remesher` est défini sur "true". |
| `target_polycount` | INT | Non* | 100 - 300000 | Le nombre cible de polygones pour le modèle remaillé. La valeur par défaut est 300000. Ce paramètre n'est disponible et requis que lorsque `doit_remesher` est défini sur "true". |
| `mode_symétrie` | COMBO | Oui | `"auto"`<br>`"on"`<br>`"off"` | Contrôle la symétrie dans le modèle généré. |
| `mode_pose` | COMBO | Oui | `""`<br>`"A-pose"`<br>`"T-pose"` | Spécifie le mode de pose pour le modèle généré. Une chaîne vide signifie qu'aucune pose spécifique n'est demandée. |
| `graine` | INT | Oui | 0 - 2147483647 | Une valeur de graine pour la génération. La définition de ce paramètre contrôle si le nœud doit être réexécuté, mais les résultats sont non déterministes quelle que soit la valeur de la graine. La valeur par défaut est 0. |

*Remarque : Les paramètres `topology` et `target_polycount` sont conditionnellement requis. Ils n'apparaissent et ne doivent être définis que lorsque le paramètre `should_remesh` est défini sur "true".

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `meshy_task_id` | STRING | Le nom du fichier du modèle GLB généré. Cette sortie est fournie pour la rétrocompatibilité. |
| `GLB` | MESHY_TASK_ID | L'identifiant unique de la tâche API Meshy. |
| `FBX` | FILE3DGLB | Le fichier de modèle 3D généré au format GLB. |
| `FBX` | FILE3DFBX | Le fichier de modèle 3D généré au format FBX. |

---
**Source fingerprint (SHA-256):** `122eee5488a89433bd1f3bf79ccd8e9c51fd23cc1dfb208c39a0628c2ad3d817`
