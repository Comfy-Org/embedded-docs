Le nœud ConditioningConcat est conçu pour concaténer les vecteurs de conditionnement, fusionnant spécifiquement le vecteur 'conditioning_from' dans le vecteur 'conditioning_to'. Cette opération est fondamentale dans les scénarios où les informations de conditionnement de deux sources doivent être combinées en une seule représentation unifiée.

Imaginez que vous cuisinez un plat, `conditioning_to` est la recette de base, et `conditioning_from` sont des assaisonnements ou condiments supplémentaires. La classe ConditioningConcat est comme un outil qui vous aide à ajouter ces assaisonnements à la recette, rendant votre plat plus coloré et riche.

## Entrées

| Paramètre             | Comfy dtype        | Description |
|-----------------------|--------------------|-------------|
| `conditioning_to`     | `CONDITIONING`     | Représente l'ensemble principal de vecteurs de conditionnement auquel les vecteurs 'conditioning_from' seront concaténés. Il sert de base pour le processus de concaténation. |
| `conditioning_from`   | `CONDITIONING`     | Se compose de vecteurs de conditionnement qui doivent être concaténés aux vecteurs 'conditioning_to'. Ce paramètre permet d'intégrer des informations de conditionnement supplémentaires dans l'ensemble existant. |

## Sorties

| Paramètre            | Comfy dtype        | Description |
|----------------------|--------------------|-------------|
| `conditioning`       | `CONDITIONING`     | La sortie est un ensemble unifié de vecteurs de conditionnement, résultant de la concaténation des vecteurs 'conditioning_from' dans les vecteurs 'conditioning_to'. |
