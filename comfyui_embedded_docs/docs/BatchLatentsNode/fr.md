> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchLatentsNode/fr.md)

## Présentation

Le nœud Batch Latents combine plusieurs entrées latentes en un seul lot. Il prend un nombre variable d'échantillons latents et les fusionne le long de la dimension du lot, permettant ainsi leur traitement conjoint dans les nœuds suivants. Cela est utile pour générer ou traiter plusieurs images en une seule opération.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `latents` | LATENT | Oui | N/A | Le premier échantillon latent à inclure dans le lot. |
| `latent_2` à `latent_50` | LATENT | Non | N/A | Échantillons latents supplémentaires à inclure dans le lot. Vous pouvez ajouter entre 2 et 50 entrées latentes au total. |

**Note :** Vous devez fournir au moins deux entrées latentes pour que le nœud fonctionne. Le nœud créera automatiquement des emplacements d'entrée à mesure que vous connectez davantage de latents, jusqu'à un maximum de 50.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | LATENT | Une seule sortie latente contenant toutes les entrées latentes combinées en un seul lot. |
