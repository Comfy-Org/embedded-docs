Ce nœud annule des éléments spécifiques au sein de la structure de données de conditionnement, neutralisant ainsi leur influence dans les étapes de traitement ultérieures. Il est conçu pour des opérations de conditionnement avancées où une manipulation directe de la représentation interne du conditionnement est requise.

## Entrées

| Paramètre | Comfy dtype                | Description |
|-----------|----------------------------|-------------|
| `CONDITIONING` | CONDITIONING | La structure de données de conditionnement à modifier. Ce nœud annule les éléments 'pooled_output' au sein de chaque entrée de conditionnement, si présents. |

## Sorties

| Paramètre | Comfy dtype                | Description |
|-----------|----------------------------|-------------|
| `CONDITIONING` | CONDITIONING | La structure de données de conditionnement modifiée, avec les éléments 'pooled_output' mis à zéro là où c'est applicable. |
