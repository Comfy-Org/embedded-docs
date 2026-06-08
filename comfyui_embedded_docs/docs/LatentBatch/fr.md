Le nœud LatentBatch est conçu pour fusionner deux ensembles d'échantillons latents en un seul lot, avec un redimensionnement potentiel d'un ensemble pour correspondre aux dimensions de l'autre avant la concaténation. Cette opération facilite la combinaison de différentes représentations latentes pour des tâches de traitement ou de génération ultérieures.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `échantillons1` | Le premier ensemble d'échantillons latents à fusionner. Il joue un rôle crucial dans la détermination de la forme finale du lot fusionné. | `LATENT` |
| `échantillons2` | Le second ensemble d'échantillons latents à fusionner. Si ses dimensions diffèrent du premier ensemble, il est redimensionné pour garantir la compatibilité avant la fusion. | `LATENT` |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `latent` | L'ensemble fusionné d'échantillons latents, désormais combiné en un seul lot pour un traitement ultérieur. | `LATENT` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBatch/fr.md)
