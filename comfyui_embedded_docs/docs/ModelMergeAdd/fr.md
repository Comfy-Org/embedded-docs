
Le nœud ModelMergeAdd est conçu pour fusionner deux modèles en ajoutant des éléments clés d'un modèle à un autre. Ce processus implique le clonage du premier modèle, puis l'application de patchs du second modèle, permettant ainsi la combinaison de caractéristiques ou de comportements des deux modèles.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `model1`  | `MODEL`     | Le premier modèle à cloner et auquel les patchs du second modèle seront ajoutés. Il sert de modèle de base pour le processus de fusion. |
| `model2`  | `MODEL`     | Le second modèle à partir duquel des éléments clés sont extraits et ajoutés au premier modèle. Il apporte des caractéristiques ou des comportements supplémentaires au modèle fusionné. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `model`   | MODEL     | Le résultat de la fusion de deux modèles en ajoutant des éléments clés du second modèle au premier. Ce modèle fusionné combine des caractéristiques ou des comportements des deux modèles. |
