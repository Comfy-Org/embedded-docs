Le nœud LatentFlip est conçu pour manipuler les représentations latentes en les retournant verticalement ou horizontalement. Cette opération permet de transformer l'espace latent, offrant potentiellement de nouvelles variations ou perspectives au sein des données.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `échantillons` | Le paramètre `échantillons` représente les représentations latentes à retourner. L'opération de retournement modifie ces représentations, soit verticalement, soit horizontalement, selon le paramètre `méthode_de_retournement`, transformant ainsi les données dans l'espace latent. | `LATENT` |
| `méthode_de_retournement` | Le paramètre `méthode_de_retournement` spécifie l'axe selon lequel les échantillons latents seront retournés. Il peut être défini sur 'x-axis: vertically' (axe x : verticalement) ou 'y-axis: horizontally' (axe y : horizontalement), déterminant la direction du retournement et donc la nature de la transformation appliquée aux représentations latentes. | COMBO[STRING] |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `latent` | La sortie est une version modifiée des représentations latentes d'entrée, ayant été retournées selon la méthode spécifiée. Cette transformation peut introduire de nouvelles variations au sein de l'espace latent. | `LATENT` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentFlip/fr.md)
