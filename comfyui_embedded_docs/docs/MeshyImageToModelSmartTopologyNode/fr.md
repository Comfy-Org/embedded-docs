# Meshy: Image to Model (Smart Topology)

Ce nœud génère un maillage triangulaire prêt pour le jeu à partir d’une image de référence, avec un nombre de faces cible, via Meshy T2.5. La topologie est construite au nombre de polygones demandé plutôt que d’être décimée après coup ; le résultat est donc directement utilisable dans un moteur de jeu, sans passe de retopologie séparée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Version du modèle Meshy à utiliser pour la génération. | COMBO | Oui | `"meshy-t2.5"` |
| `image` | Image de référence à partir de laquelle le modèle est généré. | IMAGE | Oui | - |
| `target_polycount` | Nombre approximatif de triangles dans le maillage généré. Par défaut : 15000. | INT | Oui | 100 à 30000 |
| `should_texture` | Détermine si les textures sont générées. `"false"` ignore la phase de texturation et renvoie un maillage non texturé. | DYNAMIC_COMBO | Oui | `"true"`<br>`"false"` |
| `enable_pbr` | Génère des cartes PBR (métallique, rugosité, normale) en plus de la couleur de base. Cette entrée n'est disponible que lorsque `should_texture` est défini sur `"true"`. Par défaut : `False`. | BOOLEAN | Non | - |
| `texture_prompt` | Prompt textuel pour guider le processus de texturation. Maximum 800 caractères. Il ne peut pas être utilisé en même temps que `texture_image`. Cette entrée n'est disponible que lorsque `should_texture` est défini sur `"true"`. Par défaut : `""` (chaîne vide). | STRING | Non | 1 à 800 caractères |
| `texture_image` | Image de référence pour le processus de texturation. Seule l'une des entrées `texture_image` ou `texture_prompt` peut être utilisée à la fois. Cette entrée n'est disponible que lorsque `should_texture` est défini sur `"true"`. | IMAGE | Non | - |
| `texture_resolution` | Résolution de la texture. Des résolutions plus élevées capturent davantage de détails de surface. Cette entrée n'est disponible que lorsque `should_texture` est défini sur `"true"`. | COMBO | Non | `"2k"`<br>`"4k"`<br>`"8k"` |
| `pose_mode` | Pose du personnage généré. Une chaîne vide indique qu'aucune pose spécifique n'est demandée. Il s'agit d'un paramètre avancé. Par défaut : `""` (chaîne vide). | COMBO | Oui | `""`<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | La graine détermine si le nœud doit être réexécuté ; les résultats ne sont pas déterministes, quelle que soit la graine. Par défaut : 42. | INT | Oui | 0 à 2147483647 |

**Remarque :** Les entrées `enable_pbr`, `texture_prompt`, `texture_image` et `texture_resolution` ne sont disponibles que lorsque `should_texture` est défini sur `"true"`.

**Contraintes :**

* `target_polycount` correspond au nombre de triangles à partir duquel le maillage est construit, et non à une limite appliquée après la génération.
* Lorsque `should_texture` est défini sur `"true"`, `texture_prompt` et `texture_image` ne peuvent pas être utilisés en même temps. Si les deux sont fournis, le nœud lève une erreur.
* `texture_prompt` a une longueur maximale de 800 caractères.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `meshy_task_id` | Identifiant unique de la tâche API Meshy. | MESHY_TASK_ID |
| `GLB` | Modèle 3D généré au format GLB. | FILE3DGLB |
| `FBX` | Modèle 3D généré au format FBX. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToModelSmartTopologyNode/fr.md)

---
**Source fingerprint (SHA-256):** `e78034a591825ec6e105df1942cf501e882ac780cc2584bfa04b424ecc34a02e`
