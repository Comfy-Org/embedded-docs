# ConditioningZeroOut

Ce nœud met à zéro des éléments spécifiques au sein de la structure de données de conditionnement, neutralisant ainsi leur influence dans les étapes de traitement ultérieures. Il est conçu pour des opérations de conditionnement avancées nécessitant une manipulation directe de la représentation interne du conditionnement.

## Entrées

| Paramètre | Description | Type Comfy |
| --- | --- | --- |
| `CONDITIONING` | La structure de données de conditionnement à modifier. Ce nœud met à zéro les éléments 'pooled_output' dans chaque entrée de conditionnement, le cas échéant. | CONDITIONING |

## Sorties

| Paramètre | Description | Type Comfy |
| --- | --- | --- |
| `CONDITIONING` | La structure de données de conditionnement modifiée, avec les éléments 'pooled_output' mis à zéro lorsque applicable. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningZeroOut/fr.md)
