
Le nœud LatentBatch est conçu pour fusionner deux ensembles d'échantillons latents en un seul lot, en redimensionnant potentiellement un ensemble pour correspondre aux dimensions de l'autre avant la concaténation. Cette opération facilite la combinaison de différentes représentations latentes pour des tâches de traitement ou de génération ultérieures.

## Entrées

| Paramètre    | Data Type | Description |
|--------------|-------------|-------------|
| `samples1`   | `LATENT`    | Le premier ensemble d'échantillons latents à fusionner. Il joue un rôle crucial dans la détermination de la forme finale du lot fusionné. |
| `samples2`   | `LATENT`    | Le second ensemble d'échantillons latents à fusionner. Si ses dimensions diffèrent du premier ensemble, il est redimensionné pour assurer la compatibilité avant la fusion. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | L'ensemble fusionné d'échantillons latents, maintenant combiné en un seul lot pour un traitement ultérieur. |
