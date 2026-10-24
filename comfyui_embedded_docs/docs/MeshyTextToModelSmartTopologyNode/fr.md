# Meshy: Text to Model (Smart Topology)

Ce nœud génère un maillage triangulaire prêt pour le jeu avec un nombre de faces cible via Meshy T2.5. La topologie est construite avec le nombre de polygones demandé plutôt que d’être décimée après coup, de sorte que le résultat est prêt pour un moteur de jeu sans passe de retopologie distincte.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | La version du modèle Meshy à utiliser pour la génération. | COMBO | Oui | `"meshy-t2.5"` |
| `prompt` | Description textuelle du modèle 3D à générer. | STRING | Oui | 1 à 800 caractères |
| `target_polycount` | Nombre approximatif de triangles dans le maillage généré. Par défaut : 15000. | INT | Oui | 100 à 30000 |
| `pose_mode` | Pose du personnage généré. Une chaîne vide ne demande aucune pose spécifique. Il s’agit d’un paramètre avancé. Par défaut : `""` (chaîne vide). | COMBO | Oui | `""`<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats ne sont pas déterministes quelle que soit la graine. Par défaut : 42. | INT | Oui | 0 à 2147483647 |

**Contraintes :**

* Le prompt doit contenir entre 1 et 800 caractères.
* `target_polycount` correspond au nombre de triangles à partir duquel le maillage est construit, et non à une limite appliquée après la génération.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `meshy_task_id` | Identifiant unique de la tâche d’API Meshy. | MESHY_TASK_ID |
| `GLB` | Le modèle 3D généré au format GLB. | FILE3DGLB |
| `FBX` | Le modèle 3D généré au format FBX. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextToModelSmartTopologyNode/fr.md)

---
**Source fingerprint (SHA-256):** `9fcdc846a4ba39cf3d099629637fbb0cf6d9c8d65bcee8aff5ec6ac5c76b6af3`
