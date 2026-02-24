> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySoftSwitchNode/fr.md)

Le nœud Soft Switch sélectionne entre deux valeurs d'entrée possibles en fonction d'une condition booléenne. Il renvoie la valeur de l'entrée `on_true` lorsque l'interrupteur (`switch`) est vrai, et la valeur de l'entrée `on_false` lorsque l'interrupteur est faux. Ce nœud est conçu pour être "paresseux" (lazy), ce qui signifie qu'il n'évalue que l'entrée nécessaire en fonction de l'état de l'interrupteur.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `switch` | BOOLEAN | Oui | | La condition booléenne qui détermine quelle entrée transmettre. Lorsqu'elle est vraie, l'entrée `on_true` est sélectionnée. Lorsqu'elle est fausse, l'entrée `on_false` est sélectionnée. |
| `on_false` | MATCH_TYPE | Non | | La valeur à renvoyer lorsque la condition `switch` est fausse. Cette entrée est facultative, mais au moins l'une des entrées `on_false` ou `on_true` doit être connectée. |
| `on_true` | MATCH_TYPE | Non | | La valeur à renvoyer lorsque la condition `switch` est vraie. Cette entrée est facultative, mais au moins l'une des entrées `on_false` ou `on_true` doit être connectée. |

**Note :** Les entrées `on_false` et `on_true` doivent être du même type de données, tel que défini par le modèle interne du nœud. Au moins l'une de ces deux entrées doit être connectée pour que le nœud fonctionne.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | MATCH_TYPE | La valeur sélectionnée. Elle correspondra au type de données de l'entrée connectée `on_false` ou `on_true`. |
