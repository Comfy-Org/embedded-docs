> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentConcat/fr.md)

Le nœud LatentConcat combine deux échantillons latents le long d'une dimension spécifiée. Il prend deux entrées latentes et les concatène ensemble le long de l'axe choisi (dimension x, y ou t). Le nœud ajuste automatiquement la taille du lot de la deuxième entrée pour correspondre à la première entrée avant d'effectuer l'opération de concaténation.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `samples1` | LATENT | Oui | - | Le premier échantillon latent à concaténer |
| `samples2` | LATENT | Oui | - | Le deuxième échantillon latent à concaténer |
| `dim` | COMBO | Oui | `"x"`<br>`"-x"`<br>`"y"`<br>`"-y"`<br>`"t"`<br>`"-t"` | La dimension le long de laquelle concaténer les échantillons latents. Les valeurs positives concatènent samples1 avant samples2, les valeurs négatives concatènent samples2 avant samples1 |

**Note :** Le deuxième échantillon latent (`samples2`) est automatiquement ajusté pour correspondre à la taille du lot du premier échantillon latent (`samples1`) avant la concaténation.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | LATENT | Les échantillons latents concaténés résultant de la combinaison des deux échantillons d'entrée le long de la dimension spécifiée |