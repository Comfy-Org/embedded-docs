# Cond Pair Set Props Combine

Voici la traduction en français de la documentation du nœud ComfyUI `PairConditioningSetPropertiesAndCombine` :

Le nœud `PairConditioningSetPropertiesAndCombine` modifie et combine des paires de conditionnement en appliquant de nouvelles données de conditionnement aux entrées de conditionnement positif et négatif existantes. Il permet d'ajuster la force du conditionnement appliqué et de contrôler la définition de la zone de conditionnement. Ce nœud est particulièrement utile pour les workflows avancés de manipulation du conditionnement où vous devez fusionner plusieurs sources de conditionnement.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | L'entrée de conditionnement positif d'origine | CONDITIONING | Oui | - |
| `negative` | L'entrée de conditionnement négatif d'origine | CONDITIONING | Oui | - |
| `positive_NEW` | Le nouveau conditionnement positif à appliquer | CONDITIONING | Oui | - |
| `negative_NEW` | Le nouveau conditionnement négatif à appliquer | CONDITIONING | Oui | - |
| `force` | Le facteur de force pour l'application du nouveau conditionnement (par défaut : 1.0) | FLOAT | Oui | 0.0 à 10.0 |
| `set_cond_area` | Contrôle la manière dont la zone de conditionnement est appliquée (par défaut : "default") | STRING | Oui | "default"<br>"mask bounds" |
| `masque` | Masque optionnel pour contraindre la zone d'application du conditionnement | MASK | Non | - |
| `crochets` | Groupe de hooks optionnel pour un contrôle avancé | HOOKS | Non | - |
| `pas de temps` | Spécification optionnelle de la plage de pas de temps | TIMESTEPS_RANGE | Non | - |


| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | La sortie de conditionnement positif combinée | CONDITIONING |
| `negative` | La sortie de conditionnement négatif combinée | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetPropertiesAndCombine/fr.md)

---
**Source fingerprint (SHA-256):** `d434fdc1ccbe3ddee6293a6300cc55d30cb5bf357025b26777791746f51e755e`
