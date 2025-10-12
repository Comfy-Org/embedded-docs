> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetProperties/fr.md)

Le nœud PairConditioningSetProperties permet de modifier simultanément les propriétés des paires de conditionnement positif et négatif. Il applique des ajustements de force, des paramètres de zone de conditionnement, et des contrôles optionnels de masquage ou de timing aux deux entrées de conditionnement, renvoyant les données de conditionnement positif et négatif modifiées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `positive_NEW` | CONDITIONING | Oui | - | L'entrée de conditionnement positif à modifier |
| `negative_NEW` | CONDITIONING | Oui | - | L'entrée de conditionnement négatif à modifier |
| `strength` | FLOAT | Oui | 0.0 à 10.0 | Le multiplicateur de force appliqué au conditionnement (par défaut : 1.0) |
| `set_cond_area` | STRING | Oui | "default"<br>"mask bounds" | Détermine comment la zone de conditionnement est calculée |
| `mask` | MASK | Non | - | Masque optionnel pour contraindre la zone de conditionnement |
| `hooks` | HOOKS | Non | - | Groupe de hooks optionnel pour des modifications avancées du conditionnement |
| `timesteps` | TIMESTEPS_RANGE | Non | - | Plage de pas de temps optionnelle pour limiter quand le conditionnement est appliqué |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Le conditionnement positif modifié avec les propriétés appliquées |
| `negative` | CONDITIONING | Le conditionnement négatif modifié avec les propriétés appliquées |