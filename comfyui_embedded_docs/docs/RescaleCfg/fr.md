
Le nœud RescaleCFG est conçu pour ajuster les échelles de conditionnement et de non-conditionnement de la sortie d'un modèle en fonction d'un multiplicateur spécifié, visant à obtenir un processus de génération plus équilibré et contrôlé. Il fonctionne en rééchelonnant la sortie du modèle pour modifier l'influence des composants conditionnés et non conditionnés, améliorant ainsi potentiellement les performances ou la qualité de sortie du modèle.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `model`   | MODEL     | Le paramètre modèle représente le modèle génératif à ajuster. Il est crucial car le nœud applique une fonction de rééchelonnement à la sortie du modèle, influençant directement le processus de génération. |
| `multiplier` | `FLOAT` | Le paramètre multiplicateur contrôle l'étendue du rééchelonnement appliqué à la sortie du modèle. Il détermine l'équilibre entre les composants originaux et rééchelonnés, affectant les caractéristiques finales de la sortie. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `model`   | MODEL     | Le modèle modifié avec des échelles de conditionnement et de non-conditionnement ajustées. Ce modèle est censé produire des sorties avec des caractéristiques potentiellement améliorées grâce au rééchelonnement appliqué. |
