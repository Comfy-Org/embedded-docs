> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyMathExpression/fr.md)

Le nœud ComfyMathExpression évalue une formule mathématique en utilisant un ensemble de valeurs d'entrée. Vous pouvez écrire une expression en utilisant des noms de variables (comme `a`, `b`, `c`), et le nœud calculera le résultat. Il permet d'ajouter dynamiquement autant de valeurs d'entrée que nécessaire pour votre calcul.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `expression` | STRING | Oui | N/A | La formule mathématique à évaluer. Vous pouvez utiliser des noms de variables qui correspondent aux valeurs d'entrée (par défaut : "a + b"). |
| `values` | FLOAT, INT | Non | N/A | Un ensemble d'entrées numériques qui peuvent être ajoutées dynamiquement. Chaque entrée se voit attribuer une lettre de l'alphabet (a, b, c, ...) pour être utilisée comme variable dans l'expression. |

**Contraintes des paramètres :**
*   Le paramètre `expression` ne peut pas être vide ou contenir uniquement des espaces.
*   L'expression doit s'évaluer en un résultat numérique fini (INT ou FLOAT). Un résultat booléen ou autre non numérique provoquera une erreur.
*   Les valeurs d'entrée pour le paramètre `values` doivent être des nombres valides (INT ou FLOAT).

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `FLOAT` | FLOAT | Le résultat de l'expression mathématique sous forme de nombre à virgule flottante. |
| `INT` | INT | Le résultat de l'expression mathématique sous forme d'entier. |