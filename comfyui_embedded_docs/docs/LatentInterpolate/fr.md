
Le nœud LatentInterpolate est conçu pour effectuer une interpolation entre deux ensembles d'échantillons latents en fonction d'un ratio spécifié, mélangeant les caractéristiques des deux ensembles pour produire un nouvel ensemble intermédiaire d'échantillons latents.

## Entrées

| Paramètre    | Data Type | Description |
|--------------|-------------|-------------|
| `samples1`   | `LATENT`    | Le premier ensemble d'échantillons latents à interpoler. Il sert de point de départ pour le processus d'interpolation. |
| `samples2`   | `LATENT`    | Le second ensemble d'échantillons latents à interpoler. Il sert de point d'arrivée pour le processus d'interpolation. |
| `ratio`      | `FLOAT`     | Une valeur flottante qui détermine le poids de chaque ensemble d'échantillons dans le résultat interpolé. Un ratio de 0 produit une copie du premier ensemble, tandis qu'un ratio de 1 produit une copie du second ensemble. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La sortie est un nouvel ensemble d'échantillons latents qui représente un état interpolé entre les deux ensembles d'entrée, basé sur le ratio spécifié. |
