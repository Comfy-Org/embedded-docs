> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningCombine/fr.md)

Ce nœud combine deux entrées de conditionnement en une seule sortie, fusionnant ainsi leurs informations. Les deux conditions sont combinées par concaténation de listes.

## Entrées

| Nom du paramètre    | Type de données    | Description |
|---------------------|--------------------|-------------|
| `conditionnement_1`    | `CONDITIONING`     | La première entrée de conditionnement à combiner. Elle a une importance égale à `conditionnement_2` dans le processus de combinaison. |
| `conditionnement_2`    | `CONDITIONING`     | La deuxième entrée de conditionnement à combiner. Elle a une importance égale à `conditionnement_1` dans le processus de combinaison. |

## Sorties

| Nom du paramètre    | Type de données    | Description |
|---------------------|--------------------|-------------|
| `conditioning`      | `CONDITIONING`     | Le résultat de la combinaison de `conditionnement_1` et `conditionnement_2`, encapsulant les informations fusionnées. |

## Scénarios d'utilisation

Comparez les deux groupes ci-dessous : le côté gauche utilise le nœud ConditioningCombine, tandis que le côté droit montre une sortie normale.

![Comparaison](./asset/compare.jpg)

Dans cet exemple, les deux conditions utilisées dans `Conditioning Combine` ont une importance équivalente. Par conséquent, vous pouvez utiliser différents encodages de texte pour le style de l'image, les caractéristiques du sujet, etc., permettant ainsi aux caractéristiques du prompt d'être produites plus complètement. Le deuxième prompt utilise le prompt complet combiné, mais la compréhension sémantique peut encoder des conditions complètement différentes.

En utilisant ce nœud, vous pouvez réaliser :

- **Fusion de texte basique** : Connectez les sorties de deux nœuds `CLIP Text Encode` aux deux ports d'entrée de `Conditioning Combine`
- **Combinaison de prompts complexes** : Combinez des prompts positifs et négatifs, ou encodez séparément les descriptions principales et les descriptions de style avant de les fusionner
- **Combinaison en chaîne conditionnelle** : Plusieurs nœuds `Conditioning Combine` peuvent être utilisés en série pour réaliser une combinaison progressive de multiples conditions