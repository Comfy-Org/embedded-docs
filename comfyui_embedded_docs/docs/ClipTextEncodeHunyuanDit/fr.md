Le nœud `CLIPTextEncodeHunyuanDiT` a pour fonction principale de convertir le texte d'entrée dans une forme compréhensible par le modèle. C'est un nœud de conditionnement avancé spécialement conçu pour l'architecture à double encodeur de texte du modèle HunyuanDiT.
Son rôle principal est celui d'un traducteur, convertissant nos descriptions textuelles en "langage machine" que le modèle d'IA peut comprendre. Les entrées `bert` et `mt5xl` préfèrent différents types de prompts.

## Entrées

| Paramètre | Data Type | Description |
|-----------|-----------|-------------|
| `clip` | CLIP | Une instance du modèle CLIP utilisée pour la tokenisation et l'encodage du texte, essentielle pour générer les conditions. |
| `bert` | STRING | Entrée de texte pour l'encodage, préfère les phrases et mots-clés, prend en charge les prompts multilignes et dynamiques. |
| `mt5xl` | STRING | Autre entrée de texte pour l'encodage, prend en charge les prompts multilignes et dynamiques (multilingue), peut utiliser des phrases complètes et des descriptions complexes. |

## Sorties

| Paramètre | Data Type | Description |
|-----------|-----------|-------------|
| `CONDITIONNEMENT` | CONDITIONING | La sortie conditionnelle encodée utilisée pour le traitement ultérieur dans les tâches de génération. |
