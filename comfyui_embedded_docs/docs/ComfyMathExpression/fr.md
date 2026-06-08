Le nœud ComfyMathExpression évalue une formule mathématique à l'aide d'un ensemble de valeurs d'entrée. Vous pouvez écrire une expression en utilisant des noms de variables (comme `a`, `b`, `c`), et le nœud calculera le résultat. Il prend en charge l'ajout dynamique d'autant de valeurs d'entrée que nécessaire pour votre calcul.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `expression` | La formule mathématique à évaluer. Vous pouvez utiliser des noms de variables qui correspondent aux valeurs d'entrée (par défaut : "a + b"). | STRING | Oui | N/A |
| `valeurs` | Un ensemble d'entrées numériques ou booléennes pouvant être ajoutées dynamiquement. Chaque entrée se voit attribuer une lettre de l'alphabet (a, b, c, ...) à utiliser comme variable dans l'expression. | FLOAT, INT, BOOLEAN | Non | N/A |

**Contraintes des paramètres :**
*   Le paramètre `expression` ne peut pas être vide ou contenir uniquement des espaces.
*   L'expression doit produire un résultat numérique fini (INT ou FLOAT). Un résultat booléen ou non numérique provoquera une erreur.
*   Les valeurs d'entrée pour le paramètre `values` peuvent être des nombres (INT ou FLOAT) ou des valeurs booléennes (TRUE/FALSE).

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `FLOAT` | Le résultat de l'expression mathématique sous forme de nombre à virgule flottante. | FLOAT |
| `BOOL` | Le résultat de l'expression mathématique sous forme de nombre entier. | INT |
| `BOOL` | Le résultat de l'expression mathématique sous forme de valeur booléenne. | BOOLEAN |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyMathExpression/fr.md)

---
**Source fingerprint (SHA-256):** `962f82684d9dc58a67a57e6738d6d2ed457d7f30288cedb21fd46b5c655c1708`
