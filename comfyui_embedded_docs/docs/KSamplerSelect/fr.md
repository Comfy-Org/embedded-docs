# KSamplerSelect

Le nœud KSamplerSelect est conçu pour sélectionner un échantillonneur spécifique en fonction du nom d'échantillonneur fourni. Il abstrait la complexité de la sélection d'échantillonneur, permettant aux utilisateurs de basculer facilement entre différentes stratégies d'échantillonnage pour leurs tâches.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `sampler_name` | Spécifie le nom de l'échantillonneur à sélectionner. Ce paramètre détermine la stratégie d'échantillonnage utilisée, ce qui influence le comportement global d'échantillonnage et les résultats. | COMBO[STRING] |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `sampler` | Renvoie l'objet échantillonneur sélectionné, prêt à être utilisé pour les tâches d'échantillonnage. | `SAMPLER` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSamplerSelect/fr.md)
