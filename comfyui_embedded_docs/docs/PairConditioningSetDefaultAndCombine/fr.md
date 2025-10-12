> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetDefaultAndCombine/fr.md)

Le nœud PairConditioningSetDefaultAndCombine définit des valeurs de conditionnement par défaut et les combine avec les données de conditionnement d'entrée. Il prend des entrées de conditionnement positif et négatif ainsi que leurs contreparties par défaut, puis les traite via le système de hooks de ComfyUI pour produire des sorties de conditionnement finales qui intègrent les valeurs par défaut.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Oui | - | L'entrée de conditionnement positif principale à traiter |
| `negative` | CONDITIONING | Oui | - | L'entrée de conditionnement négatif principale à traiter |
| `positive_DEFAULT` | CONDITIONING | Oui | - | Les valeurs de conditionnement positif par défaut à utiliser comme solution de repli |
| `negative_DEFAULT` | CONDITIONING | Oui | - | Les valeurs de conditionnement négatif par défaut à utiliser comme solution de repli |
| `hooks` | HOOKS | Non | - | Groupe de hooks optionnel pour une logique de traitement personnalisée |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Le conditionnement positif traité avec les valeurs par défaut incorporées |
| `negative` | CONDITIONING | Le conditionnement négatif traité avec les valeurs par défaut incorporées |