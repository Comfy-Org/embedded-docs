> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetDefaultAndCombine/fr.md)

Ce nœud combine des données de conditionnement avec des données de conditionnement par défaut en utilisant un système basé sur des hooks. Il prend une entrée de conditionnement principale et une entrée de conditionnement par défaut, puis les fusionne selon la configuration de hook spécifiée. Le résultat est une sortie de conditionnement unique qui intègre les deux sources.

## Entrées

| Paramètre | Type de données | Type d'entrée | Par défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `cond` | CONDITIONING | Requis | - | - | L'entrée de conditionnement principale à traiter |
| `cond_DEFAULT` | CONDITIONING | Requis | - | - | Les données de conditionnement par défaut à combiner avec le conditionnement principal |
| `hooks` | HOOKS | Optionnel | - | - | Configuration optionnelle des hooks qui contrôle la manière dont les données de conditionnement sont traitées et combinées |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Les données de conditionnement combinées résultant de la fusion des entrées de conditionnement principale et par défaut |
