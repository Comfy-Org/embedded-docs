> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetPropertiesAndCombine/fr.md)

Le nœud PairConditioningSetPropertiesAndCombine modifie et combine des paires de conditionnement en appliquant de nouvelles données de conditionnement aux entrées de conditionnement positif et négatif existantes. Il vous permet d'ajuster la force du conditionnement appliqué et de contrôler la manière dont la zone de conditionnement est définie. Ce nœud est particulièrement utile pour les workflows avancés de manipulation du conditionnement où vous devez mélanger plusieurs sources de conditionnement ensemble.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Oui | - | L'entrée de conditionnement positif d'origine |
| `negative` | CONDITIONING | Oui | - | L'entrée de conditionnement négatif d'origine |
| `positive_NEW` | CONDITIONING | Oui | - | Le nouveau conditionnement positif à appliquer |
| `negative_NEW` | CONDITIONING | Oui | - | Le nouveau conditionnement négatif à appliquer |
| `force` | FLOAT | Oui | 0.0 à 10.0 | Le facteur de force pour l'application du nouveau conditionnement (par défaut : 1.0) |
| `set_cond_area` | STRING | Oui | "default"<br>"mask bounds" | Contrôle la manière dont la zone de conditionnement est appliquée |
| `masque` | MASK | Non | - | Masque optionnel pour contraindre la zone d'application du conditionnement |
| `crochets` | HOOKS | Non | - | Groupe de hooks optionnel pour un contrôle avancé |
| `pas de temps` | TIMESTEPS_RANGE | Non | - | Spécification optionnelle de la plage de pas de temps |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `negative` | CONDITIONING | La sortie de conditionnement positif combiné |
| `negative` | CONDITIONING | La sortie de conditionnement négatif combiné |