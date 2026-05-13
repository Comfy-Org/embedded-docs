> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetArea/fr.md)

Ce nœud est conçu pour modifier les informations de conditionnement en définissant des zones spécifiques dans le contexte de conditionnement. Il permet une manipulation spatiale précise des éléments de conditionnement, facilitant des ajustements et des améliorations ciblés en fonction des dimensions et de l'intensité spécifiées.

## Entrées

| Paramètre | Type de données | Description |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | Les données de conditionnement à modifier. Elles servent de base pour appliquer les ajustements spatiaux. |
| `largeur`   | `INT`      | Spécifie la largeur de la zone à définir dans le contexte de conditionnement, influençant la portée horizontale de l'ajustement. |
| `hauteur`  | `INT`      | Détermine la hauteur de la zone à définir, affectant l'étendue verticale de la modification du conditionnement. |
| `x`       | `INT`      | Le point de départ horizontal de la zone à définir, positionnant l'ajustement dans le contexte de conditionnement. |
| `y`       | `INT`      | Le point de départ vertical pour l'ajustement de la zone, établissant sa position dans le contexte de conditionnement. |
| `force`| `FLOAT`    | Définit l'intensité de la modification du conditionnement dans la zone spécifiée, permettant un contrôle nuancé de l'impact de l'ajustement. |

## Sorties

| Paramètre | Type de données | Description |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | Les données de conditionnement modifiées, reflétant les paramètres et ajustements de zone spécifiés. |