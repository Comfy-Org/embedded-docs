Le nœud ConditioningSetAreaPercentage est spécialisé dans l'ajustement de la zone d'influence des éléments de conditionnement en fonction de valeurs en pourcentage. Il permet de spécifier les dimensions et la position de la zone en pourcentages de la taille totale de l'image, ainsi qu'un paramètre de force pour moduler l'intensité de l'effet de conditionnement.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | Représente les éléments de conditionnement à modifier, servant de base pour appliquer les ajustements de zone et de force. |
| `width`   | `FLOAT`     | Spécifie la largeur de la zone en pourcentage de la largeur totale de l'image, influençant la part de l'image affectée horizontalement par le conditionnement. |
| `height`  | `FLOAT`     | Détermine la hauteur de la zone en pourcentage de la hauteur totale de l'image, affectant l'étendue verticale de l'influence du conditionnement. |
| `x`       | `FLOAT`     | Indique le point de départ horizontal de la zone en pourcentage de la largeur totale de l'image, positionnant l'effet de conditionnement. |
| `y`       | `FLOAT`     | Spécifie le point de départ vertical de la zone en pourcentage de la hauteur totale de l'image, positionnant l'effet de conditionnement. |
| `strength`| `FLOAT`     | Contrôle l'intensité de l'effet de conditionnement dans la zone spécifiée, permettant un ajustement précis de son impact. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | Retourne les éléments de conditionnement modifiés avec des paramètres de zone et de force mis à jour, prêts pour un traitement ou une application ultérieure. |
