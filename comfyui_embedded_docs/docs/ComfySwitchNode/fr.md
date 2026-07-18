Le nœud Switch sélectionne entre deux entrées possibles en fonction d'une condition booléenne. Il produit en sortie l'entrée `on_true` lorsque le `switch` est activé, et l'entrée `on_false` lorsque le `switch` est désactivé. Cela permet de créer une logique conditionnelle et de choisir différents chemins de données dans votre flux de travail.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `interrupteur` | Une condition booléenne qui détermine quelle entrée transmettre. Lorsqu'elle est activée (true), l'entrée `vrai` est sélectionnée. Lorsqu'elle est désactivée (false), l'entrée `faux` est sélectionnée. | BOOLEAN | Oui |  |
| `faux` | Les données à transmettre à la sortie lorsque le `interrupteur` est désactivé (false). Cette entrée n'est requise que lorsque le `interrupteur` est false. | MATCH_TYPE | Non |  |
| `vrai` | Les données à transmettre à la sortie lorsque le `interrupteur` est activé (true). Cette entrée n'est requise que lorsque le `interrupteur` est true. | MATCH_TYPE | Non |  |

**Remarque sur les exigences d'entrée :** Les entrées `on_false` et `on_true` sont conditionnellement requises. Le nœud demandera l'entrée `on_true` uniquement lorsque le `switch` est true, et l'entrée `on_false` uniquement lorsque le `switch` est false. Les deux entrées doivent être du même type de données.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `sortie` | Les données sélectionnées. Il s'agira de la valeur de l'entrée `vrai` si le `interrupteur` est true, ou de la valeur de l'entrée `faux` si le `interrupteur` est false. | MATCH_TYPE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/fr.md)

---
**Source fingerprint (SHA-256):** `9f3cf58c1a04116fa0cbe8007fe3ed90e93c4de2e65f6778761d03fb21a63af3`
