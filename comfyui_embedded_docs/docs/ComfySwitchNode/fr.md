# Commutateur

Le nœud Switch sélectionne entre deux entrées possibles en fonction d'une condition booléenne. Il transmet l'entrée `on_true` lorsque le `switch` est activé, et l'entrée `on_false` lorsque le `switch` est désactivé. Seule la branche sélectionnée est évaluée, l'autre entrée n'est donc pas requise. Cela permet de créer une logique conditionnelle et de choisir différents chemins de données dans votre flux de travail.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `interrupteur` | Condition booléenne qui détermine quelle entrée doit être transmise. Lorsqu'elle est activée (true), l'entrée `on_true` est sélectionnée. Lorsqu'elle est désactivée (false), l'entrée `on_false` est sélectionnée. | BOOLEAN | Oui |  |
| `faux` | Données à transmettre à la sortie lorsque le `switch` est désactivé (false). Cette entrée n'est requise que lorsque le `switch` est false. | MATCH_TYPE | Non |  |
| `vrai` | Données à transmettre à la sortie lorsque le `switch` est activé (true). Cette entrée n'est requise que lorsque le `switch` est true. | MATCH_TYPE | Non |  |

**Remarque sur les exigences d'entrée :** Les entrées `on_false` et `on_true` sont requises de manière conditionnelle. Le nœud demandera l'entrée `on_true` uniquement lorsque le `switch` est true, et l'entrée `on_false` uniquement lorsque le `switch` est false. Les deux entrées doivent être du même type de données et correspondre au type de données de sortie.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sortie` | Les données sélectionnées. Il s'agit de la valeur de l'entrée `on_true` si le `switch` est true, ou de la valeur de l'entrée `on_false` si le `switch` est false. | MATCH_TYPE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/fr.md)

---
**Source fingerprint (SHA-256):** `d0adda02e7f997f27182cb26e11e934660ae5bd80f3091bed2fed7c981632ce5`
