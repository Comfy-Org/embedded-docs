
ModelMergeBlocks est conçu pour des opérations avancées de fusion de modèles, permettant l'intégration de deux modèles avec des ratios de mélange personnalisables pour différentes parties des modèles. Ce nœud facilite la création de modèles hybrides en fusionnant sélectivement des composants de deux modèles sources selon des paramètres spécifiés.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `model1`  | `MODEL`     | Le premier modèle à fusionner. Il sert de modèle de base sur lequel les patchs du second modèle sont appliqués. |
| `model2`  | `MODEL`     | Le second modèle à partir duquel les patchs sont extraits et appliqués au premier modèle, selon les ratios de mélange spécifiés. |
| `input`   | `FLOAT`     | Spécifie le ratio de mélange pour la couche d'entrée des modèles. Il détermine combien de la couche d'entrée du second modèle est fusionnée dans le premier modèle. |
| `middle`  | `FLOAT`     | Définit le ratio de mélange pour les couches intermédiaires des modèles. Ce paramètre contrôle le niveau d'intégration des couches intermédiaires des modèles. |
| `out`     | `FLOAT`     | Détermine le ratio de mélange pour la couche de sortie des modèles. Il affecte la sortie finale en ajustant la contribution de la couche de sortie du second modèle. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `model`   | MODEL     | Le modèle fusionné résultant, qui est un hybride des deux modèles d'entrée avec des patchs appliqués selon les ratios de mélange spécifiés. |
