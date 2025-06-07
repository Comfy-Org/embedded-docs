Le nœud ConditioningAverage est conçu pour mélanger deux ensembles de données de conditionnement en appliquant une moyenne pondérée basée sur une force spécifiée. Ce processus permet un ajustement dynamique de l'influence du conditionnement, facilitant le réglage fin du contenu ou des caractéristiques générés.

## Entrées

| Paramètre             | Comfy dtype        | Description |
|----------------------|--------------------|-------------|
| `conditioning_to`     | `CONDITIONING`     | Représente l'ensemble principal de données de conditionnement auquel le mélange sera appliqué. Il sert de base pour l'opération de moyenne pondérée. |
| `conditioning_from`   | `CONDITIONING`     | Désigne l'ensemble secondaire de données de conditionnement qui sera mélangé à l'ensemble principal. Ces données influencent le résultat final en fonction de la force spécifiée. |
| `conditioning_to_strength` | `FLOAT` | Une valeur scalaire qui détermine la force du mélange entre les données de conditionnement principales et secondaires. Elle influence directement l'équilibre de la moyenne pondérée. |

## Sorties

| Paramètre            | Comfy dtype        | Description |
|----------------------|--------------------|-------------|
| `conditioning`        | `CONDITIONING`     | Le résultat du mélange des données de conditionnement principales et secondaires, produisant un nouvel ensemble de conditionnement qui reflète la moyenne pondérée. |
