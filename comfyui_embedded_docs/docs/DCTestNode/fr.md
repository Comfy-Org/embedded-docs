# DCTestNode

Le nœud DCTestNode est un nœud logique qui renvoie différents types de données en fonction de la sélection de l'utilisateur dans une liste déroulante dynamique. Il agit comme un routeur conditionnel, où l'option choisie détermine quel champ d'entrée est actif et quel type de valeur le nœud va produire.

## Entrées

Le sélecteur `combo` est toujours visible. Les champs d'entrée affichés en dessous dépendent de l'option sélectionnée.

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `combo` | La sélection principale qui détermine quel champ d'entrée est actif et ce que le nœud va produire. | DYNAMIC_COMBO | Oui | `"option1"`<br>`"option2"`<br>`"option3"`<br>`"option4"` |

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

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `subcombo` | Une sélection secondaire qui apparaît lorsque `combo` est défini sur `"option4"`. Elle détermine quels champs d'entrée imbriqués sont actifs. | DYNAMIC_COMBO | Oui | `"opt1"`<br>`"opt2"` |

#### Entrées opt1

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `float_x` | Une saisie de nombre décimal. Ce champ n'est actif et requis que lorsque `combo` est défini sur `"option4"` et `subcombo` est défini sur `"opt1"`. | FLOAT | Oui | - |
| `float_y` | Une saisie de nombre décimal. Ce champ n'est actif et requis que lorsque `combo` est défini sur `"option4"` et `subcombo` est défini sur `"opt1"`. | FLOAT | Oui | - |

#### Entrées opt2

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `mask1` | Un champ de saisie de masque. Ce champ n'est actif que lorsque `combo` est défini sur `"option4"` et `subcombo` est défini sur `"opt2"`. Il est optionnel. | MASK | Non | - |

**Contraintes des paramètres :**

* Le paramètre `combo` contrôle la visibilité et le caractère requis de tous les autres champs d'entrée. Seules les entrées associées à l'option `combo` sélectionnée sont affichées et requises (sauf `mask1`, qui est optionnel).
* Lorsque `combo` est défini sur `"option4"`, le paramètre `subcombo` devient actif et requis, et contrôle un second ensemble d'entrées imbriquées : `"opt1"` affiche `float_x` et `float_y` ; `"opt2"` affiche `mask1`.
* Si `combo` est défini sur une valeur inattendue, le nœud lève une ValueError.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La sortie dépend de l'option `combo` sélectionnée. Il peut s'agir d'une chaîne STRING (`"option1"`), d'un INT (`"option2"`), d'une IMAGE (`"option3"`), ou d'une représentation sous forme de chaîne du dictionnaire `subcombo` (`"option4"`). | ANYTYPE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DCTestNode/fr.md)

---
**Source fingerprint (SHA-256):** `9dd616a427a56eddb78b48d6eea6f71419b7097d417afae5557132b333641e69`
