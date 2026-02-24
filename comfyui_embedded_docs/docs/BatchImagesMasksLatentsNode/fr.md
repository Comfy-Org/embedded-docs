> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchImagesMasksLatentsNode/fr.md)

Le nœud Batch Images/Masks/Latents combine plusieurs entrées du même type en un seul lot. Il détecte automatiquement si les entrées sont des images, des masques ou des représentations latentes et utilise la méthode de regroupement appropriée. Ceci est utile pour préparer plusieurs éléments à être traités par des nœuds qui acceptent des entrées groupées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `inputs` | IMAGE, MASK ou LATENT | Oui | 1 à 50 entrées | Une liste dynamique d'entrées à combiner en un lot. Vous pouvez ajouter entre 1 et 50 éléments. Tous les éléments doivent être du même type (toutes des images, tous des masques ou tous des latents). |

**Note :** Le nœud détermine automatiquement le type de données (IMAGE, MASK ou LATENT) en fonction du premier élément de la liste `inputs`. Tous les éléments suivants doivent correspondre à ce type. Le nœud échouera si vous essayez de mélanger différents types de données.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | IMAGE, MASK ou LATENT | Une seule sortie groupée. Le type de données correspond au type d'entrée (IMAGE groupée, MASK groupée ou LATENT groupée). |
