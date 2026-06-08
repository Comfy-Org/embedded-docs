Ce nœud est conçu pour extraire un sous-ensemble spécifique d'échantillons latents d'un lot donné, en fonction de l'index et de la longueur du lot spécifiés. Il permet un traitement sélectif des échantillons latents, facilitant les opérations sur des segments plus petits du lot pour plus d'efficacité ou une manipulation ciblée.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `échantillons` | La collection d'échantillons latents à partir de laquelle un sous-ensemble sera extrait. Ce paramètre est essentiel pour déterminer le lot source d'échantillons à traiter. | `LATENT` |
| `index_de_batch` | Spécifie l'index de départ dans le lot à partir duquel le sous-ensemble d'échantillons commencera. Ce paramètre permet l'extraction ciblée d'échantillons à des positions spécifiques dans le lot. | `INT` |
| `longueur` | Définit le nombre d'échantillons à extraire à partir de l'index de départ spécifié. Ce paramètre contrôle la taille du sous-ensemble à traiter, permettant une manipulation flexible des segments du lot. | `INT` |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `latent` | Le sous-ensemble extrait d'échantillons latents, désormais disponible pour un traitement ou une analyse ultérieure. | `LATENT` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentFromBatch/fr.md)
