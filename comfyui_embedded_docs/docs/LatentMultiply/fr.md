Le nœud LatentMultiply est conçu pour mettre à l'échelle la représentation latente d'échantillons à l'aide d'un multiplicateur spécifié. Cette opération permet d'ajuster l'intensité ou l'amplitude des caractéristiques dans l'espace latent, facilitant le réglage fin du contenu généré ou l'exploration de variations dans une direction latente donnée.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `échantillons` | Le paramètre `échantillons` représente les représentations latentes à mettre à l'échelle. Il est essentiel pour définir les données d'entrée sur lesquelles l'opération de multiplication sera effectuée. | `LATENT` |
| `multiplicateur` | Le paramètre `multiplicateur` spécifie le facteur d'échelle à appliquer aux échantillons latents. Il joue un rôle clé dans l'ajustement de l'amplitude des caractéristiques latentes, permettant un contrôle nuancé de la sortie générée. | `FLOAT` |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `latent` | La sortie est une version modifiée des échantillons latents d'entrée, mise à l'échelle par le multiplicateur spécifié. Cela permet d'explorer des variations dans l'espace latent en ajustant l'intensité de ses caractéristiques. | `LATENT` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentMultiply/fr.md)
