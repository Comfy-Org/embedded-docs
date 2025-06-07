
Ce nœud est conçu pour des opérations avancées de fusion de modèles, spécifiquement pour soustraire les paramètres d'un modèle d'un autre en fonction d'un multiplicateur spécifié. Il permet la personnalisation des comportements des modèles en ajustant l'influence des paramètres d'un modèle sur un autre, facilitant la création de nouveaux modèles hybrides.

## Entrées

| Paramètre     | Type de Donnée | Description |
|---------------|--------------|-------------|
| `model1`      | `MODEL`     | Le modèle de base dont les paramètres seront soustraits. |
| `model2`      | `MODEL`     | Le modèle dont les paramètres seront soustraits du modèle de base. |
| `multiplier`  | `FLOAT`     | Une valeur flottante qui échelle l'effet de soustraction sur les paramètres du modèle de base. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `model`   | MODEL     | Le modèle résultant après soustraction des paramètres d'un modèle d'un autre, échelonné par le multiplicateur. |
