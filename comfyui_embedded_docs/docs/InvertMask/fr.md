
Le nœud InvertMask est conçu pour inverser les valeurs d'un masque donné, inversant ainsi les zones masquées et non masquées. Cette opération est fondamentale dans les tâches de traitement d'image où l'intérêt doit être déplacé entre le premier plan et l'arrière-plan.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|--------------|-------------|
| `mask`    | MASK         | Le paramètre 'mask' représente le masque d'entrée à inverser. Il est crucial pour déterminer les zones à inverser dans le processus d'inversion. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|--------------|-------------|
| `mask`    | MASK         | La sortie est une version inversée du masque d'entrée, avec les zones précédemment masquées devenant non masquées et vice versa. |
