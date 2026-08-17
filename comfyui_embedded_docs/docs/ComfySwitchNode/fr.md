# Commutateur

Le nœud Switch sélectionne entre deux entrées possibles en fonction d'une condition booléenne. Il génère l'entrée `on_true` lorsque le `switch` est activé, et l'entrée `on_false` lorsque le `switch` est désactivé, vous permettant de créer une logique conditionnelle et de choisir différents chemins de données dans votre flux de travail. Ce nœud est actuellement marqué comme expérimental.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `switch` | Une condition booléenne qui détermine quelle entrée transmettre. Lorsqu'elle est activée (true), l'entrée `on_true` est sélectionnée. Lorsqu'elle est désactivée (false), l'entrée `on_false` est sélectionnée. | BOOLEAN | Oui |  |
| `on_false` | Les données à transmettre à la sortie lorsque le `switch` est désactivé (false). Cette entrée n'est requise que lorsque le `switch` est false. | MATCH_TYPE | Non |  |
| `on_true` | Les données à transmettre à la sortie lorsque le `switch` est activé (true). Cette entrée n'est requise que lorsque le `switch` est true. | MATCH_TYPE | Non |  |

**Remarque sur les exigences d'entrée :** Les entrées `on_false` et `on_true` sont requises conditionnellement. Le nœud demandera l'entrée `on_true` uniquement lorsque le `switch` est true, et l'entrée `on_false` uniquement lorsque le `switch` est false. Les deux entrées doivent être du même type de données.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Les données sélectionnées. Il s'agira de la valeur de l'entrée `on_true` si le `switch` est true, ou de la valeur de l'entrée `on_false` si le `switch` est false. | MATCH_TYPE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/fr.md)

---
**Source fingerprint (SHA-256):** `d0adda02e7f997f27182cb26e11e934660ae5bd80f3091bed2fed7c981632ce5`
