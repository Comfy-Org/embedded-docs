> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningTimestepsRange/fr.md)

Le nœud ConditioningTimestepsRange crée trois plages de pas de temps distinctes pour contrôler quand les effets de conditionnement sont appliqués pendant le processus de génération. Il prend des valeurs de pourcentage de début et de fin et divise la plage complète des pas de temps (0.0 à 1.0) en trois segments : la plage principale entre les pourcentages spécifiés, la plage avant le pourcentage de début et la plage après le pourcentage de fin.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `start_percent` | FLOAT | Oui | 0.0 - 1.0 | Le pourcentage de début de la plage de pas de temps (par défaut : 0.0) |
| `end_percent` | FLOAT | Oui | 0.0 - 1.0 | Le pourcentage de fin de la plage de pas de temps (par défaut : 1.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `AVANT_PLAGE` | TIMESTEPS_RANGE | La plage principale de pas de temps définie par start_percent et end_percent |
| `APRÈS_PLAGE` | TIMESTEPS_RANGE | La plage de pas de temps de 0.0 à start_percent |
| `AFTER_RANGE` | TIMESTEPS_RANGE | La plage de pas de temps de end_percent à 1.0 |
