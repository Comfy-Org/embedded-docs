> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBatch/fr.md)

Le nœud LatentBatch est conçu pour fusionner deux ensembles d'échantillons latents en un seul lot, avec un redimensionnement potentiel d'un ensemble pour correspondre aux dimensions de l'autre avant la concaténation. Cette opération facilite la combinaison de différentes représentations latentes pour des tâches de traitement ou de génération ultérieures.

## Entrées

| Paramètre   | Type de données | Description |
|-------------|-----------------|-------------|
| `échantillons1`  | `LATENT`        | Le premier ensemble d'échantillons latents à fusionner. Il joue un rôle crucial dans la détermination de la forme finale du lot fusionné. |
| `échantillons2`  | `LATENT`        | Le second ensemble d'échantillons latents à fusionner. Si ses dimensions diffèrent du premier ensemble, il est redimensionné pour garantir la compatibilité avant la fusion. |

## Sorties

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `latent`  | `LATENT`        | L'ensemble fusionné d'échantillons latents, désormais combiné en un seul lot pour un traitement ultérieur. |