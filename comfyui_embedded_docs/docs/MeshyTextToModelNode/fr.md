# Meshy : Texte vers modèle

Le nœud Meshy : Text to Model utilise l'API Meshy pour générer un modèle 3D à partir d'une description textuelle. Il envoie une requête à l'API avec votre prompt et vos paramètres, puis attend que la génération soit terminée et télécharge les fichiers du modèle résultant.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `modèle` | Spécifie la version du modèle IA à utiliser pour la génération. | COMBO | Oui | `"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `invite` | La description textuelle du modèle 3D que vous souhaitez générer. La longueur doit être comprise entre 1 et 600 caractères. | STRING | Oui | 1 - 600 caractères |
| `style` | Le style artistique du modèle 3D généré. | COMBO | Oui | `"realistic"` |
| `doit_remesher` | Lorsqu'il est défini sur « false », renvoie un maillage triangulaire non traité. La sélection de « true » révèle des paramètres supplémentaires pour la topologie et le nombre de polygones cible. | DYNAMIC_COMBO | Oui | `"true"`<br>`"false"` |
| `topology` | Le type de polygones cible pour le modèle remaillé. Ce paramètre n'est disponible que lorsque `should_remesh` est défini sur « true ». | COMBO | Non* | `"triangle"`<br>`"quad"` |
| `target_polycount` | Le nombre de polygones cible pour le modèle remaillé. La valeur par défaut est 300000. Ce paramètre n'est disponible que lorsque `should_remesh` est défini sur « true ». | INT | Non* | 100 - 300000 |
| `mode_symétrie` | Contrôle la symétrie du modèle généré. Ce paramètre est avancé. | COMBO | Oui | `"auto"`<br>`"on"`<br>`"off"` |
| `mode_pose` | Spécifie le mode de pose du modèle généré. Une chaîne vide signifie qu'aucune pose spécifique n'est demandée. Ce paramètre est avancé. | COMBO | Oui | `""`<br>`"A-pose"`<br>`"T-pose"` |
| `graine` | Le seed contrôle si le nœud doit être relancé ; les résultats sont non déterministes quel que soit le seed. La valeur par défaut est 0. | INT | Oui | 0 - 2147483647 |
| `ultra_mode` | Exécute une passe de raffinement supplémentaire pour une géométrie de plus haute fidélité avec un niveau de détail de surface plus fin. La valeur par défaut est false. | BOOLEAN | Oui | true<br>false |

*Remarque : Les paramètres `topology` et `target_polycount` sont disponibles sous condition. Ils n'apparaissent que lorsque le paramètre `should_remesh` est défini sur « true ».

Lorsque `ultra_mode` est activé, le paramètre `model` doit être défini sur `"meshy-7"` ou `"latest"`.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `fichier_modèle` | Le nom de fichier du modèle GLB généré. Cette sortie est fournie pour la rétrocompatibilité. | STRING |
| `meshy_task_id` | L'identifiant unique de la tâche API Meshy. | MESHY_TASK_ID |
| `GLB` | Le fichier de modèle 3D généré au format GLB. | FILE3DGLB |
| `FBX` | Le fichier de modèle 3D généré au format FBX. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextToModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `131f17bfb788f206e15c1d48c877e822114902fadf073a6f9fb25e8340421122`
