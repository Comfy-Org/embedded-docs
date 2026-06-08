Le nœud DCTestNode est un nœud logique qui renvoie différents types de données en fonction de la sélection de l'utilisateur dans une liste déroulante dynamique. Il agit comme un routeur conditionnel, où l'option choisie détermine quel champ d'entrée est actif et quel type de valeur le nœud va produire en sortie.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `combo` | La sélection principale qui détermine quel champ d'entrée est actif et ce que le nœud va produire en sortie. | COMBO | Oui | `"option1"`<br>`"option2"`<br>`"option3"`<br>`"option4"` |
| `string` | Un champ de saisie de texte. Ce champ est uniquement actif et requis lorsque `combo` est défini sur `"option1"`. | STRING | Non | - |
| `integer` | Un champ de saisie de nombre entier. Ce champ est uniquement actif et requis lorsque `combo` est défini sur `"option2"`. | INT | Non | - |
| `image` | Un champ de saisie d'image. Ce champ est uniquement actif et requis lorsque `combo` est défini sur `"option3"`. | IMAGE | Non | - |
| `subcombo` | Une sélection secondaire qui apparaît lorsque `combo` est défini sur `"option4"`. Elle détermine quels champs d'entrée imbriqués sont actifs. | COMBO | Non | `"opt1"`<br>`"opt2"` |
| `float_x` | Une saisie de nombre décimal. Ce champ est uniquement actif et requis lorsque `combo` est défini sur `"option4"` et `subcombo` est défini sur `"opt1"`. | FLOAT | Non | - |
| `float_y` | Une saisie de nombre décimal. Ce champ est uniquement actif et requis lorsque `combo` est défini sur `"option4"` et `subcombo` est défini sur `"opt1"`. | FLOAT | Non | - |
| `mask1` | Un champ de saisie de masque. Ce champ est uniquement actif lorsque `combo` est défini sur `"option4"` et `subcombo` est défini sur `"opt2"`. Il est facultatif. | MASK | Non | - |

**Contraintes des paramètres :**

* Le paramètre `combo` contrôle la visibilité et le caractère obligatoire de tous les autres champs d'entrée. Seules les entrées associées à l'option `combo` sélectionnée seront affichées et seront requises (à l'exception de `mask1` qui est facultatif).
* Lorsque `combo` est défini sur `"option4"`, le paramètre `subcombo` devient obligatoire et contrôle un deuxième ensemble d'entrées imbriquées (`float_x`/`float_y` ou `mask1`).

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La sortie dépend de l'option `combo` sélectionnée. Il peut s'agir d'une STRING (`"option1"`), d'un INT (`"option2"`), d'une IMAGE (`"option3"`) ou d'une représentation textuelle du dictionnaire `subcombo` (`"option4"`). | ANYTYPE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DCTestNode/fr.md)

---
**Source fingerprint (SHA-256):** `98c4ca2100a27594df360935cc1507960480fe75a76ca0df2af75925d399be00`
