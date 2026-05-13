> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaStrength/fr.md)

Ce nœud est conçu pour modifier l'attribut de force d'un ensemble de conditionnement donné, permettant d'ajuster l'influence ou l'intensité du conditionnement sur le processus de génération.

## Entrées

| Paramètre | Type de données | Description |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | L'ensemble de conditionnement à modifier, représentant l'état actuel du conditionnement qui influence le processus de génération. |
| `force` | `FLOAT` | La valeur de force à appliquer à l'ensemble de conditionnement, déterminant l'intensité de son influence. |

## Sorties

| Paramètre | Type de données | Description |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | L'ensemble de conditionnement modifié avec des valeurs de force mises à jour pour chaque élément. |