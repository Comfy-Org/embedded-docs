> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningCombine/fr.md)

Le nœud PairConditioningCombine combine deux paires de données de conditionnement (positive et négative) en une seule paire. Il prend deux paires de conditionnement distinctes en entrée et les fusionne en utilisant la logique interne de combinaison de conditionnement de ComfyUI. Ce nœud est expérimental et principalement utilisé pour des workflows avancés de manipulation de conditionnement.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `positive_A` | CONDITIONING | Oui | - | Première entrée de conditionnement positive |
| `negative_A` | CONDITIONING | Oui | - | Première entrée de conditionnement négative |
| `positive_B` | CONDITIONING | Oui | - | Deuxième entrée de conditionnement positive |
| `negative_B` | CONDITIONING | Oui | - | Deuxième entrée de conditionnement négative |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Sortie de conditionnement positive combinée |
| `negative` | CONDITIONING | Sortie de conditionnement négative combinée |