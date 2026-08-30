# Meshy : Affiner le modèle brouillon

Le nœud Meshy: Refine Draft Model prend un modèle 3D provisoire issu d'une tâche Meshy précédente et l'améliore, en ajoutant éventuellement des textures à l'aide d'une invite de texte ou d'une image de référence. Il soumet la tâche d'affinage à l'API Meshy et renvoie le modèle finalisé sous forme de fichiers GLB et FBX une fois la tâche terminée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle IA utilisé pour affiner le modèle provisoire. | COMBO | Oui | `"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `meshy_task_id` | L'identifiant unique de la tâche du modèle provisoire que vous souhaitez affiner. | MESHY_TASK_ID | Oui | - |
| `activer_pbr` | Génère des cartes PBR (métallique, rugosité, normale) en plus de la couleur de base. Remarque : cette option doit être définie sur false lors de l'utilisation du style Sculpture, car ce style génère son propre ensemble de cartes PBR. (par défaut : False) | BOOLEAN | Oui | - |
| `invite_texture` | Fournissez une invite de texte pour guider le processus de texturation. 600 caractères maximum. Ne peut pas être utilisé en même temps que `texture_image`. (par défaut : chaîne vide) | STRING | Oui | - |
| `image_texture` | Un seul de `texture_image` ou `texture_prompt` peut être utilisé en même temps. | IMAGE | Non | - |
| `texture_resolution` | Résolution de la texture de couleur de base. Des résolutions plus élevées capturent plus de détails de surface. | COMBO | Oui | `"2k"`<br>`"4k"`<br>`"8k"` |

**Remarque :** Les entrées `texture_prompt` et `texture_image` sont mutuellement exclusives. Vous ne pouvez pas fournir à la fois une invite de texte et une image pour la texturation dans la même opération.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_file` | Le nom de fichier du modèle GLB généré. (Uniquement pour la rétrocompatibilité) | STRING |
| `meshy_task_id` | L'identifiant unique de la tâche pour le travail d'affinage soumis. | MESHY_TASK_ID |
| `GLB` | Le modèle 3D affiné final au format GLB. | FILE3DGLB |
| `FBX` | Le modèle 3D affiné final au format FBX. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRefineNode/fr.md)

---
**Source fingerprint (SHA-256):** `73c9d712c4fd9fdd2792600ce874916ce9447d386407353c886f624641fa0e0f`
