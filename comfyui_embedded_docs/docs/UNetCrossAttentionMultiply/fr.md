> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetCrossAttentionMultiply/fr.md)

Le nœud UNetCrossAttentionMultiply applique des facteurs de multiplication au mécanisme d'attention croisée dans un modèle UNet. Il vous permet de mettre à l'échelle les composantes de requête, clé, valeur et de sortie des couches d'attention croisée pour expérimenter avec différents comportements et effets d'attention.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `modèle` | MODEL | Oui | - | Le modèle UNet à modifier avec les facteurs d'échelle d'attention |
| `q` | FLOAT | Non | 0.0 - 10.0 | Facteur d'échelle pour les composantes de requête dans l'attention croisée (par défaut : 1.0) |
| `k` | FLOAT | Non | 0.0 - 10.0 | Facteur d'échelle pour les composantes de clé dans l'attention croisée (par défaut : 1.0) |
| `v` | FLOAT | Non | 0.0 - 10.0 | Facteur d'échelle pour les composantes de valeur dans l'attention croisée (par défaut : 1.0) |
| `sortie` | FLOAT | Non | 0.0 - 10.0 | Facteur d'échelle pour les composantes de sortie dans l'attention croisée (par défaut : 1.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `modèle` | MODEL | Le modèle UNet modifié avec les composantes d'attention croisée mises à l'échelle |