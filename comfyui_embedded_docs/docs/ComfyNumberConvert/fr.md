# Conversion de nombre

Le nœud Number Convert transforme divers types de données d'entrée en valeurs numériques. Il accepte une seule entrée de type entier, nombre à virgule flottante, chaîne de caractères ou booléen, et produit deux sorties : un nombre à virgule flottante et un entier. Cela est utile pour convertir du texte ou des valeurs logiques dans un format pouvant être utilisé par d'autres nœuds mathématiques ou de traitement dans votre flux de travail.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `value` | La valeur à convertir en sorties numériques. Accepte un entier, un nombre à virgule flottante, une chaîne de texte ou un booléen vrai/faux. | INT, FLOAT, STRING, BOOLEAN | Oui | N/A |

**Remarque :** Lorsque l'entrée est une chaîne de caractères, elle ne doit pas être vide et doit contenir une représentation valide d'un nombre (par exemple, `"123"`, `"3.14"`). Le nœud générera une erreur pour les chaînes vides, le texte qui ne peut pas être interprété comme un nombre, ou les valeurs qui ne sont pas finies (comme `"inf"` ou `"nan"`). Pour les entrées booléennes, `true` est converti en 1.0 (FLOAT) et 1 (INT), tandis que `false` est converti en 0.0 (FLOAT) et 0 (INT). Pour les entrées de type float et pour les chaînes contenant un nombre décimal, la sortie entière est obtenue par troncature de la partie décimale.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `FLOAT` | La valeur d'entrée convertie en nombre à virgule flottante. | FLOAT |
| `INT` | La valeur d'entrée convertie en entier. Pour les entrées de type float et les chaînes décimales, cela effectue une troncature. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyNumberConvert/fr.md)

---
**Source fingerprint (SHA-256):** `d6a774bf7c3ad9482b2275adc6ccc9e47c82b1f35f11c5a241b00efd29526f94`
