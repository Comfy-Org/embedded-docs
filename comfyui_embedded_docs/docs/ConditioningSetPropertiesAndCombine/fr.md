> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetPropertiesAndCombine/fr.md)

Le nœud ConditioningSetPropertiesAndCombine modifie les données de conditionnement en appliquant les propriétés d'une nouvelle entrée de conditionnement à une entrée de conditionnement existante. Il combine les deux ensembles de conditionnement tout en contrôlant l'intensité du nouveau conditionnement et en spécifiant comment la zone de conditionnement doit être appliquée.

## Entrées

| Paramètre | Type de données | Type d'entrée | Défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `cond` | CONDITIONING | Requis | - | - | Les données de conditionnement originales à modifier |
| `cond_NOUVEAU` | CONDITIONING | Requis | - | - | Les nouvelles données de conditionnement fournissant les propriétés à appliquer |
| `force` | FLOAT | Requis | 1.0 | 0.0 - 10.0 | Contrôle l'intensité des nouvelles propriétés de conditionnement |
| `définir_zone_cond` | STRING | Requis | default | ["default", "mask bounds"] | Détermine comment la zone de conditionnement est appliquée |
| `masque` | MASK | Optionnel | - | - | Masque optionnel pour définir des zones spécifiques pour le conditionnement |
| `hooks` | HOOKS | Optionnel | - | - | Fonctions de hook optionnelles pour un traitement personnalisé |
| `pas_de_temps` | TIMESTEPS_RANGE | Optionnel | - | - | Plage de pas de temps optionnelle pour contrôler quand le conditionnement est appliqué |

**Note :** Lorsqu'un `mask` est fourni, le paramètre `set_cond_area` peut utiliser "mask bounds" pour limiter l'application du conditionnement aux régions masquées.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Les données de conditionnement combinées avec les propriétés modifiées |
