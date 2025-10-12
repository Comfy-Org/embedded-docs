> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentageVideo/fr.md)

Le nœud ConditioningSetAreaPercentageVideo modifie les données de conditionnement en définissant une zone spécifique et une région temporelle pour la génération vidéo. Il vous permet de définir la position, la taille et la durée de la zone où le conditionnement sera appliqué en utilisant des valeurs en pourcentage par rapport aux dimensions globales. Ceci est utile pour concentrer la génération sur des parties spécifiques d'une séquence vidéo.

## Entrées

| Paramètre | Type de données | Type d'entrée | Par défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `conditionnement` | CONDITIONING | Requis | - | - | Les données de conditionnement à modifier |
| `largeur` | FLOAT | Requis | 1.0 | 0.0 - 1.0 | La largeur de la zone en pourcentage de la largeur totale |
| `hauteur` | FLOAT | Requis | 1.0 | 0.0 - 1.0 | La hauteur de la zone en pourcentage de la hauteur totale |
| `temporel` | FLOAT | Requis | 1.0 | 0.0 - 1.0 | La durée temporelle de la zone en pourcentage de la longueur totale de la vidéo |
| `x` | FLOAT | Requis | 0.0 | 0.0 - 1.0 | La position de départ horizontale de la zone en pourcentage |
| `y` | FLOAT | Requis | 0.0 | 0.0 - 1.0 | La position de départ verticale de la zone en pourcentage |
| `z` | FLOAT | Requis | 0.0 | 0.0 - 1.0 | La position de départ temporelle de la zone en pourcentage de la timeline vidéo |
| `force` | FLOAT | Requis | 1.0 | 0.0 - 10.0 | Le multiplicateur de force appliqué au conditionnement dans la zone définie |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `conditionnement` | CONDITIONING | Les données de conditionnement modifiées avec les paramètres de zone et de force spécifiés appliqués |