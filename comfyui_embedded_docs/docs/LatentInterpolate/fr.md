> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentInterpolate/fr.md)

Voici la traduction en français de la documentation du nœud LatentInterpolate :

Le nœud LatentInterpolate est conçu pour effectuer une interpolation entre deux ensembles d'échantillons latents selon un rapport spécifié, en mélangeant les caractéristiques des deux ensembles pour produire un nouvel ensemble intermédiaire d'échantillons latents.

## Entrées

| Paramètre    | Type de données | Description |
|--------------|-----------------|-------------|
| `samples1`   | `LATENT`        | Le premier ensemble d'échantillons latents à interpoler. Il sert de point de départ pour le processus d'interpolation. |
| `samples2`   | `LATENT`        | Le second ensemble d'échantillons latents à interpoler. Il sert de point d'arrivée pour le processus d'interpolation. |
| `ratio`      | `FLOAT`         | Une valeur à virgule flottante qui détermine le poids de chaque ensemble d'échantillons dans la sortie interpolée. Un rapport de 0 produit une copie du premier ensemble, tandis qu'un rapport de 1 produit une copie du second ensemble. |

## Sorties

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `latent`  | `LATENT`        | La sortie est un nouvel ensemble d'échantillons latents représentant un état interpolé entre les deux ensembles d'entrée, basé sur le rapport spécifié. |