Ce document a été généré par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySoftSwitchNode/en.md)

Le nœud Soft Switch sélectionne entre deux valeurs d'entrée possibles en fonction d'une condition booléenne. Il produit la valeur de l'entrée `on_true` lorsque le `switch` est vrai, et la valeur de l'entrée `on_false` lorsque le `switch` est faux. Ce nœud est conçu pour être paresseux, ce qui signifie qu'il n'évalue que l'entrée nécessaire en fonction de l'état du commutateur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `switch` | La condition booléenne qui détermine quelle entrée transmettre. Lorsqu'elle est vraie, l'entrée `on_true` est sélectionnée. Lorsqu'elle est fausse, l'entrée `on_false` est sélectionnée. | BOOLEAN | Oui |  |
| `on_false` | La valeur à produire lorsque la condition `switch` est fausse. Cette entrée est facultative, mais au moins l'une des entrées `on_false` ou `on_true` doit être connectée. | MATCH_TYPE | Non |  |
| `on_true` | La valeur à produire lorsque la condition `switch` est vraie. Cette entrée est facultative, mais au moins l'une des entrées `on_false` ou `on_true` doit être connectée. | MATCH_TYPE | Non |  |

**Remarque :** Les entrées `on_false` et `on_true` doivent être du même type de données, tel que défini par le modèle interne du nœud. Au moins l'une de ces deux entrées doit être connectée pour que le nœud fonctionne.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La valeur sélectionnée. Elle correspondra au type de données de l'entrée `on_false` ou `on_true` connectée. | MATCH_TYPE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySoftSwitchNode/fr.md)

---
**Source fingerprint (SHA-256):** `f5e40e7f43948b81b5442c885c3e1ff15e38f8f7ddda00ef3be42225765bfd1c`
