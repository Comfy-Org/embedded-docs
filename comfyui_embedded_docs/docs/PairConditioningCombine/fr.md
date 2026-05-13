> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningCombine/fr.md)

Le nœud **PairConditioningCombine** fusionne deux paires de conditionnement distinctes (chacune composée d'un conditionnement positif et négatif) en une seule paire combinée. Il prend le conditionnement positif et négatif de deux sources différentes et les combine à l'aide de la logique interne de ComfyUI, produisant un conditionnement positif final et un conditionnement négatif final. Ce nœud est expérimental et conçu pour des workflows avancés de manipulation de conditionnement.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `positive_A` | CONDITIONING | Oui | - | Première entrée de conditionnement positif |
| `negative_A` | CONDITIONING | Oui | - | Première entrée de conditionnement négatif |
| `positive_B` | CONDITIONING | Oui | - | Deuxième entrée de conditionnement positif |
| `negative_B` | CONDITIONING | Oui | - | Deuxième entrée de conditionnement négatif |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `negative` | CONDITIONING | Sortie de conditionnement positif combiné |
| `negative` | CONDITIONING | Sortie de conditionnement négatif combiné |

---
**Source fingerprint (SHA-256):** `34c14207930ba31fea054b2e641e9666e738ed786aa117449c4a27667bde41b1`
