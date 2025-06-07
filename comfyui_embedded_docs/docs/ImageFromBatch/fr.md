Le nœud `ImageFromBatch` est conçu pour extraire un segment spécifique d'images d'un lot en fonction de l'index et de la longueur fournis. Il permet un contrôle plus précis sur les images en lot, permettant des opérations sur des images individuelles ou des sous-ensembles d'images au sein d'un lot plus large.

## Entrées

| Champ          | Data Type | Description                                                                           |
|----------------|-------------|---------------------------------------------------------------------------------------|
| `image`        | `IMAGE`     | Le lot d'images à partir duquel un segment sera extrait. Ce paramètre est crucial pour spécifier le lot source. |
| `batch_index`  | `INT`       | L'index de départ dans le lot à partir duquel l'extraction commence. Il détermine la position initiale du segment à extraire du lot. |
| `length`       | `INT`       | Le nombre d'images à extraire du lot à partir du batch_index. Ce paramètre définit la taille du segment à extraire. |

## Sorties

| Champ | Data Type | Description                                                                                   |
|-------|-------------|-----------------------------------------------------------------------------------------------|
| `image` | `IMAGE`    | Le segment extrait d'images du lot spécifié. Cette sortie représente un sous-ensemble du lot original, déterminé par les paramètres batch_index et length. |
