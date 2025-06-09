
Le nœud VideoLinearCFGGuidance applique une échelle de guidage de conditionnement linéaire à un modèle vidéo, ajustant l'influence des composants conditionnés et non conditionnés sur une plage spécifiée. Cela permet un contrôle dynamique du processus de génération, permettant un ajustement fin de la sortie du modèle en fonction du niveau de conditionnement souhaité.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `model`   | MODEL     | Le paramètre model représente le modèle vidéo auquel le guidage linéaire CFG sera appliqué. Il est crucial pour définir le modèle de base qui sera modifié avec l'échelle de guidage. |
| `min_cfg` | `FLOAT`     | Le paramètre min_cfg spécifie l'échelle minimale de guidage de conditionnement à appliquer, servant de point de départ pour l'ajustement de l'échelle linéaire. Il joue un rôle clé dans la détermination de la limite inférieure de l'échelle de guidage, influençant la sortie du modèle. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `model`   | MODEL     | La sortie est une version modifiée du modèle d'entrée, avec l'échelle de guidage linéaire CFG appliquée. Ce modèle ajusté est capable de générer des sorties avec des degrés de conditionnement variés, basés sur l'échelle de guidage spécifiée. |
