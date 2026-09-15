# ComfySoftSwitchNode

Le nœud Soft Switch sélectionne entre deux valeurs d'entrée possibles en fonction d'une condition booléenne. Il produit la valeur de l'entrée `on_true` lorsque le `switch` est vrai, et la valeur de l'entrée `on_false` lorsque le `switch` est faux. Ce nœud est conçu pour être paresseux (lazy), ce qui signifie qu'il n'évalue que l'entrée réellement nécessaire en fonction de l'état du `switch`.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `switch` | La condition booléenne qui détermine quelle entrée transmettre. Lorsqu'elle est vraie, l'entrée `on_true` est sélectionnée. Lorsqu'elle est fausse, l'entrée `on_false` est sélectionnée. | BOOLEAN | Oui | True or False |
| `on_false` | La valeur à produire lorsque la condition `switch` est fausse. Cette entrée est facultative, mais au moins l'une des entrées `on_false` ou `on_true` doit être connectée. | MATCH_TYPE | Non | Même type de données que `on_true` |
| `on_true` | La valeur à produire lorsque la condition `switch` est vraie. Cette entrée est facultative, mais au moins l'une des entrées `on_false` ou `on_true` doit être connectée. | MATCH_TYPE | Non | Même type de données que `on_false` |

**Note :** Les entrées `on_false` et `on_true` doivent être du même type de données, tel que défini par le template interne du nœud. Au moins une de ces deux entrées doit être connectée ; sinon, le nœud renvoie le message de validation « At least one of on_false or on_true must be connected to Switch node ». Comme le nœud est paresseux (lazy), lorsqu'une seule entrée est connectée, le nœud produit toujours la valeur de cette entrée, quel que soit l'état du `switch`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La valeur sélectionnée. Elle correspond au type de données de l'entrée `on_false` ou `on_true` connectée. Lorsque les deux entrées sont connectées, elle produit `on_true` si `switch` est vrai, et `on_false` si `switch` est faux. | MATCH_TYPE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySoftSwitchNode/fr.md)

---
**Source fingerprint (SHA-256):** `7bf4bed69d8fd8c360e971ab8068382cd8ebaa02004d5df44312977a7309ae00`
