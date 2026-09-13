# Expression mathématique

Le nœud ComfyMathExpression évalue une formule mathématique que vous écrivez sous forme de texte. La formule peut référencer les valeurs d'entrée du nœud à l'aide de noms de lettres tels que `a`, `b`, `c`, et vous pouvez ajouter autant de valeurs d'entrée que nécessaire via le groupe extensible `values`. Le résultat du calcul est renvoyé simultanément sous forme de nombre à virgule flottante, d'entier et de valeur booléenne.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `expression` | La formule mathématique à évaluer, écrite sous forme de texte (par exemple `a + b`), en utilisant les noms de lettres des valeurs d'entrée comme variables. Entrée multiligne. (valeur par défaut : "a + b") | STRING | Oui | N/A |
| `values` | Groupe extensible de valeurs d'entrée qui fournit les variables pour l'expression. Chaque valeur ajoutée au groupe reçoit automatiquement le nom de lettre minuscule suivant en commençant par `a` (`a`, `b`, `c`, ...), et ce nom peut ensuite être utilisé dans `expression`. Chaque élément accepte un nombre (INT ou FLOAT) ou un booléen (TRUE/FALSE). | FLOAT, INT, BOOLEAN | Oui | 1 à 26 valeurs, nommées `a` à `z` |

### Notes et contraintes

- `expression` ne peut pas être vide ni contenir uniquement des espaces blancs.
- L'expression doit s'évaluer en un résultat numérique (INT ou FLOAT) ou un résultat booléen (TRUE/FALSE). Les résultats booléens sont traités comme 1 pour TRUE et 0 pour FALSE. Si le résultat est d'un autre type, comme du texte, le nœud génère une erreur.
- Le résultat numérique doit être fini et convertible en FLOAT. Les résultats trop grands ou non finis provoquent une erreur.
- L'ensemble des valeurs d'entrée est également disponible dans l'expression sous le nom de variable `values` (sous forme de liste), ce qui permet des expressions telles que `sum(values)`.
- Les fonctions mathématiques suivantes sont disponibles dans l'expression : `sum`, `min`, `max`, `abs`, `round`, `pow`, `sqrt`, `ceil`, `floor`, `log`, `log2`, `log10`, `sin`, `cos`, `tan`, `int`, `float`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `FLOAT` | Le résultat de l'expression sous forme de nombre à virgule flottante. | FLOAT |
| `INT` | Le résultat de l'expression converti en entier, avec la partie décimale tronquée. | INT |
| `BOOL` | Le résultat converti en valeur booléenne : TRUE lorsque le résultat numérique est différent de zéro, FALSE lorsqu'il est égal à zéro. | BOOLEAN |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyMathExpression/fr.md)

---
**Source fingerprint (SHA-256):** `4c77e9834fe7341143352f95ed8808dc81def3361b197c67e33a531bb3696d71`
