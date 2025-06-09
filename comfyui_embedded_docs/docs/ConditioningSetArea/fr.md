Ce nœud est conçu pour modifier les informations de conditionnement en définissant des zones spécifiques dans le contexte de conditionnement. Il permet une manipulation spatiale précise des éléments de conditionnement, permettant des ajustements et des améliorations ciblés basés sur des dimensions et une force spécifiées.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | Les données de conditionnement à modifier. Elles servent de base pour appliquer des ajustements spatiaux. |
| `width`   | `INT`      | Spécifie la largeur de la zone à définir dans le contexte de conditionnement, influençant la portée horizontale de l'ajustement. |
| `height`  | `INT`      | Détermine la hauteur de la zone à définir, affectant l'étendue verticale de la modification du conditionnement. |
| `x`       | `INT`      | Le point de départ horizontal de la zone à définir, positionnant l'ajustement dans le contexte de conditionnement. |
| `y`       | `INT`      | Le point de départ vertical pour l'ajustement de la zone, établissant sa position dans le contexte de conditionnement. |
| `strength`| `FLOAT`    | Définit l'intensité de la modification du conditionnement dans la zone spécifiée, permettant un contrôle nuancé de l'impact de l'ajustement. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | Les données de conditionnement modifiées, reflétant les paramètres et ajustements de zone spécifiés. |
