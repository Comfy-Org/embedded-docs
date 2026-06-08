Le nœud **PairConditioningSetDefaultAndCombine** définit des valeurs de conditionnement par défaut et les combine avec les données de conditionnement d'entrée. Il prend des entrées de conditionnement positif et négatif ainsi que leurs homologues par défaut, puis les traite via le système de hooks de ComfyUI pour produire des sorties de conditionnement finales intégrant les valeurs par défaut.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | L'entrée de conditionnement positif principale à traiter | CONDITIONING | Oui | - |
| `negative` | L'entrée de conditionnement négatif principale à traiter | CONDITIONING | Oui | - |
| `positive_DEFAULT` | Les valeurs de conditionnement positif par défaut à utiliser comme solution de repli | CONDITIONING | Oui | - |
| `negative_DEFAULT` | Les valeurs de conditionnement négatif par défaut à utiliser comme solution de repli | CONDITIONING | Oui | - |
| `hooks` | Groupe de hooks optionnel pour une logique de traitement personnalisée | HOOKS | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Le conditionnement positif traité avec les valeurs par défaut intégrées | CONDITIONING |
| `negative` | Le conditionnement négatif traité avec les valeurs par défaut intégrées | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetDefaultAndCombine/fr.md)

---
**Source fingerprint (SHA-256):** `dfa47d0fe02e81db8b68d20ae9b765c2518773f4f7fc8caf774cb870267dbb21`
