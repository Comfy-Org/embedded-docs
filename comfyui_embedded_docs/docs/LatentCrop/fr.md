
Le nœud LatentCrop est conçu pour effectuer des opérations de recadrage sur les représentations latentes des images. Il permet de spécifier les dimensions et la position du recadrage, permettant des modifications ciblées de l'espace latent.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `samples` | `LATENT`    | Le paramètre 'samples' représente les représentations latentes à recadrer. Il est crucial pour définir les données sur lesquelles l'opération de recadrage sera effectuée. |
| `width`   | `INT`       | Spécifie la largeur de la zone de recadrage. Elle influence directement les dimensions de la représentation latente de sortie. |
| `height`  | `INT`       | Spécifie la hauteur de la zone de recadrage, affectant la taille de la représentation latente recadrée résultante. |
| `x`       | `INT`       | Détermine la coordonnée x de départ de la zone de recadrage, influençant la position du recadrage au sein de la représentation latente originale. |
| `y`       | `INT`       | Détermine la coordonnée y de départ de la zone de recadrage, définissant la position du recadrage au sein de la représentation latente originale. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La sortie est une représentation latente modifiée avec le recadrage spécifié appliqué. |
