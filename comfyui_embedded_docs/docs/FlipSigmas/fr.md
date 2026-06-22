# InverserSigmas

Le nœud `FlipSigmas` est conçu pour manipuler la séquence des valeurs sigma utilisées dans les modèles de diffusion en inversant leur ordre et en garantissant que la première valeur soit non nulle si elle l'était initialement. Cette opération est cruciale pour adapter les niveaux de bruit dans l'ordre inverse, facilitant ainsi le processus de génération dans les modèles qui fonctionnent en réduisant progressivement le bruit à partir des données.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `sigmas` | Le paramètre 'sigmas' représente la séquence des valeurs sigma à inverser. Cette séquence est cruciale pour contrôler les niveaux de bruit appliqués pendant le processus de diffusion, et son inversion est essentielle pour le processus de génération inverse. | `SIGMAS` |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `sigmas` | La sortie est la séquence modifiée des valeurs sigma, inversée et ajustée pour garantir que la première valeur soit non nulle si elle l'était initialement, prête à être utilisée dans les opérations ultérieures du modèle de diffusion. | `SIGMAS` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FlipSigmas/fr.md)
