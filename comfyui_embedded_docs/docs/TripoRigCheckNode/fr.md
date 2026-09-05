# TripoRigCheckNode

Ce nœud envoie l’identifiant d’une tâche Tripo 3D terminée à l’API Tripo et vérifie si ce modèle peut être armaturé (riggé). Il attend la fin de la vérification, puis renvoie un résultat oui/non ainsi que le type de squelette recommandé par Tripo pour le modèle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_task_id` | L’identifiant de tâche Tripo du modèle à analyser. Il identifie un modèle précédemment généré, importé ou autrement créé via une tâche Tripo. | STRING | Oui | N/A |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `riggable` | Indique si le modèle peut être armaturé. | BOOLEAN |
| `rig_type` | Squelette recommandé : biped, quadruped, hexapod, octopod, avian, serpentine ou aquatic ; « others » lorsque le modèle ne peut pas être armaturé. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigCheckNode/fr.md)

---
**Source fingerprint (SHA-256):** `3aa0bc194e887804b92ca1f9f2b12997c73e111fb282c5de96e55f664c21545e`
