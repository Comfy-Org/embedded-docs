# Meshy : Texte vers modèle

Le nœud Meshy: Text to Model utilise l'API Meshy pour générer un modèle 3D à partir d'une description textuelle. Il envoie une requête à l'API avec votre prompt et vos paramètres, puis attend la fin de la génération et télécharge les fichiers de modèle résultants.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Spécifie la version du modèle d'IA à utiliser pour la génération. | COMBO | Oui | `"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `prompt` | Description textuelle du modèle 3D que vous souhaitez générer. Doit contenir entre 1 et 600 caractères. La valeur par défaut est une chaîne vide. | STRING | Oui | 1 - 600 caractères |
| `style` | Le style artistique du modèle 3D généré. | COMBO | Oui | `"realistic"` |
| `should_remesh` | Lorsqu'il est défini sur false, renvoie un maillage triangulaire non traité. Sélectionner "true" révèle des paramètres supplémentaires pour la topologie et le nombre de polygones cible. | DYNAMIC_COMBO | Oui | `"true"`<br>`"false"` |
| `topology` | Type de polygone cible pour le modèle remaillé. Ce paramètre n'est disponible que lorsque `should_remesh` est défini sur "true". | COMBO | Non* | `"triangle"`<br>`"quad"` |
| `target_polycount` | Nombre cible de polygones pour le modèle remaillé. La valeur par défaut est 300000. Ce paramètre n'est disponible que lorsque `should_remesh` est défini sur "true". | INT | Non* | 100 - 300000 |
| `symmetry_mode` | Contrôle la symétrie dans le modèle généré. Il s'agit d'un paramètre avancé. Les options sont `"auto"`, `"on"` et `"off"`. | COMBO | Oui | `"auto"`<br>`"on"`<br>`"off"` |
| `pose_mode` | Spécifie le mode de pose du modèle généré. Une chaîne vide signifie qu'aucune pose spécifique n'est demandée. Il s'agit d'un paramètre avancé. | COMBO | Oui | `""`<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. La valeur par défaut est 0. | INT | Oui | 0 - 2147483647 |
| `ultra_mode` | Exécute une passe de raffinement supplémentaire pour une géométrie de plus haute fidélité avec des détails de surface plus fins. La valeur par défaut est false. | BOOLEAN | Oui | true<br>false |

*Remarque : Les paramètres `topology` et `target_polycount` sont disponibles conditionnellement. Ils n'apparaissent que lorsque le paramètre `should_remesh` est défini sur "true".

Lorsque `ultra_mode` est activé, le paramètre `model` doit être défini sur `"meshy-7"` ou `"latest"`. Si un autre modèle est sélectionné avec `ultra_mode`, le nœud génère une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_file` | Nom de fichier du modèle GLB généré. Cette sortie est fournie pour la compatibilité descendante. | STRING |
| `meshy_task_id` | Identifiant unique de la tâche de l'API Meshy. | MESHY_TASK_ID |
| `GLB` | Fichier de modèle 3D généré au format GLB. | FILE3DGLB |
| `FBX` | Fichier de modèle 3D généré au format FBX. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextToModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `131f17bfb788f206e15c1d48c877e822114902fadf073a6f9fb25e8340421122`
