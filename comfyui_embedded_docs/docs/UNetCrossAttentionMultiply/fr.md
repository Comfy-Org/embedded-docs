# UNetMultiplicationAttentionCroisée

Le nœud UNetCrossAttentionMultiply applique des facteurs de multiplication au mécanisme d'attention croisée dans un modèle UNet. Il permet de mettre à l'échelle les composants de requête, clé, valeur et sortie des couches d'attention croisée afin d'expérimenter différents comportements et effets d'attention.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle UNet à modifier avec des facteurs d'échelle d'attention | MODEL | Oui | - |
| `q` | Facteur d'échelle pour les composants de requête dans l'attention croisée (par défaut : 1,0) | FLOAT | Non | 0,0 - 10,0 |
| `k` | Facteur d'échelle pour les composants de clé dans l'attention croisée (par défaut : 1,0) | FLOAT | Non | 0,0 - 10,0 |
| `v` | Facteur d'échelle pour les composants de valeur dans l'attention croisée (par défaut : 1,0) | FLOAT | Non | 0,0 - 10,0 |
| `sortie` | Facteur d'échelle pour les composants de sortie dans l'attention croisée (par défaut : 1,0) | FLOAT | Non | 0,0 - 10,0 |


| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle UNet modifié avec des composants d'attention croisée mis à l'échelle | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetCrossAttentionMultiply/fr.md)

---
**Source fingerprint (SHA-256):** `2623858c11e93ab5952194670c9e4ea74bba4e2ea32089540665eea361dc1491`
