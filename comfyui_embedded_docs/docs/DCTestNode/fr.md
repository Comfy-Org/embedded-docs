# DCTestNode

DCTestNode est un nœud logique qui retourne différents types de données en fonction de la sélection de l'utilisateur dans une liste déroulante dynamique. Il agit comme un routeur conditionnel : l'option choisie détermine quel champ d'entrée est actif et quel type de valeur le nœud va produire.

## Entrées

Le nœud utilise un sélecteur combiné dynamique : le paramètre `combo` est toujours visible, et les autres champs d'entrée n'apparaissent que lorsque l'option correspondante est sélectionnée.

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `combo` | La sélection principale qui détermine quel champ d'entrée est actif et ce que le nœud produit en sortie. | DYNAMIC_COMBO | Oui | `"option1"`<br>`"option2"`<br>`"option3"`<br>`"option4"` |

### Entrées option1

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `string` | Un champ de saisie de texte. Ce champ n'est actif et requis que lorsque `combo` est défini sur `"option1"`. | STRING | Oui | - |

### Entrées option2

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `integer` | Un champ de saisie de nombre entier. Ce champ n'est actif et requis que lorsque `combo` est défini sur `"option2"`. | INT | Oui | - |

### Entrées option3

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | Un champ de saisie d'image. Ce champ n'est actif et requis que lorsque `combo` est défini sur `"option3"`. | IMAGE | Oui | - |

### Entrées option4

Lorsque `combo` est défini sur `"option4"`, le nœud affiche un second sélecteur combiné dynamique (`subcombo`) qui contrôle un ensemble imbriqué de champs d'entrée.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `subcombo` | Un sélecteur combiné dynamique secondaire qui apparaît lorsque `combo` est défini sur `"option4"`. Il détermine quels champs d'entrée imbriqués sont actifs. | DYNAMIC_COMBO | Oui | `"opt1"`<br>`"opt2"` |
| `float_x` | Un champ de saisie de nombre décimal. Ce champ n'est actif et requis que lorsque `combo` est défini sur `"option4"` et `subcombo` sur `"opt1"`. | FLOAT | Oui | - |
| `float_y` | Un champ de saisie de nombre décimal. Ce champ n'est actif et requis que lorsque `combo` est défini sur `"option4"` et `subcombo` sur `"opt1"`. | FLOAT | Oui | - |
| `mask1` | Un champ de saisie de masque. Ce champ n'est actif que lorsque `combo` est défini sur `"option4"` et `subcombo` sur `"opt2"`. Il est facultatif. | MASK | Non | - |

**Contraintes des paramètres :**

* Le paramètre `combo` contrôle la visibilité et le caractère obligatoire de tous les autres champs d'entrée. Seules les entrées associées à l'option `combo` sélectionnée sont affichées et requises (à l'exception de `mask1` qui est facultatif).
* Lorsque `combo` est défini sur `"option4"`, le paramètre `subcombo` devient requis et contrôle un second ensemble d'entrées imbriquées (`float_x`/`float_y` ou `mask1`).

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La sortie dépend de l'option `combo` sélectionnée. Elle peut être une STRING (`"option1"`), un INT (`"option2"`), une IMAGE (`"option3"`), ou une représentation sous forme de chaîne du dictionnaire `subcombo` (`"option4"`). | ANYTYPE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DCTestNode/fr.md)

---
**Source fingerprint (SHA-256):** `9dd616a427a56eddb78b48d6eea6f71419b7097d417afae5557132b333641e69`
