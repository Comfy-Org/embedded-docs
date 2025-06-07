
Le nœud SplitSigmas est conçu pour diviser une séquence de valeurs sigma en deux parties en fonction d'une étape spécifiée. Cette fonctionnalité est cruciale pour les opérations nécessitant un traitement ou une manipulation différente des parties initiale et subséquente de la séquence sigma, permettant une manipulation plus flexible et ciblée de ces valeurs.

## Entrées

| Paramètre | Type Comfy | Description |
|-----------|------------|-------------|
| `sigmas`  | `SIGMAS`   | Le paramètre 'sigmas' représente la séquence de valeurs sigma à diviser. Il est essentiel pour déterminer le point de division et les deux séquences de valeurs sigma résultantes, influençant l'exécution et les résultats du nœud. |
| `step`    | `INT`      | Le paramètre 'step' spécifie l'index auquel la séquence sigma doit être divisée. Il joue un rôle crucial dans la définition de la limite entre les deux séquences sigma résultantes, influençant la fonctionnalité du nœud et les caractéristiques de la sortie. |

## Sorties

| Paramètre | Type Comfy | Description |
|-----------|------------|-------------|
| `sigmas`  | `SIGMAS`   | Le nœud produit deux séquences de valeurs sigma, chacune représentant une partie de la séquence originale divisée à l'étape spécifiée. Ces sorties sont cruciales pour les opérations ultérieures nécessitant un traitement différencié des valeurs sigma. |
