> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionBucket/fr.md)

Ce nœud organise une liste d'images latentes et leurs données de conditionnement correspondantes par leur résolution. Il regroupe les éléments qui partagent la même hauteur et largeur, créant des lots distincts pour chaque résolution unique. Ce processus est utile pour préparer des données pour un entraînement efficace, car il permet aux modèles de traiter plusieurs éléments de même taille ensemble.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `latents` | LATENT | Oui | N/A | Liste de dictionnaires latents à regrouper par résolution. |
| `conditioning` | CONDITIONING | Oui | N/A | Liste de listes de conditionnement (doit correspondre à la longueur de `latents`). |

**Note :** Le nombre d'éléments dans la liste `latents` doit correspondre exactement au nombre d'éléments dans la liste `conditioning`. Chaque dictionnaire latent peut contenir un lot d'échantillons, et la liste de conditionnement correspondante doit contenir un nombre correspondant d'éléments de conditionnement pour ce lot.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `latents` | LATENT | Liste de dictionnaires latents groupés en lots, un par groupe de résolution. |
| `conditioning` | CONDITIONING | Liste de listes de conditionnement, une par groupe de résolution. |
