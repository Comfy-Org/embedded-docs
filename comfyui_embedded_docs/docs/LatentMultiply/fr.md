
Le nœud LatentMultiply est conçu pour mettre à l'échelle la représentation latente des échantillons par un multiplicateur spécifié. Cette opération permet d'ajuster l'intensité ou l'ampleur des caractéristiques au sein de l'espace latent, facilitant ainsi le réglage fin du contenu généré ou l'exploration de variations dans une direction latente donnée.

## Entrées

| Paramètre    | Data Type | Description |
|--------------|-------------|-------------|
| `samples`    | `LATENT`    | Le paramètre 'samples' représente les représentations latentes à mettre à l'échelle. Il est crucial pour définir les données d'entrée sur lesquelles l'opération de multiplication sera effectuée. |
| `multiplier` | `FLOAT`     | Le paramètre 'multiplier' spécifie le facteur d'échelle à appliquer aux échantillons latents. Il joue un rôle clé dans l'ajustement de l'ampleur des caractéristiques latentes, permettant un contrôle nuancé sur le résultat généré. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La sortie est une version modifiée des échantillons latents d'entrée, mise à l'échelle par le multiplicateur spécifié. Cela permet l'exploration de variations au sein de l'espace latent en ajustant l'intensité de ses caractéristiques. |
