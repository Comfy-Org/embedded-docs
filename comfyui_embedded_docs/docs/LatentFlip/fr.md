
Le nœud LatentFlip est conçu pour manipuler les représentations latentes en les inversant soit verticalement, soit horizontalement. Cette opération permet de transformer l'espace latent, potentiellement en révélant de nouvelles variations ou perspectives au sein des données.

## Entrées

| Paramètre     | Type de Donnée | Description |
|---------------|--------------|-------------|
| `samples`     | `LATENT`     | Le paramètre 'samples' représente les représentations latentes à inverser. L'opération d'inversion modifie ces représentations, soit verticalement, soit horizontalement, en fonction du paramètre 'flip_method', transformant ainsi les données dans l'espace latent. |
| `flip_method` | COMBO[STRING] | Le paramètre 'flip_method' spécifie l'axe le long duquel les échantillons latents seront inversés. Il peut être soit 'x-axis: verticalement' soit 'y-axis: horizontalement', déterminant la direction de l'inversion et donc la nature de la transformation appliquée aux représentations latentes. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La sortie est une version modifiée des représentations latentes d'entrée, ayant été inversée selon la méthode spécifiée. Cette transformation peut introduire de nouvelles variations au sein de l'espace latent. |
