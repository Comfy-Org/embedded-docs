> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetCrossAttentionMultiply/fr.md)

Le nœud UNetCrossAttentionMultiply applique des facteurs de multiplication au mécanisme d'attention croisée dans un modèle UNet. Il permet de mettre à l'échelle les composants de requête, clé, valeur et sortie des couches d'attention croisée afin d'expérimenter différents comportements et effets d'attention.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle UNet à modifier avec des facteurs d'échelle d'attention |
| `q` | FLOAT | Non | 0,0 - 10,0 | Facteur d'échelle pour les composants de requête dans l'attention croisée (par défaut : 1,0) |
| `k` | FLOAT | Non | 0,0 - 10,0 | Facteur d'échelle pour les composants de clé dans l'attention croisée (par défaut : 1,0) |
| `v` | FLOAT | Non | 0,0 - 10,0 | Facteur d'échelle pour les composants de valeur dans l'attention croisée (par défaut : 1,0) |
| `out` | FLOAT | Non | 0,0 - 10,0 | Facteur d'échelle pour les composants de sortie dans l'attention croisée (par défaut : 1,0) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `model` | MODEL | Le modèle UNet modifié avec des composants d'attention croisée mis à l'échelle |

---
**Source fingerprint (SHA-256):** `2623858c11e93ab5952194670c9e4ea74bba4e2ea32089540665eea361dc1491`
