# ConditioningSetDefaultAndCombine

Ce nœud combine une entrée de conditionnement principale avec une entrée de conditionnement par défaut à l'aide d'un système basé sur des hooks. Il fusionne les deux sources de conditionnement en une seule sortie, permettant au conditionnement par défaut de servir de solution de repli ou de base lorsque le conditionnement principal est incomplet.

## Entrées

| Paramètre | Description | Type de données | Type d'entrée | Défaut | Plage |
| --- | --- | --- | --- | --- | --- |
| `cond` | L'entrée de conditionnement principale à traiter et à combiner | CONDITIONING | Requis | - | - |
| `cond_DEFAULT` | Les données de conditionnement par défaut à combiner avec le conditionnement principal | CONDITIONING | Requis | - | - |
| `hooks` | Configuration de hook optionnelle qui contrôle la manière dont les données de conditionnement sont traitées et combinées | HOOKS | Optionnel | - | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | Les données de conditionnement combinées résultant de la fusion des entrées de conditionnement principale et par défaut | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetDefaultAndCombine/fr.md)

---
**Source fingerprint (SHA-256):** `5e6c95f454c7e262878cc362c6b199e01abff10f803c81afe6e76a317c30d039`
