> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetSelfAttentionMultiply/fr.md)

Le nœud UNetSelfAttentionMultiply applique des facteurs de multiplication aux composantes requête, clé, valeur et sortie du mécanisme d'auto-attention dans un modèle UNet. Il vous permet de mettre à l'échelle différentes parties du calcul d'attention pour expérimenter comment les pondérations d'affectation influencent le comportement du modèle.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle UNet à modifier avec les facteurs de mise à l'échelle de l'attention |
| `q` | FLOAT | Non | 0.0 - 10.0 | Facteur de multiplication pour la composante requête (par défaut : 1.0) |
| `k` | FLOAT | Non | 0.0 - 10.0 | Facteur de multiplication pour la composante clé (par défaut : 1.0) |
| `v` | FLOAT | Non | 0.0 - 10.0 | Facteur de multiplication pour la composante valeur (par défaut : 1.0) |
| `out` | FLOAT | Non | 0.0 - 10.0 | Facteur de multiplication pour la composante sortie (par défaut : 1.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `MODEL` | MODEL | Le modèle UNet modifié avec les composantes d'attention mises à l'échelle |