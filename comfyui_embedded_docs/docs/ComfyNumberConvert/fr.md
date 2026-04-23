> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyNumberConvert/fr.md)

Le nœud Number Convert transforme divers types de données d'entrée en valeurs numériques. Il accepte une seule entrée de type entier, nombre à virgule flottante, chaîne de caractères ou booléen et produit deux sorties : un nombre à virgule flottante et un entier. Ceci est utile pour convertir du texte ou des valeurs logiques dans un format utilisable par d'autres nœuds mathématiques ou de traitement dans votre flux de travail.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `value` | INT, FLOAT, STRING, BOOLEAN | Oui | N/A | La valeur à convertir en sorties numériques. Accepte un entier, un nombre à virgule flottante, une chaîne de caractères ou un booléen vrai/faux. |

**Note :** Lorsque l'entrée est une chaîne de caractères, elle ne doit pas être vide et doit contenir une représentation valide d'un nombre (par exemple, `"123"`, `"3.14"`). Le nœud générera une erreur pour les chaînes vides, le texte qui ne peut pas être analysé comme un nombre, ou les valeurs qui ne sont pas finies (comme `"inf"` ou `"nan"`).

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `FLOAT` | FLOAT | La valeur d'entrée convertie en nombre à virgule flottante. |
| `INT` | INT | La valeur d'entrée convertie en entier. Pour les entrées de type FLOAT, cela effectue une troncature. |