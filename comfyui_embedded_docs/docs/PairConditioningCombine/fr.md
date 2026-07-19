# Cond Pair Combiner

Le nœud **PairConditioningCombine** fusionne deux paires de conditionnement distinctes (chacune composée d'un conditionnement positif et négatif) en une seule paire combinée. Il prend le conditionnement positif et négatif de deux sources différentes et les combine à l'aide de la logique interne de ComfyUI, produisant un conditionnement positif final et un conditionnement négatif final. Ce nœud est expérimental et conçu pour des workflows avancés de manipulation de conditionnement.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive_A` | Première entrée de conditionnement positif | CONDITIONING | Oui | - |
| `negative_A` | Première entrée de conditionnement négatif | CONDITIONING | Oui | - |
| `positive_B` | Deuxième entrée de conditionnement positif | CONDITIONING | Oui | - |
| `negative_B` | Deuxième entrée de conditionnement négatif | CONDITIONING | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Sortie de conditionnement positif combiné | CONDITIONING |
| `negative` | Sortie de conditionnement négatif combiné | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningCombine/fr.md)

---
**Source fingerprint (SHA-256):** `34c14207930ba31fea054b2e641e9666e738ed786aa117449c4a27667bde41b1`
