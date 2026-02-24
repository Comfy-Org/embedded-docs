> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCutToBatch/fr.md)

Le nœud LatentCutToBatch prend une représentation latente et la découpe selon une dimension spécifiée en plusieurs tranches. Ces tranches sont ensuite empilées dans une nouvelle dimension de lot, convertissant ainsi un échantillon latent unique en un lot de plus petits échantillons latents. Cela est utile pour traiter différentes parties d'un espace latent de manière indépendante.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `samples` | LATENT | Oui | - | La représentation latente à découper et à regrouper en lot. |
| `dim` | COMBO | Oui | `"t"`<br>`"x"`<br>`"y"` | La dimension le long de laquelle découper les échantillons latents. `"t"` fait référence à la dimension temporelle, `"x"` à la largeur, et `"y"` à la hauteur. |
| `slice_size` | INT | Oui | 1 à 16384 | La taille de chaque tranche à découper dans la dimension spécifiée. Si la taille de la dimension n'est pas parfaitement divisible par cette valeur, le reste est ignoré. (par défaut : 1) |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `samples` | LATENT | Le lot latent résultant, contenant les échantillons découpés et empilés. |
