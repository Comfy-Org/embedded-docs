# Plage de pas de temps

Le nœud `ConditioningTimestepsRange` crée trois plages de pas de temps distinctes pour contrôler le moment où les effets de conditionnement sont appliqués pendant le processus de génération. Il prend des valeurs de pourcentage de début et de fin et divise la plage de pas de temps entière (0,0 à 1,0) en trois segments : la plage principale entre les pourcentages spécifiés, la plage avant le pourcentage de début et la plage après le pourcentage de fin.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `start_percent` | Le pourcentage de début de la plage de pas de temps (par défaut : 0,0) | FLOAT | Oui | 0,0 - 1,0 |
| `end_percent` | Le pourcentage de fin de la plage de pas de temps (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |


| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `TIMESTEPS_RANGE` | La plage de pas de temps principale définie par `start_percent` et `end_percent` | TIMESTEPS_RANGE |
| `BEFORE_RANGE` | La plage de pas de temps de 0,0 à `start_percent` | TIMESTEPS_RANGE |
| `AFTER_RANGE` | La plage de pas de temps de `end_percent` à 1,0 | TIMESTEPS_RANGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningTimestepsRange/fr.md)

---
**Source fingerprint (SHA-256):** `dee21b5ac80fabdeacf3f4a985550fff795702e02911400ae49a97baae834e5e`
