# ComfySoftSwitchNode

Le nœud Soft Switch sélectionne entre deux valeurs d'entrée possibles en fonction d'une condition booléenne. Il renvoie la valeur de l'entrée `on_true` lorsque `switch` est vrai, et la valeur de l'entrée `on_false` lorsque `switch` est faux. Ce nœud est conçu pour être paresseux, c'est-à-dire qu'il n'évalue que l'entrée nécessaire en fonction de l'état du commutateur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `switch` | La condition booléenne qui détermine quelle entrée transmettre. Lorsqu'elle est vraie, l'entrée `on_true` est sélectionnée. Lorsqu'elle est fausse, l'entrée `on_false` est sélectionnée. | BOOLEAN | Oui | True or False |
| `on_false` | La valeur à afficher en sortie lorsque la condition `switch` est fausse. Cette entrée est facultative, mais au moins une des entrées `on_false` ou `on_true` doit être connectée. | MATCH_TYPE | Non | Même type de données que `on_true` |
| `on_true` | La valeur à afficher en sortie lorsque la condition `switch` est vraie. Cette entrée est facultative, mais au moins une des entrées `on_false` ou `on_true` doit être connectée. | MATCH_TYPE | Non | Même type de données que `on_false` |

**Remarque :** Les entrées `on_false` et `on_true` doivent être du même type de données, comme défini par le modèle interne du nœud. Au moins une de ces deux entrées doit être connectée pour que le nœud fonctionne. Comme le nœud est paresseux, lorsqu'une seule entrée est connectée, le nœud renvoie toujours la valeur de cette entrée, indépendamment de l'état de `switch`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La valeur sélectionnée. Elle correspond au type de données de l'entrée connectée `on_false` ou `on_true`. Lorsque les deux entrées sont connectées, elle renvoie `on_true` si `switch` est vrai, et `on_false` si `switch` est faux. | MATCH_TYPE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySoftSwitchNode/fr.md)

---
**Source fingerprint (SHA-256):** `7bf4bed69d8fd8c360e971ab8068382cd8ebaa02004d5df44312977a7309ae00`
