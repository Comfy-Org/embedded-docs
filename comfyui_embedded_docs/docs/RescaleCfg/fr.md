> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RescaleCFG/fr.md)

Voici la traduction en français de la documentation du nœud RescaleCFG :

Le nœud RescaleCFG est conçu pour ajuster les échelles de conditionnement et de non-conditionnement de la sortie d'un modèle en fonction d'un multiplicateur spécifié, afin d'obtenir un processus de génération plus équilibré et contrôlé. Il fonctionne en redimensionnant la sortie du modèle pour modifier l'influence des composants conditionnés et non conditionnés, améliorant ainsi potentiellement les performances ou la qualité de la sortie du modèle.

## Entrées

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `model`   | MODEL           | Le paramètre `model` représente le modèle génératif à ajuster. Il est crucial car le nœud applique une fonction de redimensionnement à la sortie du modèle, influençant directement le processus de génération. |
| `multiplier` | `FLOAT`       | Le paramètre `multiplier` contrôle l'ampleur du redimensionnement appliqué à la sortie du modèle. Il détermine l'équilibre entre les composants d'origine et redimensionnés, affectant les caractéristiques finales de la sortie. |

## Sorties

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `model`   | MODEL           | Le modèle modifié avec des échelles de conditionnement et de non-conditionnement ajustées. Ce modèle est censé produire des sorties aux caractéristiques potentiellement améliorées grâce au redimensionnement appliqué. |