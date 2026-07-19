# ImageDeBatch

Le nœud `ImageFromBatch` est conçu pour extraire un segment spécifique d'images d'un lot en fonction de l'index et de la longueur fournis. Il permet un contrôle plus granulaire des images par lots, en autorisant des opérations sur des images individuelles ou des sous-ensembles au sein d'un lot plus large.

## Entrées

| Champ | Description | Type de données |
| --- | --- | --- |
| `image` | Le lot d'images à partir duquel un segment sera extrait. Ce paramètre est essentiel pour spécifier le lot source. | `IMAGE` |
| `index_de_lot` | L'index de départ dans le lot à partir duquel l'extraction commence. Il détermine la position initiale du segment à extraire du lot. | `INT` |
| `longueur` | Le nombre d'images à extraire du lot à partir de l'`index_de_lot`. Ce paramètre définit la taille du segment à extraire. | `INT` |

## Sorties

| Champ | Description | Type de données |
| --- | --- | --- |
| `image` | Le segment extrait d'images du lot spécifié. Cette sortie représente un sous-ensemble du lot d'origine, déterminé par les paramètres `index_de_lot` et `longueur`. | `IMAGE` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageFromBatch/fr.md)
