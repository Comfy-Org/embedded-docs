
Le nœud ModelMergeSimple est conçu pour fusionner deux modèles en mélangeant leurs paramètres selon un ratio spécifié. Ce nœud facilite la création de modèles hybrides qui combinent les forces ou les caractéristiques des deux modèles d'entrée.

Le paramètre `ratio` détermine le ratio de mélange entre les deux modèles. Lorsque cette valeur est 1, le modèle de sortie est 100% `model1`, et lorsque cette valeur est 0, le modèle de sortie est 100% `model2`.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `model1`  | `MODEL`     | Le premier modèle à fusionner. Il sert de modèle de base sur lequel les patchs du second modèle sont appliqués. |
| `model2`  | `MODEL`     | Le second modèle dont les patchs sont appliqués au premier modèle, influencés par le ratio spécifié. |
| `ratio`   | `FLOAT`     | Lorsque cette valeur est 1, le modèle de sortie est 100% `model1`, et lorsque cette valeur est 0, le modèle de sortie est 100% `model2`. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `model`   | MODEL     | Le modèle fusionné résultant, incorporant des éléments des deux modèles d'entrée selon le ratio spécifié. |
