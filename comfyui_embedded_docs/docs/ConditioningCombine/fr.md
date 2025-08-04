Ce nœud combine deux entrées de conditionnement en une seule sortie, fusionnant efficacement leurs informations. Les deux conditions sont combinées en utilisant la concaténation de listes.

## Entrées

| Nom du Paramètre     | Type de Données    | Description |
|----------------------|--------------------|-------------|
| `conditionnement_1`  | `CONDITIONING`     | La première entrée de conditionnement à combiner. Elle a une importance égale avec `conditionnement_2` dans le processus de combinaison. |
| `conditionnement_2`  | `CONDITIONING`     | La deuxième entrée de conditionnement à combiner. Elle a une importance égale avec `conditionnement_1` dans le processus de combinaison. |

## Sorties

| Nom du Paramètre     | Type de Données    | Description |
|----------------------|--------------------|-------------|
| `conditionnement`    | `CONDITIONING`     | Le résultat de la combinaison de `conditionnement_1` et `conditionnement_2`, encapsulant les informations fusionnées. |

## Scénarios d'Utilisation

Comparez les deux groupes ci-dessous : le côté gauche utilise le nœud ConditioningCombine, tandis que le côté droit montre la sortie normale.

![Compare](./asset/compare.jpg)

Dans cet exemple, les deux conditions utilisées dans `Conditionnement (Combiner)` ont une importance équivalente. Par conséquent, vous pouvez utiliser différents encodages de texte pour le style d'image, les caractéristiques du sujet, etc., permettant aux caractéristiques du prompt d'être sorties plus complètement. Le deuxième prompt utilise le prompt complet combiné, mais la compréhension sémantique peut encoder des conditions complètement différentes.

En utilisant ce nœud, vous pouvez réaliser :

- Fusion de texte basique : Connectez les sorties de deux nœuds `Encodage de Texte CLIP` aux deux ports d'entrée de `Conditionnement (Combiner)`
- Combinaison complexe de prompts : Combinez des prompts positifs et négatifs, ou encodez séparément les descriptions principales et les descriptions de style avant de les fusionner
- Combinaison conditionnelle en chaîne : Plusieurs nœuds `Conditionnement (Combiner)` peuvent être utilisés en série pour réaliser la combinaison progressive de plusieurs conditions
