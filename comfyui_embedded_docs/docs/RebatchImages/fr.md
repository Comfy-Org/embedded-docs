
Le nœud RebatchImages est conçu pour réorganiser un lot d'images en une nouvelle configuration de lot, en ajustant la taille du lot comme spécifié. Ce processus est essentiel pour gérer et optimiser le traitement des données d'image dans les opérations par lot, en veillant à ce que les images soient regroupées selon la taille de lot souhaitée pour une gestion efficace.

## Entrées

| Champ        | Data Type | Description                                                                         |
|--------------|-------------|-------------------------------------------------------------------------------------|
| `images`     | `IMAGE`     | Une liste d'images à réorganiser. Ce paramètre est crucial pour déterminer les données d'entrée qui subiront le processus de réorganisation. |
| `batch_size` | `INT`       | Spécifie la taille souhaitée des lots de sortie. Ce paramètre influence directement la manière dont les images d'entrée sont regroupées et traitées, impactant la structure de la sortie. |

## Sorties

| Champ  | Data Type | Description                                                                   |
|--------|-------------|-------------------------------------------------------------------------------|
| `image`| `IMAGE`     | La sortie consiste en une liste de lots d'images, réorganisés selon la taille de lot spécifiée. Cela permet un traitement flexible et efficace des données d'image dans les opérations par lot. |
