# Cond Définir Propriétés Combinaison

Le nœud `ConditioningSetPropertiesAndCombine` modifie les données de conditionnement en appliquant les propriétés d'une nouvelle entrée de conditionnement à une entrée de conditionnement existante. Il combine les deux ensembles de conditionnement tout en contrôlant la force du nouveau conditionnement et en spécifiant comment la zone de conditionnement doit être appliquée.

## Entrées

| Paramètre | Description | Type de données | Type d'entrée | Défaut | Plage |
| --- | --- | --- | --- | --- | --- |
| `cond` | Les données de conditionnement d'origine à modifier | CONDITIONING | Requis | - | - |
| `cond_NOUVEAU` | Les nouvelles données de conditionnement fournissant les propriétés à appliquer | CONDITIONING | Requis | - | - |
| `force` | Contrôle l'intensité des nouvelles propriétés de conditionnement | FLOAT | Requis | 1.0 | 0.0 - 10.0 |
| `définir_zone_cond` | Détermine comment la zone de conditionnement est appliquée | STRING | Requis | default | ["default", "mask bounds"] |
| `masque` | Masque optionnel pour définir des zones spécifiques pour le conditionnement | MASK | Optionnel | - | - |
| `hooks` | Fonctions hook optionnelles pour un traitement personnalisé | HOOKS | Optionnel | - | - |
| `pas_de_temps` | Plage de pas de temps optionnelle pour contrôler le moment d'application du conditionnement | TIMESTEPS_RANGE | Optionnel | - | - |

**Remarque :** Lorsque `mask` est fourni, le paramètre `set_cond_area` peut utiliser "mask bounds" pour limiter l'application du conditionnement aux zones masquées.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | Les données de conditionnement combinées avec les propriétés modifiées | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetPropertiesAndCombine/fr.md)

---
**Source fingerprint (SHA-256):** `da57eeae428a103cbad77af063419ed0e85aeaa0b8805c8c197df27613477fa8`
