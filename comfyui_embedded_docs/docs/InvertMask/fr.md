> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InvertMask/fr.md)

Le nœud InvertMask est conçu pour inverser les valeurs d’un masque donné, en échangeant les zones masquées et non masquées. Cette opération est fondamentale dans les tâches de traitement d’image où il est nécessaire de basculer l’intérêt entre le premier plan et l’arrière-plan.

## Entrées

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `mask`    | MASK            | Le paramètre `mask` représente le masque d’entrée à inverser. Il est essentiel pour déterminer les zones à permuter lors du processus d’inversion. |

## Sorties

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `mask`    | MASK            | La sortie est une version inversée du masque d’entrée, où les zones précédemment masquées deviennent non masquées et vice versa. |