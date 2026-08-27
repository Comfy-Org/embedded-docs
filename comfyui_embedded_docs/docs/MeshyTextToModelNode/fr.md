# Meshy : Texte vers modèle

Le nœud Meshy: Text to Model utilise l'API Meshy pour générer un modèle 3D à partir d'une description textuelle. Il envoie une requête à l'API avec votre prompt et vos paramètres, puis attend que la génération soit terminée et télécharge les fichiers de modèle résultants.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Spécifie la version du modèle IA à utiliser. Actuellement, seule la version "latest" est disponible. | COMBO | Oui | `"latest"` |
| `invite` | La description textuelle du modèle 3D que vous souhaitez générer. Doit contenir entre 1 et 600 caractères. | STRING | Oui | - |
| `style` | Le style artistique du modèle 3D généré. | COMBO | Oui | `"realistic"`<br>`"sculpture"` |
| `doit_remesher` | Contrôle si le maillage généré est traité. Lorsqu'il est défini sur "false", le nœud renvoie un maillage triangulaire non traité. La sélection de "true" révèle des paramètres supplémentaires pour la topologie et le nombre de polygones. | DYNAMIC_COMBO | Oui | `"true"`<br>`"false"` |
| `topology` | Le type de polygone cible pour le modèle remaillé. Ce paramètre n'est disponible que lorsque `should_remesh` est défini sur "true". | COMBO | Non* | `"triangle"`<br>`"quad"` |
| `target_polycount` | Le nombre de polygones cible pour le modèle remaillé. La valeur par défaut est 300000. Ce paramètre n'est disponible que lorsque `should_remesh` est défini sur "true". | INT | Non* | 100 - 300000 |
| `mode_symétrie` | Contrôle la symétrie du modèle généré. Ceci est un paramètre avancé. | COMBO | Oui | `"auto"`<br>`"on"`<br>`"off"` |
| `mode_pose` | Spécifie le mode de pose pour le modèle généré. Une chaîne vide signifie qu'aucune pose spécifique n'est demandée. Ceci est un paramètre avancé. | COMBO | Oui | `""`<br>`"A-pose"`<br>`"T-pose"` |
| `graine` | Le paramètre `seed` contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. La valeur par défaut est 0. | INT | Oui | 0 - 2147483647 |

*Remarque : Les paramètres `topology` et `target_polycount` sont disponibles conditionnellement. Ils n'apparaissent que lorsque le paramètre `should_remesh` est défini sur "true".

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `fichier_modèle` | Le nom du fichier du modèle GLB généré. Cette sortie est fournie pour la rétrocompatibilité. | STRING |
| `meshy_task_id` | L'identifiant unique pour la tâche de l'API Meshy. | MESHY_TASK_ID |
| `GLB` | Le fichier de modèle 3D généré au format GLB. | FILE3DGLB |
| `FBX` | Le fichier de modèle 3D généré au format FBX. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextToModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `1860b2d760aa81d611d4f44114591b4d98ccb85075bd1e06beabf462fb58bd53`
