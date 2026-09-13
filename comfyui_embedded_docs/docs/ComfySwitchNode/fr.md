# Commutateur

Le nœud If/Else Switch sélectionne entre deux entrées possibles en fonction d'une condition booléenne. Lorsque `switch` est activé (true), il transmet l'entrée `on_true` vers la sortie ; lorsqu'il est désactivé (false), il transmet `on_false`. Les entrées sont évaluées paresseusement, donc seule la branche sélectionnée est évaluée et l'autre entrée n'a pas besoin d'être connectée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `switch` | Une condition booléenne qui détermine quelle entrée est transmise à la sortie. Lorsqu'elle est activée (true), l'entrée `on_true` est sélectionnée. Lorsqu'elle est désactivée (false), l'entrée `on_false` est sélectionnée. | BOOLEAN | Oui |  |
| `on_false` | Les données à transmettre à la sortie lorsque `switch` est désactivé (false). Cette entrée n'est demandée que lorsque `switch` est false. | MATCH_TYPE | Non |  |
| `on_true` | Les données à transmettre à la sortie lorsque `switch` est activé (true). Cette entrée n'est demandée que lorsque `switch` est true. | MATCH_TYPE | Non |  |

**Note sur les exigences des entrées :** Les entrées `on_false` et `on_true` sont demandées de manière conditionnelle. Le nœud demande `on_true` uniquement lorsque `switch` est true, et demande `on_false` uniquement lorsque `switch` est false. Les deux entrées doivent être du même type de données, et ce type doit correspondre au type de données de la sortie. Si l'entrée sélectionnée n'est pas connectée, le nœud ne produit aucune valeur.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Les données sélectionnées : la valeur de `on_true` lorsque `switch` est true, ou la valeur de `on_false` lorsque `switch` est false. | MATCH_TYPE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/fr.md)

---
**Source fingerprint (SHA-256):** `42c442efeda0197d950702c52647233dee1a30216fb07e1ce4bc844784a6c5f2`
