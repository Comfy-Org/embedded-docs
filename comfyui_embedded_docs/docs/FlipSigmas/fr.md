Le nœud `FlipSigmas` est conçu pour manipuler la séquence des valeurs sigma utilisées dans les modèles de diffusion en inversant leur ordre et en s'assurant que la première valeur n'est pas nulle si elle l'était initialement. Cette opération est cruciale pour adapter les niveaux de bruit dans l'ordre inverse, facilitant le processus de génération dans les modèles qui fonctionnent en réduisant progressivement le bruit des données.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `sigmas`  | `SIGMAS`    | Le paramètre 'sigmas' représente la séquence des valeurs sigma à inverser. Cette séquence est cruciale pour contrôler les niveaux de bruit appliqués pendant le processus de diffusion, et son inversion est essentielle pour le processus de génération inverse. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `sigmas`  | `SIGMAS`    | La sortie est la séquence modifiée des valeurs sigma, inversée et ajustée pour s'assurer que la première valeur n'est pas nulle si elle l'était initialement, prête à être utilisée dans les opérations ultérieures des modèles de diffusion. |
