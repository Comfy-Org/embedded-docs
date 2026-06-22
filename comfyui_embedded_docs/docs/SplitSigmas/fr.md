# SplitSigmas

Le nœud SplitSigmas est conçu pour diviser une séquence de valeurs sigma en deux parties en fonction d’un pas spécifié. Cette fonctionnalité est essentielle pour les opérations nécessitant un traitement différencié des parties initiale et suivante de la séquence sigma, permettant une manipulation plus flexible et ciblée de ces valeurs.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `sigmas` | Le paramètre `sigmas` représente la séquence de valeurs sigma à diviser. Il est essentiel pour déterminer le point de division et les deux séquences de valeurs sigma résultantes, influençant l’exécution et les résultats du nœud. | `SIGMAS` |
| `étape` | Le paramètre `étape` spécifie l’index auquel la séquence sigma doit être divisée. Il joue un rôle critique dans la définition de la frontière entre les deux séquences sigma résultantes, influençant la fonctionnalité du nœud et les caractéristiques de la sortie. | `INT` |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `sigmas_bas` | Le nœud produit deux séquences de valeurs sigma, chacune représentant une partie de la séquence originale divisée au pas spécifié. Ces sorties sont cruciales pour les opérations ultérieures nécessitant un traitement différencié des valeurs sigma. | `SIGMAS` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmas/fr.md)
